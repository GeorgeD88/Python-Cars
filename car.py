from Composition.Car.parts import *
from Composition.Car.body import *
import json
import sys


engine = Engine()                                                      # Default engine object to use when one isn't passed in the kwargs.
transmission = Transmission()                                          # Default transmission object to use when one isn't passed in the kwargs.
tire = Tire()                                                          # Default tire object to use when one isn't passed in the kwargs.


class Car:  # Object representing a car.

    def __init__(self, **kwargs):
        # Car Details                                                          --------------------------------------------------------------------------
        self.make = kwargs.get('make', None)         # ADD COLOR                          # Make of the car, ex. Mercedes-Benz, McLaren, etc.
        self.model = kwargs.get('model', None)                                 # Model of the car, ex. M5, Huracan, etc.
        self.year = kwargs.get('year', None)                                   # Year of the car, ex. 2008, 2017, etc.
        self.mileage = kwargs.get('mileage', None)                             # Mileage of the car, ex. 61,000 mi, 14,XXX mi, etc.
        self.VIN = kwargs.get('VIN', None)                                     # VIN number of the car, ex. 4TAVN52N4YZ694434, etc.
        # Car Parts and Systems                                                --------------------------------------------------------------------------
        self.engine = kwargs.get('engine', engine)
        self.drivetrain = kwargs.get('drivetrain', 'rear-wheel')               # Drivetrain of the car, ex. rear-wheel, all-wheel, etc.
        self.transmission = kwargs.get('transmission', transmission)         # Transmission object of the car
        self.tires = kwargs.get('tires', [tire]*4)     # List of tire objects of the car.
        self.seats = [Seat(position='driver'),                            # List of seat objects of the car.
                      Seat(position='passenger'),                         # |:
                      Seat(position='rear left'),                         # |:
                      Seat(position='rear center'),                       # |:
                      Seat(position='rear right')]                        # \:
        self.led_headlights = kwargs.get('led', False)                         # Whether or not the car has LED headlights: true or false.
        self.paddle_shifters = kwargs.get('paddle_shifters', False)            # Whether or not the car has paddle shifters: true or false.
        # Car Specifications                                                   --------------------------------------------------------------------------
        self.horsepower = kwargs.get('horsepower', None)                       # Horsepower of the car engine.
        self.torque = kwargs.get('torque', None)                               # Torque of the car engine.
        self.acceleration = kwargs.get('acceleration', None)                   # Acceleration of the car.
        self.top_speed = kwargs.get('top_speed', None)                         # Top speed of the car.

    def save_to_json(self, file_name: str):
        with open(file_name+'.json', 'w+') as out_file:
            save = dict_attrs(self)
            json.dump(save, out_file, indent=2)


def dict_attrs(obj: object) -> dict:
    attributes = {}
    obj_dict = obj.__dict__
    for attr in obj_dict:
        called_attr = obj_dict[attr]
        if is_container(called_attr):
            container = []
            for element in called_attr:
                container.append(dict_attrs(element))
            attributes[attr] = container
        elif is_object_of_import(called_attr):
            attributes[attr] = dict_attrs(called_attr)
        elif not is_object_of_import(called_attr):
            attributes[attr] = getattr(obj, attr)
        else:
            raise TypeError('HOW THE FUCK DID YOU GET HERE')
    return attributes


def is_container(value) -> bool:
    for container in [list, tuple, dict]:
        if isinstance(value, container):
            return True
    return False


def is_object_of_import(value) -> bool:
    for im_class in [Engine, Transmission, Tire, Body, Door, Seat]:  # For every imported class.
        if isinstance(value, im_class):
            return True
    return False  # If the function didn't already return True (and exit the function), the code continues to return False.


# TODO: Attempt __getitem__()
