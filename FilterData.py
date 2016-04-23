# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 09:14:22 2016

@author: askery
"""


from datetime import datetime
start=datetime.now()

#1 - folders location
#1.1 - input
path = "/media/data/rowData_201304_201602/*.TXT"

#1.2 - output
outpath = "/media/data/outputData/"

#2 - get the path of every single file in the path folder, also sort the list
import glob   
files = glob.glob(path)
files.sort()   

#3 - open file, filter lines
# readlines() instead

for i in files:
    output  = outpath + i[-12:]
    fw      = open(output, "w+")
    fo      = open(i, "r+")
    line    = fo.readlines()
    if 'NEG' in line:
        fw.write(line)


print datetime.now() - start