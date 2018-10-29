
#!/usr/bin/env python3
from fbctf_cli import ctf_session
from fbctf_cli import ctf_gameboard
from termcolor import colored
import argparse
import sys
import os

def main():
  parser = argparse.ArgumentParser()
#   parser.add_argument('-d', '--dirname', default="files", help="Output directory, to place the files in")
  parser.add_argument('-s', "--settings", default= os.environ.get('CTF_SETTINGS', None), help="file to load settings from")
  parser.add_argument('-pp', "--prettyprint", action="store_true", help = "Pretty print only the challenge information")
  parser.add_argument('-c', "--color", action="store_true", help="Use color escape codes for pretty printing.")
  args = parser.parse_args()
  settings = ctf_session.load_settings_from_file(args.settings)

  session = ctf_session.new_session(settings)
#   result = ctf_activity.get_announcements(session)
  gameboard = ctf_gameboard.get_all_countries(session)

  color = lambda x, c: colored(x, c) if args.color else x
  green = lambda x: color(x, 'green')
  magenta = lambda x: color(x, 'magenta')
  blue = lambda x: color(x, 'blue')
  yellow = lambda x: color(x, 'yellow')

  if args.prettyprint:
      for i in gameboard:
          print(magenta('Country(%s): ' % i.points), blue(i.name))
          print(blue('----------'))
          print(magenta('Description: '), yellow(i.intro))
          print(blue('----------'))
          print(magenta('Hint: '), i.hint)
          print(blue('----------'))
          print(magenta('Attachments: '), i.attachments)
          print(green('~!|----------|!~'))
  else:
    for i in gameboard:
        # print(colored(i, color='blue'), colored(i.announcement, 'yellow'))

        print(i)

if __name__ == "__main__":
    main()

