import sys
import urllib, json, os
from download import *
from classes import *
import time

#fMatchId = open('./AP_ITEM_DATASET/5.14/RANKED_SOLO/NA.json');
fMatchId = open('./vladMatches.json');
matchId = json.loads(fMatchId.read());

fPartId = open('./vladHighMains.json','w');
fMatchList = open('./vladHighMatches.json','w');

matchList = [];
mainsList = [];
mainsCount = 0;

for i in xrange(0,len(matchId)):
	#print matchId[i];
	if i%100==0: print 'Progress = ' + str(i*100.0/float(len(matchId))) + '%';
	path = './5.14/RANKED_SOLO/NA/'+str(matchId[i])+'.json';
	#path = open(fPath);
	#data = json.loads(path.read());
	try:
		fPath = open(path);
		data = json.loads(fPath.read());
	except:
		continue;

	for j in xrange(0,10):
		if data['participants'][j]['championId'] == 8:
			tier = data['participants'][j]['highestAchievedSeasonTier'];
			if tier == 'DIAMOND' or tier == 'PLATINUM' or tier =='MASTER' or tier == 'CHALLENGER':
				matchList.append(matchId[i]);
				mainsList.append(
					data['participantIdentities']
					[j]['player']['summonerId']);
				mainsCount = mainsCount + 1;
	#fPath.close();

print mainsCount;
json.dump(matchList,fMatchList);
json.dump(mainsList,fPartId);

fMatchId.close();
fPartId.close();
fMatchList.close();
fPath.close();