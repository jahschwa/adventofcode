#!/usr/bin/env python

def main(s):

  s = int(s.strip())
  buf = [0]
  current = 0
  value = 1
  while value<2018:
    target = (current+s)%len(buf)
    current = target+1
    buf.insert(current,value)
    value += 1
  return buf[(buf.index(2017)+1)%len(buf)]

INPUT="""
376
"""

if __name__=='__main__':
  print main(INPUT)
