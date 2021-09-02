import numpy as np

def rand_norm(mean,std,num):
  pick = np.random.normal(0.0,1.0,num*10)
  choice = np.random.choice(pick,num)
  rand_numbers = (choice * std) + mean
  return rand_numbers

def rand_uniform(num):
  pick = np.random.uniform(low=0.0,high=1.0,size=num*10)
  choice = np.random.choice(pick,num)
  return choice

def judge_acceptance(p):
  test_p = rand_uniform(1)
  out = False
  if test_p <= p:
    out = True
  return out
