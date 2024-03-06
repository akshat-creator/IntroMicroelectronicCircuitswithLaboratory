
from numpy import *

def linefit(x, y, epsilon = 0.001):
    '''
    Attempts to fit a straight line to an appropriate part of the curve 
    specified by x and y.  It steps through the curve specified by 
    ndarrays x and y searching for a consecutive run of at least 10 
    coordinate pairs to which a straight line can be fit using linear 
    regression with an R^2 (i.e., goodness of fit) value of greater 
    than 1-epsilon.  If there is more than one such run of points, 
    the one with the steepest slope is selected.  A typical value 
    for epsilon is in the range of 5e-4 to 5e-3.  The return values 
    are [first, last, mmax, bmax, Nmax], where

        first is the index of the first point used in the fit,
        last is the index of the last point used in the fit,
        mmax is the slope of the best fit line,
        bmax is the y-axis intercept of the best-fit line, and
        Nmax is the number of points used in the fit.
    '''
    if isinstance(x, ndarray) and isinstance(y, ndarray):
        if len(x) == len(y):
            first = 0
            last = 0
            mmax = 0
            bmax = 0
            Nmax = 0
            i = 0
            while i < len(x) - 1:
                R2 = 1
                N = 1
                sumX = x[i]
                sumX2 = x[i] * x[i]
                sumY = y[i]
                sumY2 = y[i] * y[i]
                sumXY= x[i] * y[i]
                j = i
                while (j < len(x) - 1) and (R2 > 1 - epsilon):
                    j += 1
                    N += 1
                    sumX += x[j]
                    sumX2 += x[j] * x[j]
                    sumY += y[j]
                    sumY2 += y[j] * y[j]
                    sumXY += x[j] * y[j]
                    SXX = sumX2 - sumX * sumX / N
                    SYY = sumY2 - sumY * sumY / N
                    SXY = sumXY - sumX * sumY / N
                    m = SXY / SXX
                    b = (sumY - m * sumX) / N
                    R2 = SXY * SXY / (SXX * SYY)
                if (N > 10) and (abs(m) > abs(mmax)):
                    first = i
                    last = j
                    mmax = m
                    bmax = b
                    Nmax = N
                i = j
            return [first, last, mmax, bmax, Nmax]
        else:
            raise IndexError('ndarrays supplied to linefit must be of the same length')
    else:
        raise ValueError('x and y arguments supplied to linefit must be ndarrays')

