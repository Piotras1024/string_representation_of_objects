class Position:
    instances = {}

    def __init__(self, latitude, longitude):
        if not (-90 <= latitude <= +90):
            raise ValueError(f"Latitude {latitude} out of range")

        if not (-180 <= longitude <= +180):
            raise ValueError(f"Longitude {longitude} out of range")

        self._latitude = latitude
        self._longitude = longitude

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

    @property
    def latitude_hemisphere(self) -> str:
        return "N" if self.latitude >= 0 else "S"

    @property
    def longitude_hemisphere(self) -> str:
        return "E" if self.longitude >= 0 else "W"

    def __repr__(self) -> str:
        return f"{typename(self)}(latitude={self.latitude}, longitude={self.longitude})"

    def __str__(self) -> str:
        return f"{abs(self.latitude)}° {self.latitude_hemisphere}, " \
               f"{abs(self.longitude)}° {self.longitude_hemisphere}"

    def __format__(self, format_spec) -> str:
        component_format_spec = ".2f"
        prefix, dot, precision = format_spec.partition(".")
        if dot:
            num_decimal_places = precision #int(precision) na KIEGO ROBIE Z TEGO INTA ??? !!!
            component_format_spec = f".{num_decimal_places}f"
            # num_decimal_places = int(precision)
            # component_format_spec = f".{num_decimal_places}f"

        latitude = format(abs(self.latitude), component_format_spec)
        longitude = format(abs(self.longitude), component_format_spec)

        return f"{latitude}° {self.latitude_hemisphere}, " \
               f"{longitude}° {self.longitude_hemisphere}"

# DOT . is shorting to smaller precision .2f is shorting to 2 places after DOT .
# format(q, "5f")   -->> by default f = 6 so format(q, "f") means format(q, "6f")
# '0.000077'
# print(f"magic of format with f string {q:.6f}" || analogy magic >> f"{q:.2e}" after. 2 digits and E
# magic of format with f string 0.000077


class EarthPosition(Position):
    pass


class MarsPosition(Position):
    pass


def typename(obj):
    return type(obj).__name__


'''

from position_010 import*
oslo = Position(60.0, 10.7)
repr(oslo)
'<position_010.Position object at 0x000002568E13BA90>'
str(oslo)
'<position_010.Position object at 0x000002568E13BA90>'
format(oslo)
'<position_010.Position object at 0x000002568E13BA90>'


dir(object)
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', 
'__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
'__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

'''
