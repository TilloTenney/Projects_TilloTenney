import pandas as pd
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as gr
import statsmodels.api as sm #to use ols in treandline parameter.
import warnings

pio.templates.default = "plotly_white"
warnings.filterwarnings("ignore")

EDA = pd.read_csv(r"C:\Users\vinti\PycharmProjects\pythonProject1\Datasets\Instagram_data.csv", encoding='latin-1')

#Print the first five rows of the data
print(EDA.head(), "\n")

#Print all the columns the dataset contains
print(EDA.columns, "\n")

#Print the column info
print(EDA.info(), "\n")

#Print the descriptive statistics of the data
print(EDA.describe())

#Check if data contains any missing values or not
print(EDA.isnull().sum())

#Display the distribution of the impressions in histogram
fig = px.histogram(EDA, x='Impressions',nbins=10,title='Distribution of Impressions')
fig.show()

#Display the number of impressions on each post over time
fig = px.line(EDA, x=EDA.index, y='Impressions', title='Impression over time')
fig.show()

#Display the metrics like Likes, Saves, and Follows from each post over time
fig = gr.Figure()

fig.add_trace(gr.Scatter(x=EDA.index, y=EDA['Likes'], name='Likes'))
fig.add_trace(gr.Scatter(x=EDA.index, y=EDA['Saves'], name='Saves'))
fig.add_trace(gr.Scatter(x=EDA.index, y=EDA['Follows'], name='Follows'))

fig.update_layout(title='Metrices over time', xaxis_title = 'Date', yaxis_title = 'Count')

fig.show()

#The distribution of reach from different sources:
reach_sources = ['From Home', 'From Hashtags', 'From Explore', 'From Other']
reach_counts = [EDA[source].sum() for source in reach_sources]

colors = ['#FFB6C1', '#87CEFA', '#90EE90', '#FFDAB9']

fig = px.pie(data_frame=EDA, names=reach_sources,
             values=reach_counts,
             title='Reach from Different Sources',
             color_discrete_sequence=colors)
fig.show()

#the distribution of engagement sources
engagement_metrics = ['Saves', 'Comments', 'Shares', 'Likes']
engagement_counts = [EDA[metric].sum() for metric in engagement_metrics]

colors = ['#FFB6C1', '#87CEFA', '#90EE90', '#FFDAB9']

fig = px.pie(data_frame=EDA, names=engagement_metrics,
             values=engagement_counts,
             title='Engagement Sources',
             color_discrete_sequence=colors)
fig.show()

#the relationship between the number of profile visits and follows
fig = px.scatter(EDA,
                 x='Profile Visits',
                 y='Follows',
                 trendline = 'ols',
                 title='Profile Visits vs. Follows')
fig.show()

#The type of hashtags used in the posts using a wordcloud
from wordcloud import WordCloud

hashtags = ' '.join(EDA['Hashtags'].astype(str))
wordcloud = WordCloud().generate(hashtags)

fig = px.imshow(wordcloud, title='Hashtags Word Cloud')
fig.show()

#the correlation between all the features
# EDA_1 = EDA.loc[:,:'Follows']
# print(EDA_1.head())
corr_matrix = EDA.corr(numeric_only=True) # Here we are using numeric_only=True to extract int,float and bool data type fields alone for the heat map. Because we couldn't use str for this visualisation.

fig = gr.Figure(data=gr.Heatmap(z=corr_matrix.values,
                               x=corr_matrix.columns,
                               y=corr_matrix.index,
                               colorscale='RdBu',
                               zmin=-1,
                               zmax=1))

fig.update_layout(title='Correlation Matrix',
                  xaxis_title='Features',
                  yaxis_title='Features')

fig.show()

#the distribution of hashtags to see which hashtag is used the most in all the posts

# Create a list to store all hashtags
all_hashtags = []

# Iterate through each row in the 'Hashtags' column
for row in EDA['Hashtags']:
    hashtags = str(row).split()
    hashtags = [tag.strip() for tag in hashtags]
    all_hashtags.extend(hashtags)

# Create a pandas DataFrame to store the hashtag distribution
hashtag_distribution = pd.Series(all_hashtags).value_counts().reset_index()
hashtag_distribution.columns = ['Hashtag', 'Count']

fig = px.bar(hashtag_distribution, x='Hashtag',
             y='Count', title='Distribution of Hashtags')
fig.show()

#the distribution of likes and impressions received from the presence of each hashtag on the post

# Create a dictionary to store the likes and impressions for each hashtag
hashtag_likes = {}
hashtag_impressions = {}

# Iterate through each row in the dataset
for index, row in EDA.iterrows():
    hashtags = str(row['Hashtags']).split()
    for hashtag in hashtags:
        hashtag = hashtag.strip()
        if hashtag not in hashtag_likes:
            hashtag_likes[hashtag] = 0
            hashtag_impressions[hashtag] = 0
        hashtag_likes[hashtag] += row['Likes']
        hashtag_impressions[hashtag] += row['Impressions']

# Create a DataFrame for likes distribution
likes_distribution = pd.DataFrame(list(hashtag_likes.items()), columns=['Hashtag', 'Likes'])

# Create a DataFrame for impressions distribution
impressions_distribution = pd.DataFrame(list(hashtag_impressions.items()), columns=['Hashtag', 'Impressions'])

fig_likes = px.bar(likes_distribution, x='Hashtag', y='Likes',
                   title='Likes Distribution for Each Hashtag')

fig_impressions = px.bar(impressions_distribution, x='Hashtag',
                         y='Impressions',
                         title='Impressions Distribution for Each Hashtag')

fig_likes.show()
fig_impressions.show()

