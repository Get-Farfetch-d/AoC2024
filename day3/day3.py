def read_report(p):
    """..."""
    with open(p, 'r') as file:
        data = file.read().split("mul(")
    return data


def add_correct_mul(mul_function):
    """..."""
    add_them = []
    for input in mul_function:
        print(input)
        if input[0].isdigit():
            comma_index = input.find(",")
            if input[0:comma_index].isdigit():
                value_a = int(input[0:comma_index])
                endbracket_index = input.find(")")
                if input[comma_index + 1:endbracket_index].isdigit():
                    value_b = int(input[comma_index + 1:endbracket_index])
                    print(f"input = {input}, a = {value_a}, b = {value_b}")
                    add_them.append(value_a * value_b)
    return sum(add_them)


if __name__ == "__main__":
    report_of_levels = read_report(r"data.txt")
    print(f"data: {report_of_levels}")
    print(f"add those: {add_correct_mul(report_of_levels)}")

    report_of_levels = read_report(r"test_data.txt")
    print(f"test_data: {report_of_levels}")
    print(f"add those: {add_correct_mul(report_of_levels)}")
