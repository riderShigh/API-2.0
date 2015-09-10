# ************************************************
# 	filterPatchDates.py
#	Filter out matches not played on patches
#	5.10 to 5.16
#	
#	Usage: python filterPatchDates.py [champion]
# ************************************************

import sys
import urllib, json, os, math
import operator
import errno
from classes import *
from processing import *
from download import *

thisChamp = str(sys.argv[1]);

# Patch start times in epoch
patch510epoch = 1432810800000;
patch513epoch = 1436438400000;
patch516epoch = 1440068400000;

# Load time stamps for matches played by mains
fTimeStamps = open('./pickDropStats/' + str(thisChamp) + '.json');
timeStamps = json.loads(fTimeStamps.read());

playCounts = {};
summonerCount = 0;

# Loop through regions
for region,thisRegion in timeStamps.iteritems():

	# Loop through patches
	for patch,thisPatch in thisRegion.iteritems():

		# Loop through summoners
		for summoners in thisPatch:

			playCounts[summonerCount] = [0,0];

			# Check which patch the match is played on
			# Count increments when either match is in 5.10-5.13 or 5.14-5.16
			for thisSummoner,matchTimeList in summoners.iteritems():
				for matchTime in matchTimeList:
					if matchTime > patch510epoch and matchTime < patch513epoch:
						playCounts[summonerCount][0] += 1;
					if matchTime > patch513epoch and matchTime < patch516epoch:
						playCounts[summonerCount][1] += 1;
			summonerCount += 1;

# Save filtered data to file
try:
	os.makedirs('./pickDropStats/filtered/');
except OSError as exception:
	if exception.errno != errno.EEXIST:
		raise

fWriteFiltered = open('./pickDropStats/filtered/' + str(thisChamp) + '.json','w');
json.dump(playCounts,fWriteFiltered);
fWriteFiltered.close();