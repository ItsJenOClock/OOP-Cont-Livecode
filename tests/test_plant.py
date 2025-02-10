from classes.plant import Plant

def test_plant_initialization():
    name = "Butterfly pea flower"
    water_level = 6
    sunlight_hours = 7
    is_blooming = True
    plant = Plant(name, water_level, sunlight_hours, is_blooming)
    plant_2 = Plant(name, water_level, sunlight_hours)
    assert plant.name == name
    assert plant.water_level == water_level
    assert plant.sunlight_hours == sunlight_hours
    assert plant.is_blooming == is_blooming
    assert not plant_2.is_blooming