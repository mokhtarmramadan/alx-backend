#!/usr/bin/env python3
''' LRU Caching '''
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    ''' BaseCaching class '''
    
    elements_key = [] # recently used first

    def put(self, key, item):
        ''' Assigns key to it's item in the chache dict
            if data is more than the max_limit we pop
            we discard the least recently used element '''
        if key is not None and item is not None:
            discard_element = ''
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard_element = LRUCache.elements_key.pop(0)
                del BaseCaching.cache_data[discard_element]
                print("Discard:", discard_element)
            self.cache_data[key] = item
            LRUCache.elements_key.append(key)
    
    def get(self, key):
        ''' Gets a certain item by it's key '''
        value = self.cache_data.get(key, None)
        return value
