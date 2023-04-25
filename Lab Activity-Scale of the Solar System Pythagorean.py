#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 11:53:05 2023

@author: bradymcgawn
"""

import math

#define variables- in feet
points_data = {
    'Outdoor Chapel': {'h': 1127, 'e': 124},
    'Obser. Lookout': {'h': 2633, 'e': 349},
    'Tw pks Loouout': {'h': 6970, 'e': 2052},
}

#calculate the distances using the pythagorean theorem 
for points, data in points_data.items():
    d = math.sqrt(data['h']**2 + data['e']**2)
    theta = math.atan(data['e']/data['h'])
    theta_deg = math.degrees(theta)
    print(f"{points}: d = {d: .2e},     "
          
          f"{points}: inclination = {theta_deg: .2e} degrees")
