#!/usr/bin/env python

import math

def main(s):

  x = int(s)
  vals = [1]
  while vals[-1]<x:
    vals.append(get_next_sum(vals))

  return vals[-1]

def spiral_to_coord(x):

  ring = int(math.ceil((math.sqrt(x-0.5)-1)/2))
  square = (2*ring+1)**2

  corners = corners = [square-i*2*ring for i in range(0,4)]
  excursions = [abs(x-i) for i in corners]
  if x<min(corners)-ring:
    excursions[0] = 2*ring-excursions[-1]
  quadrant = excursions.index(min(excursions))

  axes = [square-ring-i*2*ring for i in range(0,4)]
  excursions = [abs(x-i) for i in axes]
  excursion = min(excursions)
  axis = excursions.index(excursion)

  (x,y) = (excursion,ring) if axis in (0,2) else (ring,excursion)
  x *= -1 if quadrant in (1,2) else 1
  y *= -1 if quadrant in (0,1) else 1

  return (x,y)

def coord_to_spiral(x,y):

  ring = max([abs(x),abs(y)])
  square = (2*ring+1)**2
  spiral_dist = abs(ring-x)+abs(-ring-y)
  corner_dist = abs(-ring-x)+abs(-ring-y)

  if corner_dist>2*ring:
    return (2*ring-1)**2+spiral_dist
  return square-spiral_dist

def get_next_sum(vals):

  (x,y) = spiral_to_coord(len(vals)+1)
  total = 0
  for dx in (-1,0,1):
    for dy in (-1,0,1):
      if dx==0 and dy==0:
        continue
      spiral_ind = coord_to_spiral(x+dx,y+dy)-1
      if spiral_ind<len(vals):
        total += vals[spiral_ind]

  return total

INPUT = '361527'

if __name__=='__main__':
  print main(INPUT)
