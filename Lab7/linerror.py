'''
linearerror.py

- Written on 2/13/2018 for CLaSP 405 by Lab TA A. Azari. 
Purpose:
- To calculate with x and y the error on the coefficents
as demonstrated in eqn. 8.15, 8.16, 8.17 in Taylor - 
An Introduction to Error Analysis.

'''

def calcCoeffsErr(x, rootMeanSquareError):
    '''
    This function calculates the error on the coefficents or
    equation 8.16 & 8.17 in Taylor. Inputs are the x values 
    of the equation and the RMSE on the fit. 

    Outputs the error on the slope, THEN on the intercept. 

    '''
    import numpy as np
    
    delta = len(x)*sum(x**2) - (sum(x)**2)

    errSlope = rootMeanSquareError * np.sqrt((len(x)) / delta)
    errIntercept = rootMeanSquareError * np.sqrt(sum((x**2)) / delta)
    
    return(errSlope, errIntercept)
    
def calcRMSE(yModel, yData):
    '''
    This calculates sigma y, or equation 8.15 in Taylor. Outputs
    error on the fit of regressions. 
    '''
    import numpy as np
    
    sumOfDiff = sum(((yModel - yData)**2))
    meanSquareError = (sumOfDiff / (len(yModel) - 2.0))
    
    return(np.sqrt(meanSquareError))
