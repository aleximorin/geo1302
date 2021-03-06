# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 19:54:19 2017

@author: giroux
"""

import sys
import inspect,dis

def nargout():
    """
    Return how many values the caller is expecting

    taken from
    http://stackoverflow.com/questions/16488872/python-check-for-the-number-of-output-arguments-a-function-is-called-with
    """
    if sys.version_info[1] > 5:
        off = 1
    else:
        off = 0
    f = inspect.currentframe()
    f = f.f_back.f_back
    c = f.f_code
    i = f.f_lasti
    bytecode = c.co_code
    instruction = bytecode[i+3-off]
    if instruction == dis.opmap['UNPACK_SEQUENCE']:
        howmany = bytecode[i+4-off]
        return howmany
    elif instruction == dis.opmap['POP_TOP']:
        return 0
    return 1
