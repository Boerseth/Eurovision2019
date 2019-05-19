#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 19 12:52:26 2019

@author: frode
"""

import matplotlib.pyplot as plt


years = [
         ["2016", [["Ukraine", 323, 211],
          ["Australia", 191, 320],
          ["Russia", 361, 130],
          ["Bulgaria", 180, 127],
          ["Sweden", 139, 122],
          ["France", 109, 148],
          ["Armenia", 134, 115],
          ["Poland", 222, 7],
          ["Lithuania", 96, 104],
          ["Belgium", 51, 130],
          ["Netherlands", 39, 114],
          ["Malta", 16, 137],
          ["Austria", 120, 31],
          ["Israel", 11, 124],
          ["Latvia", 63, 69],
          ["Italy", 34, 90],
          ["Azarbaijan", 73, 44],
          ["Serbia", 80, 35],
          ["Hungary", 56, 52],
          ["Georgia", 24, 80],
          ["Cyprus", 53, 43],
          ["Spain", 10, 67],
          ["Croatia", 33, 40],
          ["United Kingdom", 8, 54],
          ["Czech Republic", 0, 41],
          ["Germany", 10, 1]]],
        #
         ["2017", [["Portugal", 376, 382],
          ["Bulgaria", 337, 278],
          ["Moldova", 264, 110],
          ["Belgia", 255, 108],
          ["Sweden", 126, 218],
          ["Italy", 208, 126],
          ["Romania", 224, 58],
          ["Hungary", 152 , 48],
          ["Australia", 2, 171],
          ["Norway", 29, 129],
          ["Netherlands", 15, 135],
          ["France", 90, 45],
          ["Croatia", 103, 25],
          ["Azerbaijan", 42, 78],
          ["United Kingdom", 12, 99],
          ["Austria", 0, 93],
          ["Belarus", 33, 50],
          ["Armenia", 21, 58],
          ["Greece", 29, 48],
          ["Denmark", 8, 69],
          ["Cyprus", 32, 36],
          ["Poland", 41, 23],
          ["Israel", 5, 34],
          ["Ukraine", 24, 12],
          ["Germany", 3, 3],
          ["Spain", 5, 0]]],
        #
         ["2018", [["Israel", 317, 212],
          ["Cyprus", 253, 183],
          ["Austria", 71, 271],
          ["Germany", 136, 204],
          ["Italy", 249, 59],
          ["Czech Republic", 215, 66],
          ["Sweden", 21, 253],
          ["Estonia", 102, 143],
          ["Denmark", 188, 38],
          ["Moldova", 115, 94],
          ["Albania", 58, 126],
          ["Lithuania", 91, 90],
          ["France", 59, 114],
          ["Bulgaria", 66, 100],
          ["Norway", 84, 60],
          ["Ireland", 62, 74],
          ["Ukraine", 119, 11],
          ["Netherlands", 32, 89],
          ["Serbia", 75, 38],
          ["Australia", 9, 90],
          ["Hungary", 65, 28],
          ["Slovenia", 23, 41],
          ["Spain", 18, 43],
          ["United Kingdom", 25, 23],
          ["Finland", 23, 23],
          ["Portugal", 18, 21]]],
        #
        ["2019",
          [["Netherlands", 261, 231],
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
          ["United Kingdom",3,13]]]
         ]
         
levels = True

for year, scores in years:
    coun = [country[0] for country in scores]
    tele = [country[1] for country in scores]
    jury = [country[2] for country in scores]
    
    print sum(tele)
    print sum(jury)
    print 
    plt.figure(figsize=(10,10.31))
    plt.suptitle("Eurovision votes, "+year, fontsize=25)
    plt.scatter(tele, jury)
    if levels:
        for c in range(15):
            x = [-5, 400]
            y = [50*c - xi for xi in x]
            plt.plot(x, y, "k")
    plt.plot([-5,400],[-5,400])
    for country, televote, juryvote in scores:
        plt.annotate(country, (televote+5, juryvote-1.5))
    plt.xlabel("Televoting")
    plt.ylabel("Jury")
    plt.axis("equal")
    plt.axis([-3,400,-3,400])
    plt.show()


plt.figure(figsize=(10,10.31))
plt.suptitle("Eurovision votes, 2016-2019", fontsize=25)
for year, scores in years:
    coun = [country[0] for country in scores]
    tele = [country[1] for country in scores]
    jury = [country[2] for country in scores]
    plt.scatter(tele, jury, label=year)
if levels:
    for c in range(15):
        x = [-5, 400]
        y = [50*c - xi for xi in x]
        plt.plot(x, y, "k")
plt.legend()
plt.plot([-5,400],[-5,400])
plt.xlabel("Televoting")
plt.ylabel("Jury")
plt.axis("equal")
plt.axis([-3,400,-3,400])
plt.show()

