# ************************************************
# 	dl2na.py
#	Script for downloading data from the API
#	
#	Usage: python dl2na.py [region]
#
#	1. Reads in given match Ids from a list file.
#	2. For each match Id download full match data
#		with timeline
#	3. Save match data to files in json format
# ************************************************

import sys
import urllib, json, os
from download import *
import time

# Define patches, queue type, and region
patch = ['5.11','5.14'];
queueType = ['RANKED_SOLO'];	#queueType = ['NORMAL_5X5'];
region = [sys.argv[1]];			#region = ['BR','EUNE','EUW','KR','LAN','LAS','NA','OCE','RU','TR'];

# Loop over patches
for iPatch in xrange(0,len(patch)):

	# Loop over queue types
	for iQType in xrange(0,len(queueType)):

		# Loop over regions
		for iRegion in xrange(0,len(region)):

			# Define directory paths for reading and writing data
			pathName = buildPathName(patch[iPatch],queueType[iQType],region[iRegion]);
			folderPath = buildFolderName(patch[iPatch],queueType[iQType],region[iRegion]);

			# Read and parse match Id's from match list file
			fData = open(pathName,'r');
			parsedData = json.loads(fData.read());

			# Loop through parsed match Id's
			for i in xrange(0,len(parsedData)):

				# Create output file to save match data with timeline
				newFileName = folderPath+str(parsedData[i])+'.json';
				if os.path.exists(newFileName): continue;
				dat = dlURLData_match(region[iRegion].swapcase(),str(parsedData[i]),1);
				if not os.path.exists(folderPath): os.makedirs(folderPath);
				try:
					fWrite = open(newFileName,'w');
				except:
					os.remove(newFileName);
					fWrite = open(newFileName,'w');

				# Write data to output file
				fWrite.write(dat);
				fileSize = os.path.getsize(newFileName);
				if fileSize < 5000: 
					time.sleep(0.0035);