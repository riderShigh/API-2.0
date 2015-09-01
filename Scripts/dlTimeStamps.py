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

patches = ['5.11','5.14'];
thisChamp = sys.argv[1];
region = ['BR','EUNE','EUW','KR','LAN','LAS','NA','OCE','RU','TR'];
timeStamps = [];
saveTimeStamps = {};

fGoodPlayerList = open('./champGoodMains.json');
goodPlayerList = json.loads(fGoodPlayerList.read());

fGoodPlayerMatchList = open('./champGoodMainMatches.json');
goodPlayerMatchList = json.loads(fGoodPlayerMatchList.read());

for thisRegion in region:
	saveTimeStamps[thisRegion] = {};
	print 'on region ' + thisRegion;
	for thisPatch in patches:
		print 'on patch ' + str(thisPatch);
		saveTimeStamps[thisRegion][thisPatch] = [];
		for thisSummoner in goodPlayerList[thisPatch][thisRegion][thisChamp]:
			timeStamps = [];
			print 'summoner ' + str(thisSummoner);
			#fMatchData = './' + thisPatch + '/RANKED_SOLO/' + thisRegion + '/' str(thisMatch) + '.json';
			try:
				fMatchList = dlURLData_matchList(thisRegion.lower(),str(thisSummoner),str(thisChamp),'RANKED_SOLO_5x5');
				matchList = json.loads(fMatchList);
			except:
				print 'match not read';
				continue;
			try:
				a = int(matchList['totalGames']);
			except:
				print 'no total games';
				continue;
			for i in xrange(0,int(matchList['totalGames'])):
				timeStamps.append(matchList['matches'][i]['timestamp']);
			saveTimeStamps[thisRegion][thisPatch].append({str(thisSummoner):timeStamps})


try:
	os.makedirs('./pickDropStats/'+ str(thisChamp) + '/');
except OSError as exception:
	if exception.errno != errno.EEXIST:
		raise

fWriteStats = open('./pickDropStats/' + str(thisChamp) + '.json','w');
json.dump(saveTimeStamps,fWriteStats);
fWriteStats.close();