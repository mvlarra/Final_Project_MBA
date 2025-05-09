import pandas as pd

from .core.Graph import GraphInterface, Graph
from .core.GraphData import GraphDataInterface, GraphData


class RulesGraphManager:
    def __init__(
        self,
        rules,
        col_source='antecedents',
        col_target='consequents',
        graph_data: GraphDataInterface = GraphData,
        graph: GraphInterface = Graph
    ):
        self.rules = rules.copy()
        self.col_source = col_source
        self.col_target = col_target
        
        self.graph_data = graph_data(rules, col_source, col_target, graph)
    
    def get_graph_features(self, graph_layout: str = None):
        """
        return df_nodes, df_edges
        
        """
        if graph_layout is not None:
            graph_layout = self.graph_data.get_graph_layout(graph_layout)
        
        df_nodes = self.graph_data.get_nodes_features(graph_layout)
        df_nodes = self._get_support_from_edges(df_nodes)
        
        # add edges column as combination of source -> target
        df_edges = self.rules.copy()
        df_edges['edges'] = df_edges[self.col_source
                                    ] + ' -> ' + df_edges[self.col_target]
        
        return df_nodes, df_edges
    
    def get_nodes_neighbors(
        self, df_nodes, neighbors_type='adjacent_edges', col_node='nodes'
    ):
        """
        neighbors_type: out_edges | in_edges | mutual_edges | adjacent_edges
        """
        
        df_edges = self.rules.copy()
        df_nodes = df_nodes.copy()
        
        if neighbors_type == 'out_edges':
            df_nodes['neighbors'] = df_nodes[col_node].map(
                lambda x: set(
                    [x] + df_edges[df_edges[self.col_source] == x][
                        self.col_target].to_list()
                )
            )
        elif neighbors_type == 'in_edges':
            df_nodes['neighbors'] = df_nodes[col_node].map(
                lambda x: set(
                    [x] + df_edges[df_edges[self.col_target] == x][
                        self.col_source].to_list()
                )
            )
        elif neighbors_type == 'mutual_edges':
            df_nodes['neighbors'] = df_nodes[col_node].map(
                lambda x: set(
                    [x] + list(
                        set(
                            df_edges[df_edges[self.col_source] == x][self.
                                                                     col_target]
                        ).intersection(
                            df_edges[df_edges[self.col_target] == x][self.
                                                                     col_source]
                        )
                    )
                )
            )
        else:  # get all adjacent nodes
            df_nodes['neighbors'] = df_nodes[col_node].map(
                lambda x: set(
                    [x] + df_edges[df_edges[self.col_source] == x][
                        self.col_target].to_list() + df_edges[df_edges[
                            self.col_target] == x][self.col_source].to_list()
                )
            )
        
        return df_nodes
    
    def _get_support_from_edges(self, df_nodes):
        df_nodes = df_nodes.copy()
        nodes = self.rules[['antecedents',
                            'consequents']].melt(value_name='nodes')
        support = self.rules[['antecedent support',
                              'consequent support']].melt(value_name='support')
        nodes_support = pd.concat([nodes, support],
                                  axis=1).drop(columns='variable')
        nodes_support = nodes_support.drop_duplicates(subset='nodes')
        
        return df_nodes.merge(nodes_support, on='nodes', how='inner')
