import requests
import functools as fp
from collections import namedtuple
from xml.etree import ElementTree
from . import ctf_session
import re

Announcement = namedtuple('Announcement', ['when', 'announcement'])
Activity = namedtuple('Activity', ['when', 'who', 'what', 'where'])

def parse_announcements(xml: str) :
    tree = ElementTree.fromstring(xml)
    res = tree.findall('./div/div/div/ul/li')

    out = [Announcement(when = x.text, announcement = x[0].text) for x in res]

    return out

def get_announcements(session: ctf_session.OpenSession, parse = parse_announcements):
    response = ctf_session.get(session, "/inc/gameboard/modules/announcements.php?ajax=true")
    if response.status_code != 200:
        raise ValueError("Announcements did not return a success %s" % response.content)
    return parse(response.content)

def parse_activities(xml: str) :
    # tree = ElementTree.fromstring(xml)
    # res = tree.findall('./div/div/div/ul/li')
    # map(lambda node: )
    reg = re.compile('<li class="opponent-team">(.*?)<span class="opponent-name">(.*?)</span>\xa0(.*?)\xa0 (.*?)</li>')
    result = reg.findall(xml.decode("utf-8"))

    return [Activity(when = x[0], who =x[1], what= x[2], where= x[3]) for x in result]

def get_activities(session: ctf_session.OpenSession, parse = parse_activities):
    response = ctf_session.get(session, "/inc/gameboard/modules/activity.php?ajax=true")

    if response.status_code != 200:
        raise ValueError("Activities did not return a success %s" % response.content)

    return parse(response.content)

def main(auth_file: str = "/Users/nick.gridinskiy/mule-pass.txt"):
    # result = get_announcements(ctf_session.new_session(ctf_session.load_settings_from_file(auth_file)))
    result = get_activities(ctf_session.new_session(ctf_session.load_settings_from_file(auth_file)))

    for a in result:
        print(a)
        
if __name__ == "__main__":
    main()