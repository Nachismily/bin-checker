#!/usr/bin/env python
# Space Howen 2019-2020
from urllib2 import *

bin = raw_input('INGRESE BIM:')
api = "https://lookup.binlist.net/" + bin
consultar = urlopen(api).read()
print consultar
