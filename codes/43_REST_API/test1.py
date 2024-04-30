import requests
import json


def getTotalGoals(competition, year):
    goals_1 = {}
    goals_2 = {}
    sum = 0
    home_competition = requests.get(
        'https://jsonmock.hackerrank.com/api/football_matches?competition=%s&year=%s' %
        (competition, year))
    visiting_team = requests.get(
        'https://jsonmock.hackerrank.com/api/football_matches?competition=%s&year=%s' %
        (competition, year))
    result_1 = home_competition.content
    result_2 = visiting_team.content
    home = result_1.decode('utf-8')
    visit = result_2.decode('utf-8')
    home = json.loads(home)
    visit = json.loads(visit)

    sum1 = 0
    for rec in home['data']:
        for k, v in rec.items():
            if 'competition' not in rec:
                break
            if k == 'competition':
                if rec['competition'] == competition:
                    if rec['team1goals'] > rec['team2goals']:
                        sum1 += int(rec['team1goals'])
                    else:
                        sum1 += int(rec['team2goals'])
                    goals_1[k] = sum1

    sum += goals_1['competition']

    sum2 = 0
    for rec in visit['data']:
        for k, v in rec.items():
            if 'competition' not in rec:
                break
            if k == 'competition':
                if rec['competition'] == competition:
                    if rec['team1goals'] > rec['team2goals']:
                        sum2 += int(rec['team1goals'])
                    else:
                        sum2 += int(rec['team2goals'])
                    goals_2[k] = sum2
    sum += goals_2['competition']

    return sum


print(getTotalGoals('UEFA Champions League', 2011))
