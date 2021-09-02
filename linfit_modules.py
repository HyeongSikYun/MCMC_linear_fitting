import numpy as np
from MCMC_modules import *

def generate_test_data(x,y,ysig):
  n_vals_x = np.shape(x)[0]
  n_vals_y = np.shape(y)[0]
  if n_vals_x != n_vals_y:
    print 'number of elements of x and y are different'
    print 'please input x and y with the same size.'
    raise SystemExit(0)
  n_vals = n_vals_x
  y_err = rand_norm(0.0,ysig,n_vals)
  test_y = y + y_err
  return x, test_y

def linear_function(x,slope,yinte):
  y = (x*slope)+yinte
  return y

def linear_residual(x,y,slope,yinte):
  fit_y = linear_function(x,slope,yinte)
  return y-fit_y

def linear_chisq(x,y,slope,yinte,yerr):
  resid = linear_residual(x,y,slope,yinte)
  return np.sum(resid**2.0)/(yerr**2.0)

def log_likelyhood_const_sig(x,y,p,yerr):
  slope = p[0]
  yinte = p[1]
  n_elem = np.shape(x)[0]
  c = 0.5*n_elem*(0-np.log10(2*np.pi)-np.log10(yerr**2.0))
  chisq_val = linear_chisq(x,y,slope,yinte,yerr)
  return c-(0.5*chisq_val)
