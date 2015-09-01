import sys
import urllib, json, os, numpy, math
from numpy import linalg, ndarray
import plotly.plotly as py
import operator
from plotly.graph_objs import *
from classes import *
from processing import *
py.sign_in('pa1087','5lnuuhu8xi');

fBigItems = open('./bigItems.json');
#readBigItems = '"""'+fBigItems.read()+'"""';
#print readBigItems
bigItems = json.loads(fBigItems.read());

fItems = open('./itemNameIds.json');
items = json.loads(fItems.read());

itemStore = {};

fBigItemIds = open('./bigItemNameIds.json','w');

for region in items:
	thisRegion = items[region];
	itemStore[region] = {};
	for patch in thisRegion:
		#if region=='na' and str(patch)=='5.11': print patch;
		itemStore[region][str(patch)] = {};
		thisPatch = thisRegion[str(patch)];
		for item in thisPatch:
			#print item;
			if item in bigItems: 
				if float(patch) > 5.125 and item == 'Enchantment: Magus': continue;
				if float(patch) < 5.125 and item == 'Enchantment: Runeglaive': continue;
				itemStore[region][str(patch)][thisPatch[str(item)]] = item;
				#if region=='na' and str(patch)=='5.14' and thisPatch[str(item)]=='3708': 
				#	print item;


json.dump(itemStore,fBigItemIds);
fBigItems.close();
fItems.close();
fBigItemIds.close()