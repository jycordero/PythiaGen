
# coding: utf-8

# In[2]:


import numpy as np


# In[1]:


def find_eff_interval(k,N):
    if k>N:
        return [0,0,0]
    
    tempa,tempb = 0,1

    alpha = stats.beta.rvs(k+1,N-k+1,size=100)
    beta  = stats.beta.rvs(k+1,N-k+1,size=100)
    alpha.sort()
    beta.sort()
    
    for i in range(len(alpha)):
        for j in range(len(beta)):
            if beta[j] > alpha[i]:
                K=(betainc(k+1,N-k+1,beta[j]))-(betainc(k+1,N-k+1,alpha[i]))
                if K > 0.67 and K < 0.69:
                    if tempb-tempa > beta[j]-alpha[i]:
                        tempa = alpha[i]
                        tempb = beta[j]
                        
    return [k/N,tempb-k/N,k/N-tempa]


# In[2]:


def swap(a,b):
    temp = a
    a = b
    b = temp
    return a,b


# In[3]:


def delta_phi(obj1,obj2):
    d_phi =  obj1 - obj2
    if d_phi > np.pi: 
        d_phi = 2*np.pi - d_phi
    if d_phi < -np.pi: 
        d_phi = 2*np.pi + d_phi
    return d_phi


# In[4]:


def cut_indices_out(data,MIN,MAX):
    data =  np.array(data)
    return np.logical_or( data < MIN, data > MAX)


# In[5]:


def cut_indices(data,MIN,MAX):
    data =  np.array(data)
    return np.logical_and( data > MIN, data < MAX)

