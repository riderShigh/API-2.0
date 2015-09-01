import sys
import urllib, json

def dlURLData_match(region,matchId,includeTL):
	url = 'https://' + region + '.api.pvp.net/api/lol/' + region + '/v2.2/match/' + matchId + '?';
	if includeTL == 1:
		url += 'includeTimeline=true&';
	url += 'api_key=ac3b3bf8-1aa6-4570-8a84-8163ba9e0a89'
	response = urllib.urlopen(url);
	#print(url);
	data = response.read();
	return data;

def dlURLData_matchList(region,summonerId,championIds=0,rankedQueues='',beginIndex=-1,endIndex=-1):
	url = 'https://' + region + '.api.pvp.net/api/lol/' + region + '/v2.2/matchlist/by-summoner/' + summonerId + '?';
	if championIds != 0:
		url += 'championIds=' + str(championIds) + '&';
	if rankedQueues != '':
		url += 'rankedQueues=' + rankedQueues + '&';
	if beginIndex != -1 and endIndex != -1:
		url += 'beginIndex=' + str(beginIndex) + '&endIndex=' + str(endIndex) + '&';
	url += 'api_key=ac3b3bf8-1aa6-4570-8a84-8163ba9e0a89';
	response = urllib.urlopen(url);
	data = response.read();
	return data;

def dlURLData_stats(region,summonerId,isRankedSummary):
	url = 'https://' + region + '.api.pvp.net/api/lol/' + region + '/v1.3/stats/by-summoner/' + summonerId + '/' + isRankedSummary;
	url += '?api_key=ac3b3bf8-1aa6-4570-8a84-8163ba9e0a89';
	response = urllib.urlopen(url);
	data = response.read();
	return data;

def buildPathName(patch,queueType,region):
	return './AP_ITEM_DATASET/' + patch + '/' + queueType + '/' + region + '.json';
	#return 'I:/Others/' + patch + '/' + queueType + '/' + region + '.json';

def buildFolderName(patch,queueType,region):
	#return './AP_ITEM_DATASET/' + patch + '/' + queueType + '/' + region + '/';
	return './' + patch + '/' + queueType + '/' + region + '/';

def checkPatch(matchVersion):
	end = matchVersion.index('.',matchVersion.index('.') + 1);
	return matchVersion[:end];