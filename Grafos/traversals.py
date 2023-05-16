# -*- coding: utf-8 -*-

from graph2 import Graph
import sys

class Graph2(Graph):
    """ Graph2 is a Graph's subclass. In this class,
    we will implement the breadth-first and depth-first traversals
    """ 
    def bfs(self) -> None:
        """This function prints all vertices of 
        the graph by BFS traversal"""
        print('bfs traversal:')
        # Mark all the vertices as not visited 
        visited_vertex = {}
        for vertex in self._vertices.keys():
            visited_vertex[vertex] = False

        for vertex in self._vertices.keys():
            if not visited_vertex[vertex]:
                self._bfs(vertex, visited_vertex)

    def _bfs(self, vertex: object, visited_vertex: dict) -> None:
        """This function prints the BFS traversal from the vertex
        whose index is indexV."""
        
        # Create a list for BFS.
        # It will save the indices of vertices to visit
        queue = [] 
        # mark the source vertex as visited
        visited_vertex[vertex] = True
        # and enqueue it 
        queue.append(vertex)
        
        while queue: 
            # Dequeue an index from queue and print its corresponding vertex(label)
            s = queue.pop(0) 
            # print (s, end = " ")
            # we print the vertex, so we need to get its label
            print(s, end=" ")

            # Get all adjacent vertices of the dequeued index. 
            # If an adjacent vertex has not been visited, 
            # then mark it visited and enqueue it 
            for adj in self._vertices[s]: 
                if not visited_vertex[adj.vertex]:
                    queue.append(adj.vertex)
                    visited_vertex[adj.vertex] = True

    def dfs(self):
        """This function prints all vertices of the graph
        by the DFS traversal."""

        print('dfs traversal:')
        # Mark all the vertices as not visited
        visited_vertex = {}
        for vertex in self._vertices.keys():
            visited_vertex[vertex] = False

        for vertex in self._vertices.keys():
            if not visited_vertex[vertex]:
                self._dfs(vertex, visited_vertex)
                # self._dfs_iterative(vertex, visited_vertex)

    def _dfs_iterative(self, vertex: object, visited_vertex: dict) -> None:
        # we use a list as a stack. We add and remove always from the end (peak) of the list.
        stack = [vertex]
        # mark the source vertex as visited
        visited_vertex[vertex] = True

        while len(stack) > 0:
            # remove the last added
            s = stack.pop()
            # print (s, end = " ")
            # we print the vertex, so we need to get its label
            print(s, end=" ")

            # Get all adjacent vertices of the dequeued index.
            # If an adjacent vertex has not been visited,
            # then mark it visited and enqueue it
            for adj in reversed(self._vertices[s]):
                # print(adj)
                if not visited_vertex[adj.vertex]:
                    # we add at the end (peak) of the stack
                    stack.append(adj.vertex)
                    visited_vertex[adj.vertex] = True

    def _dfs(self, vertex: object, visited_vertex: dict) -> None:
        """This function prints the DFS traversal
        from the vertex whose index is indexV"""
        # Mark the current node as visited and print it
        visited_vertex[vertex] = True
        # print(vertex, end = ' ')
        # Instead of printing the index, we have to print its label
        #print(vertex, end=' ')
        # Recur for all the vertices  adjacent to this vertex
        for adj in self._vertices[vertex]:
            if not visited_vertex[adj.vertex]:
                # self._dfs(adj.vertex, visited_vertex)
                self._dfs(adj.vertex, visited_vertex)



    def non_accessible(self, vertex) ->list:
        acc=[]
        visited={}

        for v in self._vertices:
            visited[v]=False

        self._dfs(vertex,visited)
        
        for v in self._vertices:
            if visited[v]==False:
                acc.append(v)

        return acc
    

    def get_reachable(self, vertex) -> list:
        acc=[]
        visited={}

        for v in self._vertices:
            visited[v]=False

        self._dfs(vertex,visited)
        
        for v in self._vertices:
            if visited[v] and v!=vertex:
                acc.append(v)

        return acc
    
        
    def is_connected(self) -> bool:

        outcome=True
        visited={}
        for v in self._vertices:
            visited[v]=False


        x=list(self._vertices.keys())[0]
        self._dfs(x, visited)

        for v in self._vertices:
            if visited[v]==False:
                outcome=False
        
        return outcome

        
    def is_bridge(self, vertex_u, vertex_v)->bool:


        
        if vertex_u not in self._vertices:
            return "u is not a vertex"

        if vertex_v not in self._vertices:
            return "v is not a vertex"

        if vertex_v ==vertex_u:
            return "is the same vertex!"
        
        if vertex_u not in self._vertices[vertex_v]:
            return "no edge!"
        
        self.remove_edge(vertex_v, vertex_u)

        if self.is_connected():
            outcome= False
        else:
            outcome= True
        
        self.add_edge(vertex_v, vertex_u)
        return outcome
    
      
    def minDist(self, visited, distances):
        
        min=sys.maxsize
        

        for i in self._vertices:
            n=i._vertex

            if visited[n]==False and distances[n] <= min:
                min=distances[n]
                outcome=i

        return outcome



    def minPath(self, start, end)->list:

        if start not in self._vertices:
            return []
        
        if end not in self._vertices:
            return []
        
        previous={}
        distances={}
        visited={}


        for v in self._vertices:
            previous[v]=None
            distances[v]=sys.maxsize()
            visited[v]=False

        #marcamos origen 
        distances[start]=0

        for n in range (len(self._vertices)):

            u=self.minDist(visited, distances)

            for adj in self._vertices[u]



            for x in self._vertices[start]











