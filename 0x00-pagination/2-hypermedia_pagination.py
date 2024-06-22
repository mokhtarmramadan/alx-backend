#!/usr/bin/env python3
''' Simple pagination '''
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''  takes two integer arguments page and page_size
     return in a list for those particular pagination parameters '''
    end_index = page * page_size
    start_index = end_index - page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        ''' takes two integer arguments page with default value 1
        and page_size with default value 10 '''
        dataset = self.dataset()
        # Verify tha arguments are positive integers
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0
        start_index, end_index = index_range(page, page_size)
        data_payload = []
        if start_index >= len(dataset) or end_index >= len(dataset):
            return []
        for row in range(start_index, end_index):
            data_payload.append(list(dataset[row]))
        return data_payload

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        ''' returns a dictionary containing the following key-value pairs:
        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer '''
        
        next_page = page + 1
        prev_page = page - 1
        total_pages = (len(self.dataset()) + page_size - 1) // page_size
        data_payload = self.get_page(page, page_size)
        if data_payload == []:
            next_page = None
            page_size = 0
        if page == 1:
            prev_page = None
        return {
                'page_size': page_size,
                'page': page,
                'data': data_payload,
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': total_pages
                }
