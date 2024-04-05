import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from IPython.display import display, HTML

# Read the data
df = pd.read_csv("FUEL.csv")

# Handle mixed data types
# For columns with mixed types, we can convert them to a consistent data type, such as string or numeric
# For example, if column 7 has mixed types, we can convert it to string
df.iloc[:, 7] = df.iloc[:, 7].astype(str)

print(df.shape)
df.head()

df['fuel_type'].unique()

# Plot GHG score distribution
fig = px.histogram(df, x="ghg_score")
fig.update_layout(title='GHG score distribution')
fig.show()

# Remove rows with negative GHG score
dfg = df[df['ghg_score'] > -1]
fig = px.histogram(dfg, x="ghg_score")
fig.update_layout(title='GHG score distribution')
fig.show()

# Plot distribution of per mile CO2 production
fig = px.histogram(df, x="tailpipe_co2_in_grams_mile_ft1")
fig.update_layout(title='Distribution of per mile CO2 production')
fig.show()

# Compute mean CO2 by cylinders and displacement
mean_co2_cylinders = df.groupby('engine_cylinders')['tailpipe_co2_in_grams_mile_ft1'].mean()
mean_co2_displacement = df.groupby('engine_displacement')['tailpipe_co2_in_grams_mile_ft1'].mean()

# Plot CO2 vs Cylinders
scatter_trace1 = go.Scatter(
    x=df['engine_cylinders'],
    y=df['tailpipe_co2_in_grams_mile_ft1'],
    mode='markers',
    marker=dict(
        size=5,
        color='blue',
    ),
    name='Tailpipe CO2'
)

mean_trace1 = go.Scatter(
    x=mean_co2_cylinders.index,
    y=mean_co2_cylinders,
    mode='markers',
    marker=dict(
        size=8,
        color='lime',
        symbol='triangle-up'
    ),
    name='Mean CO2'
)

layout1 = go.Layout(
    xaxis=dict(title='Cylinders'),
    yaxis=dict(title='CO2')
)

fig1 = go.Figure(data=[scatter_trace1, mean_trace1], layout=layout1)
fig1.update_layout(title='CO2 vs Cylinders')
fig1.show()

# Plot CO2 vs Displacement
scatter_trace2 = go.Scatter(
    x=df['engine_displacement'],
    y=df['tailpipe_co2_in_grams_mile_ft1'],
    mode='markers',
    marker=dict(
        size=5,
        color='blue',
    ),
    name='Tailpipe CO2'
)

mean_trace2 = go.Scatter(
    x=mean_co2_displacement.index,
    y=mean_co2_displacement,
    mode='markers',
    marker=dict(
        size=8,
        color='lime',
        symbol='triangle-up'
    ),
    name='Mean CO2'
)

layout2 = go.Layout(
    xaxis=dict(title='Displacement'),
    yaxis=dict(title='CO2')
)

fig2 = go.Figure(data=[scatter_trace2, mean_trace2], layout=layout2)
fig2.update_layout(title='CO2 vs Displacement')
fig2.show()

# Further analysis and visualization can be performed based on the project requirements
