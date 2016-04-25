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

#1.2 - output folder
outpath = "/media/data/outputData/"

#2 - get the path of every single file in the path folder, also sort the list
import glob   
files = glob.glob(path)
files.sort()   

#3 - open file, filter lines
#3.1 - desired stocks (all in IBOV)
stocks = ['PETR3','ABEV3','BBAS3']
#stocks = ['ABEV3','BBAS3','BBDC3','BBDC4','BBSE3','BRAP4','BRFS3','BRKM5','BRML3','BVMF3',
#'CCRO3','CESP6','CIEL3','CMIG4','CPFE3','CPLE6','CSAN3','CSNA3','CTIP3','CYRE3',
#'ECOR3','EMBR3','ENBR3','EQTL3','ESTC3','FIBR3','GGBR4','GOAU4','HGTX3','HYPE3',
#'ITSA4','ITUB4','JBSS3','KLBN11','KROT3','LAME4','LREN3','MRFG3','MRVE3','MULT3',
#'NATU3','OIBR3','PCAR4','PETR3','PETR4','QUAL3','RADL3','RENT3','RUMO3','SANB11',
#'SBSP3','SMLE3','SUZB5','TBLE3','TIMP3','UGPA3','USIM5','VALE3','VALE5','VIVT4','WEGE3']

#4 function create folder (or check if it already exists) for distinct stock
import os
def check_create(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
    
#4 - loop over all files in folder and all the desired stocks
for i in files:
    # if to select specific month (MM) and year (YYYY)
    # i[-12:-6] gets the year and month in a string with the following pattern
    # i = '/media/data/rowData_201304_201602/YYYYMMDD.TXT'
    # "if i[-12:-6] == '201304':" selects April 2013  
    if i[-12:-6] == '201304':
        for stock in stocks:
            folder      = outpath + str(stock) +"/"
            check_create(folder)
            output      = folder + i[-12:]
            with open(output, "w+") as fw:
                with open(i, "r+") as fo:
                    for line in fo:
                        if stock in line:
                            fw.write(line)

print datetime.now() - start