#!/usr/bin/python3
'''script that contains a class that avoids dynamic created attributes'''


class LockedClass:
    """Locked class """

    __slots__ = ['first_name']

    def __init__(self):
        """ Init method """
        pass
