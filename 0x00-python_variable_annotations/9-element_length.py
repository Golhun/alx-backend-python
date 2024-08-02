#!/usr/bin/env python3
'''Module for computing lengths of sequences.
'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Returns a list of tuples containing sequences and their lengths.
    '''
    return [(i, len(i)) for i in lst]
