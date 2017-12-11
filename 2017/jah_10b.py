#!/usr/bin/env python

ROUNDS = 64
SUFFIX = [17, 31, 73, 47, 23]

def main(s):

  lengths = map(ord,s.strip())+SUFFIX

  circle = CircularList(range(0,256))
  cur = 0
  skip = 0

  for i in range(0,ROUNDS):
    for l in lengths:
      circle[cur:cur+l] = reversed(circle[cur:cur+l])
      cur += l+skip
      skip += 1

  return ''.join([hex(x)[2:].zfill(2) for x in condense(circle)])

def condense(circle):

  dense = []
  for i in range(0,16):
    dense.append(reduce(lambda a,b:a^b,circle[16*i:16*(i+1)]))
  return dense

class CircularList(list):

  def __getitem__(self,x):
    if isinstance(x,slice):
      return [self[i] for i in self._make_range(x)]
    return super(CircularList,self).__getitem__(x%len(self))

  def __getslice__(self,a,b):
    return self.__getitem__(slice(a,b))

  def __setitem__(self,x,v):
    if isinstance(x,slice):
      for (i,v) in zip(self._make_range(x),v):
        self[i] = v
      return
    return super(CircularList,self).__setitem__(x%len(self),v)

  def __setslice__(self,a,b,c):
    self.__setitem__(slice(a,b),c)

  def _make_range(self,x):

    start = x.start or 0
    stop = x.stop or len(self)
    step = x.step or 1
    stop = stop+len(self) if stop<start and step>0 else stop


    return range(start,stop,step)

INPUT = """
14,58,0,116,179,16,1,104,2,254,167,86,255,55,122,244
"""

if __name__=='__main__':
  print main(INPUT)
