# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 22:55:09 2019

@author: Ian Wood
"""

import pandas as pd
import matplotlib

Location = "crime.csv"
cmnStreets = {}
df = pd.read_csv(Location, engine='python')
for street in df["STREET"]:
    if street in cmnStreets:
        cmnStreets[street] += 1
    else:
        cmnStreets[street] = 1
answer = max(cmnStreets, key=cmnStreets.get)
print("")
print("The most dangerous street in Boston is", answer.lower().title())
print("With a total of", cmnStreets[answer], "crimes committed here since 2015.")
