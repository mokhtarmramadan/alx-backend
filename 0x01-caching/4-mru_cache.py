#!/usr/bin/python3
''' MRC Caching '''
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    ''' A caching system that folow MRU algorithm '''
    elements_key = []  # Sorted by most used

    def put(self, key, item):
        ''' Assigns key to it's item in the chache dict
            if data is more than the max_limit we pop
            we discard the Most recently used element '''
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard_element = ''
                if key not in list(self.cache_data.keys()):
                    discard_element = MRUCache.elements_key.pop(0)
                    del self.cache_data[discard_element]
                    print("DISCARD:", discard_element)
                else:
                    MRUCache.elements_key.remove(key)
            MRUCache.elements_key.insert(0, key)
            self.cache_data[key] = item

    def get(self, key):
        ''' Gets a certain item by it's key and adds them in the
        end of the list as the were recently used '''
        value = self.cache_data.get(key, None)
        if value is not None:
            MRUCache.elements_key.remove(key)
            MRUCache.elements_key.insert(0, key)
        return value
