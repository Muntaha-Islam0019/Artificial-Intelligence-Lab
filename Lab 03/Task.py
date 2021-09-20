import numpy as np

minimum = - np.inf
maximum = np.inf


def func_a_b(depth, node, max_player, value, a, b):

    if depth == 3:
        return value[node]

    if max_player:

        best_val = minimum

        for i in range(0, 2):
            value = func_a_b(depth + 1, node * 2 + i, False, value, a, b)
            best_val = max(best_val, value)
            a = max(a, best_val)
            if b <= a:
                break
        return best_val

    else:
        best_val = maximum
        for i in range(0, 2):
            value = func_a_b(depth + 1, node * 2 + i, True, value, a, b)
            best_val = min(best_val, value)
            b = min(b, best_val)
            if b <= a:
                break
        return best_val


score = []
x = int(input("Enter the number of leaf node: "))

for i in range(x):
    y = int(input("Enter the node value: "))
    score.append(y)

if __name__ == "main":

    print("After pruning: ", func_a_b(
        3, 2, True, score, minimum, maximum))
