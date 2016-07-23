#!/usr/bin/env python
# Linear regression
# NOTE: my R installation isn't working, so I guessed at the output
# Michelle L. Gill
# 2016/07/17

from __future__ import print_function
from scipy.stats import linregress
import numpy as np

ing = np.array([10, 18, 25, 40, 50, 63, 42, 30, 5, 55]) # x
svol = np.array([ 25, 55, 50, 75, 110, 138, 90, 60, 10, 100]) # y

xmean = ing.mean()
ymean = svol.mean()

sxx = (ing - xmean)**2
sxy = (ing - xmean)*(svol - ymean)

slope = sxy.sum() / sxx.sum()
intercept = ymean - slope * xmean

ypred = slope * ing + intercept
residuals = svol - ypred

ssres = residuals**2
ssexpl = (ypred - ymean)**2
ssyy = (svol - ymean)**2
sstot = (svol - ymean)**2

rval2 = ssexpl.sum() / sstot.sum()

slope_reg, intercept_reg, rval_reg, pval, stderr = linregress(ing, svol)

print('Slope, calculated: {:.2f}, linregress: {:.2f}'.format(slope, slope_reg))
print('Intercept, calculated: {:.2f}, linregress: {:.2f}'.format(intercept, intercept_reg))
print('R2, calculated: {:.2f}, linregress: {:.2f}'.format(rval2, rval_reg**2))

print('Explained Sum of Squares')
print('{}'.format(ssexpl.sum()))

print('Residual Sum of Squares')
print('{}'.format(ssres.sum()))

print('Residuals')
print(residuals)

##### RESULTS #####

# Slope, calculated: 1.97, linregress: 1.97
# Intercept, calculated: 4.70, linregress: 4.70
# R2, calculated: 0.95, linregress: 0.95
# Explained Sum of Squares
# 13230.9699378
# Residual Sum of Squares
# 651.130062214
# Residuals
# [  0.59737058  14.83354854  -3.95979575  -8.51696208   6.77826036
#    9.16204954   2.5420824   -3.81218453  -4.55024064 -13.07412842]