#!/usr/bin/env python3
"""
This module provides the class `FIFOCache` which
inherits for BaseCaching
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """defines the class"""
    def __init__(self):
        """initializes the class"""
        super().__init__()

    def put(self, key, item):
        """assigns to the dict self.cache_data"""
        if key is not None and item is not None:
            if key in self.cache_data.keys():
                self.cache_data[key] = item
            else:
                if len(self.cache_data) >= super().MAX_ITEMS:
                    first_key = next(iter(self.cache_data))
                    print("DISCARD: {}".format(first_key))
                    del self.cache_data[first_key]

                self.cache_data[key] = item

    def get(self, key):
        """returns the value of the key"""
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
