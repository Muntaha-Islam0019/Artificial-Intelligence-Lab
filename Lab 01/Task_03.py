# should have used text files before to reduce testing errors
# or maybe unit-testing, but i'm just learning the basics of unit-testing, hope to use them in later labs


def bfs(highest_land, predecessor):
    position_queue = []
    position_queue.insert(len(position_queue), predecessor)

    visit = [False]*int(lines[0])
    visit[predecessor] = True

    parents = ['null']*int(lines[0])

    while position_queue:
        v = position_queue.pop()
        for n in highest_land[v]:
            if visit[n] == False:
                position_queue.insert(len(position_queue), n)
                visit[n] = True
                parents[n] = v
    return parents


def shortest_path(parent, destination, predecessor):
    shortest_path = [destination]
    node = parent[destination]
    while predecessor != node:
        shortest_path.insert(len(shortest_path), node)
        node = parent[node]
    return shortest_path


shortest_path_list = []

if __name__ == '__main__':

    with open('Task_03.txt') as f:
        lines = [line.rstrip() for line in f]
    total_positions = int(lines[0])
    total_connections = int(lines[1])+2
    highest_land = [[] for i in range(total_positions)]
    for i in range(2, total_connections):
        u = int(lines[i].split(' ')[0])
        v = int(lines[i].split(' ')[1])
        highest_land[v].append(u)
    find = (bfs(highest_land, int(lines[int(lines[1])+2])))
    p = []
    for i in range(total_connections+2, int(lines[total_connections+1])+(total_connections+2)):
        p.append(len(shortest_path(find, int(lines[i]), int(lines[total_connections]))))
    print(min(p))
