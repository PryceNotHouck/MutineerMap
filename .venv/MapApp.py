import dash
import os
import pandas as pd

from dash import dcc
from dash import html

import plotly.express as px
df = pd.read_csv(os.path.join("data", "largestcities.csv"))

fig = px.scatter_geo(df, lat = "Lat", lon = "Lon", hover_name = "Country", size = "2021 pop.")

def main():
    fig.show()

# function for damage index implementation and generation of data for size on fig
def damage_index():
    index = 0
    return index


# implementation below is for dash integration
# app = dash.Dash()
# app.layout = html.Div([
#     dcc.Graph(figure = fig)
# ])
