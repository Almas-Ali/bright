# usr/bin/env python3
# -*- coding: utf-8 -*-

'''
A Brightness control utility for Linux systems.

Easy to use it
'''

from os import system as cmd
import subprocess
import argparse

def version():
    print("Version: 1.1")

def author():
    print("Author: MD. ALMAS ALI")

def set_brightness(persent: int) -> None:
    SET_BRIGHTNESS = int(persent)/100
    cmd(f'xrandr --output LVDS-1 --brightness {SET_BRIGHTNESS}')

def get_brightness() -> None:
    GET_BRIGHTNESS = "xrandr --verbose | awk '/Brightness/ { print $2; exit }'"

    process = subprocess.Popen([GET_BRIGHTNESS], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    CURRENT_BRIGHTNESS = int(float(str(stdout, 'utf-8')) * 100)
    print(CURRENT_BRIGHTNESS)


parser = argparse.ArgumentParser()

parser.add_argument('--set', help='Set brightness level (1-100+)', type=int, metavar='PERSENT')
parser.add_argument(
    '--get', help='Get brightness level (1-100+)', action='store_true')
parser.add_argument(
    '--version', help='Get version information', action='store_true')
parser.add_argument(
    '--author', help='Get author information', action='store_true')

args = parser.parse_args() 

if args.set:
    if args.set > 300:
        print("Danger: screen can be overbright!")

    elif args.set < 10:
        print("Danger: screen can be blackout!")

    elif args.set > 100 or args.set < 30:
        print("Warning: visibility problem may occurs!")
        set_brightness(args.set)

    else:
        set_brightness(args.set)

elif args.get:
    get_brightness()

elif args.version:
    version()

elif args.author:
    author()

else:
    parser.print_help()

# xrandr --verbose | awk '/Brightness/ { print $2; exit }'
