from collections import deque, defaultdict
import heapq

#i have made the graph as a dictionary where each key is a city and the value is a list of tuples (neighbor, cost)
graph = {
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Drobeta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)]
}

#heuristics (straight-line distances to Bucharest)
heuristics = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Drobeta': 242,
    'Eforie': 161,
    'Fagaras': 176,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 100,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}

#helper function to calculate the cost of a path
def calculate_path_cost(path):
    cost = 0
    for i in range(len(path) - 1):
        current_city = path[i]
        next_city = path[i + 1]
        # Find the cost between current city and next city
        for (neighbor, edge_cost) in graph[current_city]:
            if neighbor == next_city:
                cost += edge_cost
                break
    return cost

#breadth-First Search
def bfs(start, goal):
    queue = deque([(start, [start])])
    while queue:
        (node, path) = queue.popleft()
        for (neighbor, _) in graph[node]:
            if neighbor not in path:
                if neighbor == goal:
                    return path + [neighbor]
                else:
                    queue.append((neighbor, path + [neighbor]))
    return None

#uniform cost search
def ucs(start, goal):
    queue = [(0, start, [start])]
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node == goal:
            return path, cost
        for (neighbor, edge_cost) in graph[node]:
            if neighbor not in path:
                heapq.heappush(queue, (cost + edge_cost, neighbor, path + [neighbor]))
    return None, float('inf')

#greedy best-first search
def gbfs(start, goal):
    queue = [(heuristics[start], start, [start])]
    while queue:
        (_, node, path) = heapq.heappop(queue)
        if node == goal:
            return path
        for (neighbor, _) in graph[node]:
            if neighbor not in path:
                heapq.heappush(queue, (heuristics[neighbor], neighbor, path + [neighbor]))
    return None

#iterative deepening depth-first search
def iddfs(start, goal):
    depth = 0
    while True:
        result = dls(start, goal, depth)
        if result != "cutoff":
            return result
        depth += 1

def dls(node, goal, depth):
    if depth == 0 and node == goal:
        return [node]
    elif depth > 0:
        for (neighbor, _) in graph[node]:
            result = dls(neighbor, goal, depth - 1)
            if result != "cutoff":
                return [node] + result
    return "cutoff"

#i have used main function logic to compare the algorithms
def main():
    start = input("Enter the start city: ")
    goal = input("Enter the goal city: ")

    # BFS
    bfs_path = bfs(start, goal)
    if bfs_path:
        bfs_cost = calculate_path_cost(bfs_path)
        print(f"BFS Path: {bfs_path}, Cost: {bfs_cost}")
    else:
        print("BFS: No path found.")

    # UCS
    ucs_path, ucs_cost = ucs(start, goal)
    if ucs_path:
        print(f"UCS Path: {ucs_path}, Cost: {ucs_cost}")
    else:
        print("UCS: No path found.")

    # GBFS
    gbfs_path = gbfs(start, goal)
    if gbfs_path:
        gbfs_cost = calculate_path_cost(gbfs_path)
        print(f"GBFS Path: {gbfs_path}, Cost: {gbfs_cost}")
    else:
        print("GBFS: No path found.")

    # IDDFS
    iddfs_path = iddfs(start, goal)
    if iddfs_path and iddfs_path != "cutoff":
        iddfs_cost = calculate_path_cost(iddfs_path)
        print(f"IDDFS Path: {iddfs_path}, Cost: {iddfs_cost}")
    else:
        print("IDDFS: No path found.")

if __name__ == "__main__":
    main()
    
#the results are showing uniform cost search to perform the best in the scenario where ARAD is the start city and bucharest is the goal
