#-------------------------------------------------------------------------------
# Name:        IS 602 Assignment 3
# Purpose:
#
# Author:      OluwakemiOmotunde
#
# Created:     27/02/2017
# Copyright:   (c) OluwakemiOmotunde 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#First to import the needed modules:

import re
import Tkinter
import tkFileDialog
import csv
import operator

#Create class to hold the input

class carData:

#convert to numeric for better handling

    safety_con = {'LOW': 0, 'MED': 1, 'HIGH': 2}
    maint_con = {'LOW': 0, 'MED': 1, 'HIGH': 2, 'VHIGH': 3}
    buying_con = {'LOW': 0, 'MED': 1, 'HIGH': 2, 'VHIGH': 3}
    doors_con = {'2': 2, '3': 3, '4': 4, '5MORE': 5}
    car_con = {'UNACC': 0, 'ACC': 1, 'GOOD': 2, 'VGOOD': 3}
    boot_con = {'SMALL': 0, 'MED': 1, 'BIG': 2}
    persons_con = {'2': 2, '4': 4, 'MORE': 5}


    def __init__(self, buy_price, maint_price, doors, persons, boot, safety, car_accept):
        self.buy_price = buy_price.upper()
        self.maint_price = maint_price.upper()
        self.doors = doors.upper()
        self.persons = persons.upper()
        self.boot = boot.upper()
        self.safety = safety.upper()
        self.car_accept = car_accept.upper()

#import cars data and saves using Tkinter interface

root =  Tkinter.Tk()
root.withdraw()

file_name = tkFileDialog.askopenfilename(parent = root)
data =open(file_name)

#keep in mind how you specify the column you want to sort by

print "Part A: Print to console the top 10 rows of the data sorted by 'safety"
cars_data = csv.reader(data, delimiter = ',')
sort_data = sorted(cars_data, key = operator.itemgetter(5)) #5 tells us which column to work with
try:
    for row in sort.data:
        if row[0] == 'vlow' or row[1] == 'vlow' or row[2] == '1'\
        or row[3] == '1' or row [4] == 'vbig' or row[5] == 'vhig': raise IOError
except:
    pass
sort_data = sort_data[0:10]
for row in sort_data:
    print row
data.close()


print "Part B: Print to the console the bottom 15 rows of the data sorted by 'maint' in ascending order"

data = open(file_name)
data_maint = csv.reader(data, delimiter = ',')
sort_maint = sorted(data_maint, key = operator.itemgetter(1), reverse = False) #5 tells us which column to work with

for row in sort_data:
    sort_maint = sort_maint[-15:]
    for line in sort_maint:
        print line
        data.close()
#I think I have a mistake somewhere in my code but I'm not sure where.

print "Part C: Print to the console all rows that a high or vhigh in fields buying, maint, and saftey sorted by doors in ascending order"

#we first want to filter our the fields containing high or vhigh

data = open(file_name)
data_doors = csv.reader(data, delimiter = ',')
for row in data:
    pattern = '^v{0,1}high'
    sorted_saftey = sorted(data_doors, key = operator.itemgetter(2))
    nlist = []

    for row in sorted_saftey:
        if re.match(pattern, row[0]) and re.match(pattern, row[1]) and re.match(pattern, row[5]):
            nlist.append(row)
            for row in nlist:
                print row
data.close()

print "Part C: Save to a file all rows (in any order) that are: buying:vhigh, maint:med, doors:4 and persons:4 or more"

data = open(file_name)
data_partc = csv.reader(data, delimiter = ',')

nlist_c = []

for row in data_partc:
    if row[0] == 'vhigh' and row[1] == 'med' and row[2] == '4' and (row[3] == '4' or row[3] == 'more'):
        nlist_c.append(row)

#now to save

with open("carsoutput.csv", 'wb') as f:
    fileWriter = csv.writer(f, delimiter = ',')
    for row in nlist_c:
        fileWriter.writerow(row)
f.close()

#I found this assignement quite difficult. I initially wanted to use pandas as I was familiar with dataframes but I had to switch my approach.