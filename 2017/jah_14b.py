#!/usr/bin/env python

from jah_10b import main as knot_hash

(N,E,S,W) = range(0,4)

def main(s):

  s = s.strip()
  grid = gen_grid(s)
  return label_regions(grid)

def gen_grid(key):

  grid = [None]*128
  for r in xrange(0,128):
    h = knot_hash('%s-%s' % (key,r))
    s = ''.join([bin(int(x,16))[2:].zfill(4) for x in h])
    grid[r] = map(int,s)
  return grid

def label_regions(grid):

  for i in range(0,len(grid)):
    grid[i] = [(0,-1)[c] for c in grid[i]]
  counter = 1
  for r in xrange(0,128):
    for c in xrange(0,128):
      if grid[r][c]==-1:
        label_region(grid,r,c,counter)
        counter += 1
  return counter-1

def label_region(grid,row,col,counter):

  grid[row][col] = counter
  dirs = [
      (N,row>0,row-1,col),
      (E,col<127,row,col+1),
      (S,row<127,row+1,col),
      (W,col>0,row,col-1)
  ]
  for (d,t,r,c) in dirs:
    if t and grid[r][c]==-1:
      label_region(grid,r,c,counter)

INPUT = """
ffayrhll
"""

if __name__=='__main__':
  print main(INPUT)
