import numpy as np
from MCMC_modules import *
from linfit_modules import *

slope_guess = -2.0
yinte_guess = -2.0
y_err = 1.0
jump_scale = 0.1
n_jump = 10000

x=[]; y=[]
with open('./test_data.txt','r') as ascii_data:
  for line in ascii_data:
    line = line.strip()
    data = line.split()
    x = np.append(x,np.float(data[0]))
    y = np.append(y,np.float(data[1]))

initial_p = np.array([slope_guess,yinte_guess])
prior_p = initial_p
jump_count = 0
pri_likehood = log_likelyhood_const_sig(x,y,prior_p,y_err)
MC_likehood = pri_likehood
MC_slope = prior_p[0]; MC_yinte = prior_p[1]
while jump_count < n_jump:
  pri_likehood = log_likelyhood_const_sig(x,y,prior_p,y_err)
  trial_dp = rand_norm(0.0,jump_scale,2)
  trial_p = prior_p+trial_dp
  tri_likehood = log_likelyhood_const_sig(x,y,trial_p,y_err)
  judge = judge_acceptance(10.0**(tri_likehood-pri_likehood))
  if judge == True:
    jump_count = jump_count + 1
    prior_p = trial_p
    MC_likehood = np.append(MC_likehood,tri_likehood)
    MC_slope = np.append(MC_slope,trial_p[0])
    MC_yinte = np.append(MC_yinte,trial_p[1])

out_file = open('out_MC_test.txt','wb')
for i in range(np.shape(MC_likehood)[0]):
  string = "{0:}    {1:}    {2:}\n".format(10.0**MC_likehood[i],MC_slope[i],MC_yinte[i])
  out_file.write(string)
out_file.close()

print 'Finished'
print 'use the other code to check the output_file'
