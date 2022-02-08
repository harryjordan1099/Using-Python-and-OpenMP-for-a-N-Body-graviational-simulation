#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 09:46:35 2022

The OpenMP version of the nbody simulation. Nearly identical to the numba nbody but with
Parallel set to True and a prange function in the for loops. 

@author: harryjordan
"""
import os
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"

from numba import njit, prange, set_num_threads
import math
import time
import numpy as np
import sys


@njit(parallel=True)
def nbody_omp(N,nSteps): # NumPy arrays as input
    #np.random.seed(19) #for testing
    position = np.random.standard_normal((N, 3)) #generates the particle initial conditions
    velocity = np.zeros_like(position) 
    #nSteps = 1000 #values for time steop
    dt = 0.01
    pos_save = np.zeros((nSteps,N, 3)) #Used to save all positons so they can be graphed
    pos_save[0,:,:] = position
    for step in range(1, nSteps + 1, 1): #time loop
        for i in prange(N): # Loops through all particles to calculate the force between them, prange is used here 
            Fx = 0.0; Fy = 0.0; Fz = 0.0
            for j in range(N): #Main Force calculation
                if j != i:
                    dx = position[j,0] - position[i,0]
                    dy = position[j,1] - position[i,1]
                    dz = position[j,2] - position[i,2]
                    drSquared = dx * dx + dy * dy + dz * dz
                    drPowerN32 = 1.0 / (drSquared + math.sqrt(drSquared) + 0.0001)
                    Fx += dx * drPowerN32
                    Fy += dy * drPowerN32
                    Fz += dz * drPowerN32
                velocity[i, 0] += dt * Fx #modified particle velocity
                velocity[i, 1] += dt * Fy
                velocity[i, 2] += dt * Fz
        for i in range(N):
            position[i,0] += velocity[i,0] * dt #Now modifies particle position
            position[i,1] += velocity[i,1] * dt
            position[i,2] += velocity[i,2] * dt
        pos_save[step-1,:,:] = position #Saves position
    return pos_save




if __name__ == '__main__':
    if int(len(sys.argv)) == 4:
        N = int(sys.argv[1])
        nSteps = int(sys.argv[2])
        threads = int(sys.argv[3])
        set_num_threads(threads)
        
        nbody_omp(10, nSteps)
        start = time.time()
        nbody_omp(N, nSteps)
        print(time.time() - start)
        
    else:
        print("Usage: {} <N> <nSteps> <THREADS> ".format(sys.argv[0]))