from .core.Egraph import Egraph


class EgraphStandard(Egraph):
    def get_option(
        self,
        title={
            "text": "Graph",
            "subtext": "Default layout",
            "top": "bottom",
            "left": "right"
        },
        label={
            "show": False,
            "position": "right",
            "formatter": "{b}"
        },
        symbol='circle',
        symbol_size=10,
        edge_label={
            "show": False,
            "position": "right",
            "formatter": "{b}",
            "fontSize": 20
        },
        edges_symbol=[None, 'triangle'],
        edges_symbol_size=[10, 10],
        edges_style={
            "color": "source",
            "curveness": 0.2,
            "width": 1,
            "opacity": 0.5
        },
        tooltip={
            "trigger": "item",
            "formatter": "{a} <br/>{b} - {c}"
        },
        scaleLimit={
            "min": 0.4,
            "max": 5
        },
        zoom=1.0,
        name_series="Series",
        onhover_show_node_label=False,
        onhover_show_edge_label=False,
        show_legend=True,
    ):
        if ('x' not in self.df_nodes) or ('y' not in self.df_nodes):
            raise ValueError("No column x or y found for node position")
        
        if self.df_categories is None:
            if 'category' in self.df_nodes.columns:
                legends = self.df_nodes['category'].unique()
                categories = [{'name': legend} for legend in legends]
            else:
                legends = categories = []
            
            legend = [{"data": [legend for legend in legends]}]
        
        else:
            legend = [{"data": self.df_categories.to_dict(orient="records")}]
            categories = self.df_categories[['name']].to_dict(orient="records")
        
        data = self.df_nodes.to_dict(orient="records")
        links = self.df_edges.to_dict(orient="records")
        
        option = {
            "title":
                title,
            "tooltip":
                tooltip,
            "legend":
                legend if show_legend else None,
            "animationDuration":
                1500,
            "animationEasingUpdate":
                "quinticInOut",
            "series":
                [
                    {
                        "name": name_series,
                        "type": "graph",
                        "layout": "none",
                        "data": data,
                        "links": links,
                        "categories": categories,
                        "roam": True,
                        "label": label,
                        "edgeLabel": edge_label,
                        #                     "labelLayout": {"hideOverlap": False},
                        "symbol": symbol,
                        "symbolSize": symbol_size,
                        "edgeSymbol": edges_symbol,
                        "edgeSymbolSize": edges_symbol_size,
                        "lineStyle": edges_style,
                        "scaleLimit": scaleLimit,
                        "zoom": zoom,
                        "emphasis":
                            {
                                "focus": "adjacency",
                                "lineStyle": {
                                    "width": 10
                                },
                                "label":
                                    {
                                        "show": onhover_show_node_label,
                                        "position": "right",
                                        "formatter": "{b}"
                                    },
                                "edgeLabel":
                                    {
                                        "show": onhover_show_edge_label,
                                        "position": "right",
                                        "formatter": "{b}"
                                    }
                            },
                    }
                ],
        }
        
        return option
