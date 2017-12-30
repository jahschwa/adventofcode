#!/usr/bin/env python

def main(s):

  s = int(s.strip())
  buf = [0]
  current = 0
  value = 1
  after_zero = 0
  while value<=50000000:
    target = (current+s)%value
    current = target+1
    if current==1:
      after_zero = value
    value += 1
  return after_zero

INPUT="""
376
"""

if __name__=='__main__':
  print main(INPUT)
