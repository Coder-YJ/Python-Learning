# -*- coding: utf-8 -*-
#！/usr/bin/env python
"readTextFile.py --- read text file"

fname = input('Enter filename:')

try:
    fobj = open(fname,'r')
except IOError as e:
    print (" *** file open error:",e)
else:
    for eachline in fobj:
	    print (eachline)
    fobj.close()