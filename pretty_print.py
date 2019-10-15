class BinTree:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right


def print_tree(B):
    print_tree_interval([B], 1, max_level_compute(B))


def print_tree_interval(L, level, max_level):
    if len(L) == 0 or are_all_elements_none(L):
        return

    floor = max_level - level
    edge_lines = 2 ** (max(floor - 1, 0))
    first_spaces = 2 ** floor - 1
    between_spaces = 2 ** (floor + 1) - 1

    print_white_spaces(first_spaces)

    L2 = []
    for B in L:
        if B is not None:
            print(B.key, end='')
            L2.append(B.left)
            L2.append(B.right)
        else:
            L2.append(None)
            L2.append(None)
            print(' ', end='')

        print_white_spaces(between_spaces)

    print()

    for i in range(1, edge_lines + 1):
        for j in range(len(L)):
            print_white_spaces(first_spaces - i)

            if L[j] is None:
                print_white_spaces(edge_lines + edge_lines + i + 1)
                continue

            if L[j].left is not None:
                print('/', end='')
            else:
                print_white_spaces(1)

            print_white_spaces(i + i - 1)

            if L[j].right is not None:
                print('\\', end='')
            else:
                print_white_spaces(1)

            print_white_spaces(edge_lines + edge_lines - i)

        print()

    print_tree_interval(L2, level + 1, max_level)


def print_white_spaces(count):
    for i in range(count):
        print(' ', end='')


def max_level_compute(B):
    if B is None:
        return 0
    return max(max_level_compute(B.left), max_level_compute(B.right)) + 1


def are_all_elements_none(L):
    for B in L:
        if B is not None:
            return False
    return True
