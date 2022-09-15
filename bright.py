# usr/bin/env python3
# -*- coding: utf-8 -*-

'''
A Brightness control utility for Linux systems.

Easy to use it
'''

from os import system as cmd
import subprocess
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--set', help='Set brightness level (1-100+)', type=int)
parser.add_argument(
    '--get', help='Get brightness level (1-100+)', action='store_true')

args = parser.parse_args()

if args.set:
    bright = int(args.set)/100
    cmd(f'xrandr --output LVDS-1 --brightness {bright}')
elif args.get:
    # br = subprocess.Popen(
    #     "xrandr", "--verbose | awk '/Brightness/ { print $2; exit }'")
    # print("brightness: ", br.stdout.read())

    process = subprocess.Popen(["xrandr", "--verbose", "|", "awk", "'/Brightness/ { print $2; exit }'"],
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    print(stdout)
    print(stderr)
else:
    parser.print_help()

# xrandr --verbose | awk '/Brightness/ { print $2; exit }'
