class Engine:  # Object representing a car engine.

    def __init__(self, **kwargs):  # Car Engine Object                         --------------------------------------------------------------------------
        self.name = kwargs.get('name', 'I4')                                   #
        self.cylinders = kwargs.get('cylinders', 4)                            #
        self.inlet_valves = kwargs.get('inlet', 2)                             #
        self.exhaust_valves = kwargs.get('exhaust', 2)                         #
        self.configuration = kwargs.get('configuration', 'inline')             #
        self.compression_ratio = kwargs.get('compression ration', 20)          # 20 is a 20:1 ratio
        self.octane = kwargs.get('octane', 87)                                 #
        self.turbocharger = kwargs.get('turbocharger', False)                  #
        self.supercharger = kwargs.get('supercharger', False)                  #


class Tire:  # Object representing a car tire.

    def __init__(self, **kwargs):  # Car Tire Object                           --------------------------------------------------------------------------
        self.brand = kwargs.get('brand', None)                                 #
        self.width = kwargs.get('width', None)                                 #
        # TODO: Write the rest of the attributes.                              #


class Transmission:  # Object representing the transmission of a car.

    def __init__(self, **kwargs):  # Car Transmission Object                   --------------------------------------------------------------------------
        self.type = kwargs.get('type', 'automatic')                            # ex. dual clutch, manual, etc.
        self.gears = kwargs.get('gears', 6)                                    #
        self.gear_ratios = []                                                  #
