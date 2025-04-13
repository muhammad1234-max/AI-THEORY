import time #to track execution time of the code
import copy

#setup Sudoku board variables
rows = "ABCDEFGHI"
cols = "123456789"
digits = "123456789"

#function to generate all combination of values from 2 lists
def cross(A, B):
    return [a + b for a in A for b in B]

#creating list of all units in a sudoku board
squares = cross(rows, cols)
unitlist = ([cross(r, cols) for r in rows] +
            [cross(rows, c) for c in cols] +
            [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI')
             for cs in ('123', '456', '789')])

units = {s: [u for u in unitlist if s in u] for s in squares}
peers = {s: set(sum(units[s], [])) - {s} for s in squares}

#goes through the whole grid and returns all the possible values for all the empty squares
def parse_grid(grid):
    values = {s: digits for s in squares}
    for s, d in zip(squares, grid):
        if d in digits and not assign(values, s, d):
            return False
    return values

#assigns values and checks for contradiction
#when value assigned it is removed from possibilities of other squares
#in case of a contradiction it eliminates those values
def assign(values, s, d):
    other_values = values[s].replace(d, '')
    if all(eliminate(values, s, d2) for d2 in other_values):
        return values
    return False

#carrying out constraint propagations and removing contradictory values like trial and error
def eliminate(values, s, d):
    if d not in values[s]:
        return values
    values[s] = values[s].replace(d, '')
    if len(values[s]) == 0:
        return False
    elif len(values[s]) == 1:
        d2 = values[s]
        if not all(eliminate(values, s2, d2) for s2 in peers[s]):
            return False
    for u in units[s]:
        dplaces = [s2 for s2 in u if d in values[s2]]
        if len(dplaces) == 0:
            return False
        elif len(dplaces) == 1:
            if not assign(values, dplaces[0], d):
                return False
    return values

#ac3 arc consistency algorithm is run and eliminates values causing conflicts based on the provided constraints
def ac3(values):
    queue = [(xi, xj) for xi in squares for xj in peers[xi]]
    while queue:
        xi, xj = queue.pop(0)
        if revise(values, xi, xj):
            if len(values[xi]) == 0:
                return False
            for xk in peers[xi] - {xj}:
                queue.append((xk, xi))
    return values

#revising an arc 
def revise(values, xi, xj):
    revised = False
    for d in values[xi]:
        if len(values[xj]) == 1 and values[xj] == d:
            values[xi] = values[xi].replace(d, '')
            revised = True
    return revised

#checks if puzzle is solved by seeing if the square has one possible value left
def is_solved(values):
    return all(len(values[s]) == 1 for s in squares)

#implements a backtracking search algorithm and keeps running until it finds a solution
def backtrack(values):
    if values is False:
        return False
    if is_solved(values):
        return values
    n, s = min((len(values[s]), s) for s in squares if len(values[s]) > 1)
    for d in values[s]:
        new_values = copy.deepcopy(values)
        if assign(new_values, s, d):
            result = backtrack(new_values)
            if result:
                return result
    return False

#main function to solve the board
def solve_custom(grid):
    values = parse_grid(grid)
    values = ac3(values)
    result = backtrack(values)
    return ''.join(result[s] for s in squares) if result else None

if __name__ == "__main__":
    #taking input of sudoku board from the file
    input_file = "sudoku_input.txt"

    with open(input_file, 'r') as file:
        puzzles = [line.strip() for line in file if line.strip()]

    for idx, puzzle in enumerate(puzzles):
        print(f"\nSolving Puzzle #{idx + 1}")
        print("Input:")
        for i in range(0, 81, 9):
            print(puzzle[i:i+9])
        
        start_time = time.time()
        solution = solve_custom(puzzle)
        end_time = time.time()

        if solution:
            print("\nSolved:")
            for i in range(0, 81, 9):
                print(solution[i:i+9])
        else:
            print("No solution found.")

        print(f"Time taken: {end_time - start_time:.4f} seconds")
