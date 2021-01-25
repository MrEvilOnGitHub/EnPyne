import math

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
        if type(other) is vector3D:
            return vector3D(
                x=self._x+other._x,
                y=self._y+other._y,
                z=self._z+other._z)
        else:
            raise TypeError("Vectoraddition can only be performed with two vectors")

    def __isub__(self, other):
        if type(other) is vector3D:
            return vector3D(
                x=self._x-other._x,
                y=self._y-other._y,
                z=self._z-other._z)
        else:
            raise TypeError("Vectorsubstraction can only be performed with two vectors")

    def __imul__(self, other):
        if type(other) is int or type(other) is float:
            return vector3D(
                x=self._x*other,
                y=self._y*other,
                z=self._z*other)
        else:
            raise TypeError()

    def __idiv__(self, other):
        if type(other) is int or type(other) is float:
            if other != 0 or other != 0.0:
                return vector3D(
                    x=self._x/other,
                    y=self._y/other,
                    z=self._z/other)
            else:
                raise ZeroDivisionError
        else:
            raise TypeError()

    def __add__(self, other):
        if type(other) is vector3D:
            return vector3D(
                x=self._x+other._x,
                y=self._y+other._y,
                z=self._z+other._z)
        else:
            raise TypeError("Vectoraddition can only be performed with two vectors")

    def __sub__(self, other):
        if type(other) is vector3D:
            return vector3D(
                x=self._x-other._x,
                y=self._y-other._y,
                z=self._z-other._z)
        else:
            raise TypeError("Vectorsubstraction can only be performed with two vectors")

    def __mul__(self, other):
        if type(other) is int or type(other) is float:
            return vector3D(
                x=self._x*other,
                y=self._y*other,
                z=self._z*other)
        else:
            raise TypeError()

    def __truediv__(self, other):
        if type(other) is int or type(other):
            return vector3D(
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

    def set_norm_x(self, value):
        if type(value) is int or type(value) is float:
            self._norm_x = value
        else:
            raise ValueError(f"Expected float or int, received {type(value)} instead")

    def set_norm_y(self, value):
        if type(value) is int or type(value) is float:
            self._norm_y = value
        else:
            raise ValueError(f"Expected float or int, received {type(value)} instead")

    def set_norm_z(self, value):
        if type(value) is int or type(value) is float:
            self._norm_z = value
        else:
            raise ValueError(f"Expected float or int, received {type(value)} instead")

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
        self._norm_x = self._x / length
        self._norm_y = self._y / length
        self._norm_z = self._z / length