
import numpy as np
import collections
import itertools

def create(strings):
  return np.array([[int(c) for c in s] for s in strings])

def row(sudoku,i):
  return sudoku[i,:]

def column(sudoku,j):
  return sudoku[:,j]

def block(sudoku,i,j):
  i_start = i - i%3
  j_start = j - j%3
  return sudoku[i_start:i_start+3, j_start:j_start+3].flat

def solve(sudoku, depth=0):

  while True:
    possibles = []
    for i,j in itertools.product(range(9),repeat=2):
      if sudoku[i,j] == 0:
        possibles_for_this_cell = set(range(10)) - set(row(sudoku,i)) - set(column(sudoku,j)) - set(block(sudoku,i,j))
        if len(possibles_for_this_cell) == 0:
          raise ValueError
        elif len(possibles_for_this_cell) == 1:
          sudoku[i,j] = list(possibles_for_this_cell)[0]
          break
        else: 
          possibles.append(((i,j),possibles_for_this_cell))
    else:
      break

  possibles.sort(key=lambda item: len(item[1]))

  if len(possibles) == 0:
    return sudoku

  for cell, values in possibles:
    for value in values:
      sudoku_with_a_possible = sudoku.copy()
      sudoku_with_a_possible[cell] = value
      try:
        return solve(sudoku_with_a_possible,depth+1)
      except ValueError:
        pass

  raise ValueError




with open('data/p096_sudoku.txt') as f:
  lines = f.read().splitlines()
  sudokus = [create(lines[1+i:10+i]) for i in range(0,len(lines),10)]
  

  for sudoku in sudokus[:3]:
    solution = solve(sudoku)
    print()
    print(solution)
    for i in range(9):
      assert set(row(solution,i)) == set(range(1,10))
      assert set(column(solution,i)) == set(range(1,10))
      assert set(block(solution,(i//3)*3,(i%3)*3)) == set(range(1,10))


