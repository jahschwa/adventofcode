#!/usr/bin/env python

from jah_10b import main as knot_hash

def main(s):

  s = s.strip()
  grid = gen_grid(s)
  return sum(map(sum,grid))

def gen_grid(key):

  grid = [None]*128
  for r in xrange(0,128):
    h = knot_hash('%s-%s' % (key,r))
    s = ''.join([bin(int(x,16))[2:].zfill(4) for x in h])
    grid[r] = map(int,s)
  return grid

INPUT = """
ffayrhll
"""

if __name__=='__main__':
  print main(INPUT)
