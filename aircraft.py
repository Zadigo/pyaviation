import functools
import json
from collections import OrderedDict

from pyaviation.mixins import FlightMixin


class BaseAirplane(type):
    """Represents the base element for an aircraft"""
    def __new__(cls, name, bases, attrs):
        new_class = super().__new__
        if not bases:
            return new_class(cls, name, bases, attrs)
        return new_class(cls, name, bases, attrs)


class Airplane(FlightMixin, metaclass=BaseAirplane):
    speed = {}
    max_range = None
    weight = {}
    ceiling = {}
    passengers = {}
    fuel = {}

    manufacturer = None
    version = None

    def __init__(self, *, speed=None, max_range=None, 
                 weight=None, ceiling=None, passengers=None, fuel=None):
        self.name = None

    def __setattr__(self, name, value):
        if name == 'speed' or name == 'passengers' or name == 'fuel':
            if not isinstance(value, dict):
                raise ValueError(
                    f'"{name}" attribute should be of type dictionnary')
        if name == 'speed':
            required_keys = ['max']
            if value:
                result, missing_keys = self._check_keys(
                    value.keys(), required_keys)
                if not result:
                    raise ValueError(
                        f'The "speed" dictionnary must contain: {", ".join([result[0] for result in missing_keys if not result[1]])}')
        return super().__setattr__(name, value)

    @staticmethod
    def _check_keys(incoming, required):
        truth_array = []
        for key in required:
            if key in incoming:
                truth_array.append((key, True))
            else:
                truth_array.append((key, False))
        return all([result[1] for result in truth_array]), truth_array

    @classmethod
    def characteristics(cls):
        airplane_characteristics = OrderedDict()
        values = cls.__dict__
        keys = filter(lambda k: not k.startswith('__'), values.keys())
        for key in keys:
            airplane_characteristics.update({key: values[key]})
        return airplane_characteristics

    @property
    def get_full_version(self):
        return f'{self.__class__.__name__} {self.version}'

    def safety_factor(self):
        pass

    def net_performance(self, mode='landing'):
        pass

    def gross_performance(self, mode='landing'):
        pass

    def gradient_of_climb(self):
        """
        (T - D / W) * 100
        """
        pass

    # def ground_gradient(self, air_gradient, airspeed, headwind, r=0):
    #     # true_ground_speed = airspeed - headwind
    #     return round((air_gradient / 100) * airspeed / headwind, r)

    def maximum_payload(self, weight_empty, weight_of_fuel, passengers:list=[]):
        """
        Calculate the maximum payload of the aircraft

        Formula
        -------

            max_payload = (weight_empty + weight_of_fuel) - max_gross_weight or max_takeoff_weight
            max_payload - passengers [70 for men, 57.6 for women]
        """
        pass

    def save(self):
        data_to_save = {
            'airplane': {
                'name': self.__class__.__name__,
                'characteristics': self.characteristics()
            }
        }
        with open('mydata.json', 'w') as f:
            json.dump(data_to_save, f, indent=4)
        return data_to_save


class Cessna(Airplane):
    manufacturer = 'Cessna'


class Airbus(Airplane):
    manufacturer = 'Airbus'


class Boeing(Airplane):
    manufacturer = 'Airbus'


class Dassault(Airplane):
    manufacturer = 'Dassault'
