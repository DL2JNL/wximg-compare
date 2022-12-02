#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Weathercam image comparison software
By Jan Niklas Lorenz - October 2022
"""

import cv2 as cv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


#---CONFIG---

# OUTPUT OPTIONS
# verbose (more detailed) [Ture] or simple [False] output?
verboseOutput = True
# single database-match output [False] or list output [True]?
listOutput = True
# plot histogram or not?
printHistogram = False

# INPUT OPTIONS
# path to input picture
picturePath = '/home/jan/wximg_compare/input/input.jpg'
# path to database and name of the weathertag file
databasePath = '/home/jan/wximg_compare/database/'
databaseFile = 'weathertags.csv'

# OTHER SETTINGS
# histogram compare method, see OpenCV documetation for details
histogramCompareMethod = cv.HISTCMP_CORREL
# verbose output : number of most-similar database entries to display in the output ; non-verbose output : number of most-similar database entries to use for determination of the weather-tags
outputNumber = 10

#------------

# import the input image
image = cv.imread(picturePath)

# read the database, insert colum names and add colum for similarity value
database = pd.read_csv(databasePath + databaseFile, header=None, names=['filename','clouds','percip','misc'])
database.insert(4, 'similarity', 0)

# dictorys for case-routine
clouds={
    0: 'clear/sunny',
    1: 'only high/cirrus clouds',
    2: 'few clouds',
    3: 'partly cloudy',
    4: 'cloudy',
    5: 'fog'
}

percip={
    0: 'no percipitation',
    1: 'rain',
    2: 'snowfall',
    3: 'hail'
}

misc={
    0: 'none',
    1: 'rainshowers in the distance',
    2: 'snow on ground',
    3: 'thunderstorm'
}

# calculates the BGR histograms for an input image, returns a list containing the B- G- and R-channel histograms
def histogram(img):
    
    histB = cv.calcHist([img], [0], None, [256], [0,256])
    cv.normalize(histB, histB, 0, 1, cv.NORM_MINMAX)
    histG = cv.calcHist([img], [1], None, [256], [0,256])
    cv.normalize(histG, histG, 0, 1, cv.NORM_MINMAX)
    histR = cv.calcHist([img], [2], None, [256], [0,256])
    cv.normalize(histR, histR, 0, 1, cv.NORM_MINMAX)
    
    hist = [histB, histG, histR]
    return hist

# compares the two image-objects given in file1 and file2
def compareimage(file1, file2):
    
    hist = histogram(file1)
    histComp = histogram(file2)
    
    similarityB = cv.compareHist(hist[0], histComp[0], histogramCompareMethod)
    similarityG = cv.compareHist(hist[1], histComp[1], histogramCompareMethod)
    similarityR = cv.compareHist(hist[2], histComp[2], histogramCompareMethod)
    
    similarity = [similarityB, similarityG, similarityR]
    return similarity

# prints list output (verbose=True) or simple output (verbose=false)
def createOutput(verbose = True):
    cloudCount = [0]*6
    percipCount = [0]*4
    miscCount = [0]*4
    if (verbose):
        print(maxSimilarList)
    else:
        
        for c in range(0,6):
            cloudCount[c] = maxSimilarList.clouds[maxSimilarList.clouds==c].count()
        for p in range(0,4):
            percipCount[p] = maxSimilarList.percip[maxSimilarList.percip==p].count()
        for m in range(0,4):
            miscCount[m] = maxSimilarList.misc[maxSimilarList.misc==m].count()
        print(clouds.get(cloudCount.index(max(cloudCount))), end='')
        if (percipCount.index(max(percipCount))!=0):
            print(', ', percip.get(percipCount.index(max(percipCount))), end='')
        if (miscCount.index(max(miscCount))!=0):
            print(', ', misc.get(miscCount.index(max(miscCount))), end='')
        print('')

# plots the histograms for a given image-object (file)
def plothist(file):
    
    hist = histogram(file)
    
    plt.plot(hist[0], color='blue')
    plt.plot(hist[1], color='green')
    plt.plot(hist[2], color='red')
        
    plt.xlim([0,256])
    plt.show()

# compares the input image to all images in the database and adds the similarity value to the dataframe
for i, picture in enumerate(database.filename):
    compareimg = cv.imread(databasePath + picture)
    database.at[i,'similarity'] = np.mean(compareimage(image, compareimg))
# create List of [outputNumber] most-similar database-enteries
maxSimilarList = database.sort_values(by='similarity', ascending=False)[0:outputNumber]

# list output or singel-match output
if (verboseOutput):
    createOutput(verbose=True)
else:
    createOutput(verbose=False)

# plot the histogram of the input image
if (printHistogram):
    plothist(image)