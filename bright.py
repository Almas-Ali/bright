'''
A Brightness control utility for Linux systems.

Easy to use it
'''

from os import system as cmd
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--set', help='Set brightness level (1-100)')

args = parser.parse_args()

if args.set:
    bright = int(args.set)/100
    cmd(f'xrandr --output LVDS-1 --brightness {bright}')
else:
    parser.print_help()

# xrandr --verbose | awk '/Brightness/ { print $2; exit }'
