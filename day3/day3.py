import re

expression_task1 = r"(mul\((\d+),(\d+)\))"
expression_task2 = r"(mul\((\d+),(\d+)\))|(don\'t\(\))|(do\(\))"


def task1(commands):
    result = 0
    do = True
    for match in re.finditer(expression_task2, commands):
        for group in match.groups():
            if group is None:
                continue
            elif "mul" in group and do:
                group = group.replace("mul(", "")
                group = group.replace(")","")
                factors = group.split(",")
                result += int(factors[0]) * int(factors[1])
    print("Task 1: Result", result)


def task2(commands):
    result = 0
    do = True
    for match in re.finditer(expression_task2, commands):
        for group in match.groups():
            if group is None:
                continue
            if "don't" in group:
                do = False
            elif "do" in group:
                do = True
            elif "mul" in group and do:
                group = group.replace("mul(", "")
                group = group.replace(")","")
                factors = group.split(",")
                result += int(factors[0]) * int(factors[1])
    print("Task 2: Result", result)


if __name__ == "__main__":
    with open(r"data.txt", "r") as f:
        file_commands = f.read()
    task1(file_commands)
    task2(file_commands)
