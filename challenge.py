from collections import defaultdict

def challenge(file_path):
    # Part 1: Set up an adjacency list
    n = None
    graph = defaultdict(set)

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if not n:
                n = int(line)
                continue

            u, v = line.split()
            graph[int(u)].add(int(v))
            graph[int(v)].add(int(u))


    # Part 2: Count connected components
    visited = [False] * n
    counter = 0

    def dfs(node):
        stk = [node]
        while len(stk) > 0:
            curr = stk.pop()

            for neighbor in graph[curr]:
                if not visited[neighbor]:
                    stk.append(neighbor)
                    visited[neighbor] = True

    for node in range(n):
        if not visited[node]:
            visited[node] = True
            counter += 1
            dfs(node)
        

challenge('sample_input/s1.txt')