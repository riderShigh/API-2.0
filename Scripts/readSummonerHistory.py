import sys
import urllib, json, os
from download import *
from classes import *
import time

#fPlayer = open('vladMains.json','r');
fPlayer = open('vladHighMains.json','r');
pPlayer = json.loads(fPlayer.read());

statList = {};

fSave = open('vladHighMainStats.json','w');

totalPlayed = 0;
championPlayed = 0;

for i in xrange(0,len(pPlayer)):
	totalPlayed = 0;
	data = json.loads(dlURLData_stats('na',str(pPlayer[i]),'ranked'));
	for champion in data['champions']:
		totalPlayed += champion['stats']['totalSessionsPlayed'];
		if champion['id'] == 8:
			if i%10 == 0:
				print('Completed ' + str(i+1) + ' out of ' + str(len(pPlayer))); 
				print('ID = ' + str(pPlayer[i]));
			totalSessionsPlayed = champion['stats']['totalSessionsPlayed'];
			thisStat = stats(pPlayer[i],totalSessionsPlayed,
				champion['stats']['totalSessionsWon'],
				champion['stats']['totalChampionKills']/float(totalSessionsPlayed),
				champion['stats']['totalDeathsPerSession']/float(totalSessionsPlayed),
				champion['stats']['totalAssists']/float(totalSessionsPlayed));
			championPlayed = totalSessionsPlayed;
			#print('KDA = ' + str(thisStat.totalKDA));
			#print('Kills = ' + str(thisStat.totalChampionKills));
			#print('Deaths = ' + str(thisStat.totalDeaths));
			#print('Assists = ' + str(thisStat.totalAssists));
			
			#statList.append(json.dumps(thisStat.__dict__));
			#statObj = stats(this);
			#json.dump(stats,)
	thisStat.championPlayRate = championPlayed/float(totalPlayed);
	print thisStat.championPlayRate
	statList[i] = thisStat.__dict__;
json.dump(statList,fSave);


#dlURLData_matchList('na',str(pPlayer[1]));