#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 18:20:24 2022

@author: maria

It integrates the Lorenz system and plots its time series
for a given input value beta
"""

    
import numpy as np 
import matplotlib.pyplot as plt
import sys
from scipy.integrate import ode

T = int(5e4) #Total simulation time
dt = 0.1 #integration time step
nt = int(T/dt)

"""
Lorentz Attractor: Definition and integration

"""
def f(t, y, arg):
    sigma = arg['sigma']
    rho = arg['rho']
    beta = arg['beta']
    TC = arg['TC']
    MD = arg['MD']
    dy = np.zeros(3)
    dy[0] = sigma*(y[1]-y[0])
    dy[1] = rho*y[0]-MD*y[0]*y[2]-y[1]
    dy[2] = MD*y[0]*y[1]-beta*y[2];
    dy = dy*TC
    return dy

m = 3 #Lorentz's dimension
MD = 70
rho = 28
sigma = 10
beta = float(sys.argv[1])
beta = np.round(beta,2)
TC = 0.1

arg = {'rho':rho,'sigma':sigma, 'beta':beta, 'MD':MD, 'TC': TC}
y0 = [0.1,0.1,0.1]
t0 = 0
y = ode(f).set_integrator("dopri5")
y.set_initial_value(y0, t0).set_f_params(arg)
sup = np.zeros((m, nt))
for i in range (nt):
    sup[:, i] = y.integrate(y.t+dt)
    


#from mpl_toolkits import mplot3d
"""
Plot

"""
fig = plt.figure(figsize = (10,5))
ax = fig.add_subplot(1, 1,1, projection='3d')  
ax.plot3D(sup[0,1000:12000], sup[1,1000:12000], sup[2,1000:12000])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')    

figure_nom = 'lorenz_beta_'+str(beta)+'.png'
plt.tight_layout()
plt.savefig(figure_nom, dpi=400)
    

"""
Saving text

"""    
np.savetxt('lorenz_beta_'+str(beta)+'.txt', sup)