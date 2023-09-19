

import pandas as pd
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as gr


pio.templates.default = "plotly_white"

air = pd.read_csv(r"C:\Users\vinti\PycharmProjects\pythonProject1\Datasets\trichyaqi.csv")

#print(air.head())--To check the details of this dataframe from first 10 data

# Here we coverted the date data into date time format
air['date'] = pd.to_datetime(air['date'],format='%d-%m-%Y %H:%M')

print(air.describe())


# time series plot for each air pollutant
fig = gr.Figure()

#In this line name=pollutant used to name the scatter lines by it's data name like 'co', 'no' ...
for pollutant in ['co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3']:
    fig.add_trace(gr.Scatter(x=air['date'], y=air[pollutant], mode='lines',
                             name=pollutant))

#In this line we gave the suitable name for X and Y axis for the better understanding.
fig.update_layout(title='Time Series Analysis of Air Pollutants in Trichy',
                  xaxis_title='Date', yaxis_title='Concentration (µg/m³)')

#In this line we displayed the scattered graph in default browser window.
fig.show()

# Define AQI breakpoints and corresponding AQI values (low, high, aqi)
aqi_breakpoints = [
    (0, 12.0, 50), (12.1, 35.4, 100), (35.5, 55.4, 150),
    (55.5, 150.4, 200), (150.5, 250.4, 300), (250.5, 350.4, 400),
    (350.5, 500.4, 500)
]

def calculate_aqi(pollutant_name, concentration):
    for low, high, aqi in aqi_breakpoints:
        if low <= concentration <= high:
            return aqi
    return None

def calculate_overall_aqi(row):
    aqi_values = []
    pollutants = ['co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3']
    for pollutant in pollutants:
        aqi = calculate_aqi(pollutant, row[pollutant])
        if aqi is not None:
            aqi_values.append(aqi)
    return max(aqi_values)

# Calculate AQI for each row
air['AQI'] = air.apply(calculate_overall_aqi, axis=1)

# Define AQI categories (low, high, category)
aqi_categories = [
    (0, 50, 'Good'), (51, 100, 'Moderate'), (101, 150, 'Unhealthy for Sensitive Groups'),
    (151, 200, 'Unhealthy'), (201, 300, 'Very Unhealthy'), (301, 500, 'Hazardous')
]

def categorize_aqi(aqi_value):
    for low, high, category in aqi_categories:
        if low <= aqi_value <= high:
            return category
    return None

# Categorize AQI
air['AQI Category'] = air['AQI'].apply(categorize_aqi)
print(air.head())

# AQI over time
fig = px.bar(air, x="date", y="AQI",
             title="AQI of Trichy in January")
fig.update_xaxes(title="Date")
fig.update_yaxes(title="AQI")
fig.show()

#AQI category distribution:
fig = px.histogram(air, x="date",
                    color="AQI Category",
                    title="AQI Category Distribution Over Time")
fig.update_xaxes(title="Date")
fig.update_yaxes(title="Count")
fig.show()

#PIE chart
# Define pollutants and their colors
pollutants = ["co", "no", "no2", "o3", "so2", "pm2_5", "pm10", "nh3"]
pollutant_colors = px.colors.qualitative.Plotly

# Calculate the sum of pollutant concentrations
total_concentrations = air[pollutants].sum()

# Create a DataFrame for the concentrations
concentration_data = pd.DataFrame({
    "Pollutant": pollutants,
    "Concentration": total_concentrations
})

# Create a donut plot for pollutant concentrations
fig = px.pie(concentration_data, names="Pollutant", values="Concentration",
             title="Pollutant Concentrations in Trichy",
             hole=0, color_discrete_sequence=pollutant_colors)

# Update layout for the donut plot
fig.update_traces(textinfo="percent+label")
fig.update_layout(legend_title="Pollutant")

# Show the donut plot
fig.show()

# Correlation Between Pollutants
correlation_matrix = air[pollutants].corr()
print(correlation_matrix.head())
fig = px.imshow(correlation_matrix, x=pollutants,
                 y=pollutants, title="Correlation Between Pollutants")
fig.show()

# Extract the hour from the date
air['Hour'] = pd.to_datetime(air['date']).dt.hour
print(air.head())

# Calculate hourly average AQI
hourly_avg_aqi = air.groupby('Hour')['AQI'].mean().reset_index()
print(hourly_avg_aqi.head())

# Create a line plot for hourly trends in AQI
fig = px.line(hourly_avg_aqi, x='Hour', y='AQI',
              title='Hourly Average AQI Trends in Trichy (Jan 2023)')
fig.update_xaxes(title="Hour of the Day")
fig.update_yaxes(title="Average AQI")
fig.show()

# Average AQI by Day of the Week
air['Day_of_Week'] = air['date'].dt.day_name()
average_aqi_by_day = air.groupby('Day_of_Week')['AQI'].mean().reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
fig = px.bar(average_aqi_by_day, x=average_aqi_by_day.index, y='AQI',
              title='Average AQI by Day of the Week')
fig.update_xaxes(title="Day of the Week")
fig.update_yaxes(title="Average AQI")
fig.show()