#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 14:08:53 2022

A Numpy version of the original n body simulation, the structure of the program is still
the same however the postion and velocity matrices are now numpy arrays and the use of numpy
vectorisation allows for the removal of a for loop and the need for individual components.

@author: harryjordan
"""

import time
import numpy as np
import sys






def nbody_np(N, nSteps):# NumPy arrays as input
    t0 = time.time()
    position = np.random.standard_normal((N, 3))
    velocity = np.zeros_like(position)
    t0 = time.time()
    #nSteps = 1000
    dt = 0.01
    pos_save = np.zeros((nSteps,N, 3))
    pos_save[0,:,:] = position
    for step in range(1, nSteps + 1, 1):
        Fp = np.zeros((N, 3))
        for i in range(N):
            dp = position - position[i]
            drSquared = np.sum(dp ** 2, axis=1)
            h = drSquared + np.sqrt(drSquared)
            drPowerN32 = 1. / np.maximum(h, 1E-10)
            Fp += -(dp.T * drPowerN32).T
            position += dt * Fp
        position += velocity * dt
        pos_save[step-1,:,:] = position
    print(time.time() -t0)
    return  pos_save


if __name__ == '__main__':
    N = int(sys.argv[1])
    nSteps = int(sys.argv[2])
    nbody_np(N, nSteps)


