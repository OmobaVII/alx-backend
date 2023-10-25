#!/usr/bin/env python3
"""
This module provides the class `LRUCache` which
inherits from BaseCaching
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """defines the class"""
    def __init__(self):
        """initializes the class"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """assigns value based on lifo to the dictionary"""
        if key is not None and item is not None:
            if len(self.cache_data) >= super().MAX_ITEMS:
                lru_key = self.order.pop(0)
                print("DISCARD: {}".format(lru_key))
                del self.cache_data[lru_key]

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
