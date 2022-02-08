#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 14:52:50 2022


Lists of data that was used to generate the releant graphs
@author: harryjordan
"""

import matplotlib.pyplot as plt
N = [10,20,25,50,75,100,200,400]

p = [0.0967,0.345,0.534,2.04,4.569,8.08,32.1,132.5]
pstd = [0.01,0.006,0.01,0.02,0.06,0.005,0.01,0.35]

np = [0.14,0.282,0.334,0.706,1.11,1.53,3.95,9.68]
npstd = [0.02,0.01,0.01,0.02,0.02,0.007,0.04,0.02]

nb = [0.000417,0.000153,0.00224,0.00914,0.0212,0.0374,0.142,0.577]
nbstd = [0.00004,0.0001,0.000003,0.00005,0.0009,0.002,0.002,0.01]

somp2 = [0.00725,0.004,0.00777,0.0102,0.0147,0.0258,0.0625,0.226]
somp2std = [0.002,0.00005,0.0004,0.001,0.003,0.003,0.003,0.002]
esomp2 = [0.416,0.855,0.53,0.944,1.342,1.236,1.81,1.91]
esomp2std = [0.00008,0.0001,0.0001,0.0001,0.001,0.0004,0.0008,0.002]


somp8 = [0.212,0.176,0.244,0.192,0.28,0.266,0.441,0.93]
somp8std = [0.0207,0.037,0.024,0.027,0.02,0.036,0.01,0.05]
esomp8 = [0.012,0.02,0.00180,0.051,0.067,0.118,0.26,0.462]
esomp8std = [0.00001,0.00002,0.00001,0.00001,0.00001,0.00003,0.00005,0.002]

'''
omp1std 

omp2
omp2std
'''

bigN = [1000,2000,3000,4000,5000,10000]

omp2     = [0.0271, 0.0630,0.350,1.41, 5.49,33.9]
omp2std  = [0.003, 0.003, 0.009, 0.006, 0.06,0.02 ]
eomp2    = [1.15,   1.76, 1.93, 1.93, 1.96, 1.97]
eomp2std = [0.0004, 0.0006, 0.00200,0.01,0.003, 0.07]    

omp4 = [0.0572,0.140,0.162,0.805,2.88,17.7]
omp4std = [0.02,0.01,0.002,0.01,0.02,0.2]
eomp4 = [0.543,0.807,2.74,3.36,3.47,3.77]
eomp4std = [0.0004,0.002,0.002,0.008,0.1,0.052]


omp8 = [0.326,0.451,1.14,3.41,4.253,18.0]
omp8std = [0.07,0.003,0.02,0.2,0.07,0.07]
eomp8 = [0.10,0.252,0.597,0.799,2.52,3.71]
eomp8std = [0.0001,0.002,0.002,0.03,0.006,0.2]

thousand = [1.93,2.56,3.36,1.32,0.799]
sthousand = [0.002,0.002,0.0005,0.0003,0.002]
twothousand = [1.96,2.9,3.47,2.99,2.52]
stwothousand = [0.003,0.008,0.009,0.001,0.006]
threethousand = [1.96,2.97,3.85,3.14,3.056]
sthreethousand = [0.002,0.002,0.001,0.002,0.002]
fourthousand = [1.99,2.9,3.86,3.59,2.86]
sfourthousand = [0.004,0.001,0.002,0.0008,0.005]
fivethousand = [1.97,2.95,3.77,3.54,3.71]
sfivethousand = [0.07,0.001,0.052,0.01,0.02]
tenthousand = [1.96,2.95,3.86,4.31,4.62]
stenthousand = [0.002,0.006,0.0008,0.008,0.002]

processor = [2,3,4,6,8]





fig,ax = plt.subplots()
ax.errorbar(N, nb, yerr=npstd,linewidth=0.5,elinewidth=1.0,color = 'r',label='p=1')
ax.errorbar(N, somp2 , yerr=somp2std,linewidth=0.5,elinewidth=1.0,color = 'b',label='p=2')
ax.errorbar(N, somp8 , yerr=somp8std,linewidth=0.5,elinewidth=1.0,color = 'g',label='p=8')
ax.set_xlabel('Number of particles')
ax.set_ylabel('Time')
ax.set_yticks([])
ax.legend()
ax2=ax.twinx()
ax2.errorbar(N, esomp2 , yerr=esomp2std,linewidth=0.5,elinewidth=1.0,color = 'y',linestyle='--')
ax2.errorbar(N, esomp8 , yerr=esomp8std,linewidth=0.5,elinewidth=1.0,color = 'g',linestyle='--')
ax2.set_ylabel('efficiency')

'''
plt.errorbar(processor, thousand , yerr=sthousand,linewidth=0.5,elinewidth=1.0,color = 'r',label='1000')
plt.errorbar(processor,twothousand , yerr=stwothousand,linewidth=0.5,elinewidth=1.0,color = 'g',label='2000')
plt.errorbar(processor,threethousand , yerr=sthreethousand,linewidth=0.5,elinewidth=1.0,color = 'b',label='3000')
plt.errorbar(processor,fourthousand , yerr=sfourthousand,linewidth=0.5,elinewidth=1.0,color = 'y',label='4000')
plt.errorbar(processor,fivethousand , yerr=sfivethousand,linewidth=0.5,elinewidth=1.0,color = 'c',label='5000')
plt.errorbar(processor,tenthousand , yerr=stenthousand,linewidth=0.5,elinewidth=1.0,color = 'm',label='10000')
'''


       
plt.xlabel('Number of processors')
plt.ylabel('Efficiency')
plt.legend()
plt.show()
