class Plant:

# Write your plant class here!
    def __init__(self, name, water_level, sunlight_hours, is_blooming=False):
        self.name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours
        self.is_blooming = is_blooming

    def water(self, water_amount):
        self.water_level  += water_amount

        return f"{self.name} New water level: {self.water_level}"

    def give_sunlight(self, hours):
        self.sunlight_hours += hours

    def check_growth(self):
        if self.sunlight_hours > 5 and self.water_level > 5:
            self.growth = "mature"
        else:
            self.growth = "sprout"
            
        # return f"{self.name} is {self.growth_state}"

plant = Plant("Butterfly pea flower", 4, 5, True)

print(plant)
print(plant.name, plant.water_level, plant.sunlight_hours, plant.is_blooming)
print(plant.water(3))
print(plant.check_growth())
print(plant.growth)