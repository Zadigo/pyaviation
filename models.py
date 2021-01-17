from pyaviation.aircraft import Airbus, Boeing


class A320(Airbus):
    version = 'base'
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


class A320Neo(A320):
    version = 'neo'


class A321(A320):
    version = None


class B777200(Boeing):
    version = '200'
    passengers = 440
    weight = {
        'empty': 134800,
        'taxi': 0,
        'takeoff': 247200,
        'landing': 201840
    }


class B777200ER(B777200):
    version = '200ER'
    weight = {
        'empty': 138100,
        'taxi': 0,
        'takeoff': 297550,
        'landing': 213180
    }
    ceiling = {
        'max': 35000
    }

airplane = B777200ER()
s = airplane.glide_angle(200, 15)
print(s)
