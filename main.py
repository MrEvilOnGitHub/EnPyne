import math

def __init__(self):
    pass

class definitions:
    class vector3D:
        # magic methods
        def __init__(self, x=float(1.0), y=float(0.0), z=float(0.0)):
            self.set_x(x)
            self.set_y(y)
            self.set_z(z)
            self.normalize()

        def __str__(self):
            return f"x: {self._x} ; y: {self._y} ; z: {self._z} \n norm_x: {self._norm_x} ; norm_y: {self._norm_y} ; norm_z: {self._norm_z} \n length: {self.get_length()}"

        def __iadd__(self, other):
            if type(other) is definitions.vector3D:
                return definitions.vector3D(
                    x=self._x+other._x,
                    y=self._y+other._y,
                    z=self._z+other._z)
            else:
                raise TypeError("Vectoraddition can only be performed with two vectors")

        def __isub__(self, other):
            if type(other) is definitions.vector3D:
                return definitions.vector3D(
                    x=self._x-other._x,
                    y=self._y-other._y,
                    z=self._z-other._z)
            else:
                raise TypeError("Vectorsubstraction can only be performed with two vectors")

        def __imul__(self, other):
            if type(other) is int or type(other) is float:
                return definitions.vector3D(
                    x=self._x*other,
                    y=self._y*other,
                    z=self._z*other)
            else:
                raise TypeError()

        def __idiv__(self, other):
            if type(other) is int or type(other) is float:
                if other != 0 or other != 0.0:
                    return definitions.vector3D(
                        x=self._x/other,
                        y=self._y/other,
                        z=self._z/other)
                else:
                    raise ZeroDivisionError
            else:
                raise TypeError()

        def __add__(self, other):
            if type(other) is definitions.vector3D:
                return definitions.vector3D(
                    x=self._x+other._x,
                    y=self._y+other._y,
                    z=self._z+other._z)
            else:
                raise TypeError("Vectoraddition can only be performed with two vectors")

        def __sub__(self, other):
            if type(other) is definitions.vector3D:
                return definitions.vector3D(
                    x=self._x-other._x,
                    y=self._y-other._y,
                    z=self._z-other._z)
            else:
                raise TypeError("Vectorsubstraction can only be performed with two vectors")

        def __mul__(self, other):
            if type(other) is int or type(other) is float:
                return definitions.vector3D(
                    x=self._x*other,
                    y=self._y*other,
                    z=self._z*other)
            else:
                raise TypeError()

        def __truediv__(self, other):
            if type(other) is int or type(other):
                return definitions.vector3D(
                    x=self._x/other,
                    y=self._y/other,
                    z=self._z/other)
            else:
                raise TypeError()

        # Get'er and Set'er
        def set_x(self, value):
            if type(value) is int or type(value) is float:
                self._x = value
            else:
                raise ValueError(f"Expected float or int, received {type(value)} instead")

        def set_y(self, value):
            if type(value) is int or type(value) is float:
                self._y = value
            else:
                raise ValueError(f"Expected float or int, received {type(value)} instead")

        def set_z(self, value):
            if type(value) is int or type(value) is float:
                self._z = value
            else:
                raise ValueError(f"Expected float or int, received {type(value)} instead")

        def get_x(self):
            return self._x

        def get_y(self):
            return self._y

        def get_z(self):
            return self._z

        def get_norm_x(self):
            return self._norm_x

        def get_norm_y(self):
            return self._norm_y

        def get_norm_z(self):
            return self._norm_z

        # Get length of vector
        def get_length(self):
            return math.sqrt((self._x * self._x) + (self._y * self._y) + (self._z * self._z))

        # Normalizer (set vector length to 1)
        def normalize(self):
            length = self.get_length()
            if length != 0:
                self._norm_x = self._x / length
                self._norm_y = self._y / length
                self._norm_z = self._z / length
            else:
                raise ZeroDivisionError

class object_tree:
    class scene3D:
        def __init__(self):
            pass # modify root to fit to new object inheriting from this class

        children = [] # List of children objects
        children_state = [] # State of each child, index-linked

        def new_child(self, child, initial_state):
            pass

        class child:
            def __init__(self):
                pass

            position = definitions.vector3D
            viewing_direction = definitions.vector3D

class event_handler:
    pass
    # Tick system:
    # Global & live ticks
    # - Global try to update every 1/nth of a seconds
    # - live try to update as often as possible
    # 
    # Events are divided into multiple categories:
    # - Active: Update every tick (global or live)
    # - Once: Perform event once, then set it to sleep
    # - Sleep: don't activate unless explicitly called
    # 
    # Sub-categories:
    # - Input: Triggers on User input when not sleeping
    # - Engine: Events to keep the engine working (This includes rendering, physics etc)
    # - Object: Events asigned to objects that don't fit into any of the above categories

# exceptions

class BaseError(Exception):
    """Base exception class for this module"""
    pass

class EventError(BaseError):
    """Exception raised when attempting to add a non-callable event object"""
    pass

def run():
    pass