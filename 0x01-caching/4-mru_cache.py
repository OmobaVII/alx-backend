#!/usr/bin/env python3
"""
This module provides the class `MRUCache` which
inherits from BaseCaching
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """defines the class"""
    def __init__(self):
        """initializes the class"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """assigns value based on lifo to the dictionary"""
        if key is not None and item is not None:
            if len(self.cache_data) >= super().MAX_ITEMS:
                mru_key = self.order.pop()
                del self.cache_data[mru_key]
                print("DISCARD: {}".format(mru_key))

            self.cache_data[key] = item
            if key in self.order:
                self.order.remove(key)
            self.order.append(key)

    def get(self, key):
        """returns the value of the key"""
        if key is not None:
            if key in self.cache_data:
                self.order.remove(key)
                self.order.append(key)
                return self.cache_data[key]
        return None
