#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 19 12:52:26 2019

@author: frode
"""

import matplotlib.pyplot as plt


scores = [["Netherlands", 261, 231],
          ["Italy",253,212],
          ["Russia",244,125],
          ["Switzerland",212,148],
          ["Norway",291,47],
          ["Sweden",93,239],
          ["Azarbaijan",100,197],
          ["North Macedonia",58,237],
          ["Australia",131,154],
          ["Iceland",186,48],
          ["Czech Republic",7,150],
          ["Denmark",51,69],
          ["Slovenia",59,46],
          ["France",38,67],
          ["Cyprus",32,69],
          ["Malta",20,75],
          ["Serbia",54,38],
          ["Albania",47,43],
          ["Estonia",48,38],
          ["San Marino",65,16],
          ["Greece",24,47],
          ["Spain",53,7],
          ["Israel",35,12],
          ["Germany",0,32],
          ["Belarus",13,18],
          ["United Kingdom",3,13]]

coun = [country[0] for country in scores]
tele = [country[1] for country in scores]
jury = [country[2] for country in scores]


plt.figure(figsize=(11.1,9))
plt.scatter(tele, jury)
for country, televote, juryvote in scores:
    plt.annotate(country, (televote+5, juryvote-1.5))
plt.xlabel("Televoting")
plt.ylabel("Jury")
plt.axis("equal")
plt.axis([-3,350,-3,275])
plt.show()
