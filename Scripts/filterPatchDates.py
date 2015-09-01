import sys
import urllib, json, os, math
import operator
import errno
from classes import *
from processing import *
from download import *

thisChamp = str(sys.argv[1]);
#thisChamp = str(3);
patch510epoch = 1432810800000;
patch513epoch = 1436438400000;
patch516epoch = 1440068400000;

fTimeStamps = open('./pickDropStats/' + str(thisChamp) + '.json');
timeStamps = json.loads(fTimeStamps.read());

playCounts = {};
summonerCount = 0;
x = [];
y = [];

for region,thisRegion in timeStamps.iteritems():
	for patch,thisPatch in thisRegion.iteritems():
		for summoners in thisPatch:
		#for summoner,thisSummoner in thisPatch.iteritems():
			playCounts[summonerCount] = [0,0];
			for thisSummoner,matchTimeList in summoners.iteritems():
				for matchTime in matchTimeList:
					if matchTime > patch510epoch and matchTime < patch513epoch:
						playCounts[summonerCount][0] += 1;
					if matchTime > patch513epoch and matchTime < patch516epoch:
						playCounts[summonerCount][1] += 1;
			summonerCount += 1;
			#x.append(playCounts[str(summonerCount-1)][0]);
			#y.append(playCounts[str(summonerCount-1)][1]);

try:
	os.makedirs('./pickDropStats/filtered/');
except OSError as exception:
	if exception.errno != errno.EEXIST:
		raise

#analyzedData = tuple(analyzedData);
#trace0 = Scatter(x=x,y=y,mode='markers',name='Data');
#traceData = Data([trace0]);

#layout = Layout(
#	title= '',
#	xaxis = XAxis(title='pre patch'),
#	yaxis = YAxis(title='post patch')
#	);
#fig = Figure(data=traceData,layout=layout);

#plot_url = py.plot(fig);

fWriteFiltered = open('./pickDropStats/filtered/' + str(thisChamp) + '.json','w');
json.dump(playCounts,fWriteFiltered);
fWriteFiltered.close();