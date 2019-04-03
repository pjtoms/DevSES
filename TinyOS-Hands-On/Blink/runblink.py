#!/usr/bin/python
from TOSSIM import *
import sys
t = Tossim([])
r = t.radio()
t.addChannel("BlinkC", sys.stdout)
m = t.getNode(1)
m.bootAtTime(100)
print "while loop"
while (m.isOn() == 0):
  t.runNextEvent()
print "for loop"
for i in range(0, 2000):
  t.runNextEvent()
