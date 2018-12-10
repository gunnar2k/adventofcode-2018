input = open("input.txt")
graph = {}
for line in input:
    line = line.strip()
    line = line.replace("Step ", "")
    line = line.replace(" must be finished before step ", "")
    line = line.replace(" can begin.", "")

    first = line[0]
    second = line[1]

    if first not in graph.keys():
        graph[first] = []

    if second not in graph.keys():
        graph[second] = []

    graph[second].append(first)

answer = []
while len(graph.keys()) != 0:
    emptys = filter(lambda x: len(graph[x]) == 0, graph.keys())
    emptys.sort()
    first = emptys[0]
    answer.append(first)
    for x in graph:
        if first in graph[x]:
            graph[x] = [value for value in graph[x] if value != first]
    del graph[first]

print("".join(answer))
