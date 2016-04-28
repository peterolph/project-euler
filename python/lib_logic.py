
def ones(n):
  return (1 << n) - 1

class logic(object):
  
  def __init__(self,v,s=32):
    if v.bit_length() > s:
      raise ValueError
    self.size  = s
    self.value = v
  
  def __getitem__(self,s):
    hi, lo = self._bounds(s)
    return self.value >> lo & ones(hi-lo+1)
  
  def __setitem__(self,s,v):
    hi, lo = self._bounds(s)
    if not isinstance(v,int):
      raise TypeError
    if v.bit_length() > hi-lo+1:
      raise ValueError
    self.value = (self.value & ~(ones(hi-lo+1)<<lo)) | (v << lo)
  
  def split(self,*args):
    total = sum(args)
    if total != self.size:
      raise ValueError
    output = []
    for a in args:
      output.append(self[total-1:total-a])
      total -= a
    return output
  
  def __repr__(self):
    return hex(self.value)
  
  def _bounds(self,s):
    if isinstance(s,int):
      hi, lo = s, s
    elif isinstance(s,slice):
      if s.start is None:
        start = 0
      else:
        start = s.start
      if s.stop is None:
        stop = self.size-1
      else:
        stop = s.stop
      hi, lo = max(start,stop),min(start,stop)
    else:
      raise TypeError
    if hi > self.size - 1:
      raise ValueError
    return hi, lo
