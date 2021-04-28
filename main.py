import math
import types
#import OpenGL Not used so far.         Uncomment when adding a renderer class

class definitions:
    """
    A class containing definitions for various other elements used in this engine
    """
    class vector2D:
        """
        A representation of a 2D vector
        """

        # Magic methods
        def __init__(self, x=1, y=0):
                if x is float or int and y is float or int:
                    self.__x = x
                    self.__y = y
                    self.normalize()

        def __str__(self):
            return f"x: {self.__x} ; y: {self.__y} \n norm_x: {self.__norm_x} ; norm_y: {self.__norm_y} \n length: {self.get_length()}"

        def __iadd__(self, other):
            if type(other) is definitions.vector2D:
                return definitions.vector2D(
                    x=self.__x+other.x,
                    y=self.__y+other.y)
            else:
                raise TypeError("Vectoraddition can only be performed with two vectors")

        def __isub__(self, other):
            if type(other) is definitions.vector2D:
                return definitions.vector2D(
                    x=self.__x-other.x,
                    y=self.__y-other.y)
            else:
                raise TypeError("Vectorsubstraction can only be performed with two vectors")

        def __imul__(self, other):
            if type(other) is int or type(other) is float:
                return definitions.vector2D(
                    x=self.__x*other,
                    y=self.__y*other)
            else:
                raise TypeError()

        def __idiv__(self, other):
            if type(other) is int or type(other) is float:
                if other != 0 or other != 0.0:
                    return definitions.vector2D(
                        x=self.__x/other,
                        y=self.__y/other)
                else:
                    raise ZeroDivisionError
            else:
                raise TypeError()

        def __add__(self, other):
            if type(other) is definitions.vector2D:
                return definitions.vector2D(
                    x=self.__x+other.x,
                    y=self.__y+other.y)
            else:
                raise TypeError("Vectoraddition can only be performed with two vectors")

        def __sub__(self, other):
            if type(other) is definitions.vector2D:
                return definitions.vector2D(
                    x=self.__x-other.x,
                    y=self.__y-other.y)
            else:
                raise TypeError("Vectorsubstraction can only be performed with two vectors")

        def __mul__(self, other):
            if type(other) is int or type(other) is float:
                return definitions.vector2D(
                    x=self.__x*other,
                    y=self.__y*other)
            else:
                raise TypeError()

        def __truediv__(self, other):
            if type(other) is int or type(other):
                return definitions.vector2D(
                    x=self.__x/other,
                    y=self.__y/other)
            else:
                raise TypeError()

        # Other methods
        def normalize(self):
            length = self.get_length()
            if length != 0:
                self.__norm_x = self.__x / length
                self.__norm_y = self.__y / length
            else:
                raise ZeroDivisionError

        def get_length(self):
            return math.sqrt(self.__x ** 2 + self.__y ** 2)

        # Get'er and Set'er
        @property
        def __x(self):
            return self.__x

        @property
        def __y(self):
            return self.__y

        @property
        def __norm_x(self):
            return self.__norm_x

        @property
        def __norm_y(self):
            return self.__norm_y

        @__x.setter
        def __x(self, value):
            if type(value) is int or type(value) is float:
                self.__x = value
                self.normalize()
            else:
                raise ValueError(f"Expected float or int, received {type(value)} instead")

        @__y.setter
        def __y(self, value):
            if type(value) is int or type(value) is float:
                self.__y = value
                self.normalize()
            else:
                raise ValueError(f"Expected float or int, received {type(value)} instead")


        # variables
        __x = float(1.0)
        __y = float(0.0)
        __norm_x = float(1)
        __norm_y = float(0)

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

    class scene2D:
        """
        Base class for scenes with 2d objects. Includes an event handler
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

    class child2D:
        """
        General class for 2D objects
        """
        def __init__(self, position=definitions.vector2D, direction=definitions.vector2D) -> None:
            self.position = position
            self.direction = direction

        position = definitions.vector2D
        direction = definitions.vector2D
        children = []
        children_state = []
        a = None # Type of the child

        # Decorator for new sub-childs to this child
        def link(self,obj=None,*,state=0) -> object:
            self.children.append(obj)
            self.children_state.append(state)
            return obj

        def unlink_child(self, child) -> None:
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
    class input_events:
        def add_event(self, func, *, event="key_pressed") -> types.MethodType:
            self._events.append(func)
            self._event_triggers.append(event)
            return func

        def on_event(self):
            pass

        _events = []
        _event_triggers = []

    def __init__(self):
        self.user_events = self.input_events

class renderer2D:
    """
    Base rendering class for 2d objects
    """
    pass

# exceptions

class BaseError(Exception):
    """Base exception class for this module"""
    pass

class EventError(BaseError):
    """Exception raised when attempting to add a non-callable event object"""
    pass

def run():
    pass
