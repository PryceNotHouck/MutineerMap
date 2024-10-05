import csv

class pirate():
    captains = ['Black Sam Bellamy', 'Henry Every', 'William Kidd', 'Edward Teach', 'Henry Morgan']
    ships =    [70, 25, 1, 18, 36]
    range = [3775, 5522, 2183, 1761, 1128]
    power_scale = [0.5130276681, 2.262611615, 1.352245998, 0.7681988986, 0.10391582]
    actions = [3, 4, 1, 5, 5]
    speed = [24, 26, 44, 37, 56]
    movement_constant = 5.75
    pirates_per_ship = 68.55
    kills_per_pirate = 0.42
    plunder_per_ship = 1_422_238.78
    shells_per_ship = 3.48
    damage_per_ship = 251_752.31

    def city_density(self, city):
        average_pop = 0
        var_pop = -1
        reader = csv.reader(open('.venv/data/largestcities.csv', 'r', newline=''))
        next(reader)
        for row in reader:
            if row[2] in city:
                var_pop = int(row[5])
            average_pop += int(row[5])
        average_pop /= 1000
        return var_pop / average_pop

    def expand_radius(self, radius, selection):
        expansion = self.movement_constant * self.speed[selection] * self.actions[selection]
        if radius + expansion <= self.range[selection]:
            return radius + expansion

    def pillage(self, selection, city):
        population = -1
        reader = csv.reader(open('.venv/data/largestcities.csv', 'r', newline=''))
        next(reader)
        for row in reader:
            if row[2] in city:
                population = int(row[5])
        density = self.city_density(city)
        pirates = self.pirates_per_ship * self.ships[selection]
        shells = self.ships[selection]  * self.shells_per_ship
        damage = self.ships[selection] * self.damage_per_ship * shells * density * self.power_scale[selection]
        kills = self.kills_per_pirate * pirates * population * density * self.power_scale[selection]
        if kills > population:
            kills = population
        plunder = self.plunder_per_ship * self.ships[selection] * density * self.power_scale[selection]
        return [damage, kills, plunder]



pirate.pillage(0, 0, 'China')