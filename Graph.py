import networkx as nx
import matplotlib.pyplot as plt
import heapq


class Graf:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, node1, node2, weight):
        if node1 in self.nodes and node2 in self.nodes:
            if not any(
                ([node1, node2] in x or [node2, node1] in x) for x in self.edges
            ):
                self.edges.append([[node1, node2], weight])

    def visualize_graph(self):
        G = nx.Graph()
        for edge in self.edges:
            G.add_edge(edge[0][0], edge[0][1], weight=edge[1])

        pos = nx.spring_layout(G, seed=7)
        nx.draw_networkx_nodes(G, pos, node_size=500, node_color="#86ceeb")
        nx.draw_networkx_edges(G, pos, edgelist=G.edges, width=1)
        nx.draw_networkx_labels(G, pos, font_size=7, font_family="sans-serif")
        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels)
        plt.axis("off")
        plt.tight_layout()
        plt.show()

    def shortest_path(self, start, end, willReturn=False):
        distances = {node: float("inf") for node in self.nodes}
        distances[start] = 0
        prev_nodes = {node: None for node in self.nodes}
        pq = [(0, start)]
        while pq:
            current_distance, current_node = heapq.heappop(pq)
            if current_distance > distances[current_node]:
                continue
            for edge in self.edges:
                node1, node2 = edge[0]
                weight = edge[1]
                if node1 == current_node or node2 == current_node:
                    neighbor = node2 if current_node == node1 else node1
                    new_distance = current_distance + weight
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        prev_nodes[neighbor] = current_node
                        heapq.heappush(pq, (new_distance, neighbor))
        path = []
        current = end
        while current is not None:
            path.insert(0, current)
            current = prev_nodes[current]
        if distances[end] < float("inf"):
            if not willReturn: print(f"{path}")
            return path
        else:
            print("No Path Found!")
            return []

    def visual_shortest_path(self, start, end):
        shortest_path = self.shortest_path(start, end, True)
        shortest_edges = []
        for i in range(0, len(shortest_path)-1):
            shortest_edges.append([shortest_path[i], shortest_path[i+1]])
        
        G = nx.Graph()
        for edge in self.edges:
            G.add_edge(edge[0][0], edge[0][1], weight=edge[1])

        pos = nx.spring_layout(G, seed=7)
        nx.draw_networkx_nodes(G, pos, node_size=500, node_color="#86ceeb")
        nx.draw_networkx_edges(G, pos, edgelist=G.edges, width=1)
        nx.draw_networkx_edges(G, pos, edgelist=shortest_edges, width=1, edge_color="#ff3d3d")
        nx.draw_networkx_labels(G, pos, font_size=7, font_family="sans-serif")
        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels)
        plt.axis("off")
        plt.tight_layout()
        plt.show()
