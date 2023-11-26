def set_cover_problem(N, B, preferences):
    graph = {beer: set() for beer in range(B)}
    for beer in range(B):
        for i, pref in enumerate(preferences):
            if pref[beer] == 'Y':
                graph[beer].add(i)

    all_beers = set(graph.keys())
    selected_beers = set()
    uncovered_employees = set(range(N))

    while uncovered_employees:
        best_beer = max(all_beers, key=lambda beer: len(uncovered_employees & graph[beer]))
        selected_beers.add(best_beer)
        uncovered_employees -= graph[best_beer]

    return len(selected_beers)


with open('input.txt', 'r') as file:
    N, B = map(int, file.readline().split())
    preferences_str = file.readline().split()
    preferences = [list(string) for string in preferences_str]


result = set_cover_problem(N, B, preferences)

print(str(result))
with open('output.txt', 'w') as file:
    file.write(str(result))

