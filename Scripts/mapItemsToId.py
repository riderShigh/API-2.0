import sys
import urllib, json, os, numpy, math
from classes import *

region = ['br','eune','euw','kr','lan','las','na','oce','ru','tr'];

regionMap = {};
mapItemIds = {};
patchItems = {};
fItemIds = open('itemNameIds.json','w');

for reg in region:
	print 'current region = ' + reg;
	url = 'https://global.api.pvp.net/api/lol/static-data/' + reg + '/v1.2/versions?api_key=ac3b3bf8-1aa6-4570-8a84-8163ba9e0a89';
	urlData = urllib.urlopen(url);
	versions = json.loads(urlData.read());

	i = 0;
	season = '5';
	skipOldVersion = 0;

	while season == '5':
		if skipOldVersion > 0:
			i += 1;
			skipOldVersion -= 1;
			continue;

		url1 = 'http://ddragon.leagueoflegends.com/cdn/' + versions[i] + '/data/en_US/item.json';
		fItems = urllib.urlopen(url1);
		items = json.loads(fItems.read());
		for key in items['data']:
		#print url
			if key==3716 or key==3720 or key==3724: continue;
			if key==3718 or key==3722 or key==3726: continue;
			if key==3931 or key==3932 or key==3733: continue;
			if key==3717 or key==3721 or key==3725: continue;
			if key==3714 or key==3719 or key==3723: continue;
			mapItemIds[items['data'][key]['name']] = key;
		versionStr = versions[i];
		versionStr = versionStr[:-2];
		patchItems[versionStr] = mapItemIds;
		skipOldVersion = int(versions[i][-1]) - 1;
		print versions[i];
		i += 1;
		season = versions[i][0];
	regionMap[reg] = patchItems;


json.dump(regionMap,fItemIds);
fItemIds.close();