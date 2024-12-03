def read_report(p):
    """..."""
    with open(p, 'r') as file:
        data = file.read()
    return data


def yet_another_solution(mul_function):
    """..."""
    sumup = 0
    for input in mul_function.split("mul"):
        openbracket_index = input.find("(")
        endbracket_index = input.find(")")
        comma_index = input.find(",")
        if openbracket_index == 0 and comma_index <= 4 and 0 < endbracket_index <= comma_index + 4:
            print(input)
            value_a = input[openbracket_index+1:comma_index]
            value_b = input[comma_index+1:endbracket_index]
            if value_a.isnumeric() and value_b.isnumeric():
                sumup += int(value_a) * int(value_b)
    return sumup


if __name__ == "__main__":
    report_of_levels = read_report(r"data.txt")
    print(f"data: {report_of_levels}")
    print(f"please... {yet_another_solution(report_of_levels)}")

    report_of_levels = read_report(r"test_data.txt")
    print(f"test_data: {report_of_levels}")
    print(f"please... {yet_another_solution(report_of_levels)}")
