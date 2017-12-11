#!/usr/bin/env python

from collections import OrderedDict

def main(s):

  banks = map(int,s.strip().split('\t'))
  states = OrderedDict()
  cycles = 0
  while tuple(banks) not in states:
    states[tuple(banks)] = 1
    balance(banks)
    cycles += 1

  return cycles-states.keys().index(tuple(banks))

def balance(banks):

  (i,m) = max(enumerate(banks),key=lambda t:t[1])
  banks[i] = 0
  while m>0:
    i = (i+1)%len(banks)
    banks[i] += 1
    m -= 1

INPUT = """
11	11	13	7	0	15	5	5	4	4	1	1	7	1	15	11
"""

if __name__=='__main__':
  print main(INPUT)
