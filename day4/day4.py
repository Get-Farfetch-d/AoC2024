
import re

pattern = "XMAS"
reversed_pattern = pattern[::-1]
xmas_re = rf"{pattern}|{reversed_pattern}"


if __name__ == "__main__":
    with open(r"data.txt", "r") as f:
        content = f.readlines()
    print(content)
    xmas_count = 0

    for i in range(len(content)):
        content[i] = content[i].replace("\n", "")

    # Horizontal
    for row in content:
        for char_no in range(len(row) - (len(pattern)) + 1):
            horizontal_slice = f"{row[char_no]}{row[char_no+1]}{row[char_no+2]}{row[char_no+3]}"
            xmas_count += len(re.findall(xmas_re, horizontal_slice))

    # Vertical
    for row_no in range(len(content) - (len(pattern)) + 1):
        row = content[row_no]
        for char_no in range(len(row)):
            vertical_slice = f"{row[char_no]}{content[row_no+1][char_no]}{content[row_no+2][char_no]}{content[row_no+3][char_no]}"
            xmas_count += len(re.findall(xmas_re, vertical_slice))

    # Diagonal right
    for row_no in range(len(content) - (len(pattern)) + 1):
        row = content[row_no]
        for char_no in range(len(row) - (len(pattern)) + 1):
            diagonal_slice = f"{row[char_no]}{content[row_no+1][char_no+1]}{content[row_no+2][char_no+2]}{content[row_no+3][char_no+3]}"
            xmas_count += len(re.findall(xmas_re, diagonal_slice))

    # Diagonal left
    for row_no in range(len(content) - (len(pattern)) + 1):
        row = content[row_no]
        for char_no in range((len(pattern)) - 1, len(row)):
            diagonal_slice = f"{row[char_no]}{content[row_no+1][char_no-1]}{content[row_no+2][char_no-2]}{content[row_no+3][char_no-3]}"
            xmas_count += len(re.findall(xmas_re, diagonal_slice))

    # expected 18
    print("Result: ", xmas_count)
