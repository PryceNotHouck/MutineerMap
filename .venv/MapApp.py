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
pirate = pirate()

if os.path.isfile(store_path):
    os.remove(store_path)
with open(store_path, 'w', newline='') as f:
    dw = csv.DictWriter(f, fieldnames=['Lat', 'Lon', 'Title', 'rank', 'Country', '2021 pop.'])
    dw.writeheader()
    dw.writerow({'Lat':'0.00', 'Lon':'0.00', 'Title':'Start'})

df_data = pd.read_csv(open(data_path, 'r', newline=''))
df_store = pd.read_csv(open(store_path, 'r', newline=''))

city_names = df_data.loc[:, 'Title'].to_list()
city_x = df_data.loc[:, 'Lon'].to_list()
city_y = df_data.loc[:, 'Lat'].to_list()
coordinate_pairs = {}
for i in range(len(city_names)):
    coordinate_pairs[city_names[i]] = (float(city_x[i]), float(city_y[i]))

fig = px.scatter_geo()

def place_pirate(selection, x, y):
    consequences = []
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
            writer = csv.writer(f)
            for city in pillaged:
                consequences.append(pirate.pillage(selection, city))
                writer.writerow({'Lat': str(city[0]), 'Lon': str(city[1]), 'Title': str(city[2])})
        fig = px.scatter_geo()
        fig.show()
    return consequences

def main():
    screen = pygame.display.set_mode((1500, 1000))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running= False
        x, y = pygame.mouse.get_pos()
        screen.fill("white")
        bg = pygame.transform.scale(pygame.image.load("static/images/world-map-continents-oceans.webp"), (1500, 750))
        screen.blit(bg, (0, 0))
        if 0 <= x <= 1500 and 0 <= y <= 750:
            display_cursor(screen, x, y)
        pygame.display.update()


def display_cursor(screen, x, y):
    lat = round(((y)/(750/180) - 90)/-1, 2)
    lon = round((x)/(1500/360)-180, 2)
    text_surf = my_font.render(str(lon) + ", " + str(lat), False, (0, 0, 255))
    screen.blit(text_surf, (1400, 775))


# function for damage index implementation and generation of data for size on fig
def damage_index():
    index = 0
    return index


if __name__ == "__main__":
    main()
