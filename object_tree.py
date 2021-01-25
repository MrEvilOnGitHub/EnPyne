import definitions

class scene:
    def __init__(self):
        pass # modify root to fit to new object inheriting from this class

    children = [] # List of children objects
    children_state = [] # State of each child, index-linked

    def new_child(self, child, initial_state):
        pass

    class child:
        def __init__(self):
            pass

        position = definitions.vector3D(0,0,0)
        