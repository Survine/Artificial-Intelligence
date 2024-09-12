def bfs(graph, start_node):  # Function for BFS
    
    visited = []  # List for visited nodes
    queue = []    # Initialize a queue

    visited.append(start_node)
    queue.append(start_node)

    while queue:  # Creating loop to visit each node
        current_node = queue.pop(0)
        print(current_node, end=" ")

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

# Driver Code
graph = {
    '1': ['2', '3'],
    '2': ['4'],
    '3': ['4', '7'],
    '4': ['5', '6'],
    '7': [],
    '5': [],
    '6': []
}

print("BFS Traversal:")
bfs(graph, '1')  # Function calling starting from node 1
