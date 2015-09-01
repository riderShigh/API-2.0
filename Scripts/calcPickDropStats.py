import sys
import urllib, json, os, math
import operator
import errno
from classes import *
from processing import *
from download import *

#thisChamp = sys.argv[1];
#thisChamp = "131";
champList = [131,134,25,27,28,161,4,8,127, 268, 55, 50, 115, 117, 112, 82, 84, 85, 3, 7, 245, 103, 101, 105, 38, 31, 30, 34,60, 61, 63, 68, 69, 99, 90, 96, 10, 13, 17, 45, 43, 1, 9, 143, 76, 74];
champObj = {}

for thisChamp in champList:
	champObj[str(thisChamp)] = [];
	fData = open('./pickDropStats/filtered/' + str(thisChamp) + '.json');
	data = json.loads(fData.read());
	pickDrop = [0,0,0];
	criteria = [6.951, 0.1654,-1];

	for key,value in data.iteritems():
		if value[0] < 3 and value[1] < 3:
			continue;
		if value[0] != 0:
			ratio = value[1]/float(value[0]);
			for crit in xrange(0,len(criteria)):
				if ratio > criteria[crit]: 
					pickDrop[crit] += 1;
					break;
		else:
			pickDrop[0] += 1;

	total = pickDrop[0] + pickDrop[1] + pickDrop[2];
	#print pickDrop;
	pickDropRatio = [0,0,0];
	for i in xrange(0,3):
		pickDropRatio[i] = pickDrop[i]/float(total);
	#print pickDropRatio
	champObj[str(thisChamp)] = pickDropRatio;

	fWrite = open('./pickDropStats/tallied/' + str(thisChamp) + '.json','w');
	json.dump(pickDrop,fWrite);
	fWrite.close();
