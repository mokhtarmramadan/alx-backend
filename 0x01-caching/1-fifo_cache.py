#!/usr/bin/env python3
''' FIFOCache class '''
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    ''' A caching system that follows FIFO pattern '''

    def put(self, key, item):
        ''' Assigns key to it's item in the chache dict
            if data is more than the max_limit we pop
            the first put element '''
        if key is not None and item is not None:
            if (len(self.cache_data) >= BaseCaching.MAX_ITEMS and
                    key not in list(self.cache_data.keys())):
                first_key = list(self.cache_data.keys())[0]
                self.cache_data.pop(first_key)
                print("DISCARD:", first_key)
            self.cache_data[key] = item

    def get(self, key):
        ''' Gets a certain item by it's key '''
        value = self.cache_data.get(key, None)
        return value
