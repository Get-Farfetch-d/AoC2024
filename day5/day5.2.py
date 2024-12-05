def read_file(p):
    """..."""
    with open(p, 'r') as file:
        data = file.read()
    rules, updates = data.split("\n\n")
    rules = rules.splitlines()
    updates = updates.splitlines()
    return rules, updates


def check_ordering(update_list):
    for element_index, element in enumerate(update_list):
        for index in range(element_index + 1, len(update_list)):
            if update_list[index] in rule_map and element in rule_map[update_list[index]]:
                return False
    return True


if __name__ == "__main__":
    rules, updates = read_file(r"data.txt")

    rule_map = {}

    for rule in rules:
        before, after = rule.split("|")
        if before not in rule_map:
            rule_map[before] = []
        rule_map[before].append(after)

    sum_of_middles = 0

    incorrectly_ordered = []
    for update in updates:
        update_list = update.split(",")
        middle_element = update_list[len(update_list) // 2]

        is_valid = True
        if not check_ordering(update_list):
            incorrectly_ordered.append(update_list)

    for update_list in incorrectly_ordered:
        correctly_ordered = []

        while not check_ordering(update_list):
            for element_index, element in enumerate(update_list):
                changed = False
                for index in range(element_index + 1, len(update_list)):
                    if update_list[index] in rule_map and element in rule_map[update_list[index]]:
                        update_list[index], update_list[element_index] = update_list[element_index], update_list[index]
                        changed = True
                        break
                if changed:
                    break

        sum_of_middles += int(update_list[len(update_list) // 2])



    print("Result: ", sum_of_middles)
