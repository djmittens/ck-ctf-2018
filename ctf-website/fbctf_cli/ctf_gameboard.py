import requests
import functools as fp
from collections import namedtuple
from xml.etree import ElementTree
from . import ctf_session
import re

Country = namedtuple('Country', ['name', 'level_id', 'type',
    'points', 'title', 'intro', 
    'hint', 'hint_cost', 'attachments', 'links', 
    'bonus', 'owner', 'completed'])

def parse_countries(json):
    result = []
    for name, body in json.items():
        result.append( Country(
            name = name, 
            level_id = body['level_id'],
            points = body['points'],
            bonus = body['bonus'],
            type = body['type'],
            title = body['title'],
            intro = body['intro'],
            hint = body['hint'],
            hint_cost = body['hint_cost'],
            attachments = body['attachments'],
            links = body['links'],
            owner = body['owner'],
            completed = body['completed']
         ))
    return result

def get_all_countries(session: ctf_session.OpenSession, parse= parse_countries):
    res = ctf_session.get(session, '/data/country-data.php')
    if res.status_code != 200:
        raise ValueError("The api did not respond successfully: %s" % res.content)
    
    return parse(res.json())

def main():
    """ some test code for this file """

if __name__ == "__main__":
    main()