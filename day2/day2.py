""" TASK 1:
The engineers are trying to figure out which reports are safe.
The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing.
So, a report only counts as safe if both of the following are true:

- The levels are either all increasing or all decreasing.
- Any two adjacent levels differ by at least one and at most three.

TASK 2:
The engineers are surprised by the low number of safe reports until they realize they forgot to tell you about the Problem Dampener.
The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in what
would otherwise be a safe report. It's like the bad level never happened!
Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe,
the report instead counts as safe.
"""


def read_report(p) -> list[list[int]]:
    """Read reports consisting of levels (elements) from file in form of list of lists of ints.

    :param p: Path to file.
    :return: Report of levels - a list of lists of ints.
    """
    report = []
    with open(p, "r") as f:
        for line in f:
            report.append([int(n) for n in line.split()])
    return report


def check_if_levels_increasing_decreasing(levels: list[int]) -> bool:
    """Check if levels (elements) are all increasing or decreasing within the list.

    :param levels: List of levels (elements) to check.
    :return: True if levels only increase or only decrease within report, False otherwise.
    """
    increasing = all(i < j for i, j in zip(levels, levels[1:]))
    decreasing = all(i > j for i, j in zip(levels, levels[1:]))
    return increasing or decreasing


def check_if_levels_differ_correctly(levels: list[int]) -> bool:
    """Check if levels (elements) differ by at least one and at most three within the list.

    :param levels: List of levels (elements) to check.
    :return: True if levels differ correctly within report, False otherwise.
    """
    for i in range(1, len(levels)):
        difference = abs(levels[i] - levels[i - 1])
        if difference > 3 or difference < 1:
            return False
    return True


def calculate_safe_reports(report_of_levels: list[list[int]]) -> int:
    """Check how many unsafe single reports are within report of levels.

    :param report_of_levels: List of reports of levels.
    :return: Number of unsafe reports.
    """
    safe_reports = 0
    for _, single_report in enumerate(report_of_levels):
        if check_if_report_is_safe(single_report):
            safe_reports += 1
        else:
            if thanos_snap_one_level(single_report):
                safe_reports += 1
    return safe_reports


def thanos_snap_one_level(problematic_report: list[int]) -> bool:
    """Remove singular level and check again the report.

    :param problematic_report: Report to be tested again with singular level removed, causing issues otherwise.
    :return: True if removing singular level made report safe, False otherwise.
    """
    for index, _ in enumerate(problematic_report):
        fixed_report = problematic_report.copy()
        del fixed_report[index]
        if check_if_report_is_safe(fixed_report):
            return True
    return False


def check_if_report_is_safe(single_report: list[int]) -> bool:
    """Check if single report is considered safe or unsafe.

    :param single_report: Report to be tested.
    :return: True if report is safe, False otherwise.
    """
    if check_if_levels_increasing_decreasing(single_report) and check_if_levels_differ_correctly(single_report):
        return True
    else:
        return False


if __name__ == "__main__":
    report_of_levels = read_report(r"data.txt")
    print(f"data: {report_of_levels}")
    print(f"Number of safe reports in data: {calculate_safe_reports(report_of_levels)}")

    report_of_levels = read_report(r"test_data.txt")
    print(f"test_data: {report_of_levels}")
    print(f"Number of safe reports in test data: {calculate_safe_reports(report_of_levels)}")
