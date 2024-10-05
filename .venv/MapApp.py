import dash
import os
import pandas as pd
import csv
from dash import html
from pirates import pirate
import plotly.express as px
import pygame

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 15)

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
        x, y = pygame.mouse.get_pos()
        screen.blit(image, (0, 0))
        if 80 <= x <= 620 and 105 <= y <= 375:
            display_cursor(screen, x, y)
        pygame.display.update()


def display_cursor(screen, x, y):

    lat = round((y/(270/180) - 90)/-1, 2)
    lon = round(x/(540/360)-180, 2)
    text_surf = my_font.render(str(lon) + ", " + str(lat), False, (0, 0, 255))
    screen.blit(text_surf, (x-60, y-50))


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
