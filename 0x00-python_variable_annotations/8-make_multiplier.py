#!/usr/bin/env python3
'''Module for creating multiplier functions.
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Returns a function that multiplies by a given factor.
    '''
    return lambda x: x * multiplier
