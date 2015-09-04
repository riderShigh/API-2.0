/* ************************************************
	readMatches.js
	Script for identifying players of a champion
	
	0. Run dl2na.py before this
	1. Read from downloaded matches
	2. Search through participants for champion
	   usage
	3. Identify if the participant is plat+
	4. Save match Ids and summoner Ids that
	   used a champion to file
************************************************ */
var fs = require('fs');

// Define regions, patches, tiers, AP champion Ids, and output objects
var region = ['BR','EUNE','EUW','KR','LAN','LAS','NA','OCE','RU','TR']; //region = ['KR'];
var patch = ['5.11','5.14'];
var highTier = ['CHALLENGER','MASTER','DIAMOND','PLATINUM'];
var mageList = JSON.parse(fs.readFileSync('mages.json'));
var outputMatches = {};
var outputMains = {};
var outputGoodMains = {};
var outputGoodMainMatches = {};

// Initialize output objects
for(var pat=0; pat<patch.length; pat++){
	outputMatches[patch[pat]] = {};
	outputMains[patch[pat]] = {};
	outputGoodMainMatches[patch[pat]] = {};
	outputGoodMains[patch[pat]] = {};
}

// Loop through patches
for(var pat=0; pat<patch.length; pat++){
	//outputMatches[patch[pat]] = {};
	//outputMains[patch[pat]] = {};
	//outputGoodMainMatches[patch[pat]] = {};
	//outputGoodMains[patch[pat]] = {};

	// Loop through regions
	for(var reg=0; reg<region.length; reg++){

		// Define temporary objects and lists to save Ids
		var champMatches = {};
		var champMains = {};
		var champCounts = {};
		var champGoodMains = {};
		var champGoodMainMatches = {};

		for(var key in mageList){
			if(mageList.hasOwnProperty(key)){
				//console.log(mageList[key]);
				champMatches[key] = [];
				champMains[key] = [];
				champCounts[key] = 0;
				champGoodMains[key] = [];
				champGoodMainMatches[key] = [];
			}
		}

		// Open match file
		var matchId = JSON.parse(fs.readFileSync('./AP_ITEM_DATASET/' + patch[pat] + '/RANKED_SOLO/' + region[reg] + '.json'));
		console.log('./AP_ITEM_DATASET/' + patch[pat] + '/RANKED_SOLO/' + region[reg] + '.json');
		var data = '';
		var fileSize = 0, filePath = '';
		var line = '';
		var champCount = 0;

		// Loop through match Ids in match file
		for(var i=0;i<10000;i++){
			filePath = './' + patch[pat] + '/RANKED_SOLO/' + region[reg] + '/' + matchId[i] + '.json';

			// Read json data from a match
			try{
				data = JSON.parse(fs.readFileSync(filePath,'utf8'));
			}catch(err){
				continue;
			}
			
			// Check champion usage by champion Id for both plat+ players and everyone
			for(var j=0; j<10; j++){
				if(mageList.hasOwnProperty(data.participants[j].championId)){
					champMatches[(data.participants[j].championId).toString()].push(matchId[i]);
					champMains[(data.participants[j].championId).toString()].push(data.participantIdentities[data.participants[j].participantId-1].player.summonerId);
					champCount[(data.participants[j].championId).toString()]++;
					if(highTier.indexOf(data.participants[j].highestAchievedSeasonTier) >= 0){
						champGoodMainMatches[(data.participants[j].championId).toString()].push(matchId[i]);
						champGoodMains[(data.participants[j].championId).toString()].push(data.participantIdentities[data.participants[j].participantId-1].player.summonerId);					
					}
				}
			}
			if(i%1000==0){
				console.log('Progress = ' + (((pat*region.length+reg)*10000+i)/(region.length*patch.length*10000)*100).toString() + '%');
			}
			
		}

		// Save objects to file
		outputMatches[patch[pat]][region[reg]] = champMatches;
		outputMains[patch[pat]][region[reg]] = champMains;
		outputGoodMainMatches[patch[pat]][region[reg]] = champGoodMainMatches;
		outputGoodMains[patch[pat]][region[reg]] = champGoodMains;

	}
}


fs.writeFile('./champMatches.json',
	JSON.stringify(outputMatches),
	function(err){if(err) throw err;});

fs.writeFile('./champMains.json',
	JSON.stringify(outputMains),
	function(err){if(err) throw err;});

fs.writeFile('./champGoodMainMatches.json',
	JSON.stringify(outputGoodMainMatches),
	function(err){if(err) throw err;});

fs.writeFile('./champGoodMains.json',
	JSON.stringify(outputGoodMains),
	function(err){if(err) throw err;});

console.log('------------------');
console.log("Completed!");
console.log('------------------');