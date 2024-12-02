"""The engineers are surprised by the low number of safe reports until they realize they forgot to tell you about the Problem Dampener.
The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in what
would otherwise be a safe report. It's like the bad level never happened!
Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe,
the report instead counts as safe.
"""
import day2


if __name__ == "__main__":
    report_of_levels = day2.read_report(r"data.txt")
    print(f"data: {report_of_levels}")

    report_of_levels = day2.read_report(r"test_data.txt")
    print(f"test_data: {report_of_levels}")

