#!/usr/bin/env python3
"""
This module provides the class `LIFOCache` which
inherits from BaseCaching
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """defines the class"""
    def __init__(self):
        """initializes the class"""
        super().__init__()
        self.last_key = ''

    def put(self, key, item):
        """assigns value based on lifo to the dictionary"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > super().MAX_ITEMS:
                print("DISCARD: {}".format(self.last_key))
                del self.cache_data[self.last_key]

            self.last_key = key

    def get(self, key):
        """returns the value of the key"""
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
