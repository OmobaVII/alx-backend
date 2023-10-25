#!/usr/bin/env python3
"""
This module provides the class `LFUCache` which
inherits from BaseCaching
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """defines the class"""
    def __init__(self):
        """initializes class"""
        super().__init__()
        self.order = []
        self.freq = {}

    def put(self, key, item):
        """assigns value based on lifo to the dictionary"""
        if key is not None and item is not None:
            if len(self.cache_data) >= super().MAX_ITEMS:
                min_freq = min(self.freq.values())
                lfu_keys = []
                for k, freq in self.freq.items():
                    if freq == min_freq:
                        lfu_keys.append(k)
                if len(lfu_keys) > 1:
                    lru_key = self.order.pop(0)
                    if lru_key in lfu_keys:
                        lfu_keys.remove(lru_key)

                if lfu_keys:
                    lfu_key = lfu_keys[0]
                    print("DISCARD: {}".format(lfu_key))
                    del self.cache_data[lfu_key]
                    del self.freq[lfu_key]

            self.cache_data[key] = item
            self.freq[key] = self.freq.get(key, 0) + 1
            self.order.append(key)

    def get(self, key):
        """returns the value of the key"""
        if key is not None:
            if key in self.cache_data:
                self.freq[key] += 1
                self.order.remove(key)
                self.order.append(key)
                return self.cache_data[key]
        return None
