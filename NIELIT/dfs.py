graph = {
    "You": ["Akash", "Saurabh"],
    "Akash": ["Ritesh", "Bablu"],
    "Saurabh": ["Vipul"],
    "Ritesh": [],
    "Bablu": [],
    "Vipul": []
}

def dfs(graph, node, goal, visited=None):
    if visited is None:
        visited = set()

    print(node, end="")  # Print the current node
    visited.add(node)

    if node == goal:
        print("\nFound:", goal)
        return True  # Stop searching when goal is found

    for friend in graph[node]:
        print("Checked: ", friend)
        if friend not in visited:
            if dfs(graph, friend, goal, visited):  # Recursively search deeper
                return True  # Stop searching once goal is found

    return False  # If goal is not found

print("DFS Traversal")
dfs(graph, "You", "Vipul")
