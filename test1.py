#!/usr/bin/env python

from __future__ import division, with_statement
from numpy import *
import scipy.weave

class index(object):
    def __init__(self, *args):
        print 'creating'
        self.slices = args
    def __enter__(self):
        print 'entering'
        return self.slices
    def __exit__(self, exc_type, exc_value, traceback):
        print 'exiting'

with index((2, 3), (4, 6)) as (i, j):
    print i
    print j

