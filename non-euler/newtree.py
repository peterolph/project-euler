'''This program performs the tree summing calculation.
It assumes the input file has valid syntax.

A filename can be specified on the command line and
defaults to trees.txt if not given.
Valid syntax consists of pairings of a target value
and a binary tree given as an S expression.
eg. 7 (4 (3()()) (2()()))

 -- Peter Rolph 2013'''

import re, sys

class tree:
  '''Class representing one node of a binary tree.'''
  value = left = right = None
  def __nonzero__(self):
    '''Evaluate class as True if it contains a value.'''
    return self.value != None
  def __repr__(self):
    '''Return an S expression representation of the tree.'''
    if self:
      return ('('+str(self.value)
                 +str(self.left)
                 +str(self.right)+')')
    else:
      return '()'

def parse_s_expr(text):
  '''Returns a set of pairs of targets and binary trees
  from an input S expression.'''

  tokens = re.findall('[0-9]+|[()]',text)  # split the input text into valid tokens: ( ) 0 1 2 ...

  trees = []                               # trees will contain a list of all found trees
  stack = []                               # stack is used to hold all unfinished nodes
                                           #  in the current tree
  for token in tokens:
    if not stack:                          # if the stack is currently empty, we're not in a tree
      if token.isdigit():                  # a number outside a tree is a target value
        target = int(token)
      elif token == '(':                   # an open paren is the start of a new tree, push a top node
        top = tree()
        stack.append(top)
    else:                                  # if the stack is nonempty, we're in a tree
      curr = stack[-1]                     # peek at the top node in the stack
      if token.isdigit():                  # a number becomes the value of the current node
        curr.value = int(token)
      elif token == '(':                   # an open paren is the start of a new node
        if not curr.left:                  # add the node as the left child of the current node
          curr.left = tree()               #  and push the node to the stack
          stack.append(curr.left)
        elif not curr.right:               # unless it already has a left child
          curr.right = tree()
          stack.append(curr.right)
      elif token == ')':                   # a close paren is the end of the current node
        stack.pop()                        #  so pop it from the stack
        if curr == top:                    # if we've at the end of the top node, we're done
          trees.append([target,top])       #  output the target + tree pair
  return trees

def treesum(tree):
  '''Returns the tree sums of an input binary tree.'''

  values = []                              # values will hold a list of all tree sums
  stack = []                               # use a stack instead of recursion

  if tree:                                 # push the root to the stack, unless it's empty
    stack.append(tree)
  while stack:                             # loop until all nodes have been processed
    curr = stack.pop()
    if not curr.left and not curr.right:   # if the current node has no children, it's a leaf
      values.append(curr.value)            #  so it's current value is a tree sum
    else:
      if curr.left:                        # otherwise, add the current node's value to its
        curr.left.value += curr.value      # children and push them to the stack (if they exist)
        stack.append(curr.left)
      if curr.right:
        curr.right.value += curr.value
        stack.append(curr.right)
  return values

if __name__ == '__main__':
  if len(sys.argv) > 1:                    # use the command line filename, if there is one
    filename = sys.argv[1]
  else:
    filename = 'trees.txt'
  text = open(filename, 'r').read()        # read the whole file in

  trees = parse_s_expr(text)               # convert the file into a set of target + tree pairs

  for tree in trees:
    target = tree[0]                       # first value in each pair is a target
    sumlist = treesum(tree[1])             # second value is a tree, grab its sums
    if target in sumlist:                  # if the list of sums contains the target, success
      print 'yes'
    else:
      print 'no'
