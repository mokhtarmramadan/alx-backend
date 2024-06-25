#!/usr/bin/env python3
''' LIFOCache class '''
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    ''' A caching system that uses LIFO pattern (stack) '''
    last_in_key = ''

    def put(self, key, item):
        ''' Assigns key to it's item in the chache dict
            if data is more than the max_limit we pop
            the last put element '''
        if key is not None and item is not None:
            if (len(self.cache_data) >= BaseCaching.MAX_ITEMS and
                    key not in list(self.cache_data.keys())):
                del self.cache_data[LIFOCache.last_in_key]
                print("DISCARD:", LIFOCache.last_in_key)
            self.cache_data[key] = item
            LIFOCache.last_in_key = key

    def get(self, key):
        ''' Gets a certain item by it's key '''
        value = slef.cache_data.get(key, None)
        return value
