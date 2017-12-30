#!/usr/bin/env python
#
# 65*16807^n % 2147483647 % 65536 = 8921*48271^n % 2147483647 % 65536
#
# 2147483647 / 65536 = 32767
#
#

import time

def main():
  funcs = [builtin,mod7,mod7r]
  for func in funcs:
	  timeit(func)

def timeit(func):
  print func.__name__
  start = time.time()
  for i in xrange(0,100000000):
    func(i)
  end = time.time()
  print end-start

def builtin(x):
  return x%7

def mod7(x):
  return ((x>>3)+(x&7))%7

def mod7r(x):
  if x<7:
    return x
  elif x==7:
    return 0
  return mod7r((x>>3)+(x&7))

main()
