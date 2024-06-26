#!/usr/bin/python3
""" 0-main """


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Args:
        BaseCaching (_type_): _description_
    """

    def __init__(self):
        """_summary_
        """
        super().__init__()

    def put(self, key, item):
        """_summary_

        Args:
            key (_type_): _description_
            item (_type_): _description_
        """
        if key == None or item == None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """_summary_

        Args:
            key (_type_): _description_

        Returns:
            _type_: _description_
        """
        if key == None:
            return None
        return self.cache_data.get(key)
