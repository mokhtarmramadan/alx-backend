#!/usr/bin/env python3
''' index range '''


def index_range(page, page_size):
    '''  takes two integer arguments page and page_size
     return in a list for those particular pagination parameters '''
    end_index = page * page_size
    start_index = end_index - page_size
    return (start_index, end_index)
