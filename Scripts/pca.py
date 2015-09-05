# ************************************************
# 	pca.py
#	Recompile stats, principle component analysis,
#	and export good players list
#	
#	Usage: python pca.py [champion] [patch]
#	
#	1. Isolate a champion and the patch where
#		a set of match Ids is taken from
#	2. Re-arrange isolated match Ids 
#	3. Extract relevant statistics
#		e.g. KDA, games played, play rate, etc.
#	4. Principle component analysis
#	5. Plot pca results
#	6. Save high-performance summoners' Ids to file
# ************************************************

import sys
import urllib, json, os, numpy, math
from numpy import linalg, ndarray
import plotly.plotly as py
from plotly.graph_objs import *
from classes import *
from processing import *
py.sign_in('pa1087','5lnuuhu8xi');

# Define champion and patch to be read
thisChamp = sys.argv[1];
thisPatch = sys.argv[2];

# Extract statistics
statsFileName = 'champGoodMainsStats_' + str(thisPatch) + '_' + str(thisChamp) + '.json';
extractChampStats('champGoodMains.json',statsFileName,thisPatch,thisChamp);

# Initialize STA vectors and tallies
fStats = open(statsFileName,'r');
data = json.loads(fStats.read());
vecRawStats = [];
vecDim = 6;
vecMean = [0 for col in range(vecDim)];
vecVar = [0 for col in range(vecDim)];
scatMatrix = [[0 for col in range(vecDim)] for row in range(vecDim)];
tempVec = [0 for col in range(vecDim)];

# Initialize increment indices and conditions
goodPlayers = [];
highestKDA = 0;
highestKDAIndex = 0;
lowestKDA = 10;
lowestKDAIndex = 0;
mostPlayed = 0;
mostPlayedIndex = 0;
regionKeys = [];

# Compile statistics to temp memory
for i in xrange(0,len(data)):

	# Stats set 1
	vecRawStats.append([
		data[str(i)]['totalSessionsPlayed'],
		data[str(i)]['totalSessionsWon']/float(data[str(i)]['totalSessionsPlayed']),
		data[str(i)]['championPlayRate'],
		data[str(i)]['totalChampionKills'],
		data[str(i)]['totalAssists'],
		data[str(i)]['totalKDA']
		]);
	regionKeys.append(data[str(i)]['region']);

	# Stats set 2
	#vecRawStats.append([
	#	data[str(i)]['GPM'],
	#	data[str(i)]['DPS'],
	#	data[str(i)]['KDA'],
	#	data[str(i)]['percentDamage']
		#wl,
	#	]);

# Build mean vector
for k in xrange(0,vecDim):
	for i in xrange(0,len(vecRawStats)):
		if vecRawStats[i][vecDim-1] > highestKDA: 
			highestKDA = vecRawStats[i][vecDim-1];
			highestKDAIndex = i;
		if vecRawStats[i][vecDim-1] < lowestKDA: 
			lowestKDA = vecRawStats[i][vecDim-1];
			lowestKDAIndex = i;
		if vecRawStats[i][0] > mostPlayed: 
			mostPlayed = vecRawStats[i][0];
			mostPlayedIndex = i;
		vecMean[k] += vecRawStats[i][k];
	vecMean[k] /= float(len(vecRawStats));

# Center raw data round mean
for i in xrange(0,len(vecRawStats)):
	for j in xrange(0,vecDim):
		vecRawStats[i][j] = vecRawStats[i][j] - vecMean[j];
		#tempVec[j] = vecRawStats[i][j]/vecMean[j] - 1;

# Build variance vector
for k in xrange(0,vecDim):
	for i in xrange(0,len(vecRawStats)):
		vecVar[k] += vecRawStats[i][k]*vecRawStats[i][k];
	vecVar[k] /= float(len(vecRawStats));
	vecVar[k] = math.sqrt(vecVar[k]);

# Normalize statistics spreads
for i in xrange(0,len(vecRawStats)):
	for j in xrange(0,vecDim):
		vecRawStats[i][j] = vecRawStats[i][j]/vecVar[j];

# Compute scattering matrix
for i in xrange(0,len(vecRawStats)):
	for j in xrange(0,vecDim):
		for k in xrange(0,vecDim):
			scatMatrix[j][k] += vecRawStats[i][j] * vecRawStats[i][j];

# Compute eigenvectors and eigenvalues for scattering matrix
w,v = linalg.eigh(scatMatrix);
wArgSorted = ndarray.argsort(w);

# Build transfer matrix
transMatrix = [v[:,wArgSorted[vecDim-1]],v[:,wArgSorted[vecDim-2]]]
print transMatrix

# Prepare lists for storing processed data
analyzedData = [[0 for col in range(2)] for row in range(len(vecRawStats))]
xi = [];
yi = [];
xj = [];
yj = [];
xk = [];
yk = [];
xa = [];
ya = [];

# Reduce data vector dimensions to 2
for i in xrange(0,len(vecRawStats)):
	for j in xrange(0,2):
		for k in xrange(0,vecDim):
			analyzedData[i][j] += transMatrix[j][k] * vecRawStats[i][k];
	xi.append(analyzedData[i][0]);
	yi.append(analyzedData[i][1]);
	if i == highestKDAIndex:
		xj.append(analyzedData[i][0]);
		yj.append(analyzedData[i][1]);
	if i == lowestKDAIndex:
		xk.append(analyzedData[i][0]);
		yk.append(analyzedData[i][1]);
	if i == mostPlayedIndex:
		xa.append(analyzedData[i][0]);
		ya.append(analyzedData[i][1]);

# Plot dimensionally-reduced data
analyzedData = tuple(analyzedData);
trace0 = Scatter(x=xi,y=yi,mode='markers',name='Data');
trace1 = Scatter(x=xj,y=yj,mode='markers',name='Highest KDA');
trace2 = Scatter(x=xk,y=yk,mode='markers',name='Lowest KDA');
trace3 = Scatter(x=xa,y=ya,mode='markers',name='Most Number of Plays');
traceData = Data([trace0,trace1,trace2,trace3]);
layout = Layout(
	title='Champion ' + str(thisChamp) + '   Patch ' + str(thisPatch),
	xaxis = XAxis(title='PC1'),
	yaxis = YAxis(title='PC2')
	);
fig = Figure(data=traceData,layout=layout);
plot_url = py.plot(fig);

# Save list of good players to file
fGoodMainsId = open(statsFileName);
goodMainsId = json.loads(fGoodMainsId.read());
pcaSide = 1;
for i in xrange(0,len(vecRawStats)):
	if analyzedData[i][0] * pcaSide > 0:
		goodPlayer = {};
		goodPlayer['id'] = goodMainsId[str(i)]['summonerId'];
		goodPlayer['region'] = goodMainsId[str(i)]['region'];
		goodPlayers.append(goodPlayer);
fGoodPlayers = open('./champGoodHighStats/champGoodHighMainStats_' + thisPatch + '_' + thisChamp + '.json','w');
json.dump(goodPlayers,fGoodPlayers);
fGoodPlayers.close();
print len(goodPlayers);