#!/usr/bin/python
import sys, os

fil = sys.argv[1]

base = os.path.basename(fil)

if not base[-4:].lower() == ".wav":
    print "wav file please!"
    exit()

base = base[:-4]
print base

cmd = "rm peaks/" + base + "*.peak"
print cmd
os.system(cmd)

cmd = "sox " + fil + " -c 1 interchange/metamix/audiofiles/" + base + "-L.wav mixer -l"
print cmd
os.system(cmd)

cmd = "sox " + fil + " -c 1 interchange/metamix/audiofiles/" + base + "-R.wav mixer -r"
print cmd
os.system(cmd)
