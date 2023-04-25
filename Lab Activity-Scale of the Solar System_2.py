#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 22:45:04 2023

@author: bradymcgawn
"""

import math
"""
#this is the code I used to calculate the ratios used in the second part
#I commented it out because I didn't need it to run every time
# Define constants
sun_radius = 696340  # km
au = 149597870.7  # km
planet_data = {
    'Mercury': {'radius': 2439.7, 'distance': 0.387},
    'Venus': {'radius': 6051.8, 'distance': 0.723},
    'Earth': {'radius': 6371.0, 'distance': 1.0},
    'Mars': {'radius': 3389.5, 'distance': 1.524},
    'Jupiter': {'radius': 69911, 'distance': 5.203},
    'Saturn': {'radius': 58232, 'distance': 9.539},
    'Uranus': {'radius': 25362, 'distance': 19.18},
    'Neptune': {'radius': 24622, 'distance': 30.07},
}

# Calculate and print planet sizes and orbital radii relative to the size of the sun
for planet, data in planet_data.items():
    planet_radius = data['radius'] / sun_radius
    planet_distance = data['distance'] * au / sun_radius
    print(f"{planet}: radius = {planet_radius:.2e} times the size of the sun, "
          f"orbital radius = {planet_distance:.2e} times the size of the sun")

"""
# Define constants
a = 7.1 #feet

# Define planet data- these are all ratios, so they are unitless quantities
planet_ratios = {
    'Mercury': {'radius': 3.50e-03, 'orbital_radius': 8.31e+01},
    'Venus': {'radius': 8.69e-03, 'orbital_radius': 1.55e+02},
    'Earth': {'radius': 9.15e-03, 'orbital_radius': 2.15e+02},
    'Mars': {'radius': 4.87e-03, 'orbital_radius': 3.27e+02},
    'Jupiter': {'radius': 1.00e-01, 'orbital_radius': 1.12e+03},
    'Saturn': {'radius': 8.36e-02, 'orbital_radius': 2.05e+03},
    'Uranus': {'radius': 3.64e-02, 'orbital_radius': 4.12e+03},
    'Neptune': {'radius': 3.54e-02, 'orbital_radius': 6.46e+03}
}
print('sun radius =', a)

# update then print the planet data

for planet, ratios in planet_ratios.items():
    planet_radius = ratios['radius'] * a
    orbital_radius = ratios['orbital_radius'] * a
    print(f"{planet}: radius = {planet_radius:.2e}, "
          f"orbital radius = {orbital_radius:.2e}")

print()
print()  
# Define constants
b = 1.15 #feet

# Define planet data- these are all ratios, so they are unitless quantities
planet_ratios = {
    'Mercury': {'radius': 3.50e-03, 'orbital_radius': 8.31e+01},
    'Venus': {'radius': 8.69e-03, 'orbital_radius': 1.55e+02},
    'Earth': {'radius': 9.15e-03, 'orbital_radius': 2.15e+02},
    'Mars': {'radius': 4.87e-03, 'orbital_radius': 3.27e+02},
    'Jupiter': {'radius': 1.00e-01, 'orbital_radius': 1.12e+03},
    'Saturn': {'radius': 8.36e-02, 'orbital_radius': 2.05e+03},
    'Uranus': {'radius': 3.64e-02, 'orbital_radius': 4.12e+03},
    'Neptune': {'radius': 3.54e-02, 'orbital_radius': 6.46e+03}
}
print('sun radius =', b)
# Multiply the values by b
for planet, ratios in planet_ratios.items():
    planet_radius = ratios['radius'] * b
    orbital_radius = ratios['orbital_radius'] * b
    print(f"{planet}: radius = {planet_radius:.2e}, "
          f"orbital radius = {orbital_radius:.2e}")
