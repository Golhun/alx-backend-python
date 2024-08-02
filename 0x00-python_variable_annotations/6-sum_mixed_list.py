#!/usr/bin/env python3
'''Module for summing mixed-type lists.
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Returns the sum of a list containing ints and floats.
    '''
    return float(sum(mxd_lst))
