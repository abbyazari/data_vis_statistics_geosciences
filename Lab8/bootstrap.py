'''
bootstrap.py

- Written on 3/12/2018 for CLaSP 405 by Lab TA A. Azari. 
Purpose: To contain functions related to running a bootstrap
analysis.
-


Given the original data and fit, run a boostrap analysis and output
a dictionary of values of those fits.
'''

#import required packages for bootstrap

#for data analysis and statisics
import pandas as pd
import datetime as dt
import numpy as np
from scipy.stats import skew, kurtosis, norm
from scipy import stats
import matplotlib.pyplot as plt
#for accessing the object
import omni
#for pretty plotting
from matplotlib.ticker import MultipleLocator, FormatStrFormatter


def bootstrap(omniObj, numIterations = 50):
    
    '''
    Given the original data and fit, run a boostrap analysis and output
    a dictionary of values of those fits
    '''

    #create dictionary of bootstrap values
    bootstrapVals = {}
    bootstrapVals['rVals'] = np.zeros((numIterations))
    bootstrapVals['Intercepts'] = np.zeros((numIterations))
    bootstrapVals['Slopes'] = np.zeros((numIterations))
    
    
    for i in range(numIterations):
    
        #resample the dataframe
        reSamp = omniObj.x.sample(frac = 1, replace = True)

        #create a new object within the function that is the resampled index
        tempObj = omni.Omni(omniObj.x[reSamp.index], omniObj.y[reSamp.index])

        #caluclate the linear regression
        tempObj.linRegress()

        #within the dictionary set the values 
        #with the attributes of our temporary omni object.
        bootstrapVals['rVals'][i] = tempObj.rVal

        bootstrapVals['Intercepts'][i] = tempObj.intercept

        bootstrapVals['Slopes'][i] = tempObj.slope
    
    return(bootstrapVals)

 
def plotRValsHist(omniObj, bootstrapVals):
    
    '''
    Plot out the histogram of values for the r vals.
    '''

    #set up the figure 
    fig = plt.figure(figsize=(11, 7))

    gs = plt.GridSpec(1, 1, hspace=0.2, wspace=0.0, right = 0.8)

    #add subplots
    ax1 = fig.add_subplot(gs[0,0])
    fig.suptitle('Histogram of Pearson Corr. Coeff. \n' + 
             'Resampling Amount: {}'.format(len(bootstrapVals['rVals'])), 
             fontsize=20)
    #calculate using the general rule of thumb - 
    #minimum as the sqrt(sampleSize)
    sampleSize = len(bootstrapVals['rVals'])

    #print the number of bits
    numBins = np.ceil(np.sqrt(sampleSize))
    print("The number of bins for the histogram is: {}".format(numBins))

    #edgecolor and linewidth set up the bin edges
    ax1.hist(bootstrapVals['rVals'], int(numBins), density = 1, facecolor = '#822f59', 
             edgecolor="k")

    #set up grid
    plt.grid(color='gray', linestyle='dashed')

    #labels
    plt.xlabel('Pearson Correlation Coeff.', fontsize = 20)
    plt.ylabel('Normalized Occurrence', fontsize = 20)
    #large ticks
    plt.xticks(fontsize=16) #make the xaxis labels larger
    plt.yticks(fontsize=16) #make the yaxis labels larger
    
    #ax2.xaxis.set_minor_locator(MultipleLocator(2.5))
    ax1.xaxis.set_major_formatter(FormatStrFormatter('%.2f'))

    #print out stats on the skew etc
    print("Skew: {:.1f}, Kurtosis: {:.1f}, Standard Dev: {:.1f}, Mean: {:.1f}".format(
            skew(bootstrapVals['rVals']), 
            kurtosis(bootstrapVals['rVals'], fisher = False), 
            np.std(bootstrapVals['rVals'], ddof = 1), 
            np.mean(bootstrapVals['rVals'])))
    
    plt.savefig('./Figures/Hist_{}vs{}.png'.format(omniObj.xLabel, omniObj.yLabel))

def plotFits(omniObj, bootstrapVals):
    '''
    Given the original Omni object and fit data as attributes wihtin Omni Object,
    loop through the boostrap values and plot out the fits.
    '''
    
    fig = plt.figure(figsize=(8.5, 6))

    gs  = plt.GridSpec(1, 1, hspace=0.0, wspace=0.2, right = 0.9)

    #add subplots
    ax1 = fig.add_subplot(gs[0,0])

    #set up titles for axis through accessing the omni object attributes
    ax1.set_xlabel(omniObj.xLabel, fontsize = 20)
    ax1.set_ylabel(omniObj.yLabel, fontsize = 20)

    #plot values
    ax1.scatter(omniObj.x, omniObj.y,  
                color = '#544cac', alpha = 0.6, s = 6)
    #make line equally spaced
    minVal  = np.nanmin(omniObj.x)
    maxVal  = np.nanmax(omniObj.x)
    spacing = (maxVal - minVal) / 20.0
    
    #create new xarray for pretty plotting
    xVals = np.arange(minVal, maxVal+spacing, int(spacing))
    
    for slope, intercept in zip(bootstrapVals['Slopes'], bootstrapVals['Intercepts']):

        yModel = slope*xVals + intercept 

        ax1.plot(xVals, yModel, color = 'grey', alpha = 0.2, lw = 1.0)
        
    yModel = slope*xVals + intercept 

    ax1.plot(xVals, yModel, 
         color = '#006666', alpha = 1.0, linestyle = '--', lw = 3.0)

    #set up grid
    ax1.grid(color='gray', linestyle='dashed')

    #how to set up a share axis with alternative colors
    ax1.tick_params(labelsize = 16)

    plt.savefig('./Figures/Fits_{}vs{}.png'.format(omniObj.xLabel, omniObj.yLabel))

def printFitReport(omniObj, bootstrapVals):
    '''
    Given the original Omni object and fit data as attributes wihtin Omni Object,
    print out the fit report.
    '''
    
    print("Fit Report: \n \tUncert. on Y: +/- {:.2f}".format(omniObj.RMSE) + 
          "\n \tIntercept: {:.2f} +/- {:.2f}".format(omniObj.intercept, omniObj.errInter)
          + "\n\tSlope: {:.2f} +/- {:.2f}".format(omniObj.slope, omniObj.errSlope) 
          + "\n\tPearson Linear Correlation: {:.2f} +/- {:.5f}".format(omniObj.rVal, 
                                                                 np.std(bootstrapVals['rVals'], 
                                                                        ddof = 1)))
    
    
