# this tool will help you login or something like that.
import urllib3
import logging
import requests
import functools as fp
from collections import namedtuple

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

SessionSettings = namedtuple("SettingsFile", ['url', 'username', 'password'])

OpenSession = namedtuple("OpenSession", ['url', 'request_session'])

def post(session: OpenSession, path:str, data):
    return session.request_session.post(session.url + path, data, verify = False)

def get(session: OpenSession, path:str):
    return session.request_session.post(session.url + path, verify = False)

def new_session(settings: SessionSettings) -> OpenSession:
    """Create a new session for the FBCTF site
       arguments
    """
    session = requests.Session()

    data = {
        'action': 'login_team',
        'team_name': settings.username,
        'password': settings.password
    }
    print(settings.url)

    res = session.post(settings.url + "/index.php?p=index&ajax=true", data = data, verify = False)

    if res.status_code is not 200:
        raise ValueError('Response from the api was not success: %s' % res.content )

    response = res.json()

    if(response['result'] != 'OK'):
        raise ValueError('Response did not contain a successfull result: %s' % res.content )

    return OpenSession(
        url = settings.url,
        request_session = session
    )

def load_settings_from_file(file_path: str) -> SessionSettings:
    with open(file_path) as file:
        url  = file.readline().rstrip()
        username = file.readline().rstrip()
        password = file.readline().rstrip()

        return SessionSettings(
            url= url,
            username= username, 
            password= password
        )


def main(auth_file: str = "/Users/nick.gridinskiy/mule-pass.txt"):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    logging.basicConfig()
    # Set log level for the urllib
    # logging.getLogger().setLevel(logging.DEBUG)
    # requests_log = logging.getLogger("requests")
    # requests_log.setLevel(logging.DEBUG)
    # requests_log.propagate = True

    def getActivity(session):
        r = get(session, path = "/data/announcements.php?ajax=true")
        print(r.content)
    
    getActivity(new_session(load_settings_from_file(auth_file)))
    

if __name__ == "__main__":
    main()