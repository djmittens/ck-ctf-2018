#!/usr/bin/env python3
from fbctf_cli import ctf_session
from fbctf_cli import ctf_activity
from termcolor import colored
import argparse
import sys
import os

def main():
  parser = argparse.ArgumentParser()
#   parser.add_argument('-d', '--dirname', default="files", help="Output directory, to place the files in")
  parser.add_argument('-s', "--settings", default= os.environ.get('CTF_SETTINGS', None), help="file to load settings from")
  args = parser.parse_args()
  settings = ctf_session.load_settings_from_file(args.settings)

  session = ctf_session.new_session(settings)
  result = ctf_activity.get_announcements(session)
  for i in result:
    print(colored(i.when, color='blue'), colored(i.announcement, 'yellow'))

if __name__ == "__main__":
    main()