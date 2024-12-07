
import enum

UP = '^'
DOWN = 'v'
RIGHT = '>'
LEFT = '<'

class Direction(enum.Enum):
    UP = '^'
    DOWN = 'v'
    RIGHT = '>'
    LEFT = '<'


if __name__ == "__main__":
    with open(r"data.txt", "r") as f:
        content = f.read()

    puzzle_lines = content.split("\n")

    puzzle = []
    for line in puzzle_lines:
        puzzle.append(list(line))

    print(puzzle)

    puzzle_ongoing = True
    visited_points = 0


    while puzzle_ongoing:
        character = ''
        for line_index, puzzle_line in enumerate(puzzle):
            if UP in puzzle_line:
                print("going up")
                character = UP
                guard_index = puzzle_line.index(character)
                if line_index != 0:
                    if puzzle[line_index-1][guard_index] == '#':
                        puzzle[line_index][guard_index] = RIGHT
                    else:
                        puzzle[line_index][guard_index] = "X"
                        puzzle[line_index-1][guard_index] = character
                else:
                    puzzle_ongoing = False
                    puzzle[line_index][guard_index] = "X"
                break
            elif DOWN in puzzle_line:
                print("going down")
                character = DOWN
                guard_index = puzzle_line.index(character)
                if line_index < len(puzzle) - 1:
                    if puzzle[line_index + 1][guard_index] == '#':
                        puzzle[line_index][guard_index] = LEFT
                    else:
                        puzzle[line_index][guard_index] = "X"
                        puzzle[line_index+1][guard_index] = character
                else:
                    puzzle_ongoing = False
                    puzzle[line_index][guard_index] = "X"
                break
            elif RIGHT in puzzle_line:
                print("going right")
                character = RIGHT
                guard_index = puzzle_line.index(character)
                if guard_index < (len(puzzle_line) - 1):
                    if puzzle[line_index][guard_index + 1] == '#':
                        puzzle[line_index][guard_index] = DOWN
                    else:
                        puzzle[line_index][guard_index] = "X"
                        puzzle[line_index][guard_index + 1] = character
                else:
                    puzzle_ongoing = False
                    puzzle[line_index][guard_index] = "X"
                break
            elif LEFT in puzzle_line:
                print("going left")
                character = LEFT
                guard_index = puzzle_line.index(character)
                if guard_index > 0:
                    if puzzle[line_index][guard_index - 1] == '#':
                        puzzle[line_index][guard_index] = UP
                    else:
                        puzzle[line_index][guard_index] = "X"
                        puzzle[line_index][guard_index - 1] = character
                else:
                    puzzle_ongoing = False
                    puzzle[line_index][guard_index] = "X"
                break

    for puzzle_line in puzzle:
        print(puzzle_line)
        visited_points += puzzle_line.count("X")

    print("Result:", visited_points)