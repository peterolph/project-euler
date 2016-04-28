sudoku = ["003020600",
          "900305001",
          "001806400",
          "008102900",
          "700000008",
          "006708200",
          "002609500",
          "800203009",
          "005010300"]

def colcells(x,y):
  return [(i,y) for i in range(0,9)]
  
def rowcells(x,y):
  return [(x,j) for j in range(0,9)]

def blockcells(x,y):
  return [(i,j) for i in range((x/3)*3,(x/3)*3+3) for j in range((y/3)*3,(y/3)*3+3)]
  
def allcells(x,y):
  return colcells(x,y) + rowcells(x,y) + blockcells(x,y)

poss = [[{str(n):True for n in range(1,10)} for x in range(9)] for y in range(9)]

for x in xrange(9):
  for y in xrange(9):
    if sudoku[x][y] != '0':
      for (i,j) in allcells(x,y):
        poss[i][j][sudoku[x][y]] = False

print poss[0][0]

#for x in xrange(9):
#  for y in xrange(9):
#    if sudoku[x][y] == '0':
#      if len(banned[i][j]) == '8':
        
