#!/usr/bin/env python3
'''Module for converting key-value pairs.
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Returns a tuple of the key and the square of its value.
    '''
    return (k, float(v**2))
