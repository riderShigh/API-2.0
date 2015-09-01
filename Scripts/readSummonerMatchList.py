import sys
import urllib, json, os
from download import *
from classes import *
import time

fPlayer = open('vladMains.json','r');
pPlayer = json.loads(fPlayer.read());

statList = {};

fSave = open('vladMainMatchList.json','w');

for i in xrange(0,len(pPlayer)):
	#dlURLData_matchList('na',str(pPlayer[i]),8,'RANKED_SOLO_5x5',10,30)
	try:
		data = json.loads(dlURLData_matchList('na',str(pPlayer[i]),8,'RANKED_SOLO_5x5',10,30));
	except:
		continue;

	try:
		data['matches'];
	except:
		continue;
		
	for match in data['matches']:
		try:
			match['matchId'];
		except:
			continue;


		#print match[i]['matchId']

			#statObj = stats(this);
			#json.dump(stats,)
#json.dump(statList,fSave);


#dlURLData_matchList('na',str(pPlayer[1]));