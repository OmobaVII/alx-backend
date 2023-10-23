#!/usr/bin/env python3
"""
This module contains just one function index_range
the function takes two arguments page and page_size
"""


def index_range(page, page_size):
    """Calculates the start and end indexes for a given page
    and page size. Returns a tuple of size two which
    contains a start index and an end index"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
