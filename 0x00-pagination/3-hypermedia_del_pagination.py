#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        ''' two integer arguments: index with a None default value and
        page_size with default value of 10.

            index: the current start index of the return page.
            next_index: the next index to query with
            page_size: the current page size
            data: the actual page of the dataset'''

        dataset = self.indexed_dataset()
        data_payload = []
        limit = index + page_size

        assert isinstance(index, int)
        assert index < len(dataset)
        assert isinstance(page_size, int)
        assert limit < len(dataset)
        i = index
        while (i < limit):
            try:
                data_payload.append(dataset[i])
            except KeyError:
                limit += 1
                assert limit < len(dataset)
            i += 1
        return {
                'index': index,
                'data': data_payload,
                'page_size': page_size,
                'next_index': limit
                }
