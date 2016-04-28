'''This program performs the tree summing calculation.
It assumes the input file has valid syntax.

A filename can be specified on the command line and
defaults to trees.txt if not given.
Valid syntax consists of pairings of a target value
and a binary tree given as an S expression.
eg. 7 (4 (3()()) (2()()))

 -- Peter Rolph 2013'''

import re, sys

def treesum(tree):
    '''Returns a list of tree sums from an input tree.'''
    # if the input tree is empty, return empty
    if len(tree) == 0:
        return []
    # if the input tree is not empty, return the first
    #  value added to all values from the subtrees
    else:
        value = tree[0]
        subvalues = []
        for subtree in tree[1:]:
            subvalues += treesum(subtree)
        # if there are subtrees but they don't contain
        #  anything, just return the value
        if len(subvalues) == 0:
            return [value]
        else:
            return [value + subvalue for subvalue in subvalues]

def parse_s_expr(text):
    '''Returns a tree from an input S expression.'''
    # trim whitspace
    text = re.sub('[\n\t\r ]', '', text)

    # modify the s expressions into a python expression

    # a close paren followed by a value is always the end
    #  of a target + tree pair and the start of a new one, so
    #  add brackets to separate them
    def add_brackets(match):
        return match.group(1)+')('+match.group(2)
    text = re.sub('(\))([0-9]+)', add_brackets, text)

    # convert all ( into ,( to match python syntax
    text = re.sub('\(', ',(', text)

    # the expression matching regex above misses the
    #  start of the first tree and the end of the last
    #  one, so add extra parens, plus two more to join
    #  the whole file into one big tuple
    text = '(('+text+'))'

    # evaluate the now-valid python expression
    trees = eval(text)
    return trees

if __name__ == '__main__':
    # read in the file using the filename from
    #  the command line, if there is one
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = 'trees.txt'
    text = open(filename, 'r').read()

    trees = parse_s_expr(text)

    for tree in trees:
        target = tree[0]
        sumlist = treesum(tree[1])
        if target in sumlist:
            print "yes"
        else:
            print "no"
