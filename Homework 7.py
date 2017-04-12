#-------------------------------------------------------------------------------
# Name:        IS 602 Assignment 7
# Purpose: Build on homework 5 with SciPy
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

#reference: http://bigdata-madesimple.com/how-to-run-linear-regression-in-python-scikit-learn/

#The above is the work that I completed  for Homework 5 and I will build on it below.

#Take what you did on homework 5 as a starting point (using any of the provided datasets).  Replace the regression calculation using least squares with a #curve fitting approach (examples in the reading).  To start, just fit a linear equation.  Output the equation to the console.  You don't need to graph #anything (we'll look at that in a couple more weeks).

import numpy as np
import scipy
from scipy.optimize import curve_fit

colnames = ['Animals', 'Body', 'Brain']
df = pd.read_csv('brainandbody.csv', sep = ',', names = colnames)
df = df[1:]

#different approach to getting data so that I can refer to data by column names. From the reading, this will make working with data easier


#I will write my functions then find each component since I have that from the reading.

#Once I completed the outline of each fit, I came back to set my different variable.
brain_data = df.Brain
body_data = df.Body

brain_data = brain_data.astype(float)
body_data = body_data.astype(float)

def lin_reg(df, x, y):
    a = covar(df, x, y) / var(df, x)
    b = df[y].mean() - a * df[x].mean()
    print ("y = %s * x + %s" % (a,b))


def fit_curve(input):
    def func(x, a, b):
        return a * x + b
    popt,pcov = curve_fit(func, brain_data, body_data)
    print "The curve fit model is: "
    cf_model = "body = %s * brain +(%s)" %(popt[0],popt[1])
    print cf_model
    return cf_model

def guass_fit(input):
    def func_guass(x, a, b, c):
        return a * np.exp(-(x-b)**2/(2*c*2))
    popt, pcov = curve_fit(func_guass, brain_data, body_data)
    print "The values for a, b, and c are: "
    values = "a = %s, b = %s, c =  %s" %(popt[0], popt[1], popt[1])
    print values
    print "The Gaussian Model is: "
    guass_model = "(%s)*exp(-(x-(%s))**2 / (2*(%s)**2))" %(popt[0], popt[1], popt[1])
    print guass_model
    return guass_model

if __name__ == '__main__':
    data = load_data()
    lin_reg(data, "brain", "body")
    fit_curve(input)
    guass_fit(input)

#Again, using timeit, compare the performance of your solution in homework 5 to the scipy function.  Output the results to the console.
#(Optional)  There are other models that can be fitted to the data we have.  Try to fit other equations, like Gaussian, to the data.  Output the equation to the console.

import timeit
setup = '''
#I just copied and pasted from up top

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

#reference: http://bigdata-madesimple.com/how-to-run-linear-regression-in-python-scikit-learn/

#The above is the work that I completed  for Homework 5 and I will build on it below.

#Take what you did on homework 5 as a starting point (using any of the provided datasets).  Replace the regression calculation using least squares with a #curve fitting approach (examples in the reading).  To start, just fit a linear equation.  Output the equation to the console.  You don't need to graph #anything (we'll look at that in a couple more weeks).

import numpy as np
import scipy
from scipy.optimize import curve_fit

colnames = ['Animals', 'Body', 'Brain']
df = pd.read_csv('brainandbody.csv', sep = ',', names = colnames)
df = df[1:]

#different approach to getting data so that I can refer to data by column names. From the reading, this will make working with data easier


#I will write my functions then find each component since I have that from the reading.

#Once I completed the outline of each fit, I came back to set my different variable.
brain_data = df.Brain
body_data = df.Body

brain_data = brain_data.astype(float)
body_data = body_data.astype(float)

def lin_reg(df, x, y):
    a = covar(df, x, y) / var(df, x)
    b = df[y].mean() - a * df[x].mean()
    print ("y = %s * x + %s" % (a,b))


def fit_curve(input):
    def func(x, a, b):
        return a * x + b
    popt,pcov = curve_fit(func, brain_data, body_data)
    cf_model = "body = %s * brain +(%s)" %(popt[0],popt[1])
    return cf_model

def guass_fit(input):
    def func_guass(x, a, b, c):
        return a * np.exp(-(x-b)**2/(2*c*2))
    popt, pcov = curve_fit(func_guass, brain_data, body_data)
    values = "a = %s, b = %s, c =  %s" %(popt[0], popt[1], popt[1])
    guass_model = "(%s)*exp(-(x-(%s))**2 / (2*(%s)**2))" %(popt[0], popt[1], popt[1])
    return guass_model
'''
import timeit
if __name__ == "__main__":

    n = 200
    t = timeit.Timer("lin_reg(df,x,y)", setup = setup)
    lin_reg_time = t.timeit(n)
    print "The runtime for least squares is %s seconds" %lin_reg_time

    t = timeit.Timer('fit_curve(input)', setup)
    fit_curve_time = t.timeit(n)
    print "The runtime for curve fit is %s seconds" %fit_curve_time

    t = timeit.Timer('guass_fit(input)', setup)
    guass_fit_time = t.timeit(n)
    print "The runtime for guassian fit is %s seconds" %guass_fit_time

#I will be turning this assignment in not complete as I kept getting at error the import * is not allowed nad I can't seem to troubleshoot this.
