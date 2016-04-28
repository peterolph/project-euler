
class heap(object):
  
  def __init__(self,in_list = []):
    self.tree = [0] * 2 * len(in_list)
    self.size = 0
    for i in in_list:
      self.insert(i)
  
  def __repr__(self):
    return str(self.tree[1:self.size+1])
  
  def insert(self,item):
    self.size += 1
    k = self.size
    while k > 1 and item > self.tree[k/2]:
      self.tree[k] = self.tree[k/2]
      k >>= 1
    self.tree[k] = item
  
  def pop(self):
    output = self.tree[1]
    item = self.tree[self.size]
    self.tree[self.size] = 0
    self.size -= 1
    k = 1
    while k < self.size:
      if item < self.tree[k*2]:
        self.tree[k] = self.tree[k*2]
        k = k*2
      elif item < self.tree[k*2+1]:
        self.tree[k] = self.tree[k*2+1]
        k = k*2 + 1
      else:
        self.tree[k] = item
        break
    return output
    

if __name__ == '__main__':
  
  vals = [1,2,3,4,5,6,7]
  
  n = heap([1])
  
  print n
  print n.pop()
  print n
