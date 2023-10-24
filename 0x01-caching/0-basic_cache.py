#!/usr/bin/python3
"""
This module creates a class `BasicCache` that inherits
from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """defines the class BasicCache which
    inherits from BaseCaching"""
    def __init__(self):
        """ Initiliaze"""
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary self.cache_data"""
        if key is not None or item is not None:
            self.cache_data[key] = item
        else:
            pass

    def get(self, key):
        """returns the value in self.cache_data liked to key"""
        if key is not None or key in self.cache_data.keys():
            for k, v in self.cache_data.items():
                if k == key:
                    return v
        else:
            return None