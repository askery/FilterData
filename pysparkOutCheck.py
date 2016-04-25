#0 -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 12:05:41 2015

@author: Askery Canabarro

THIS CODE IS TO PREPROCESS DATA FROM STOCK MARKET (BRAZILIAN STOCK LAYOUT ATTACHED)
"""

# THIS IS TO DETERMINE THE COMPUTATIONAL TIME DURATION
from datetime import datetime
start=datetime.now()


from pyspark import SparkContext
#1 ALL DAILY FILES ARE IN THE SAME FOLDER - JUST ADDRESSING THE FOLDER PATH IS ENOUGHT TO GATHER EVERYTHING
logFile = "/media/data/outputData/PETR3/apetr3.txt"  # FILE FROM SYSTEM
#
sc = SparkContext("local", "Minute Data")

#2 Creates the RDD 
logData = sc.textFile(logFile)

def makeColumns(line):
    pieces  = line.split(';');          # delimiters are ";"
    date    = pieces[0].strip()         # first column  - date
    key     = date  # key definition as concatenation of columns
    return key


def minData(a, b):
    return a;


#6 THIS IS THE APPLICATION OF SOME TRANSFORMATIONS AND ACTIONS NEEDED ON THE 'logData' RDD
#   FIRST A FILTER TO DEAL ONLY WITH THE DESIRED STOCKS - filter(filterStock)
#   THEN WE SELECT THE COLUMNS OF INTEREST IN 'map(makeColumns)'
#   NOW WE EXTRACT THE MINUTE DATA USING 'reduceByKey(minData)'
#   FINALLY WE SORT BY KEY
result= logData.map(makeColumns).reduceByKey(minData).sortByKey().coalesce(1).saveAsTextFile("test")


# print the duration of execution
print datetime.now() - start