def read_report(p):
    """..."""
    with open(p, 'r') as file:
        data = file.read()
    return data


if __name__ == "__main__":
    report_of_levels = read_report(r"data.txt")
    print(f"data: {report_of_levels}")

    report_of_levels = read_report(r"test_data.txt")
    print(f"test_data: {report_of_levels}")
