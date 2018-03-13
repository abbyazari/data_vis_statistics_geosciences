'''
omni.py

- Written on 3/12/2018 for CLaSP 405 by Lab TA A. Azari. 

Purpose:
To create a class of data and functions for performing
linear regression on two variables.
        
To create an instance:

obj = omni.Omni(xvalues, yvalues, xLabel = string, yLabel = string)


To create a linear fit:

obj.plotLinRegress()


To calcualte a fit report:

obj.printFitReport()

'''

#import required packages for object methods and
#attributes
import pandas as pd     #runs in pandas 
import datetime as dt   #and datetime
import numpy as np      #and numpy
from scipy import stats #for fits 
import linerror as lr   #ext written package for error calculations.
import matplotlib.pyplot as plt #for plotting
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
                                


class Omni():
    
    '''
    Methods and attributes of the class of object called omni. So
    named after the data source Omniweb. This object is for
    analyzing 2 columns of temporal data. 
    '''

    def __init__(self, xVals, yVals, xLabel = '', yLabel = ''):
        
        '''
        This initializes the object with xVals, yVals, and labels

        '''
        
        #set up the original values
        self.x = xVals
        self.y = yVals
        
        self.xLabel = xLabel
        self.yLabel = yLabel
        
        self.rVal = np.nan
        self.slope = np.nan
        self.intercept = np.nan
        
        self.rVal = np.nan
        self.RMSE = np.nan
        self.intercept = np.nan
        self.errInter = np.nan
        self.slope = np.nan
        self.errSlope = np.nan
        
    
    def linRegress(self):
        '''
        Perform linear regression on two column omni object. Should be called
        from inside the plotter function and not externally.

        '''
    
        #replace nans
        nanMask = ((~np.isnan(self.x)) & (~np.isnan(self.y)))

        xVals = self.x[nanMask]
        yVals = self.y[nanMask]
   
        #perform linear fit
        slope, intercept, rval, pval, stderr = stats.linregress(xVals, yVals)
        
        #calculate the yvalues given the linear fit
        yModel = intercept + slope * xVals

        #find y errors
        RMSE  = lr.calcRMSE(yModel, yVals)

        #error on coefficents, slope and y-intercept and.
        errSlope,  errInter = lr.calcCoeffsErr(xVals,  RMSE)


        #set the attributes of the object
        self.rVal = rval
        self.RMSE = RMSE
        self.intercept = intercept
        self.errInter = errInter
        self.slope = slope
        self.errSlope = errSlope
        
        
    def printFitReport(self):

        '''
        Print out fit report given the data
        '''
        
        print("Fit Report: \n \tUncert. on Y: +/- {:.2f}".format(self.RMSE) + 
          "\n \tIntercept: {:.2f} +/- {:.2f}".format(self.intercept, self.errInter)
          + "\n\tSlope: {:.2f} +/- {:.2f}".format(self.slope, self.errSlope) 
          + "\n\tPearson Linear Correlation: {:.2f}".format(self.rVal))

        
   
    def plotLinReg(self):
        '''
        Plots a scatter plot and a fit of the data. 
        '''
        
        #in case the linear regression hasn't been performed yet
        self.linRegress()
            
        fig = plt.figure(figsize=(8.5, 5))

        gs  = plt.GridSpec(1, 1, hspace=0.0, wspace=0.2, right = 0.9)

        #add subplots
        ax1 = fig.add_subplot(gs[0,0])

        #set up titles for axis
        ax1.set_xlabel(self.xLabel, fontsize = 20)
        ax1.set_ylabel(self.yLabel, fontsize = 20)

        #plot values
        ax1.scatter(self.x, self.y,  color = '#660066', alpha = 0.6, s = 6)
        
        #make line equally spaced
        minVal  = np.nanmin(self.x)
        maxVal  = np.nanmax(self.x)
        spacing = (maxVal - minVal) / 20.0

        #create new xarray for pretty plotting
        xVals = np.arange(minVal, maxVal+spacing, int(spacing))
        
        ax1.plot(xVals, xVals*self.slope + self.intercept, 
                 color = '#006666', alpha = 0.8, linestyle = '--', lw = 3)
        

        #set up grid
        ax1.grid(color='gray', linestyle='dashed')

        #how to set up a share axis with alternative colors
        ax1.tick_params(labelsize = 16)
        
        
        
