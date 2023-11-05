from collections import deque


def has_cycle(graph):
    visited = set()

    for node in graph:
        if node not in visited:
            queue = deque()
            queue.append((node, None))

            while queue:
                node, parent = queue.popleft()

                if node in visited:
                    return True

                visited.add(node)

                for neighbor in graph.get(node, []):
                    if neighbor != parent:
                        queue.append((neighbor, node))

    return False


def write_graph_to_file(graph):
    with open("input.txt", "w") as file:
        for node, neighbors in graph.items():
            file.write(f"{node} {' '.join(map(str, neighbors))}\n")


graph = {
    1: [2, 3, 4],
    2: [1, 5, 6],
    3: [1],
    4: [1, 7, 8],
    5: [2, 9, 10],
    6: [2, 10],
    7: [4, 11, 12],
    8: [4],
    9: [5],
    10: [5, 6],
    11: [7],
    12: [7]
}

# Запис графа у файл
write_graph_to_file(graph)


with open("output.txt", "w") as file:
    if has_cycle(graph):
        file.write("True")
    else:
        file.write("False")

