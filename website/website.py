from types import resolve_bases
import requests

def monthly_schedule(name, month):
    response = requests.get(f'http://company.com/{name}/{month}')
    if response.ok:
        return response.text
    else:
        return 'Bad Response!'
        