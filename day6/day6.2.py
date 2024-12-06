import copy

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
    if puzz[line_index][point_index] == ".":
        puzz[line_index][point_index] = "#"
        if not check_puzzle(puzz):
            return True


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
    puzzle_backup = copy.deepcopy(puzzle)
    for line_index, puzzle_line in enumerate(puzzle):
        for point_index in range(len(puzzle_line)):
            if puzzle[line_index][point_index] == ".":
                puzzle[line_index][point_index] = "#"
                iteration += 1
                print(iteration, max_iterations)
                if not check_puzzle(copy.deepcopy(puzzle)):
                    valid_obstacles += 1
                    print("Valid obstacle: ", valid_obstacles)
                puzzle[line_index][point_index] = "."
            else:
                continue

    print("Result:", valid_obstacles)