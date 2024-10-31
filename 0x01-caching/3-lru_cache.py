#!/usr/bin/env python3
""" module to implement LRUCache class """

BaseCaching = __import__('base_caching').BaseCaching
from collections import OrderedDict

class LRUCache(BaseCaching):
    """ LRU cache class """

    def __init__(self):
        """ Constructor """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache"""
        if key is None or item is None:
            return

            self.cache_data.move_to_end(key)
        self.cache_data[key] = item
        
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lru_key = next(iter(self.cache_data))
            del self.cache_data[lru_key]
            print("DISCARD: {}".format(lru_key))

    def get(self, key):
        """ Get an item by key"""
        if key is None or key not in self.cache_data:
            return None

        self.cache_data.move_to_end(key)
        return self.cache_data[key]
