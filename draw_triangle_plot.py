import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

out_file = 'out_MC_test.txt'
show_step_range = [0,400]
Burn_in_steps = 170

likehood=[]; slope=[]; yinte=[]
with open('./'+out_file,'r') as ascii_data:
  for line in ascii_data:
    line = line.strip()
    data = line.split()
    likehood = np.append(likehood,np.float(data[0]))
    slope = np.append(slope,np.float(data[1]))
    yinte = np.append(yinte,np.float(data[2]))

step_idx = np.arange(np.shape(likehood)[0])+1
idx1 = step_idx > show_step_range[0]
idx2 = step_idx < show_step_range[1]
idx = np.logical_and(idx1,idx2)
burn_idx1 = step_idx < Burn_in_steps
burn_idx = np.logical_and(idx,burn_idx1)
post_idx = np.logical_and(idx,~burn_idx1)

fig = plt.figure(101, figsize=[6.694,3.149])
layout = gridspec.GridSpec(1,2,left=0.11,right=0.98,bottom=0.2,top=0.96,
         wspace=0.25)

first_fig = fig.add_subplot(layout[0,0])
plt.plot(step_idx[burn_idx],np.log10(likehood[burn_idx]),'-',color='red')
plt.plot(step_idx[post_idx],np.log10(likehood[post_idx]),'-',color='blue')
first_fig.set_xlabel('Steps')
first_fig.set_ylabel('log(Likelyhood)')
first_fig.set_xlim(show_step_range)

second_fig = fig.add_subplot(layout[0,1])
plt.plot(slope[0],yinte[0],'x ',color='black',markersize=7)
plt.plot(slope[burn_idx],yinte[burn_idx],'-',color='red')
plt.plot(slope[post_idx],yinte[post_idx],'-',color='blue')
second_fig.set_xlabel('Slope')
second_fig.set_ylabel('y-intercept')

fig2 = plt.figure(102, figsize=[6.694,6.694])
layout2 = gridspec.GridSpec(2,2,left=0.11,right=0.98,bottom=0.1,top=0.9)

triangle_idx = step_idx > Burn_in_steps
post_slope = slope[triangle_idx]; post_yinte = yinte[triangle_idx]
min_max_slope = [np.min(post_slope),np.max(post_slope)]
min_max_yinte = [np.min(post_yinte),np.max(post_yinte)]
image_matrix = np.zeros([300,300])
slope_arr = np.linspace(min_max_slope[0],min_max_slope[1],301)
yinte_arr = np.linspace(min_max_yinte[0],min_max_yinte[1],301)

for i in range(300):
  for j in range(300):
    idx1 = post_slope > slope_arr[i]
    idx2 = post_slope < slope_arr[i+1]
    idx3 = post_yinte > yinte_arr[j]
    idx4 = post_yinte < yinte_arr[j+1]
    idx12 = np.logical_and(idx1,idx2)
    idx34 = np.logical_and(idx3,idx4)
    idx = np.logical_and(idx12,idx34)
    image_matrix[j,i] = np.sum(idx)
slope_vals = 0.5*(slope_arr[1:]+slope_arr[0:-1])
yinte_vals = 0.5*(yinte_arr[1:]+yinte_arr[0:-1])
slope_mat, yinte_mat = np.meshgrid(slope_vals,yinte_vals)
first_fig = fig2.add_subplot(layout2[1,0])
plt.contour(slope_mat,yinte_mat,image_matrix)
first_fig.set_xlabel('Slope')
first_fig.set_ylabel('y-intercept')

second_fig = fig2.add_subplot(layout2[0,0])
plt.hist(post_slope,slope_arr,histtype='bar')
plt.axvline(x=np.mean(post_slope),linestyle='--',color='black')
second_fig.set_xlim([np.min(slope_vals),np.max(slope_vals)])
second_fig.set_title('Slope')

third_fig = fig2.add_subplot(layout2[1,1])
plt.hist(post_yinte,yinte_arr,histtype='bar')
plt.axvline(x=np.mean(post_yinte),linestyle='--',color='black')
third_fig.set_xlim([np.min(yinte_vals),np.max(yinte_vals)])
third_fig.set_title('y-intercept')

plt.show(); aaa=aaa
