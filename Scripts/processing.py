import sys
import urllib, json, os
from download import *
from classes import *
import time
import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('pa1087','5lnuuhu8xi');

def extractChampStats(mainsFile,mainsStat,patch,champId):
	region = ['BR','EUNE','EUW','KR','LAN','LAS','NA','OCE','RU','TR'];
	fPlayerList = open(mainsFile,'r');
	playerList = json.loads(fPlayerList.read());
	statList = {};
	fSave = open(mainsStat,'w');
	j = 0;

	for reg in xrange(0,len(region)):
		print '--------------------';
		print 'Patch ' + patch;
		print 'Region ' + region[reg] + ' (' + str(reg+1) + '/10)';
		print '--------------------';
		#for i in xrange(0,len(playerList[patch][region][champId])):
		for i in xrange(0,len(playerList[patch][region[reg]][champId])):
			totalPlayed = 0;
			try:
				data = json.loads(dlURLData_stats(region[reg].swapcase(),str(playerList[patch][region[reg]][champId][i]),'ranked'));
			except:
				continue;
			for champion in data['champions']:
				totalPlayed += champion['stats']['totalSessionsPlayed'];
				if champion['id'] == int(champId):
					if i%10 == 0:
						print('Completed ' + str(i+1) + ' out of ' + str(len(playerList[patch][region[reg]][champId]))); 
						print('ID = ' + str(playerList[patch][region[reg]][champId][i]));
					totalSessionsPlayed = champion['stats']['totalSessionsPlayed'];
					thisStat = stats(playerList[patch][region[reg]][champId][i],float(totalSessionsPlayed),
						champion['stats']['totalSessionsWon'],
						champion['stats']['totalChampionKills']/float(totalSessionsPlayed),
						champion['stats']['totalDeathsPerSession']/float(totalSessionsPlayed),
						champion['stats']['totalAssists']/float(totalSessionsPlayed),
						region[reg]);
					championPlayed = totalSessionsPlayed;
					#print('KDA = ' + str(thisStat.totalKDA));
					#print('Kills = ' + str(thisStat.totalChampionKills));
					#print('Deaths = ' + str(thisStat.totalDeaths));
					#print('Assists = ' + str(thisStat.totalAssists));
					
					#statList.append(json.dumps(thisStat.__dict__));
					#statObj = stats(this);
					#json.dump(stats,)
			thisStat.championPlayRate = championPlayed/float(totalPlayed);
			statList[j] = thisStat.__dict__;
			j += 1;
	json.dump(statList,fSave);

#dlURLData_matchList('na',str(pPlayer[1]));