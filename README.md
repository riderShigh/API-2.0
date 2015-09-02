**API Challenge 2.0
# AP Champions: Mains vs Non-Mains 

#Introduction

Has the patch 5.13, the patch where AP items received huge changes, impact the player base a lot? There are numbers we can direct ourselves to, such as KDA and win rates, and the biggest of all, item popularity.
There are other more subtle behavioral changes that we can look at. In particular, we want to know if champion mains react differently to the patch compared to the average citizen.
Moreover, it is interesting to learn if champion mains emerged or disappeared because of the patch. In this project we will look at these statistics, using direct observation, principle component analysis (PCA), and neural networks.

#Quick-Start
Load mainpage.html in a web brower. Specifically, you can open http://rawgit.com/riderShigh/API-2.0/master/mainpage.html. This provides all the interface and information needed to understand this project from the user-end.
For detailed discussion of the analysis, go to the "Methods" in the webpage.

#Data Usage
Initial match data were taken from the API using the original downloadable match list provided on the contest page. All regions were used, while only ranked games were analyzed as an attempt to reduce randomness in plays by only considering more serious players. In addition match list data is used for identified champion mains to train our neural network. For the sake of conciseness only analysis from heavy AP item users and AP items were presented. 

#Short Description of Scripts:

Order of important scripts being run: 

dl2na.py > fixdl.py > readMatches.js > pca.py > postPcaProcessing.bat > readPickDrop.bat > calcPickDropStats.py > pickdrop_neural.m

**Important scripts**:

- *dl2na.py*: downloads API data from server

- *fixdl.py*: re-download data that received error codes

- *readMatches.js*: convert downloaded data into statistics

- *pca.py*: principle component analysis on compiled data

- *postPcaProcessing.bat*: reads in postPcaProcessing.py to convert PCA statistics into a presentable format

- *readPickDrop.bat*: reads in dlTimeStamps.py to get number of plays for each champion from raw data

- *calcPickDropStats.py*: prepare statistics for training neural network

- *pickdrop_neural.m*: creates data structure compatible to Matlab neural network app. Run the app to obtain neural network.


**Python libraries**:

- *classes.pyc*: classes used to structure statistics to be read from the API

- *download.pyc*: functions for building URL names and downloading data from the API 

- *processing.pyc*: function for extracting important statistics from downloaded data 
