import requests
import json


def sample_response(ip_address):
    response = requests.get(
        'https://jsonmock.hackerrank.com/api/ip?ip=%s' %
        (ip_address))
    response = response.content
    response = response.decode('utf-8')
    response = json.loads(response)
    if 'data' in response and len(response['data']) >= 1:
        data = {'ip': response['data'][0]['ip'],
                'country': response['data'][0]['country']}
        return data
    return []


print(sample_response('172.217.20.46'))
