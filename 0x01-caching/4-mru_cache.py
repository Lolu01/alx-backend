#!/usr/bin/env python3
""" module to implement MRUCache class """

BaseCaching = __import__('base_caching').BaseCaching
from collections import OrderedDict

class MRUCache(BaseCaching):
    """ MRU cache class """

    def __init__(self):
        """ Constructor """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache"""
        if key is None or item is None:
            return

        self.cache_data[key] = item
        self.cache_data.move_to_end(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = next(reversed(self.cache_data))
            del self.cache_data[last_key]
            print("DISCARD: {}".format(last_key))

    def get(self, key):
        """ Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
