import requests
import json


def getTotalGoals(team, year):
    goals_1 = {}
    goals_2 = {}
    sum = 0
    for i in range(1, 1000):
        home_team = requests.get(
            'https://jsonmock.hackerrank.com/api/football_matches?year=%s&team1=%s&page=%s' %
            (year, team, i))
        visiting_team = requests.get(
            'https://jsonmock.hackerrank.com/api/football_matches?year=%s&team2=%s&page=%s' %
            (year, team, i))
        result_1 = home_team.content
        result_2 = visiting_team.content
        home = result_1.decode('utf-8')
        visit = result_2.decode('utf-8')
        home = json.loads(home)
        visit = json.loads(visit)
        if len(home['data']) == 0 and len(visit['data']) == 0:
            break

        sum1 = 0
        for rec in home['data']:
            for k, v in rec.items():
                if 'team1' not in rec:
                    break
                if k == 'team1':
                    if rec['team1'] == team:
                        sum1 += int(rec['team1goals'])
                        goals_1[k] = sum1

        sum += goals_1['team1']

        sum2 = 0
        for rec in visit['data']:
            for k, v in rec.items():
                if 'team2' not in rec:
                    break
                if k == 'team2':
                    if rec['team2'] == team:
                        sum2 += int(rec['team2goals'])
                        goals_2[k] = sum2
        sum += goals_2['team2']

    return sum


getTotalGoals('Chelsea', 2014)
