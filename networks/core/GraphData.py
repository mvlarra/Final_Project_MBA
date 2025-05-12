import pandas as pd
from abc import ABC, abstractmethod
from .Graph import GraphInterface, Graph


class GraphDataInterface(ABC):
    def __init__(
        self, df_edges: pd.DataFrame, col_source: str, col_target: str
    ):
        self.df_edges = df_edges
        self.col_source = col_source
        self.col_target = col_target
    
    @abstractmethod
    def get_graph_layout(self) -> pd.DataFrame:
        pass
    
    @abstractmethod
    def get_nodes_features(self) -> pd.DataFrame:
        pass


class GraphData(GraphDataInterface):
    def __init__(
        self, df_edges, col_source, col_target, graph: GraphInterface = Graph
    ):
        self.df_edges = df_edges.copy()
        self.col_source = col_source
        self.col_target = col_target
        self.graph = graph()
    
    def get_graph_layout(self, layout='random'):
        graph = self.graph.create_graph(
            self.df_edges, self.col_source, self.col_target
        )
        graph_layout = self.graph.create_graph_layout(graph, layout)
        
        return graph_layout
    
    def get_nodes_features(self, graph_layout=None):
        edges = self.df_edges[[self.col_source, self.col_target]].copy()
        
        # Out and In edges counts
        out_edges = edges['antecedents'].value_counts().rename('out_edges')
        in_edges = edges['consequents'].value_counts().rename('in_edges')
        
        # Remove duplicate rows to count adjacent nodes
        set_items = edges[[self.col_source,
                           self.col_target]].apply(lambda x: sorted(x), axis=1)
        clean_edges = edges.loc[~set_items.duplicated(),
                                [self.col_source, self.col_target]]
        node_counts = clean_edges.melt(value_name='nodes'
                                      )['nodes'].value_counts()
        node_counts = node_counts.rename('adjacent_edges').reset_index()
        
        # Find nodes with mutual edges
        mutual_edges = set_items.value_counts().to_frame().query('count == 2')
        mutual_edges = mutual_edges.assign(
            antecedents=lambda x: x.index.map(lambda y: y[0]),
            consequents=lambda x: x.index.map(lambda y: y[1])
        ).reset_index(drop=True)
        mutual_edges = mutual_edges.melt(value_name='nodes'
                                        )['nodes'].value_counts()
        mutual_edges = mutual_edges.rename('mutual_edges').reset_index()
        
        # Merge ALL
        node_counts = node_counts.merge(
            out_edges, left_on='nodes', right_index=True, how='left'
        )
        node_counts = node_counts.merge(
            in_edges, left_on='nodes', right_index=True, how='left'
        )
        node_counts = node_counts.merge(mutual_edges, on='nodes', how='left')
        
        # Make it clean
        df_nodes = node_counts.rename(columns={'index': 'nodes'}).fillna(0)
        
        if graph_layout is not None:
            df_nodes = df_nodes.merge(
                graph_layout, left_on="nodes", right_index=True
            )
            df_nodes = df_nodes.rename({0: "x", 1: "y"}, axis=1)
        
        return df_nodes
