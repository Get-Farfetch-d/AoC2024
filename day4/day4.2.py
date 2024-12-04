
import re

pattern = "MAS"
reversed_pattern = pattern[::-1]
xmas_re = rf"{pattern}|{reversed_pattern}"


if __name__ == "__main__":
    with open(r"data.txt", "r") as f:
        content = f.readlines()
    print(content)
    xmas_count = 0

    for i in range(len(content)):
        content[i] = content[i].replace("\n", "")

    for row_no in range(1, len(content) - 1):
        row = content[row_no]
        for char_no in range(1, len(row) - 1):
            vertical_right = f"{content[row_no-1][char_no-1]}{content[row_no][char_no]}{content[row_no+1][char_no+1]}"
            vertical_left = f"{content[row_no-1][char_no+1]}{content[row_no][char_no]}{content[row_no+1][char_no-1]}"

            if re.findall(xmas_re, vertical_left) and re.findall(xmas_re, vertical_right):
                xmas_count += 1

    # expected 9
    print("Result: ", xmas_count)
