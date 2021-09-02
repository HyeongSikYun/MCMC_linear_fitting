First try to use the MCMC code to fit the artificial data with a linear function.

This code is based on the Markov Chain Monte Carlo (MCMC) class in Sagan Summer Workshop in 2016 presented by David Kipping.
The class video is accessible via an youtube channel, 'Sagan Summer Workshop'
Please use the following link
https://www.youtube.com/watch?v=vTUwEu53uzs

I built this test code to understand how the MCMC procedure works.
It contains several python codes to initiate and run the example of MCMC.

### How to use
### 1. Open 'true_value.txt' and set true values
### 2. run initiate_test_code.py
### 3. run test_MCMC_run.py
### 4. run draw_triangle_plot.py

Followings are the description of the files.
>> MCMC_modules.py: it contains several subroutines to generate random number and to judge the acceptance of a randomized step.
>> linfit_modules.py: it contains several subroutines to run the MCMC test for the linear fitting problem.
>> true_value.txt: the text input for generating an artificial data
>> initiate_test_code.py: the code to generate the artificial data to test the linear fitting.
>> test_data.txt: the output of 'initiate_test_code.py', which contains the artificial data.  
>> test_MCMC_run.py: the code to run the MCMC procedure to find the best-fit linear function.
>> out_MC_test.txt: the output file of the MCMC procedure
>> draw_triangle_plot.py: the code to generate a triangle plot to check the result of the MCMC code. You would change the 'show_step_range' and 'Burn_in_steps'.
