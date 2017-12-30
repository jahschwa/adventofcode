#!/usr/bin/env python

from collections import OrderedDict

RAN = 0
POS = 1
DIR = 2

def main(s):

  scanners = {}
  for line in s.strip().split('\n'):
    line = map(int,line.split(': '))+[0,1]
    scanners[line[0]] = line[1:]

  last = max(scanners.keys())
  severity = 0
  current = -1
  while current<last:
    current += 1
    (r,p,d) = scanners.get(current,(0,1,0))
    if p==0:
      severity += current*r
    for (l,(r,p,d)) in scanners.items():
      new = p+d
      scanners[l][POS] = new
      scanners[l][DIR] = -d if new==0 or new==r-1 else d

  return severity

def parse(s):

  return map(int,s.split(': '))+[0,1]

INPUT = """
0: 3
1: 2
2: 4
4: 4
6: 5
8: 8
10: 6
12: 6
14: 8
16: 6
18: 6
20: 8
22: 12
24: 8
26: 8
28: 12
30: 8
32: 12
34: 9
36: 14
38: 12
40: 12
42: 12
44: 14
46: 14
48: 10
50: 14
52: 12
54: 14
56: 12
58: 17
60: 10
64: 14
66: 14
68: 12
70: 12
72: 18
74: 14
78: 14
82: 14
84: 24
86: 14
94: 14
"""

if __name__=='__main__':
  print main(INPUT)
