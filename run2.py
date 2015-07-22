#!/usr/bin/env /proj/sot/ska/bin/python
import os
import sys
import re
import string
import random
import operator
import math
import numpy

sys.path.append('/data/mta/Script/ACIS/count_rate/Scripts/')

import plot_count_rate as pcr
import print_html_page as phtml

comp_test = 'no'

for year in range(2000, 2014):
  for month in range(1, 13):
    lmon = ('JAN', 'FEB', 'MAR', 'APR','MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV','DEC')

    if year == 2013 and month == 11:
        exit(1)

    dir = '/data/mta_www/mta_dose_count2/' + lmon[month-1]  + str(year)
    print 'DIR: ' + dir


    cmd = 'rm ' + dir + '/*.html'
    os.system(cmd)

#    pcr.create_plots(dir)
    phtml.print_html_page(comp_test, in_year=year, in_mon=month)
