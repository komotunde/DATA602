#-------------------------------------------------------------------------------
# Name:        IS 602 Assignment 5
# Purpose:
#
# Author:      Oluwakemi Omotunde
#
# Created:     21/03/2017
# Copyright:   (c) OluwakemiOmotunde 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

#Download the new data set on the Lesson 5 page called brainandbody.csv.  This file is a small set of average brain weights and average body weights for a number of animals.  We want to see if a relationship exists between the two. (This data set acquired above).

#Perform a linear regression using the least squares method on the relationship of brain weight [br] to body weight [bo].  Do this using just the built in Python functions (this is really easy using scipy, but we're not there yet).  We are looking for a model in the form bo = X * br + Y.  Find values for X and Y and print out the entire model to the console.


#our first step is to load the dataset

from  Tkinter import *
import tkFileDialog
import pandas as pd


#use same method from Homework 3
def load_data():
    root = Tk()
    root.withdraw()

    file_name = tkFileDialog.askopenfilename(parent = root)
    data = open(file_name)
    #this is a little different from Homework 3 as I had not mastered importing modules then
    brain_body = pd.read_csv(data, delimiter = ",")
    return brain_body
#We will now like to calulate the variance for

def var(df, col):
    var = 0
    mean = sum(df[col])/len(df) #essentially summing the values in the column and dividing by how many columns
    #now to calculate the variance
    var =  sum((df[col] - mean) ** 2)/(len(df) - 1)
    return var

def covar(df, x, y):
    covar = 0
    mean_x = sum(df[x])/len(df)
    mean_y = sum(df[y])/len(df)
    covar = sum((df[x] - mean_x) * (df[y] - mean_y)) / (len(df)-1)
    return covar

#now to calculate our a and b values

def lin_reg(df, x, y):
    a = covar(df, x, y) / var(df, x)
    b = df[y].mean() - a * df[x].mean()
    print ("y = %s * x + %s" % (a,b))


if __name__ == '__main__':
    data = load_data()
    lin_reg(data, "brain", "body")


#reference: http://bigdata-madesimple.com/how-to-run-linear-regression-in-python-scikit-learn/

