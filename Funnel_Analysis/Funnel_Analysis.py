import pandas as pd
import plotly.io as pio
import plotly.graph_objects as gr
import warnings

warnings.filterwarnings('ignore')
pio.templates.default = "plotly_white"

browser = pd.read_csv(r'/Datasets/user_data.csv')
print(browser.head(10))
print(browser.describe())
print(browser['stage'].value_counts())
print(browser.isnull().sum())

stages = ['homepage', 'product_page', 'cart', 'checkout', 'purchase']
total_users = []
total_conversions = []

for i in stages:
    stage_user = browser[browser['stage'] == i]
    total_users.append(len(stage_user))
    total_conversions.append(stage_user['conversion'].sum())

#create a funnel chart
fig = gr.Figure(gr.Funnel(
    y=stages,
    x=total_users,
    textposition='inside',
    textinfo='value',
    name='Users'
))

fig.add_trace(gr.Funnel(
    y=stages,
    x=total_conversions,
    textposition='inside',
    textinfo='percent initial',
    name='Conversions'
))

fig.update_layout(
    title='Funnel Analysis',
    funnelmode='stack'
)

fig.show()
