#!/usr/bin/env python3
"""
This module contains copies the module 1-simple_pagination
then implements a get_hyper method
"""
import csv
import math
from typing import List, Dict


def index_range(page, page_size):
    """Calculates the start and end indexes for a given page
    and page size. Returns a tuple of size two which
    contains a start index and an end index"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """initializes the class"""
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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """a method that returns a dictionary containing:

        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        return_dict = {
                "page_size": len(data),
                "page": page,
                "data": data,
                "next_page": page + 1 if page < total_pages else None,
                "prev_page": page - 1 if page > 1 else None,
                "total_pages": total_pages
                }

        return return_dict

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """returns a dict with index, next_index, page_size and data"""
        assert isinstance(index, int) and index < len(self.indexed_dataset())
        assert isinstance(page_size, int) and page_size > 0

        data = []
        next_index = index + page_size

        for a in range(index, index + page_size):
            if not self.indexed_dataset().get(a):
                a += 1
                next_index += 1
            data.append(self.indexed_dataset()[a])

        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data
            }
