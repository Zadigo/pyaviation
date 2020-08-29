import collections
import functools
import datetime
import math
from collections import OrderedDict, namedtuple

class Math:
    @staticmethod
    def convert_to_minutes(value):
        if not isinstance(value, float):
            raise ValueError(f'The value to convert should be a float. Got {value}.')
        left, right = str(value).split('.')
        return sum([(int(left) * 60), int(right)])

    @staticmethod
    def convert_to_hours(self, value):
        return value / 60

    @staticmethod
    def kmh_to_mph(speed, invert=False, r=0):
        if not invert:
            return round(speed / 1.609, r)
        return round(speed * 1.609)


class FlightMixin(Math):
    unit_system = 'metric'

    @staticmethod
    def _create_named_tuple(name, fields: list):
        return namedtuple(name, fields)

    @staticmethod
    def _check_time(value, minutes=False):
        if minutes:
            if value < 0 or value > 60:
                raise ValueError('Minutes should be between 0 and 60')
        else:
            if value < 1:
                raise ValueError('Hours should be more than 1')
        return value

    @staticmethod
    def calculate_speed(distance, duration):
        return distance / duration

    @staticmethod
    def calculate_distance(speed, duration):
        return speed * duration

    def calculate_duration(self, distance, speed, to_minutes=False, r=2):
        """
        Calculates the duration of a flight
        """
        unit = 'hours'
        if to_minutes:
            unit = 'minutes'
        canvas = self._create_named_tuple('Duration', [unit])
        return canvas(round(distance / speed, r))

    @staticmethod
    def calculate_arrival_time(hours, minutes):
        result = (datetime.datetime.now() +
                  datetime.timedelta(hours=hours, minutes=minutes))
        return result.strftime('%H:%M:%S')

    def ground_speed(self, airspeed, wind_speed, airplane_direction, wind_direction, r=0):
        """
        Parameters
        ----------

            - airspeed: indicated air speed
            - wind_speed: speed of the wind
            - airplane_direction: direction of the airplane in degrees
            - wind_direction: direction of the wind in degrees

        Example
        -------

            An airplane going N45°E with an IAS (airspeed) of 500 kmh and a wind
            velocity of 60 kmh direction N30°W will have a ground speed of 518.77 kmh

            Where c**2 = a**2 + b**2 - 2ab * cos A  // 60**2 + 500**2 - 2 * 60 * 500 * cos 105° = 518.77 kmh
            and the drift angle, sin x / 60 = sin 105 / 518.77 and, 60 * sin 105 / 518.77 = 1/0.1117 = 3.10°

        Links
        -----

            https://www.youtube.com/watch?v=YWHYbR_dcoc

            https://www.youtube.com/watch?v=d04kbyC7ej4
        """
        canvas = self._create_named_tuple(
            'GS', ['ground_speed', 'drift_angle'])
        # We are trying to resolve a classic case
        # of finding the hypothenuse of a none
        # rectangle triangle. First, we have to
        # calculate the right angle
        missing_angle = 90 - wind_direction
        right_angle = sum([airplane_direction, missing_angle])

        speed = abs(wind_speed**2 + airspeed**2 - 2 * (wind_speed)
                    * (airspeed) * math.cos(right_angle))
        squared_speed = math.sqrt(speed)

        def drift_angle():
            return round(abs(1 / (wind_speed * math.sin(right_angle) / squared_speed)), r)

        return canvas(round(squared_speed, r), drift_angle())

    def true_air_speed(self, altitude, pressure_altitude, temperature):
        """
        Calculates the Calibrated Air Speed or True Air Speed or Equivalent Air Speed
        
        Description
        -----------

            Actual speed of the airplane through the air
        """
        density_altitude = self.density_altitude(
            pressure_altitude, temperature)
        return (altitude - density_altitude) * (1.02 / 1000)

    @staticmethod
    def density_altitude(pressure_altitude, temperature):
        """
        Formula
        -------

            pressure altitude in feet + (120 x (OAT - ISA temperature))
        

        Example
        -------

            The density altitude at an airport 7000 feet above sea level, 
            with a temperature of 18 degrees Celsius and a pressure
            altitude of 7000 (assuming standard pressure) would be calculated as follows.

                - 18 – 1 = 17
                - 17 x 120 = 2040  
                - 2040 + 7000 = 9040 feet Density Altitude

            This means the aircraft will perform as if it were at 9,040 feet
        """
        # Standard temperature
        # at sea level
        outside_air_temperature = 15
        times_thousand_in_altitude = round(pressure_altitude / 1000)
        # The standard sea temperature decreases by 2°C
        # per thousand feet of altitude about sea level
        step1 = (outside_air_temperature - (times_thousand_in_altitude * 2))
        step2 = temperature - step1
        step3 = 120 * step2
        return pressure_altitude + step3

    def fuel(self, consumption_rate, hours, minutes, total_fuel=None, r=0):
        """
        Calculates the fuel consumed during a flight of x hours and minutes
        and eventually the remaining minutes left to fly with the fuel left

        Parameters
        ----------

            - consumption_rate: the consumption rate of the aircraft per hour
            - hours: the duration of the actual flight in hours
            - minutes: the duration of the actual flight in minutes
            - total_fuel: the total amount of fuel that was injected into the aircraft
            - r: round the resulting values to n

        Example
        -------

            If an aircraft consumes 17.0 gallons per hour and has flown 1 h 10 minutes,
            then the fuel used is (1 * 60) + 10 = 70 minutes and 70 * 17 / 60 = 19.83 gallons.

            The remaning time of flight if we injected a total of 40 gallons is 40 - 19.83 ~ 2 hours
            or 2 * 60 = 120 minutes
        """
        hours = self._check_time(hours)
        minutes = self._check_time(minutes, minutes=True)

        fields = ['used']

        duration = (hours * 60) + minutes
        burned = round((duration * consumption_rate) / 60, r)

        results = [burned]

        if total_fuel:
            fuel_to_burn = total_fuel - burned
            # Returns the remaining available time
            # to fly in minutes
            time_avaible_to_fly = (fuel_to_burn / consumption_rate) * 60
            fields.append('endurance')
            results.append(round(time_avaible_to_fly, r))

        canvas = self._create_named_tuple('Fuel', fields)
        return canvas(*results)

    def fuel_consumption_rate(self, used, hours, minutes, r=0):
        """
        Calculates the fuel consumption rate of an aircraft

        Example
        -------

            If an aircraft used 16 gallons and flew for 145 minutes,
            then the consumption rate is 16 / 145 * 60 = 6.62 gallons per hour
        """
        canvas = self._create_named_tuple('ConsumptionRate', ['rate'])
        duration = (hours * 60) + minutes
        print(duration)
        return canvas(round(used / duration * 60, r))

    def ground_gradient(self, air_gradient, airspeed, wind_speed, headwind=True, obstacle_clearance=False, r=0):
        """
        Calculates the ground gradient of an aircraft during the airborne section

        Description
        -----------


        Formulae
        --------

            Tailwind: air gradient (%) * true air speed / true ground speed
            Headwind: air gradient (%) * true ground speed / true air speed

            Returns a gradiant in percentage.

            If the formulae is used for obstacle clearance, only 50% of the
            headwind must be used or 150% of the tailwind

        Example
        -------

            Assume an air gradient of 15% for an airplane travelling at 100 kt
            and a tailwind of 20 kt. The true ground speed is 100 - 20 = 80 kt.
            Therefore, 15% * 100 / 80 gives an ground gradient of 18.8%
        """
        if obstacle_clearance:
            wind_speed = wind_speed * 0.50
        true_ground_speed = airspeed - wind_speed
        if headwind:
            factor = airspeed / true_ground_speed
        else:
            factor = true_ground_speed / airspeed
        gradient = round((air_gradient / 100) * factor, r) * 100
        canvas = self._create_named_tuple(
            'GroundGradient', ['factor', 'gradient', 'wind'])
        return canvas(factor, gradient, 'headwind' if headwind else 'tailwind')

    def calculate_obstacle_clearance(self, gradient, distance_from_obstacle, obstacle_height, screen_height=0, r=0):
        """
        Calculates how high and aircraft would need to fly on climb in order
        to clear an obstable of x height

        Example
        -------

            If an aircraft climbs at a 10% gradient, what is the clearance for an
            obstacle 900 m AGL and distant from 10000 m? Determine the altitude of the aircraft?

            (10% * 10 000 + 15) / 100
        """
        canvas = self._create_named_tuple(
            'ObstacleClearance', ['altitude', 'clearance'])
        total = (gradient / 100) * distance_from_obstacle
        total = total + screen_height / 100
        clearance = total - obstacle_height
        return canvas(round(total, r), clearance)

    def distance_to_horizon(self, altitude, r=0):
        """
        Calculates the distance of the aircraft to the horizon
        given a certain height
        """
        canvas = self._create_named_tuple('DistanceToHorizon', ['distance'])
        return canvas(round(1.17 * math.sqrt(altitude), r))

    def needed_fuel(self, taxi, trip, contigency, 
                    alternate, final_reserve, additional, extra):
        """
        Calculates the fuel quantity required for a safe trip along a planned route

        Parameters
        ----------
            - taxi: fixed quantity for an average taxi duration
            - trip: The required fuel quantity from brake release at the departure airport to the
                    landing touchdown at the destination airport. Takes into account:

                        • Takeoff
                        • Climb to cruise level
                        • Flight from the end of climb to the beginning of descent, including any
                          step climb/descent
                        • Flight from the beginning of descent to the beginning of approach,
                        • Approach
                        • Landing at the destination airport

            - CF: The fuel necessary to fly for 5, 15 or 20 minutes at 1500 feet above 
                  the destination airport at holding speed in ISA conditions
            - AF: Alternate Fuel

                    • Missed approach at the destination airport
                    • Climb from the missed approach altitude to the cruise level
                    • Flight from the end of climb to the beginning of descent
                    • Flight from the beginning of descent to the beginning of the approach
                    • Approach
                    • Landing at the alternate airport
                    • When two alternate airports are required*, alternate fuel should be
                      sufficient to proceed to the alternate which requires the greater amount
                      of fuel.

            - FR: The final reserve fuel is the minimum fuel required to fly for 30 minutes at
                  1,500 feet above the alternate airport or destination airport
            - Add: minimum additional fuel which should permit 
                   holding for 15 minutes at 1500 ft (450 m) above 
                   aerodrome elevation in standard conditions
            - XF: Extra fuel is at the Captain’s discretion

        Documentation
        -------------
            
        p. 176, http://www.smartcockpit.com/docs/Getting_to_Grips_With_Aircraft_Performance.pdf
        """
        canvas = self._create_named_tuple('FuelQuantity', ['lbs'])
        if contigency < round(trip * 0.05, 0):
            raise ValueError('Contigency fuel should be at least 5%% of the trip fuel')
        total = sum([taxi, trip, contigency, alternate, final_reserve, additional, extra])
        return canvas(total)
