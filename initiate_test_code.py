import numpy as np
import matplotlib.pyplot as plt
from MCMC_modules import *
from linfit_modules import *

x = np.linspace(1,10,num=50)
ysig = 1.0
with open('./true_value.txt','r') as ascii_data:
  for i in range(4):
    next(ascii_data)
  for line in ascii_data:
    line = line.strip()
    data = line.split()
    slope = np.float(data[0])
    yinte = np.float(data[1])

y = linear_function(x,slope,yinte)
test_x,test_y = generate_test_data(x,y,ysig)

out_file = open('test_data.txt','wb')
for i in range(np.shape(test_x)[0]):
  string = "{0:}   {1:}\n".format(test_x[i],test_y[i])
  out_file.write(string)
out_file.close()
