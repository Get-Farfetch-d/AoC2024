""" TASK 1:
...
"""
import itertools
import re


def read_report(p):
    """Read data.

    :param p: Path to file.
    :return: Data.
    """
    equation = []
    with open(p, "r") as f:
        for line in f:
            numbers = re.findall(r'\d+', line)
            result = list(map(int, numbers))
            equation.append(result)
    return equation


def check_equation(report: list) -> bool:
    """..."""
    table = list(itertools.product(["+", "*", "||"], repeat=(len(report) - 2)))
    for i in table:
        result = report[1]
        for j in range(2, len(report)):
            if i[j-2] == "+":
                result += report[j]
            elif i[j-2] == "*":
                result *= report[j]
            elif i[j-2] == "||":
                result = int(str(result) + str(report[j]))
        if report[0] == result:
            return True
    return False


def count_corect_equations(report: list[list[int]]):
    """..."""
    correct_equations = 0
    for equation in report:
        if check_equation(equation):
            correct_equations += equation[0]
    return correct_equations


if __name__ == "__main__":
    report = read_report(r"test_data.txt")
    print(f"test_data: {report}")
    print(f"Sum of correct equations in test data: {count_corect_equations(report)}")

    report = read_report(r"data.txt")
    print(f"data: {report}")
    print(f"Sum of correct equations in data: {count_corect_equations(report)}")

