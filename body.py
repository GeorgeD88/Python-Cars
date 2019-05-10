class Body:  # Object representing the body of a car.

    def __init__(self, **kwargs):  # Car Body Object                           --------------------------------------------------------------------------
        self.style = kwargs.get('type', 'sedan')                               # Style of the body, ex. roadster, coupé, convertible, etc.
        self.curb_weight = kwargs.get('weight', 4000)                          # Curb weight of the car: Total mass of a vehicle with standard equipment 
        self.doors = kwargs.get('doors', [Door(position='front left'),         # List of door objects of the car.
                                          Door(position='front right'),        # |:
                                          Door(position='rear left'),          # |:
                                          Door(position='rear right')])        # \:


class Door:  # Object representing a car door.

    def __init__(self, **kwargs):  # Car Door Object                          --------------------------------------------------------------------------
        self.type = kwargs.get('type', 'standard')                             # Type of car door, ex. butterfly door, suicide doors, etc.
        self.position = kwargs.get('position', None)                           # Position of the car door, ex. front left, rear right, etc.
                                                                               

class Seat:  # Object representing a seat in a car (not car seat).

    def __init__(self, **kwargs):  # Car Seat Object                          --------------------------------------------------------------------------
        self.shape = kwargs.get('type', 'standard')                            # The shape of the car seat, ex. bucket, standard, rally, etc.
        self.position = kwargs.get('position', None)                           # The position of the seat in the car, ex. driver, rear center, etc.
        self.adjustable = kwargs.get('adjustable', True)                       # Whether or not the seat is adjustable: true or false
        if self.adjustable:                                                    # If the seat object is adjustable <= if statement (not an attribute)
            self.power_adjustable = kwargs.get('power adjustable', False)      # |= Whether or not the seat is power adjustable: true or false
            self.adjustable_lumbar = kwargs.get('lumbar adjustable', False)    # |= Whether or not the seat has adjustable lumbar support: true or false
            self.n_way_adjustable = kwargs.get('n-way adjustable', 3)          # \= Number of ways that the seat can be adjusted, ex. 3,