if __name__ == '__main__':
    # Now, we use the implementation to represent and traverse this graph:
    # <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/CPT-Graphs-directed-weighted-ex1.svg/722px-CPT-Graphs-directed-weighted-ex1.svg.png' width='25%'/>


    '''
    labels = ['A', 'B', 'C', 'D', 'E']

    g = Graph2(labels)

    # Now, we add the edges
    g.add_edge('A', 'C', 12)  # A->(12)C
    g.add_edge('A', 'D', 60)  # A->(60)D
    g.add_edge('B', 'A', 10)  # B->(10)A
    g.add_edge('C', 'B', 20)  # C->(20)B
    g.add_edge('C', 'D', 32)  # C->(32)D
    g.add_edge('E', 'A', 7)   # E->(7)A


    
    g.bfs()
    print()

    label = 'C'
    # Mark all the vertices as not visited 
    visited = {}
    for v in labels:
        visited[v] = False

    print('bfs traversal from ', label)
    # we have to pass the index of the vertex
    g._bfs(label, visited)
    print()

    label = 'E'
    visited = {}
    for v in labels:
        visited[v] = False
    print('bfs traversal from ', label)
    # we have to pass the index of the vertex
    g._bfs(label, visited)

    # We use the implementation to represent an undirected graph without weights :
    # <img src='https://computersciencesource.files.wordpress.com/2010/05/dfs_1.png' width='35%'/>

    labels = ['A', 'B', 'C', 'D', 'E']
    g = Graph2(labels, False)
    g.add_edge('A', 'B')  # A:0, B:1
    g.add_edge('A', 'C')  # A:0, C:2
    g.add_edge('A', 'E')  # A:0, E:5
    g.add_edge('B', 'D')  # B:1, D:4
    g.add_edge('B', 'E')  # C:2, B:1
    # g.add_edge('A','H',8)

    print(g)

    


    print('bfs traversal from A (A is the first vertex):')
    g.bfs()
    print()
    label = 'E'
    visited = {}
    for v in labels:
        visited[v] = False
    print('bfs traversal from ', label)
    # we have to pass the index of the vertex
    g._bfs(label, visited)

    # we use this dictionary to represent the vertices with numbers:
    labels = ['A', 'B', 'C', 'D', 'E']
    g = Graph2(labels)

    # Now, we add the edges
    g.add_edge('A', 'C', 12)  # A->(12)C
    g.add_edge('A', 'D', 60)  # A->(60)D
    g.add_edge('B', 'A', 10)  # B->(10)A
    g.add_edge('C', 'B', 20)  # C->(20)B
    g.add_edge('C', 'D', 32)  # C->(32)D
    g.add_edge('E', 'A', 7)  # E->(7)A

    print(g)
    print()

    g.dfs()
    print()
    print()

    for origin in g._vertices.keys():
        visited = {}
        for v in labels:
            visited[v] = False
        print('dfs traversal from ', origin)
        g._dfs(origin, visited)

        visited = {}
        for v in labels:
            visited[v] = False

        print('\ndfs (iterative) traversal from ', origin)
        g._dfs_iterative(origin, visited)
        print('\n\n')


    '''



    vlabels=['A', 'B', 'C', 'D', 'E']
    z=Graph2(vlabels)

    z.add_edge('A','B')
    #z.add_edge('B','A')

    z.add_edge('B','C')
    z.add_edge('C','B')

    z.add_edge('C','E')
    z.add_edge('E','C')

    z.add_edge('A','E')
    z.add_edge('E','A')


    print(z)

    
    print(z.get_reachable('E'))
    print("Is connected: ", z.is_connected())


    print(list(z._vertices['A']))
    print (z.is_bridge('B','A'))