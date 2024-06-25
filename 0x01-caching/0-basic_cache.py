#!/usr/bin/env python3
''' BasicCache class '''
from BaseCaching import BaseCaching


class BasicCache(BaseCaching):
    ''' A caching system class '''

    def put(self, key, item):
        ''' Assign new data to the dictionary
            if key or item don't exist, this method
            will skip adding it '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        ''' Returns the value of a certain key in
            the dict or None if there's not any '''
        value = self.cache_data.get(key, None)
        return value
