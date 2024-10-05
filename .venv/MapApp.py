import dash
import os
import pandas as pd
import csv
from dash import html
from pirates import pirate
import plotly.express as px
import pygame

data_path = os.path.realpath('data/largestcities.csv')
store_path = os.path.realpath('data/storecities.csv')

if os.path.isfile(store_path):
    os.remove(store_path)
with open(store_path, 'w', newline='') as f:
    dw = csv.DictWriter(f, fieldnames=['Lat', 'Lon', 'Title', 'rank', 'Country', '2021 pop.'])
    dw.writeheader()
    dw.writerow({'Lat':'0.00', 'Lon':'0.00', 'Title':'Start', 'rank':'0', 'Country':'None', '2021 pop.':'0'})
df_data = pd.read_csv(open(data_path, 'r', newline=''))
df_store = pd.read_csv(open(store_path, 'r', newline=''))
pirate = pirate()
fig = px.scatter_geo(df_store, lat = "Lat", lon = "Lon", hover_name = "Title", size = "2021 pop.")

def main():
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running= False
        fig.write_image("static/images/fig1.jpeg")
        image = pygame.image.load('static/images/fig1.jpeg')
        screen.blit(image, (0, 0))
        pygame.display.update()




# function for damage index implementation and generation of data for size on fig
def damage_index():
    index = 0
    return index


# implementation below is for dash integration
# app = dash.Dash()
# app.layout = html.Div([
#     dcc.Graph(figure = fig)
# ])

if __name__ == "__main__":
    main()
