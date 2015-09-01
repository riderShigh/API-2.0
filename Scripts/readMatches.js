var fs = require('fs');

//var matchId = JSON.parse(fs.readFileSync('./one_datum/NA.json'));
var region = ['BR','EUNE','EUW','KR','LAN','LAS','NA','OCE','RU','TR'];
//region = ['KR'];
var patch = ['5.11','5.14'];
var highTier = ['CHALLENGER','MASTER','DIAMOND','PLATINUM'];
//var region = ['EUW','NA'];
//var patch = ['5.11','5.14'];
var mageList = JSON.parse(fs.readFileSync('mages.json'));
var outputMatches = {};
var outputMains = {};

var outputGoodMains = {};
var outputGoodMainMatches = {};

for(var pat=0; pat<patch.length; pat++){
	outputMatches[patch[pat]] = {};
	outputMains[patch[pat]] = {};
	outputGoodMainMatches[patch[pat]] = {};
	outputGoodMains[patch[pat]] = {};
}


for(var pat=0; pat<patch.length; pat++){
	//outputMatches[patch[pat]] = {};
	//outputMains[patch[pat]] = {};
	//outputGoodMainMatches[patch[pat]] = {};
	//outputGoodMains[patch[pat]] = {};
	for(var reg=0; reg<region.length; reg++){

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

		var matchId = JSON.parse(fs.readFileSync('./AP_ITEM_DATASET/' + patch[pat] + '/RANKED_SOLO/' + region[reg] + '.json'));
		console.log('./AP_ITEM_DATASET/' + patch[pat] + '/RANKED_SOLO/' + region[reg] + '.json');
		var data = '';
		var fileSize = 0, filePath = '';
		var line = '';
		var champCount = 0;

		for(var i=0;i<10000;i++){
			filePath = './' + patch[pat] + '/RANKED_SOLO/' + region[reg] + '/' + matchId[i] + '.json';
			//var stats = fs.statSync(filePath);
			//fileSize = stats['size'];
			//if(fileSize < 12000){continue;}
			try{ //ascii
				data = JSON.parse(fs.readFileSync(filePath,'utf8'));
			}catch(err){
				continue;
			}
			
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

		//console.log(JSON.stringify(ahriMatches));

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