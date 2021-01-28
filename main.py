import math
import OpenGL

class definitions:
    """
    A class containing definitions for various other elements used in this engine
    """
    class vector3D:
        """
        A representation of a 3d vector
        """
        # magic methods
        def __init__(self, x=float(1.0), y=float(0.0), z=float(0.0)):
            self.set_x(x)
            self.set_y(y)
            self.set_z(z)
            self.normalize()

        def __str__(self):
            return f"x: {self.x} ; y: {self.y} ; z: {self.z} \n norm_x: {self.norm_x} ; norm_y: {self.norm_y} ; norm_z: {self.norm_z} \n length: {self.get_length()}"

        def __iadd__(self, other):
            if type(other) is definitions.vector3D:
                return definitions.vector3D(
                    x=self.x+other.x,
                    y=self.y+other.y,
                    z=self.z+other.z)
            else:
                raise TypeError("Vectoraddition can only be performed with two vectors")

        def __isub__(self, other):
            if type(other) is definitions.vector3D:
                return definitions.vector3D(
                    x=self.x-other.x,
                    y=self.y-other.y,
                    z=self.z-other.z)
            else:
                raise TypeError("Vectorsubstraction can only be performed with two vectors")

        def __imul__(self, other):
            if type(other) is int or type(other) is float:
                return definitions.vector3D(
                    x=self.x*other,
                    y=self.y*other,
                    z=self.z*other)
            else:
                raise TypeError()

        def __idiv__(self, other):
            if type(other) is int or type(other) is float:
                if other != 0 or other != 0.0:
                    return definitions.vector3D(
                        x=self.x/other,
                        y=self.y/other,
                        z=self.z/other)
                else:
                    raise ZeroDivisionError
            else:
                raise TypeError()

        def __add__(self, other):
            if type(other) is definitions.vector3D:
                return definitions.vector3D(
                    x=self.x+other.x,
                    y=self.y+other.y,
                    z=self.z+other.z)
            else:
                raise TypeError("Vectoraddition can only be performed with two vectors")

        def __sub__(self, other):
            if type(other) is definitions.vector3D:
                return definitions.vector3D(
                    x=self.x-other.x,
                    y=self.y-other.y,
                    z=self.z-other.z)
            else:
                raise TypeError("Vectorsubstraction can only be performed with two vectors")

        def __mul__(self, other):
            if type(other) is int or type(other) is float:
                return definitions.vector3D(
                    x=self.x*other,
                    y=self.y*other,
                    z=self.z*other)
            else:
                raise TypeError()

        def __truediv__(self, other):
            if type(other) is int or type(other):
                return definitions.vector3D(
                    x=self.x/other,
                    y=self.y/other,
                    z=self.z/other)
            else:
                raise TypeError()

        # Get'er and Set'er
        def set_x(self, value):
            if type(value) is int or type(value) is float:
                self.x = value
                self.normalize()
            else:
                raise ValueError(f"Expected float or int, received {type(value)} instead")

        def set_y(self, value):
            if type(value) is int or type(value) is float:
                self.y = value
                self.normalize()
            else:
                raise ValueError(f"Expected float or int, received {type(value)} instead")

        def set_z(self, value):
            if type(value) is int or type(value) is float:
                self.z = value
                self.normalize()
            else:
                raise ValueError(f"Expected float or int, received {type(value)} instead")

        def get_x(self):
            return self.x

        def get_y(self):
            return self.y

        def get_z(self):
            return self.z

        def get_norm_x(self):
            return self.norm_x

        def get_norm_y(self):
            return self.norm_y

        def get_norm_z(self):
            return self.norm_z

        # Get length of vector
        def get_length(self):
            return math.sqrt((self.x * self.x) + (self.y * self.y) + (self.z * self.z))

        # Normalizer (set vector length to 1)
        def normalize(self):
            length = self.get_length()
            if length != 0:
                self.norm_x = self.x / length
                self.norm_y = self.y / length
                self.norm_z = self.z / length
            else:
                raise ZeroDivisionError

class object_tree:
    class scene3D:
        """
        Base class for scenes with 3d objects. Includes an event handler
        """
        def __init__(self):
            self.events = event_handler

        children = [] # List of children objects
        children_state = [] # State of each child, index-linked

        def link_child(self, child, initial_state):
            """
            Link a child object to this scene
            """
            self.children.append(child)
            self.children_state.append(initial_state)
            return self.children.index(child)

        def unlink_child(self, child):
            """
            Unlink a child object from this scene
            """
            index = self.children.index(child)
            self.children.pop(index)
            self.children_state.pop(index)

    class child3D:
        """
        General class for 3D objects
        """
        def __init__(self, position=definitions.vector3D, direction=definitions.vector3D):
            self.position = position
            self.direction = direction

        position = definitions.vector3D
        direction = definitions.vector3D
        children = []
        children_state = []

        def link_child(self, child, initial_state):
            """
            Link a child object to this scene
            """
            self.children.append(child)
            self.children_state.append(initial_state)
            return self.children.index(child)

        def unlink_child(self, child):
            """
            Unlink a child object from this scene
            """
            index = self.children.index(child)
            self.children.pop(index)
            self.children_state.pop(index)

class event_handler:
    """
    Event handler system. Usually it shouldn't be neccessary to create a seperate instance of this
    since every scene assigns a new instance of it on initialisation
    """
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