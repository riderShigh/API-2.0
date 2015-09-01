class stats:
	summonerId = 0;
	region = '';
	totalSessionsPlayedPlayed = 0;
	totalSessionsWon = 0;
	winRate = 0;
	totalDeaths = 0;
	totalChampionKills = 0;
	totalAssists = 0;
	totalKDA = 0;
	championPlayRate = 0;

	def __init__(self,summId,played,won,kills,deaths,assists,region=''):
		self.summonerId = summId;
		self.totalSessionsPlayed = played;
		self.totalSessionsWon = won;
		self.winRate = won/float(played);
		self.totalChampionKills = kills;
		self.totalDeaths = deaths;
		self.totalAssists = assists;
		if deaths == 0:
			self.totalKDA = (kills+assists)/0.5;
		else:
			self.totalKDA = (kills+assists)/float(deaths);
		self.region = region;

class summonerMatchList:
	summonerId = 0;
	matchIds = [];

class stats2:
	#summonerId = 0;
	teamId = 0;
	DPS = 0;
	GPM = 0;
	win = True;
	KDA = 0;
	percentDamage = 0;
	#gamesPlayed = 0;

	def __init__(self,tid,dps,gpm,wr,kda,pd):
		self.teamId = tid;
		self.DPS = dps;
		self.GPM = gpm;
		self.win = wr;
		self.KDA = kda;
		self.percentDamage = pd;
		#self.gamesPlayed = gp;
