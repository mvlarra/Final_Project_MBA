import numpy as np
import pandas as pd

from collections import deque

from .RulesGraphManager import RulesGraphManager


class ProductNetwork:
    def __init__(
        self,
        rules,
        col_source='antecedents',
        col_target='consequents',
        RulesGraphManager=RulesGraphManager
    ):
        self.rules = rules.copy()
        self.col_source = col_source
        self.col_target = col_target
        self.RulesGraphManager = RulesGraphManager
    
    def get_bfs_rules(
        self,
        products: list,
        metric='support',
        threshold=0,
        max_depth=3,
        top_n=5
    ):
        """
        return df_bfs, rules_bfs
        """
        df_bfs = ProductNetwork.bfs_complete(
            self.rules, products, metric, threshold, max_depth, top_n
        )
        rules_bfs = self.rules[self.rules[self.col_source].isin(
            df_bfs['nodes']
        )].copy()
        
        return df_bfs, rules_bfs
    
    def get_graph_features(self, df_bfs, rules_bfs, strict_rules=False):
        """
        return df_nodes, df_edges
        """
        
        MyRGM = self.RulesGraphManager(rules_bfs)
        df_nodes, df_edges = MyRGM.get_graph_features()
        
        df_nodes = df_nodes.merge(
            df_bfs.drop_duplicates(subset='nodes'), on='nodes', how='right'
        )
        df_nodes['depth'] = df_nodes['depth'].map(lambda x: f"depth {x}")
        
        df_edges['rank'] = np.nan
        selected_rules = set()
        for idx, row in df_nodes.iterrows():
            mask = df_edges['antecedents'] == row['parent']
            mask &= df_edges['consequents'] == row['nodes']
            if any(mask):
                edges_idx = mask.idxmax()
                selected_rules.add(edges_idx)
                df_edges.at[edges_idx, 'rank'] = row['rank']
        
        if strict_rules:
            df_edges = df_edges.loc[list(selected_rules)]
        
        return df_nodes, df_edges
    
    @staticmethod
    def bfs(rules, nodes, metric='support', max_depth=3, top_n=5):
        """
        return [(node_name:str, depth:int, parent_node)]
        """
        
        queue = deque()
        for node_to_visit in nodes:
            queue.extend([(node_to_visit, 0, node_to_visit)])
        
        visited_nodes = set()
        results = []
        listed_nodes = []
        
        while queue:
            current_node, depth, parent_node = queue.popleft()
            
            if current_node in visited_nodes:
                continue
            
            if depth > max_depth:
                break
            
            visited_nodes.add(current_node)
            results.append((current_node, depth, parent_node))
            
            rules_consequents = rules.loc[rules['antecedents'] ==
                                          current_node, :]
            rules_consequents = rules_consequents.loc[
                ~rules_consequents['consequents'].isin(listed_nodes), :]
            rules_consequents = rules_consequents.sort_values(
                metric, ascending=False
            )
            consequents = rules_consequents['consequents'].tolist()
            
            listed_nodes.extend(consequents)
            if top_n > 0:
                valid_nodes = consequents[:top_n]
            else:
                valid_nodes = consequents
            
            queue.extend(
                (node, depth + 1, current_node) for node in valid_nodes
            )
        
        df_bfs = pd.DataFrame(results, columns=['nodes', 'depth', 'parent'])
        
        return df_bfs
    
    @staticmethod
    def bfs_complete(
        rules, nodes, metric='support', threshold=0, max_depth=3, top_n=5
    ):
        """
        columns description
        edges_value: (parent -> child) edges [metric] value
        
        return [(rank, depth, node_name, parent_node, edges_value, edges_values, rank_edges, route)]
        """
        
        queue = deque()
        for node in nodes:  # initialize
            root_node = node
            queue.extend([(0, node, '', root_node, 0, [0], [0], [node])])
        
        visited_nodes = set()
        results = []
        listed_nodes = []
        current_rank = 0
        
        while queue:
            depth, node, parent_node, root_node, edges_value, edges_values, rank_edges, route = queue.popleft(
            )
            
            if depth > max_depth:
                break
            
            if node in visited_nodes:
                continue
            
            if node not in nodes:
                current_rank += 1
            
            visited_nodes.add(node)
            results.append(
                (
                    current_rank, depth, node, parent_node, root_node,
                    edges_value, edges_values, rank_edges, route
                )
            )
            
            current_rules = rules.loc[rules['antecedents'] == node]
            
            invalid_nodes = current_rules['consequents'].isin(listed_nodes)
            current_rules = current_rules.loc[~invalid_nodes]
            
            valid_value = current_rules[metric] >= threshold
            current_rules = current_rules.loc[valid_value]
            
            current_rules = current_rules.sort_values(metric,
                                                      ascending=False).copy()
            consequents = current_rules['consequents'].tolist()
            
            if top_n > 0:
                valid_consequents = consequents[:top_n]
            else:
                valid_consequents = consequents
            listed_nodes.extend(valid_consequents)
            
            # get antecedent - > consequent (parent -> child) edges value
            new_edges_values = {}
            for child_node in valid_consequents:
                mask = current_rules['antecedents'] == node
                mask &= current_rules['consequents'] == child_node
                if mask.empty:
                    new_edges_values[child_node] = 0
                else:
                    new_edges_value = current_rules.at[mask.idxmax(), metric]
                    new_edges_values[child_node] = (round(new_edges_value, 3))
            
            queue.extend(
                (
                    depth + 1, child_node, node, root_node, new_edges_value,
                    edges_values + [new_edges_value], rank_edges + [rank],
                    route + [child_node]
                ) for rank, (child_node, new_edges_value
                            ) in enumerate(new_edges_values.items(), 1)
            )
        
        df_bfs = pd.DataFrame(
            results,
            columns=[
                'rank', 'depth', 'nodes', 'parent', 'root', f'edges_{metric}',
                f'edges_route_{metric}', 'rank_edges', 'route'
            ]
        )
        
        return df_bfs
