#!/usr/bin/env python3
''' LFU Caching '''
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    ''' A caching system that uses LFU algo '''
    element_frequency = {}

    def discard(self):
        ''' finds the element to be discard '''
        mini_freq = sorted(LFUCache.element_frequency.values())[0]
        for k, v in LFUCache.element_frequency.items():
            if LFUCache.element_frequency[k] == mini_freq:
                discard_element = k
                del self.cache_data[k]
                del LFUCache.element_frequency[k]
                break
        print("DISCARD:", k)

    def put(self, key, item):
        ''' Assigns key to it's item in the chache dict
            if data is more than the max_limit we pop
            we discard the least recently used element '''
        if key is not None and item is not None:
            discard_element = ''
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key not in list(self.cache_data.keys()):
                    self.discard()
                    LFUCache.element_frequency[key] = 1
                    self.cache_data[key] = item
                else:
                    freq = LFUCache.element_frequency[key] + 1
                    del LFUCache.element_frequency[key]
                    LFUCache.element_frequency[key] = freq
                    del self.cache_data[key]
                    self.cache_data[key] = item
            else:
                LFUCache.element_frequency[key] = 1
                self.cache_data[key] = item

    def get(self, key):
        ''' Gets a certain item by it's key and adds them in the
        beginning fo the list as the were recently used '''
        value = self.cache_data.get(key, None)
        if value is not None:
            freq = LFUCache.element_frequency[key] + 1
            del LFUCache.element_frequency[key]
            LFUCache.element_frequency[key] = freq
        return value
