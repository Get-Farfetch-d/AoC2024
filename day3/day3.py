def read_report(p):
    """..."""
    with open(p, 'r') as file:
        data = file.read()
    return data


# def add_correct_mul(mul_function):
#     """..."""
#     add_them = []
#     for input in mul_function.split("mul("):
#         if input[0].isdigit():
#             comma_index = input.find(",")
#             if input[0:comma_index].isdigit():
#                 value_a = int(input[0:comma_index])
#                 endbracket_index = input.find(")")
#                 if input[comma_index + 1:endbracket_index].isdigit():
#                     value_b = int(input[comma_index + 1:endbracket_index])
#                     add_them.append(abs(value_a) * abs(value_b))
#     return sum(add_them)


def dict_solution(mul_function):
    """..."""
    mapping = {}
    sumup = 0
    for input in mul_function.split("mul("):
        if input[0].isdigit():
            comma_index = input.find(",")
            if input[0:comma_index].isdigit() and input[0:comma_index] <= input[0:3]:
                endbracket_index = input.find(")")
                value_a = int(input[0:comma_index])
                if input[comma_index + 1:endbracket_index].isdigit() and input[comma_index + 1:endbracket_index] <= input[comma_index + 1:comma_index + 4]:
                    value_b = int(input[comma_index + 1:endbracket_index])
                    mapping.update({"mul(" + input: {"a": value_a, "b": value_b, "a * b": value_a * value_b}})
                    sumup += value_a * value_b
    print(mapping)
    return sumup


if __name__ == "__main__":
    report_of_levels = read_report(r"data.txt")
    print(f"data: {report_of_levels}")
    # print(f"add those: {add_correct_mul(report_of_levels)}")
    print(f"dict solution: {dict_solution(report_of_levels)}")

    report_of_levels = read_report(r"test_data.txt")
    print(f"test_data: {report_of_levels}")
    # print(f"add those: {add_correct_mul(report_of_levels)}")
    print(f"dict solution: {dict_solution(report_of_levels)}")
