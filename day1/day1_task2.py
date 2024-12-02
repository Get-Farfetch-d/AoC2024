"""Figure out exactly how often each number from the left list appears in the right list.
Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of times
that number appears in the right list.
"""

import day1


def calc_similarity_score_between_lists(l1: list[int], l2: list[int]) -> int:
    """Calculate the similarity score (number of list 1 multiplied by the number of occurrences of this number in list 2).

    :param l1: List of ints sorted ascending.
    :param l2: List of ints sorted ascending.
    :return: Similarity score for lists.
    """
    similarity_score = 0
    for i, number1 in enumerate(l1):
        similarity_score += number1 * l2.count(number1)
    return similarity_score


if __name__ == "__main__":
    l1, l2 = day1.read_lists(r"data.txt")
    similarity_score = calc_similarity_score_between_lists(l1, l2)
    print(f"Similarity scores for the whole lists: {similarity_score}\n")

    print("Proof of concept for the test list from task description")
    l1, l2 = day1.read_lists(r"test_data.txt")
    similarity_score = calc_similarity_score_between_lists(l1, l2)
    print(f"l1: {l1}")
    print(f"l2: {l2}")
    print(f"similarity_score for test data: {similarity_score}")

    """OUTPUT
    Similarity scores for the whole lists: 22776016

    Proof of concept for the test list from task description
    l1: [1, 2, 3, 3, 3, 4]
    l2: [3, 3, 3, 4, 5, 9]
    similarity_score for test data: 31
    """
