import time
import random
import warnings
import datetime

class AltitudeError(Exception):
    def __init__(self):
        super().__init__('Altitude error')
        
        
class BlackBox():
    database = []
    
    def __init__(self):
        start_time = datetime.datetime.now()
        self.database.extend([start_time])
        
    def __str__(self):
        return str(self.database)
        
    def add(self, tag, value):
        self.database.append([datetime.datetime.now(), tag, value])


# black_box = BlackBox()


def altimeter(altitude=0):
    new_altitude = altitude
    critical_altitudes = [50, 100]
    
    if altitude == 0:
        raise AltitudeError()
    
    if altitude in critical_altitudes:
        warnings.warn('Altitude error')
        
    altitude_variation = random.randrange(0, 10)
    variation_direction = ['+', '-']
    
    direction = random.choice(variation_direction)
    if direction == '+':
        new_altitude = new_altitude + altitude_variation
    
    if direction == '-':
        new_altitude = new_altitude - altitude_variation
        
    while True:
        variation = new_altitude - altitude
        return (new_altitude == altitude, new_altitude, variation)


class Flight:
    def __init__(self, flight_altitude=0):
        state, altitude, variation = altimeter(altitude=flight_altitude)
        self.altitude_state = state
        self.altitude = altitude
        self.altitude_variation = variation
        # black_box.add('altitude', [state, altitude])
    
    def rudder(self):
        if self.altitude_state is False:
            if abs(self.altitude_variation) > 100:
                warnings.warn('Excessive variation')
                
            if self.altitude_variation < 0:
                print('Up')
            elif self.altitude_variation > 0:
                print('down')
            else:
                print('Constant')
    

while True:
    flight = Flight(flight_altitude=10000)
    flight.rudder()
    time.sleep(2)
