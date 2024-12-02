"""Pair up the smallest number in the left list with the smallest number in the right list,
then the second-smallest left number with the second-smallest right number, and so on.

Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances.
For example, if you pair up a 3 from the left list with a 7 from the right list, the distance apart is 4; if you pair up a 9 with a 3, the distance apart is 6.
"""


def read_lists(p) -> (list[int], list[int]):
    """Read numbers from file in form of two lists, each sorted ascending.

    :param p: Path to file.
    :return: Two lists of ints sorted ascending.
    """
    l1 = []
    l2 = []
    with open(p, "r") as f:
        for line in f:
            numbers_in_line = [int(n) for n in line.split()]
            l1.append(numbers_in_line[0])
            l2.append(numbers_in_line[1])
    l1.sort()
    l2.sort()
    return l1, l2


def calc_distance_between_lists(l1: list[int], l2: list[int]) -> list[int]:
    """Calculate the distance (difference) between elements with the same id in two lists (sorted descending).

    :param l1: List of ints sorted ascending.
    :param l2: List of ints sorted ascending.
    :return: List of distances (differences) between elements of the input lists with the same id.
    """
    list_of_distances = []
    for i, number1 in enumerate(l1):
        list_of_distances.append(abs(number1 - l2[i]))
    return list_of_distances


if __name__ == "__main__":
    l1, l2 = read_lists(r"C:\Users\robert.piatek\OneDrive - Accenture\Desktop\AOC\AoC2024\day1\data.txt")
    list_of_distances = calc_distance_between_lists(l1, l2)
    sum_of_distances = sum(list_of_distances)
    print(f"Sum of distances for the whole lists: {sum_of_distances}\n")

    print("Proof of concept for the test list from task description")
    l1, l2 = read_lists(r"C:\Users\robert.piatek\OneDrive - Accenture\Desktop\AOC\AoC2024\day1\test_data.txt")
    list_of_distances = calc_distance_between_lists(l1, l2)
    sum_of_distances = sum(list_of_distances)
    print(f"l1: {l1}")
    print(f"l2: {l2}")
    for i, number1 in enumerate(l1):
        print(f"{number1} - {l2[i]} = list_of_distances: {list_of_distances[i]}, manual_check = {abs(number1 - l2[i])}")
    print(f"Sum of distances for the first five elements: {sum(list_of_distances)}")

    """OUTPUT
    Sum of distances for the whole lists: 1660292

    Proof of concept for the test list from task description
    l1: [1, 2, 3, 3, 3, 4]
    l2: [3, 3, 3, 4, 5, 9]
    1 - 3 = list_of_distances: 2, manual_check = 2
    2 - 3 = list_of_distances: 1, manual_check = 1
    3 - 3 = list_of_distances: 0, manual_check = 0
    3 - 4 = list_of_distances: 1, manual_check = 1
    3 - 5 = list_of_distances: 2, manual_check = 2
    4 - 9 = list_of_distances: 5, manual_check = 5
    Sum of distances for the first five elements: 11
    """

    # print("Proof of concept for the first five elements")
    # print(f"First five elements of l1: {l1[:5]}")
    # print(f"First five elements of l2: {l2[:5]}")
    # for i in range(5):
    #     print(f"{l1[i]} - {l2[i]} = list_of_distances: {list_of_distances[i]}, manual_check = {abs(l1[i] - l2[i])}")
    # print(f"Sum of distances for the first five elements: {sum(list_of_distances[:5])}")
