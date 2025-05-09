import numpy as np


class Egraph:
    REQUIREMENTS_NODES = np.array(['name'])
    REQUIREMENTS_EDGES = np.array(['source', 'target'])
    
    def __init__(
        self,
        df_edges,
        df_nodes,
        df_categories=None,
        col_source='source',
        col_target='target',
        col_name='name',
        col_x=None,
        col_y=None,
        col_value_node=None,
        col_category=None,
        col_symbol=None,
        col_symbol_size=None,
        col_label_node=None,
        col_tooltip_node=None,
        col_style_node=None,
        col_value_edges=None,
        col_label_edges=None,
        col_tooltip_edges=None,
        col_style_edges=None
    ):
        self.df_edges = df_edges
        self.df_nodes = df_nodes
        self.df_categories = df_categories
        
        # Requirements edges/links attributes
        self.col_source = col_source
        self.col_target = col_target
        
        # Requirements nodes attributes
        self.col_name = col_name
        self.col_x = col_x
        self.col_y = col_y
        
        # Optional nodes attributes
        self.col_value_node = col_value_node
        self.col_category = col_category
        self.col_symbol = col_symbol
        self.col_symbol_size = col_symbol_size
        self.col_label_node = col_label_node
        self.col_tooltip_node = col_tooltip_node
        self.col_style_node = col_style_node
        
        # Optional edges attributes
        self.col_value_edges = col_value_edges
        self.col_label_edges = col_label_edges
        self.col_tooltip_edges = col_tooltip_edges
        self.col_style_edges = col_style_edges
        
        self._edges_naming_conversion()
        self._nodes_naming_conversion()
        self._initialize_check()
    
    def _initialize_check(self):
        satisfied_nodes = [
            req in self.df_nodes.columns for req in Egraph.REQUIREMENTS_NODES
        ]
        satisfied_edges = [
            req in self.df_edges.columns for req in Egraph.REQUIREMENTS_EDGES
        ]
        
        satisfied_nodes = np.array(satisfied_nodes)
        satisfied_edges = np.array(satisfied_edges)
        
        if not (all(satisfied_nodes) & all(satisfied_edges)):
            need_nodes_columns = Egraph.REQUIREMENTS_NODES[~satisfied_nodes]
            need_edges_columns = Egraph.REQUIREMENTS_EDGES[~satisfied_edges]
            raise KeyError(
                f"require nodes columns: {need_nodes_columns}" + '\n' +
                f"require edges columns: {need_edges_columns}"
            )
    
    def _edges_naming_conversion(self):
        self.df_edges = self.df_edges.rename(
            {
                self.col_source: 'source',
                self.col_target: 'target',
                self.col_value_edges: 'value',
                self.col_label_edges: 'label',
                self.col_tooltip_edges: 'tooltip',
                self.col_style_edges: 'lineStyle',
            },
            axis=1
        )
        valid_columns = {
            'source', 'target', 'value', 'label', 'tooltip', 'lineStyle'
        }
        valid_columns = valid_columns.intersection(self.df_edges.columns)
        self.df_edges = self.df_edges[list(valid_columns)]
    
    def _nodes_naming_conversion(self):
        self.df_nodes = self.df_nodes.rename(
            {
                self.col_name: 'name',
                self.col_x: 'x',
                self.col_y: 'y',
                self.col_value_node: 'value',
                self.col_category: 'category',
                self.col_symbol: 'symbol',
                self.col_symbol_size: 'symbolSize',
                self.col_label_node: 'label',
                self.col_tooltip_node: 'tooltip',
                self.col_style_node: 'itemStyle',
            },
            axis=1
        )
        
        valid_columns = {
            'name', 'x', 'y', 'value', 'category', 'symbol', 'symbolSize',
            'label', 'tooltip', 'itemStyle'
        }
        valid_columns = valid_columns.intersection(self.df_nodes.columns)
        self.df_nodes = self.df_nodes[list(valid_columns)]
    
    def get_option(self):
        pass
