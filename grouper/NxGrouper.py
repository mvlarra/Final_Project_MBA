import networkx as nx


class NxGrouper:
    @staticmethod
    def greedy_modularity_communities(
        df_nodes,
        df_edges,
        min_member=4,
        resolution=3,
        get_leader_by='adjacent_edges'
    ):
        """
        nx.community.greedy_modularity_communities
        to find the community partition with the largest modularity.
        resolution: If resolution is less than 1, modularity favors larger communities.
        
        Required df_nodes columns: 'nodes'
        Required df_edges columns: 'antecedents', 'consequents'
        """
        df_nodes = df_nodes.copy()
        
        dG = nx.from_pandas_edgelist(
            df_edges,
            source='antecedents',
            target='consequents',
            create_using=nx.DiGraph()
        )
        groups = list(
            nx.community.greedy_modularity_communities(
                dG, resolution=resolution
            )
        )
        
        df_nodes['category'] = 'Others'
        for idx, members in enumerate(groups, 1):
            if len(members) < min_member:
                continue
            
            mask_group = df_nodes['nodes'].isin(members)
            top_rank = df_nodes[mask_group][get_leader_by].idxmax()
            series_leader = df_nodes.iloc[top_rank]
            leader_score = series_leader[get_leader_by]
            
            if (leader_score + 1) < min_member:
                continue
            
            leader_node = series_leader['nodes']
            df_nodes.loc[mask_group, 'category'] = leader_node
        
        return df_nodes
