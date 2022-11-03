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
# plot histogram or not?
printHistogram = True

# INPUT OPTIONS
# path to input picture
picturePath = '/home/jan/wximg_compare/input/input.jpg'
# path to database and name of the weathertag file
databasePath = '/home/jan/wximg_compare/database/'
databaseFile = 'weathertags.csv'

# OTHER SETTINGS
# histogram compare method, see OpenCV documetation for details
histogramCompareMethod = cv.HISTCMP_CORREL

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
    1: 'light rain',
    2: 'heavy rain',
    3: 'light snowfall',
    4: 'heavy snowfall',
    5: 'hail'
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

# plots the histograms for a given image-object (file1), optionally plots a second histogram for the image-object in file2 if doubleplot=True
def plothist(file1, doubleplot=False, file2=None):
    
    hist1 = histogram(file1)
    
    plt.plot(hist1[0], color='blue')
    plt.plot(hist1[1], color='green')
    plt.plot(hist1[2], color='red')
    
    if(doubleplot==True):
        
        hist2 = histogram(file2)
        
        plt.plot(hist2[0], color='blue')
        plt.plot(hist2[1], color='green')
        plt.plot(hist2[2], color='red')
        
    plt.xlim([0,256])
    plt.show()

# compares the input image to all images in the database and adds the similarity value to the dataframe
for i, picture in enumerate(database.filename):
    compareimg = cv.imread(databasePath + picture)
    database.at[i,'similarity'] = np.mean(compareimage(image, compareimg))

# detailed output of most similar database entry
def detailedOutput(maxSimilarID):
    print('found database match :', database.filename[maxSimilarID], 'with similarity', database.similarity[maxSimilarID])
    print(' ')
    print('cloud-cover :', clouds.get(database.clouds[maxSimilarID]))
    print('percipitation :', percip.get(database.percip[maxSimilarID]))
    print('misc :', misc.get(database.misc[maxSimilarID]))
    print(' ')
    
# simple output of most similar database entry
def simpleOutput(maxSimilarID):
    print(clouds.get(database.clouds[maxSimilarID]), end='')
    if (database.percip[maxSimilarID]!=0):
        print(', ', percip.get(database.percip[maxSimilarID]), end='')
    if (database.misc[maxSimilarID]!=0):
        print(', ', misc.get(database.misc[maxSimilarID]), end='')
    print('')

# print out most similar database entry
if (verboseOutput):
    detailedOutput(database['similarity'].idxmax())
else:
    simpleOutput(database['similarity'].idxmax())

# plot the histogram of the input image and the match
<<<<<<< HEAD
#plothist(image, doubleplot=True, file2=cv.imread(databasePath + database.filename[maxSimilarID]))
=======
if (printHistogram):
    plothist(image, doubleplot=True, file2=cv.imread(databasePath + database.filename[database['similarity'].idxmax()]))
>>>>>>> outputModes
