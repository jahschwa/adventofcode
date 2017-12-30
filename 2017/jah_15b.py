#!/usr/bin/env python

import time

def main(s):

  s = map(int,s.strip().split('\n'))
  gen_a = make_gen(16807,4,s[0])
  gen_b = make_gen(48271,8,s[1])

  same = 0
  for i in xrange(0,5000000):
    if gen_a.next()&65535==gen_b.next()&65535:
      same += 1
  return same

def make_gen(factor,constraint,start):

  current = start
  while True:
    current = (current*factor)%2147483647
    if not current%constraint:
      yield current

INPUT = """
883
879
"""

if __name__=='__main__':
  print main(INPUT)
