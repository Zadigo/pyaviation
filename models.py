from pyaviation.aircraft import Airbus, Boeing


class A320(Airbus):
    version = 'neo'
    speed = {
        'cruise': 447,
        'max': 470
    }
    max_range = 3300
    weight = {
        'taxi': 73900,
        'takeoff': 73500,
        'landing': 64500
    }
    fuel = {
        'max': 23859
    }
    passengers = 150
    ceiling = {
        'range': [39100, 41000]
    }

# weight = {max_gross_weight, max_takeoff_weight, max_landing_weight}
