import sys
import urllib, json, os, math
import operator
import errno
from classes import *
from processing import *
from download import *
import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('pa1087','5lnuuhu8xi');

thisPatch = '5.11';
thisChamp = '3';
region = ['BR','EUNE','EUW','KR','LAN','LAS','NA','OCE','RU','TR'];
timeStamps = [];

fGoodPlayerList = open('./champGoodMains.json');
goodPlayerList = json.loads(fGoodPlayerList.read());

fGoodPlayerMatchList = open('./champGoodMainMatches.json');
goodPlayerMatchList = json.loads(fGoodPlayerMatchList.read());

for thisRegion in region:
	print 'on region ' + thisRegion;
	for thisSummoner in goodPlayerList[thisPatch][thisRegion][thisChamp]:
		print 'summoner ' + str(thisSummoner);
		#fMatchData = './' + thisPatch + '/RANKED_SOLO/' + thisRegion + '/' str(thisMatch) + '.json';
		try:
			fMatchList = dlURLData_matchList(thisRegion.lower(),str(thisSummoner),str(thisChamp),'RANKED_SOLO_5x5');
			matchList = json.loads(fMatchList);
		except:
			print 'match not read';
			continue;
		for i in xrange(0,int(matchList['totalGames'])):
			timeStamps.append(matchList['matches'][i]['timestamp']);


print timeStamps;