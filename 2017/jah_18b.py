#!/usr/bin/env python

def main(s):

  instructions = [x.split(' ') for x in s.strip().split('\n')]
  (rq,sq) = ([],[])
  c1 = CPU(instructions,0,rq,sq)
  c2 = CPU(instructions,1,sq,rq)
  while (c1.running() or c2.running()) and not (c1.waiting and c2.waiting):
    if c1.running():
      c1.execute()
    if c2.running():
      c2.execute()
  return c2.sent

class CPU(object):

  def __init__(self,instr,pid,rq,sq):

    self.instructions = instr if isinstance(instr,list) else [instr]
    self.registers = {chr(i):0 for i in range(97,97+26)}
    self.registers['p'] = pid
    self.rq = rq
    self.sq = sq
    self.index = 0
    self.waiting = False
    self.sent = 0

  def running(self):
    return self.index<len(self.instructions)

  def execute(self):
    instr = self.instructions[self.index]
    result = getattr(self,instr[0])(*instr[1:])
    if result is None:
      self.index += 1

  def get(self,n):
    return int(self.registers.get(n,n))

  def snd(self,x):
    self.sq.insert(0,self.get(x))
    self.sent += 1

  def set(self,x,y):
    self.registers[x] = self.get(y)

  def add(self,x,y):
    self.registers[x] += self.get(y)

  def mul(self,x,y):
    self.registers[x] *= self.get(y)

  def mod(self,x,y):
    self.registers[x] %= self.get(y)

  def rcv(self,x):
    if self.rq:
      self.registers[x] = self.get(self.rq.pop())
      self.waiting = False
    else:
      self.waiting = True
      return False

  def jgz(self,x,y):
    if self.get(x)>0:
      self.index += self.get(y)-1

INPUT = """
set i 31
set a 1
mul p 17
jgz p p
mul a 2
add i -1
jgz i -2
add a -1
set i 127
set p 618
mul p 8505
mod p a
mul p 129749
add p 12345
mod p a
set b p
mod b 10000
snd b
add i -1
jgz i -9
jgz a 3
rcv b
jgz b -1
set f 0
set i 126
rcv a
rcv b
set p a
mul p -1
add p b
jgz p 4
snd a
set a b
jgz 1 3
snd b
set f 1
add i -1
jgz i -11
snd a
jgz f -16
jgz a -19
"""

if __name__=='__main__':
  print main(INPUT)
