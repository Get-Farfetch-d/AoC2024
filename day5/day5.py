def read_file(p):
    """..."""
    with open(p, 'r') as file:
        data = file.read()
    rules, updates = data.split("\n\n")
    rules = rules.splitlines()
    updates = updates.splitlines()
    return rules, updates


if __name__ == "__main__":
    # report = read_file(r"data.txt")
    # print(f"data: {report}")

    rules, updates = read_file(r"data.txt")
    print("rules: ", rules)
    print("updates: ", updates)

    rule_map = {}

    for rule in rules:
        before, after = rule.split("|")
        if before not in rule_map:
            rule_map[before] = []
        rule_map[before].append(after)

    print("Rule map: ", rule_map)

    sum_of_middles = 0
    for update in updates:
        update_list = update.split(",")
        middle_element = update_list[len(update_list) // 2]
        print("Update: ", update_list, "Middle: ", middle_element)

        is_valid = True
        for element_index, element in enumerate(update_list):

            for index in range(element_index + 1, len(update_list)):
                if element in rule_map and update_list[index] in rule_map[element]:
                    # Ok
                    pass
                if update_list[index] in rule_map and element in rule_map[update_list[index]]:
                    is_valid = False
                    break
            if not is_valid:
                break

        if is_valid:
            sum_of_middles += int(middle_element)

    print("Result: ", sum_of_middles)
