# API Challenge 2.0
# AP Champions: Mains vs Non-Mains 

#Introduction

Has the patch 5.13, the patch where AP items received huge changes, impact the player base a lot? There are numbers we can direct ourselves to, such as KDA and win rates, and the biggest of all, item popularity.
There are other more subtle behavioral changes that we can look at. In particular, we want to know if champion mains react differently to the patch compared to the average citizen.
Moreover, it is interesting to learn if champion mains emerged or disappeared because of the patch. In this project we will look at these statistics, using direct observation, principle component analysis (PCA), and neural networks.

#Quick-Start
Load mainpage.html in a web brower. Specifically, you can open http://rawgit.com/riderShigh/API-2.0/master/mainpage.html. This provides all the interface and information needed to understand this project from the user-end.

#Short Description of Scripts:

Order of scripts being run: 

dl2na.py > fixdl.py > readMatches.js > pca.py > postPcaProcessing.bat > readPickDrop.bat > calcPickDropStats.py

Python libraries:

classes.pyc: classes used to structure statistics to be read from the API

download.pyc: functions for building URL names and downloading data from the API 

processing.pyc : function for extracting important statistics from downloaded data