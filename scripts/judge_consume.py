#!/usr/bin/env python3

import sys, time, os, subprocess, time, shutil, json

paths = sys.argv[1:]

tot = 0
for path in paths:
    with open(path) as verdict:
        tot += float(verdict.readline())

grade = tot / len(paths) * 100

if os.isatty(1):
    print('Total Points: {}/100'.format(grade))
else:
    print(json.dumps({'grade': grade}))

