#!/usr/bin/python3
"""
This module creates a class `BasicCache` that inherits
from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """defines the class BasicCache which
    inherits from BaseCaching"""
    def put(self, key, item):
        """assign to the dictionary self.cache_data"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """returns the value in self.cache_data liked to key"""
        if key is not None or key in self.cache_data.keys():
            return self.cache_data.get(key)
        else:
            return None
