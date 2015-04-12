import sys
"""
@author Blakely Madden
@date 2014-04-08
@purpose caching related objects and functions
"""

## this file is still being worked on. not ready for use.
## this is the cache for the DB. not originally part of the project,
## but i decided to add it for fun

class CacheItem (object):
    """
    @author Blakely Madden
    @date 2014-04-08
    @purpose a wrapper for items in the cache
    @params self.item (the item to cache)
    """
    def __init__ (self, item):
        self.item = item
        self.hits = 0
        self.size = sys.getsizeof(item)

class DBCache (object):
    """
    @author Blakely Madden
    @date 2014-04-08
    @purpose this is a cache for DB requests
    @params self.limit (upper bound size in bytes of the cache)
    """
    def __init__ (self, limit):
        """
        @author Blakely Madden
        @date 2014-04-08
        @purpose Initialize a DBCache object
        @args limit [int]
        @return None
        @exceptions None
        @can_block False
        """
        self.size_limit = limit
        self.cache = {}

    def add_item (self, item):
        """
        @author Blakely Madden
        @date 2014-04-08
        @purpose adds an item to the cache
        @args item [string]
        @return None
        @exceptions None
        @can_block False
        """
        new_item = CacheItem (item)
        cached = self.cache.get(hash(item))
        if cached is None:
            self.evict_or_add (new_item)
        cached.hits += 1

    def find_eviction (self, item):
        for key,val in self.cache:
            val.

    def evict_or_add (self, item):
        """
        @author Blakely Madden
        @date 2014-04-08
        @purpose decides whether or not something needs to be evicted from the
         cache
        @args host [string], user [string], passwd [string], db [string]
        @return None
        @exceptions None
        @can_block False
        """
        
