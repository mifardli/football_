#Load in Statsbomb competition and match data
#This is a library for loading json files.
import json
#Load the competition file
#Got this by searching 'how do I open json in Python'
with open('Statsbomb/data/competitions.json') as f:
    competitions = json.load(f)

#FIFA World Cup 2018 has competition ID 43
competition_id=43
#La Liga 2021/2022 has competition ID 11
competition_id=11
#Load the list of matches for this competition
with open('Statsbomb/data/matches/'+str(competition_id)+'/90.json', encoding="utf8") as f:
    matches = json.load(f)

#Look inside matches
matches[0]
matches[0]['home_team']
matches[0]['home_team']['home_team_name']
matches[0]['away_team']['away_team_name']

#Print all match results
for match in matches:
    home_team_name=match['home_team']['home_team_name']
    away_team_name=match['away_team']['away_team_name']
    home_score=match['home_score']
    away_score=match['away_score']
    describe_text = 'The match between ' + home_team_name + ' and ' + away_team_name
    result_text = ' finished ' + str(home_score) +  ' : ' + str(away_score)
    print(describe_text + result_text)

#Now lets find a match we are interested in
home_team_required ="Real Madrid"
away_team_required ="Barcelona"

#Find ID for the match
for match in matches:
    home_team_name=match['home_team']['home_team_name']
    away_team_name=match['away_team']['away_team_name']
    if (home_team_name==home_team_required) and (away_team_name==away_team_required):
        match_id_required = match['match_id']
print(home_team_required + ' vs ' + away_team_required + ' has id:' + str(match_id_required))

#codes for only particular team
for match in matches:
    home_team_name = match['home_team']['home_team_name']
    away_team_name = match['away_team']['away_team_name']
    if home_team_name == 'Real Madrid' or away_team_name == 'Real Madrid':
        home_score = match['home_score']
        away_score = match['away_score']
        describe_text = 'The match between ' + home_team_name + ' and ' + away_team_name
        result_text = ' finished ' + str(home_score) + ' : ' + str(away_score)
        print(describe_text + result_text)

#Exercise: 
#1, Edit the code above to print out the result list for the Mens World cup 
#2, Edit the code above to find the ID for England vs. Sweden
#3, Write new code to write out a list of just Sweden's results in the tournament.

