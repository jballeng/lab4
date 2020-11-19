import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('.../Datasets/Weather2014-15.csv')

df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

df['Unrecovered'] = df['Confirmed'] - df['Deaths'] - df['Recovered']
data = [
    go.Scatter(x='month'
               y='')
]