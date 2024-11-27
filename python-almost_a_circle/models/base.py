#!/usr/bin/python3
"""
This module defines the `Base` class, which serves as the base class
for other models in this project.
"""

class Base:
    """
    A base class to manage unique IDs for instances.

    Attributes:
        __nb_objects (int): Tracks the number of objects created.
        id (int): Unique identifier for the instance.
    """
    __nb_objects = 0  # Private class attribute to track objects

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        Args:
            id (int, optional): If provided, sets the ID for the instance.
                               Otherwise, assigns a new unique ID.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
