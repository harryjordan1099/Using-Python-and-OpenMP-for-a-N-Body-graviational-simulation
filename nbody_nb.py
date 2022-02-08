#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 14:10:57 2022

The Numba compile version of nbody.py. The code is nearly identical howver with the inclusion
of the njit decortator as well as using numpy arrays.

@author: harryjordan
"""


import math
import time
import sys
import numpy as np
from numba import njit

@njit
def nbody_nb(N,nSteps):  
    position = np.random.standard_normal((N, 3))
    velocity = np.zeros_like(position)
    #nSteps = 1000
    dt = 0.01
    pos_save = np.zeros((nSteps,N, 3))
    pos_save[0,:,:] = position
    for step in range(1, nSteps + 1, 1):
        for i in range(N):
            Fx = 0.0; Fy = 0.0; Fz = 0.0
            for j in range(N):
                if j != i:
                    dx = position[j,0] - position[i,0]
                    dy = position[j,1] - position[i,1]
                    dz = position[j,2] - position[i,2]
                    drSquared = dx * dx + dy * dy + dz * dz
                    drPowerN32 = 1.0 / (drSquared + math.sqrt(drSquared))
                    Fx += dx * drPowerN32
                    Fy += dy * drPowerN32
                    Fz += dz * drPowerN32
                velocity[i, 0] += dt * Fx
                velocity[i, 1] += dt * Fy
                velocity[i, 2] += dt * Fz
        for i in range(N):
            position[i,0] += velocity[i,0] * dt
            position[i,1] += velocity[i,1] * dt
            position[i,2] += velocity[i,2] * dt
        pos_save[step-1,:,:] = position
    return pos_save

#To get the time accurately, the program must be ran once to compile it and then ran again to
#get the compiled time
if __name__ == '__main__':
    N = int(sys.argv[1])
    nSteps = int(sys.argv[2])
    nbody_nb(10, nSteps)
    start = time.time()
    nbody_nb(N, nSteps)
    print(time.time() - start)







