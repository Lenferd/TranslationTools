def print_if_i(iteration, need_iteration, value):
    if iteration == need_iteration:
        print(value)


def print_list(lists):
    for line in lists:
        print(line)


def print_lists_of_list(lists):
    for inlist in lists:
        print("=== New List ===")
        for line in inlist:
            print(line)
