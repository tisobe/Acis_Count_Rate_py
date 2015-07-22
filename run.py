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


for year in range(2000, 2014):
 for month in  ('JAN', 'FEB', 'MAR', 'APR','MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV','DEC'):
    if year == 2013 and month == 'OCT':
        exit(1)

    dir = '/data/mta_www/mta_dose_count2/' + month + str(year)
    print 'DIR: ' + dir

    cmd = 'rm -rf  ' + dir + '*.gif'
    os.system(cmd)

    pcr.create_plots(dir)
