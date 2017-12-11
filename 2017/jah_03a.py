#!/usr/bin/env python

import math

def main(s):

  x = int(s)
  ring = math.ceil((math.sqrt(x-0.5)-1)/2)
  square = (2*ring+1)**2
  corners = [square-i*2*ring for i in range(0,4)]
  excursion = min(map(lambda i:abs(x-i),corners))
  if x<min(corners)-ring:
    return excursion
  return 2*ring-excursion

INPUT = '361527'

if __name__=='__main__':
  print main(INPUT)
