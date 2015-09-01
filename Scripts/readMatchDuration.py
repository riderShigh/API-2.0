import sys
import urllib, json, os
from download import *
from classes import *
import time
import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('pa1087','5lnuuhu8xi');

fMatchIds = open('./vladMatches.json');
matchIds = json.loads(fMatchIds.read());
xi = [];
yi = [];

for i in xrange(0,len(matchIds)):
	fMatch = open('./5.14/RANKED_SOLO/NA/' + str(matchIds[i]) +'.json');
	match = json.loads(fMatch.read());
	#print 'Match Duration = ' + str(match['matchDuration']/60.0);
	xi.append(match['matchDuration']/60.0);
	for j in xrange(0,10):
		if match['participants'][j]['championId'] == 8:
			#print 'GPM = ' + str(match['participants'][j]['stats']['goldEarned'] * 60.0 / float(match['matchDuration']));
			#yi.append(match['participants'][j]['stats']['goldEarned'] * 60.0 / float(match['matchDuration']));
			yi.append(match['participants'][j]['stats']['totalDamageDealt'] * 60.0 / float(match['matchDuration']));

trace0 = Scatter(x=xi,y=yi,mode='markers');
traceData = Data([trace0]);

plot_url = py.plot(traceData);