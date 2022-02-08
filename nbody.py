#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 12:21:30 2022

The python only version of the nbody simulation, generates N stationary particles with 
random positions. then iterates the positions through the main loop to calculate the force in that
timestep. For the purposes of these simulations, the masses and graviational constant have been set to
1

@author: harryjordan
"""
import random
import math
import time
import numpy as np
import sys

#pos_save index
#1st index = steps
#2nd index = particle
#3rd index = x,y,z correlate to [0,1,2]

#particle index 
#1st index = particle
#2nd index = x,y,z

def nbody(N,nSteps):
    t0 = time.time()
    #Generates particle positions
    position = []
    for i in range(N):
        position.append([random.gauss(0.0, 1.0) for j in range(3)])
    velocity = [[0, 0, 0] for x in position]
    dt = 0.01
    pos_save = np.zeros((nSteps,N, 3))
    pos_save[0,:,:] = position

    for step in range(1, nSteps + 1, 1):
        for i in range(N):
            Fx = 0.0; Fy = 0.0; Fz = 0.0
            for j in range(N):
                if j != i:
                    dx = position[j][0] - position[i][0]
                    dy = position[j][1] - position[i][1]
                    dz = position[j][2] - position[i][2]
                    drSquared = dx * dx + dy * dy + dz * dz
                    drPowerN32 = 1.0 / (drSquared + math.sqrt(drSquared) + 0.0001) #softening factor
                    Fx += dx * drPowerN32
                    Fy += dy * drPowerN32
                    Fz += dz * drPowerN32
                velocity[i][0] += dt * Fx
                velocity[i][1] += dt * Fy
                velocity[i][2] += dt * Fz
        for i in range(N):
            position[i][0] += velocity[i][0] * dt
            position[i][1] += velocity[i][1] * dt
            position[i][2] += velocity[i][2] * dt
        pos_save[step-1,:,:] = position
        
    print(time.time() - t0,)
    return pos_save


if __name__ == '__main__':
    N = int(sys.argv[1])
    nSteps = int(sys.argv[2])
    nbody(N, nSteps)





