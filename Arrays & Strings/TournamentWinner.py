HOME_TEAM_WON = 1
def updateScore(team, points, scores):
	if team not in scores:
		scores[team] = 0
		
	scores[team] += points
		
def tournamentWinner(competitions, results):
    # Write your code here.
	
	currentBestTeam = ""
	scores = {currentBestTeam: 0}
	
	for idx, competition in enumerate(competitions):
		result = results[idx]
		homeTeam,awayTeam = competition
		
		winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam
	    
		updateScore(winningTeam, 3, scores)
		
	    if scores[winningTeam] > scores[currentBestTeam]:
			currentBestTeam = winningTeam
	
	
	
    return currentBestTeam



