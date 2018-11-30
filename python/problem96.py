
import copy
import re

b = 3
b_sq = b * b

def to_block(pos):
    return (b*(pos[0]//b), b*(pos[1]//b))

def print_item(item):
    if item > 0:
        return str(item)
    else:
        return " "

def print_grid(grid):
    line = "+-" + "--"*b_sq + "+"
    return line + "\n" + "\n".join(("| " + " ".join(print_item(grid[i][j]) for j in range(b_sq)) + " |") for i in range(b_sq)) + "\n" + line

def keyfunc(possible_item):
    return len(possible_item[1])

def solved(grid):
    return all(all(grid[i][j] for i in range(b_sq)) for j in range(b_sq))

def first(s):
    for i in s:
        return i

def solve(grid,depth):

    copied = copy.deepcopy(grid)

    while True:
        columns = {i:set(copied[i][j] for j in range(b_sq)) for i in range(b_sq)}
        rows = {j:set(copied[i][j] for i in range(b_sq)) for j in range(b_sq)}
        blocks = {(i,j):set(copied[x][y] for x in range(i,i+b) for y in range(j,j+b)) for i in range(0,b_sq,b) for j in range(0,b_sq,b)}
        possibles = {(i,j):{i for i in range(1,b_sq+1)} - columns[i] - rows[j] - blocks[to_block((i,j))] for i in range(b_sq) for j in range(b_sq) if copied[i][j]==0}
        found_some = False
        for ((i,j),item) in possibles.items():
            if len(item) == 1:
                copied[i][j] = first(item)
                found_some = True
                break
        if found_some:
            continue
        else:
            break

    if len(possibles) > 0:
        ((i,j),item) = list(possibles.items())[0]
        for value in item:
            copied[i][j] = value
            potential = solve(copied,depth+1)
            if potential is not None:
                return potential
            else:
                continue
    if solved(copied):
        return copied
    else:
        return None

def top_left_3_digits(grid):
    return 100*grid[0][0] + 10*grid[0][1] + grid[0][2]

if __name__ == "__main__":

    grids = [[[int(char) for char in line] for line in grid.splitlines()] for grid in re.split("Grid \d\d\n", open("superfiendish.txt").read())]

    total = 0

    for grid in grids:
        solution = solve(grid,0)
        before = print_grid(grid)
        after = print_grid(solution)
        print("\n".join("  ".join(item) for item in zip(before.splitlines(), after.splitlines())))
        total += top_left_3_digits(solution)

    print("TOTAL : ",total)
