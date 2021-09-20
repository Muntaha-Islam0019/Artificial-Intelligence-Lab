from collections import defaultdict

# using default dict instead of dict to eleminate keyError
# dict to save paths
highland = defaultdict(list)


def bfs(highland, initial_position, destination):
    explored_positions = []
    position_queue = [[initial_position]]

    if initial_position == destination:
        print("0")
        return

    while position_queue:
        # print("queue", position_queue)

        path = position_queue.pop(0)
        # print("path", path)
        current_position = path[-1]
        # print("current", current_position)

        # print("exploxed", explored_positions)

        if current_position not in explored_positions:
            adjacent_positions = highland[current_position]

            for a_position in adjacent_positions:
                new_path = list(path)
                new_path.append(a_position)
                position_queue.append(new_path)

                if a_position == destination:
                    return print(len(new_path) - 1)

            explored_positions.append(current_position)

    return


def connection(u, v):
    highland[str(u)].append(str(v))
    highland[str(v)].append(str(u))


if __name__ == '__main__':

    number_of_fixed_positions = int(input())
    number_of_connections = int(input())

    for i in range(number_of_connections):
        edges = input().split()
        connection(edges[0], edges[1])

    linas_position = input()
    noras_position = input()
    laras_position = input()


    if bfs(highland, laras_position, linas_position) < bfs(highland, noras_position, linas_position):
        print('Lara')
    elif bfs(highland, laras_position, linas_position) > bfs(highland, noras_position, linas_position):
        print('Nora')
    else:
        print("It'll end in a tie")