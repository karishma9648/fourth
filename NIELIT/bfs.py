from collections import deque

graph = {
    "You": ["Akash", "Saurabh"],
    "Akash":["Ritesh", "Bablu"],
    "Saurabh":["Vipul"],
    "Ritesh":[],
    "Bablu":[],
    "Vipul":[]
}

def bfs(graph, start, goal):
    queue = deque([start])
    visited = set()
    visited.add(start)
    
    while queue:
        person = queue.popleft()
        print(person, end="")
        
        if person == goal:
            print("\n found:", goal)
            return
        
        for friend in graph[person]:
            if friend not in visited:
                visited.add(friend)
                queue.append(friend)
                
print("BFS Traversal")
bfs(graph, "You", "Bablu")