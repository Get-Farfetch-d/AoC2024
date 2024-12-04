def read_report(p):
    """..."""
    with open(p, 'r') as file:
        data = file.read()
    return data


if __name__ == "__main__":
    report = read_report(r"data.txt")
    print(f"data: {report}")

    report = read_report(r"test_data.txt")
    print(f"test_data: {report}")
