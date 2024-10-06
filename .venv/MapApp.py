
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
pygame.mouse.set_visible(False)

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

def main():
    screen = pygame.display.set_mode((1500, 1000))
    pygame.display.set_caption("Mutineer Map v0.1.0")
    font = pygame.font.Font('static/fonts/booter/BOOTERZF.ttf', 24)
    bg = pygame.transform.scale(pygame.image.load("static/images/world-map-continents-oceans.webp"), (1500, 750))
    logo = pygame.image.load("static/images/img.png")
    cursor = pygame.image.load("static/images/skull.png")
    cursor2 = pygame.image.load("static/images/skull2.png")
    curs = cursor
    running = True
    selected = -1
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running= False
            if event.type == pygame.MOUSEBUTTONDOWN:
                curs = cursor2
                print(pygame.mouse.get_pos())
                if 760 <= pygame.mouse.get_pos()[0] <= 860 and 760 <= pygame.mouse.get_pos()[1] <= 810:
                    # sam
                    selected = 0
                    infocanvas = my_font.render("\" Black Sam \" Bellamy: \n Ships: " + pirate.ships[selected] +
                                                                         "\n Range: " + pirate.range[selected] +
                                                                         "\n Power: " + pirate.power_scale[selected] +
                                                                         "\n Actions: " + pirate.actions[selected] +
                                                                         "\n Speed: " + pirate.speed[selected], False, "green")
                    screen.blit()
                elif 880 <= pygame.mouse.get_pos()[0] <= 980 and 760 <= pygame.mouse.get_pos()[1] <= 810:
                    # edward
                    selected = 3
                elif 1000 <= pygame.mouse.get_pos()[0] <= 1100 and 760 <= pygame.mouse.get_pos()[1] <= 810:
                    # morgan
                    selected = 4
                elif 1120 <= pygame.mouse.get_pos()[0] <= 1220 and 760 <= pygame.mouse.get_pos()[1] <= 810:
                    # every
                    selected = 1
                elif 1240 <= pygame.mouse.get_pos()[0] <= 1300 and 760 <= pygame.mouse.get_pos()[1] <= 810:
                    # kidd
                    selected = 2
                elif pygame.mouse.get_pos()[1] >= 680:
                    if selected != -1:
                        selected = -1
                        def place_pirate(selection, x, y):
                            consequences = []
                            size = pirate.bubble(selection)[0]
                            while size <= pirate.bubble(selection)[1]:
                                old_size = size
                                size += pirate.expand_radius(size / 2, selection)
                                pillaged = []
                                for city in coordinate_pairs:
                                    coord = coordinate_pairs[city]
                                    if ((x + old_size) < coord[0] < (x + old_size)) and (
                                            (y + old_size) < coord[1] < (y + old_size)):
                                        pillaged.append([coord[1], coord[0], city])  # + + + +
                                    elif ((x + old_size) < coord[0] < (x + old_size)) and (
                                            (y + old_size) < coord[1] < (y - old_size)):
                                        pillaged.append([coord[1], coord[0], city])  # + + + -
                                    elif ((x + old_size) < coord[0] < (x + old_size)) and (
                                            (y - old_size) < coord[1] < (y + old_size)):
                                        pillaged.append([coord[1], coord[0], city])  # + + - +
                                    elif ((x + old_size) < coord[0] < (x + old_size)) and (
                                            (y - old_size) < coord[1] < (y - old_size)):
                                        pillaged.append([coord[1], coord[0], city])  # + + - -
                                    elif ((x + old_size) < coord[0] < (x - old_size)) and (
                                            (y + old_size) < coord[1] < (y + old_size)):
                                        pillaged.append([coord[1], coord[0], city])  # + - + +
                                    elif ((x + old_size) < coord[0] < (x - old_size)) and (
                                            (y + old_size) < coord[1] < (y - old_size)):
                                        pillaged.append([coord[1], coord[0], city])  # + - + -
                                    elif ((x + old_size) < coord[0] < (x - old_size)) and (
                                            (y - old_size) < coord[1] < (y + old_size)):
                                        pillaged.append([coord[1], coord[0], city])  # + - - +
                                    elif ((x + old_size) < coord[0] < (x - old_size)) and (
                                            (y - old_size) < coord[1] < (y - old_size)):
                                        pillaged.append([coord[1], coord[0], city])  # + - - -
                                    elif ((x - old_size) < coord[0] < (x + old_size)) and (
                                            (y + old_size) < coord[1] < (y + old_size)):
                                        pillaged.append([coord[1], coord[0], city])  # - + + +
                                    elif ((x - old_size) < coord[0] < (x + old_size)) and (
                                            (y - old_size) < coord[1] < (y + old_size)):
                                        pillaged.append([coord[1], coord[0], city])  # - + - +
                                    elif ((x - old_size) < coord[0] < (x + old_size)) and (
                                            (y - old_size) < coord[1] < (y - old_size)):
                                        pillaged.append([coord[1], coord[0], city])  # - + - -
                                    elif ((x - old_size) < coord[0] < (x - old_size)) and (
                                            (y + old_size) < coord[1] < (y + old_size)):
                                        pillaged.append([coord[1], coord[0], city])  # - - + +
                                    elif ((x - old_size) < coord[0] < (x - old_size)) and (
                                            (y + old_size) < coord[1] < (y - old_size)):
                                        pillaged.append([coord[1], coord[0], city])  # - - + -
                                    elif ((x - old_size) < coord[0] < (x - old_size)) and (
                                            (y - old_size) < coord[1] < (y + old_size)):
                                        pillaged.append([coord[1], coord[0], city])  # - - - +
                                    elif ((x - old_size) < coord[0] < (x - old_size)) and (
                                            (y - old_size) < coord[1] < (y - old_size)):
                                        pillaged.append([coord[1], coord[0], city])  # - - - -
                                with open(store_path, 'w', newline='') as f:
                                    writer = csv.writer(f)
                                    for city in pillaged:
                                        consequences.append(pirate.pillage(selection, city))
                                        writer.writerow({'Lat': str(city[0]), 'Lon': str(city[1]), 'Title': str(city[2])})
                                draw_consequences(screen, font, consequences)
                                pygame.draw.circle(screen, "black", [x, y], size)
                            return consequences
                        place_pirate(selected, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            else:
                curs = cursor
        x, y = pygame.mouse.get_pos()
        screen.fill("white")
        screen.blit(bg, (0, 0))
        screen.blit(logo, (50, 800))
        draw_boxes(screen)
        screen.blit(pygame.transform.scale(curs, (32, 32)), (x, y))
        if 0 <= x <= 1500 and 0 <= y <= 750:
            display_cursor(screen, x, y)
        pygame.display.update()

def draw_consequences(surface, font, consequences):
    killed, damages, plundered = 0, 0, 0
    for city in consequences:
        damages += float(city[0])
        killed += int(city[1])
        plundered += int(city[2])

    kill_text = font.render(str(killed), False, pygame.Color('black'))
    damages_text = font.render(f'${damages}', False, pygame.Color('black'))
    plunder_text = font.render(f'${plundered}', False, pygame.Color('black'))

    # killRect, damageRect, plunderRect = kill_text.get_rect(), damages_text.get_rect(), plunder_text.get_rect()
    # killRect.center = (int(killRect.width / 2), int(killRect.height / 2))
    # damageRect.center = (int(damageRect.width / 2), int(damageRect.height / 2))
    # plunderRect.center = (int(plunderRect.width / 2), int(plunderRect.height / 2))

    surface.blit(kill_text, (520, 760))
    surface.blit(damages_text, (520, 810))
    surface.blit(plunder_text, (520, 860))

def draw_boxes(surface):
    sam = pygame.image.load("static/images/black_sam_text.gif")
    edward = pygame.image.load("static/images/edward_teach_text.gif")
    morgan = pygame.image.load("static/images/henry_morgan_text.gif")
    every = pygame.image.load("static/images/henry_every_text.gif")
    kidd = pygame.image.load("static/images/william_kidd_text.gif")

    pygame.draw.rect(surface, (0, 0, 0), (760, 760, 100, 50), 3)
    surface.blit(pygame.transform.scale(sam, (100, 50)), (760, 760))

    pygame.draw.rect(surface, (0, 0, 0), (880, 760, 100, 50), 3)
    surface.blit(pygame.transform.scale(edward, (100, 50)), (880, 760))

    pygame.draw.rect(surface, (0, 0, 0), (1000, 760, 100, 50), 3)
    surface.blit(pygame.transform.scale(morgan, (100, 50)), (1000, 760))

    pygame.draw.rect(surface, (0, 0, 0), (1120, 760, 100, 50), 3)
    surface.blit(pygame.transform.scale(every, (100, 50)), (1120, 760))

    pygame.draw.rect(surface, (0, 0, 0), (1240, 760, 100, 50), 3)
    surface.blit(pygame.transform.scale(kidd, (100, 50)), (1240, 760))


def display_cursor(screen, x, y):
    lat = round((y / (750 / 180) - 90) / -1, 2)
    lon = round(x / (1500 / 360) - 180, 2)
    text_surf = my_font.render("Cursor coords: " + str(lon) + ", " + str(lat), False, (0, 0, 255))
    screen.blit(text_surf, (100, 875))


# function for damage index implementation and generation of data for size on fig
def damage_index():
    index = 0
    return index


if __name__ == "__main__":
    main()
