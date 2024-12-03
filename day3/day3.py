import re

expression = r"(mul\((\d+),(\d+)\))|(don\'t\(\))|(do\(\))"

if __name__ == "__main__":
    with open(r"data.txt", "r") as f:
        commands = f.read()
    print(commands)

    result = 0
    do = True
    for match in re.finditer(expression, commands):
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
    print("Result", result)
