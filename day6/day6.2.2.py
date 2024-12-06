import copy
import itertools
from concurrent.futures import ProcessPoolExecutor

UP = '^'
DOWN = 'v'
RIGHT = '>'
LEFT = '<'

def check_puzzle(in_puzzle):
    steps = 0
    max_steps = len(in_puzzle) * len(in_puzzle[0])
    puzzle_ongoing = True
    while puzzle_ongoing and (steps < max_steps):
        character = ''
        for line_index, puzzle_line in enumerate(in_puzzle):
            if UP in puzzle_line:
                character = UP
                guard_index = puzzle_line.index(character)
                if line_index != 0:
                    if in_puzzle[line_index - 1][guard_index] == '#':
                        in_puzzle[line_index][guard_index] = RIGHT
                    else:
                        in_puzzle[line_index][guard_index] = "X"
                        in_puzzle[line_index - 1][guard_index] = character
                else:
                    puzzle_ongoing = False
                    in_puzzle[line_index][guard_index] = "X"
                break
            elif DOWN in puzzle_line:
                character = DOWN
                guard_index = puzzle_line.index(character)
                if line_index < len(in_puzzle) - 1:
                    if in_puzzle[line_index + 1][guard_index] == '#':
                        in_puzzle[line_index][guard_index] = LEFT
                    else:
                        in_puzzle[line_index][guard_index] = "X"
                        in_puzzle[line_index + 1][guard_index] = character
                else:
                    puzzle_ongoing = False
                    in_puzzle[line_index][guard_index] = "X"
                break
            elif RIGHT in puzzle_line:
                character = RIGHT
                guard_index = puzzle_line.index(character)
                if guard_index < (len(puzzle_line) - 1):
                    if in_puzzle[line_index][guard_index + 1] == '#':
                        in_puzzle[line_index][guard_index] = DOWN
                    else:
                        in_puzzle[line_index][guard_index] = "X"
                        in_puzzle[line_index][guard_index + 1] = character
                else:
                    puzzle_ongoing = False
                    in_puzzle[line_index][guard_index] = "X"
                break
            elif LEFT in puzzle_line:
                character = LEFT
                guard_index = puzzle_line.index(character)
                if guard_index > 0:
                    if in_puzzle[line_index][guard_index - 1] == '#':
                        in_puzzle[line_index][guard_index] = UP
                    else:
                        in_puzzle[line_index][guard_index] = "X"
                        in_puzzle[line_index][guard_index - 1] = character
                else:
                    puzzle_ongoing = False
                    in_puzzle[line_index][guard_index] = "X"
                break
        steps += 1
    return steps < max_steps


def check_obstacle(in_puzzle, x, y):
    puzz = copy.deepcopy(in_puzzle)
    if puzz[x][y] == ".":
        puzz[x][y] = "#"
        if not check_puzzle(puzz):
            return True
    return False

# Helper function to unpack the arguments
def worker(args):
    return check_obstacle(*args)

if __name__ == "__main__":
    with open(r"data.txt", "r") as f:
        content = f.read()
    puzzle_lines = content.split("\n")

    puzzle = []
    for line in puzzle_lines:
        puzzle.append(list(line))

    print(puzzle)

    valid_obstacles = 0

    iteration = 0
    max_iterations = len(puzzle) * len(puzzle[0])

    # Nested for loops: range(1, 4) x range(10, 13)
    range1 = range(len(puzzle))  # Outer loop
    range2 = range(len(puzzle[0]))  # Inner loop

    # Generate combinations of (x, y) for the nested loops
    combinations = list(itertools.product(range1, range2))

    # Wrap arguments as tuples for each call to the function
    tasks = [(puzzle, x, y) for x, y in combinations]

    # Use ProcessPoolExecutor to parallelize
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(worker, tasks))

    print(results.count(True))

    print("Result:", valid_obstacles)