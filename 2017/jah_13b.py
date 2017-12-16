#!/usr/bin/env python

import sys
from fractions import gcd

def main(s):

  scanners = dict(map(parse,s.strip().split('\n')))
  periods = get_periods(scanners)
  cons = get_constraints(periods)
  (first,factors) = get_first(cons)
  jump = reduce(lcm,factors)

  new_cons = {p:r for (p,r) in cons.iteritems() if p not in factors}
  stop = reduce(lcm,periods)
  delay = first
  while delay<=stop:
    try:
      for (p,rs) in new_cons.iteritems():
        if delay%p not in rs:
          raise Collision
    except Collision:
      delay += jump
    else:
      return delay

def get_periods(scanners):

  periods = {}
  for (layer,rang) in scanners.iteritems():
    p = 2*(rang-1)
    if p in periods:
      periods[p].add(layer%p)
    else:
      periods[p] = set([layer%p])
  return periods

def get_constraints(periods):

  poss = {}
  for (period,layers) in periods.iteritems():
    poss[period] = range(0,period)

  for (period,layers) in periods.iteritems():
    for layer in layers:
      for (p,rs) in poss.iteritems():
        if p<period or p%period:
          continue
        rem = (period-layer)%period
        for i in range(rem,p,period):
          try:
            poss[p].remove(i)
          except ValueError:
            pass

  return poss

def get_first(cons):

  base = 1
  new_cons = {p:c[0] for (p,c) in cons.iteritems() if len(c)==1}
  factors = new_cons.keys()
  for period in new_cons.keys():
    r = new_cons[period]
    if r==0:
      base = lcm(base,period)
      del new_cons[period]

  first = base
  while True:
    try:
      for (p,r) in new_cons.iteritems():
        if first%p!=r:
          raise Collision
      return (first,factors)
    except Collision:
      first += base

def main_slow(s):

  fw = Firewall(dict(map(parse,s.strip().split('\n'))))

  periods = map(lambda x:2*x-2,fw.scanners.values())
  stop = reduce(lcm,periods)
  for delay in xrange(0,stop):
    if fw.safe(delay):
      break

  if delay>=stop:
    raise ValueError('Unable to find clear path')

  return delay

class Collision(Exception):
  pass

def parse(s):

  return map(int,s.split(': '))

def lcm(a,b):

  return a*b/gcd(a,b)

class Firewall(object):

  def __init__(self,scanners):

    self.scanners = scanners
    self.start = min(self.scanners)
    self.stop = max(self.scanners)
    self.original = {layer:[0,1] for layer in self.scanners}
    self.states = {0:self.original}
    self.steps = [0]

  def safe(self,delay):

    current = 0
    while current<=self.stop:
      if self.collision(delay+current,current):
        return False
      current += 1
    return True

  def collision(self,step,layer):

    if step not in self.states:
      self.update(step)
    return self.states[step].get(layer,[1])[0]==0

  def update(self,step):

    last = self.states[step-1]
    this = {}
    for (l,r) in self.scanners.iteritems():
      (p,d) = last[l]
      new = p+d
      this[l] = [new,-d if new==0 or new==r-1 else d]
    self.states[step] = this
    self.steps.append(step)

    if len(self.steps)>self.stop-self.start+1:
      drop = self.steps[0]
      del self.steps[0]
      del self.states[drop]

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
