import sys
import urllib, json, os
from download import *
import time

patch = ['5.11','5.14']; #5.11
#queueType = ['NORMAL_5X5','RANKED_SOLO'];
queueType = ['RANKED_SOLO'];
#region = ['BR','EUNE','EUW','KR','LAN','LAS','NA','OCE','RU','TR'];
region = ['EUW'];

for iPatch in xrange(0,len(patch)):

	for iQType in xrange(0,len(queueType)):

		for iRegion in xrange(0,len(region)):

			pathName = buildPathName(patch[iPatch],queueType[iQType],region[iRegion]);
			folderPath = buildFolderName(patch[iPatch],queueType[iQType],region[iRegion]);
			fData = open(pathName,'r');
			parsedData = json.loads(fData.read());
			i = 4032;

			while i < len(parsedData):
				now = time.time();
				dat = dlURLData_match(region[iRegion].swapcase(),str(parsedData[i]),1);
				newFileName = folderPath+str(parsedData[i])+'.json';
				if not os.path.exists(folderPath): os.makedirs(folderPath);
				fWrite = open(newFileName,'w');
				fWrite.write(dat);
				fileSize = os.path.getsize(newFileName);
				i += 1;
				if fileSize < 5000: 
					i -= 1;
					time.sleep(0.0035);
				else:
					elapsed = time.time() - now;
					if elapsed < 0.003: time.sleep(0.0035-elapsed);
