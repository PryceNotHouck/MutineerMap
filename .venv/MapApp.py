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
pirate = pirate()

if os.path.isfile(store_path):
    os.remove(store_path)
with open(store_path, 'w', newline='') as f:
    dw = csv.DictWriter(f, fieldnames=['Lat', 'Lon', 'Title', 'rank', 'Country', '2021 pop.'])
    dw.writeheader()
    dw.writerow({'Lat':'0.00', 'Lon':'0.00', 'Title':'Start'})

df_data = pd.read_csv(open(data_path, 'r', newline=''))
df_store = pd.read_csv(open(store_path, 'r', newline=''))

city_names = df_data.loc[:, 'Title'].tolist()
city_x = df_data.loc[:, 'Lon'].tolist()
city_y = df_data.loc[:, 'Lat'].toList()
coordinate_pairs = {}
for i in range(len(city_names)):
    coordinate_pairs[city_names[i]] = (float(city_x[i]), float(city_y[i]))

fig = px.scatter_geo(df_store, lat = "Lat", lon = "Lon", hover_name = "Title", size = "2021 pop.")

def place_pirate(selection, x, y):
    size = pirate.bubble(selection)[0]
    while size <= size[1]:
        old_size = size
        size += pirate.expand_radius(size / 2, selection)
        pillaged = []
        for city in coordinate_pairs:
            coord = coordinate_pairs[city]
            if ((x + old_size) < coord[0] < (x + old_size)) and ((y + old_size) < coord[1] < (y + old_size)):
                pillaged.append([coord[1], coord[0], city]) # + + + +
            elif ((x + old_size) < coord[0] < (x + old_size)) and ((y + old_size) < coord[1] < (y - old_size)):
                pillaged.append([coord[1], coord[0], city]) # + + + -
            elif ((x + old_size) < coord[0] < (x + old_size)) and ((y - old_size) < coord[1] < (y + old_size)):
                pillaged.append([coord[1], coord[0], city]) # + + - +
            elif ((x + old_size) < coord[0] < (x + old_size)) and ((y - old_size) < coord[1] < (y - old_size)):
                pillaged.append([coord[1], coord[0], city]) # + + - -
            elif ((x + old_size) < coord[0] < (x - old_size)) and ((y + old_size) < coord[1] < (y + old_size)):
                pillaged.append([coord[1], coord[0], city]) # + - + +
            elif ((x + old_size) < coord[0] < (x - old_size)) and ((y + old_size) < coord[1] < (y - old_size)):
                pillaged.append([coord[1], coord[0], city]) # + - + -
            elif ((x + old_size) < coord[0] < (x - old_size)) and ((y - old_size) < coord[1] < (y + old_size)):
                pillaged.append([coord[1], coord[0], city]) # + - - +
            elif ((x + old_size) < coord[0] < (x - old_size)) and ((y - old_size) < coord[1] < (y - old_size)):
                pillaged.append([coord[1], coord[0], city]) # + - - -
            elif ((x - old_size) < coord[0] < (x + old_size)) and ((y + old_size) < coord[1] < (y + old_size)):
                pillaged.append([coord[1], coord[0], city]) # - + + +
            elif ((x - old_size) < coord[0] < (x + old_size)) and ((y - old_size) < coord[1] < (y + old_size)):
                pillaged.append([coord[1], coord[0], city]) # - + - +
            elif ((x - old_size) < coord[0] < (x + old_size)) and ((y - old_size) < coord[1] < (y - old_size)):
                pillaged.append([coord[1], coord[0], city]) # - + - -
            elif ((x - old_size) < coord[0] < (x - old_size)) and ((y + old_size) < coord[1] < (y + old_size)):
                pillaged.append([coord[1], coord[0], city]) # - - + +
            elif ((x - old_size) < coord[0] < (x - old_size)) and ((y + old_size) < coord[1] < (y - old_size)):
                pillaged.append([coord[1], coord[0], city]) # - - + -
            elif ((x - old_size) < coord[0] < (x - old_size)) and ((y - old_size) < coord[1] < (y + old_size)):
                pillaged.append([coord[1], coord[0], city]) # - - - +
            elif ((x - old_size) < coord[0] < (x - old_size)) and ((y - old_size) < coord[1] < (y - old_size)):
                pillaged.append([coord[1], coord[0], city]) # - - - -
        with open(store_path, 'w', newline='') as f:
            for city in pillaged:
                writer = csv.writer(f)
                writer.writerow({'Lat': str(city[0]), 'Lon': str(city[1]), 'Title': str(city[2])})
        fig = px.scatter_geo(df_store, lat = x, lon = y, hover_name = "Title", size = size)
        fig.show()

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
