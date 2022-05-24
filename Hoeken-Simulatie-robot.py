# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 12:30:42 2022

@author: luccu
"""
import numpy as np
import math


r11 = 0
r12 = 1
r13 = 0
r21 = -0.939693
r22 = 0
r23 = 0.342020
r31 = 0.342020
r32 = 0
r33 = 0.939693

Beta = math.atan2(-r31, math.sqrt(r11**2 + r21**2))
Alpha = math.atan2(r21/math.cos(Beta), r11/math.cos(Beta))
Gamma = math.atan2(r32/math.cos(Beta), r33/math.cos(Beta))

Alpha_deg = np.degrees(Alpha)
Beta_deg = np.degrees(Beta)
Gamma_deg = np.degrees(Gamma)


print("Alpha",Alpha_deg)
print("Beta",Beta_deg)
print("Gamma",Gamma_deg)


