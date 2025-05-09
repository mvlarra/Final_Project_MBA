from abc import ABC, abstractmethod

import networkx as nx
import pandas as pd


class GraphInterface(ABC):
    @staticmethod
    @abstractmethod
    def create_graph(
        df_edges: pd.DataFrame, col_source: str, col_target: str
    ) -> nx.Graph:
        pass
    
    @staticmethod
    @abstractmethod
    def create_graph_layout(
        graph: nx.Graph, layout: str = "random"
    ) -> pd.DataFrame:
        pass


class Graph(GraphInterface):
    LAYOUTS = [
        "Random", "Spring", "Shell", "Kamada Kawai", "Spectral", "Circular",
        "Spiral"
    ]
    
    @staticmethod
    def create_graph(df_edges, col_source, col_target):
        graph = nx.Graph()
        
        sources = df_edges[col_source].values
        targets = df_edges[col_target].values
        
        for idx in range(len(sources)):
            graph.add_nodes_from([sources[idx]])  # Add antecedent node
            graph.add_nodes_from([targets[idx]])  # Add consequent node
            
            graph.add_edge(sources[idx], targets[idx], weight=1)
            graph.add_edge(targets[idx], sources[idx], weight=1)
        
        return graph
    
    @staticmethod
    def create_graph_layout(graph, layout="random"):
        layout = layout.lower()  # Convert to lowercase for case-insensitivity
        
        layouts = {
            "random": nx.random_layout(graph),
            "spring": nx.spring_layout(graph, k=0.5, iterations=50),
            "shell": nx.shell_layout(graph),
            "kamada kawai": nx.kamada_kawai_layout(graph),
            "spectral": nx.spectral_layout(graph),
            "circular": nx.circular_layout(graph),
            "spiral": nx.spiral_layout(graph),
        }
        
        graph_layout = pd.DataFrame(layouts[layout]).T
        
        return graph_layout
