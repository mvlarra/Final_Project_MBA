import pandas as pd
import plotly.express as px


class HeatmapCrosstab:
    def __init__(self, rules):
        self.rules = rules.copy()
    
    def get_tabular_data(
        self,
        products: list,
        metric='support',
        threshold=None,
        max_col=5,
        personal_placement=True
    ):
        rules = self.rules
        
        group_rules = rules[rules['antecedents'].isin(products)].copy()
        if threshold is not None:
            group_rules = group_rules[group_rules[metric] > threshold]
        
        crosstab = pd.crosstab(
            index=group_rules['antecedents'],
            columns=group_rules['consequents'],
            values=group_rules[metric],
            aggfunc='first',
        )
        
        sorted_idx_row = crosstab.sum(axis=1).sort_values(ascending=False).index
        sorted_idx_col = crosstab.sum(axis=0).sort_values(ascending=False).index
        crosstab = crosstab.loc[sorted_idx_row, sorted_idx_col]
        
        # Sorted index by value
        if personal_placement:
            if products[0] in crosstab.columns:
                crosstab = crosstab.sort_values(products[0], ascending=False)
                crosstab = crosstab.sort_values(
                    products[0], axis=1, ascending=False
                )
        
        # Sorted index
        main_idx = list(crosstab.index[crosstab.index == products[0]])
        rest_idx = list(crosstab.index[crosstab.index != products[0]])
        
        # Sorted columns
        main_col_idx = list(crosstab.columns[crosstab.columns == products[0]])
        rest_col_idx = list(crosstab.columns[crosstab.columns != products[0]])
        
        crosstab = crosstab.loc[main_idx + rest_idx,
                                main_col_idx + rest_col_idx]
        crosstab = crosstab.iloc[:, :max_col]
        crosstab.columns.name = metric
        
        return crosstab
    
    @staticmethod
    def plot_heatmap(crosstab, **layouts):
        metric = crosstab.columns.name
        
        fig = px.imshow(
            crosstab,
            labels={'color': metric},
            color_continuous_scale='reds',
            text_auto=True
        )
        
        fig.update_xaxes(side="top")
        fig.update_coloraxes(showscale=True)
        
        fig._data[0]['xgap'] = 1
        fig._data[0]['ygap'] = 1
        fig._data[0]['hoverongaps'] = False
        fig._data[0]['z'] = fig._data[0]['z'].round(3)
        
        short_x = list(map(lambda x: x[:10] + '...', fig._data[0]['x']))
        short_y = list(map(lambda y: y[:10] + '...', fig._data[0]['y']))
        
        fig.update_layout(
            yaxis=dict(tickvals=list(range(len(short_y))), ticktext=short_y),
            xaxis=dict(tickvals=list(range(len(short_x))), ticktext=short_x),
            xaxis_title='consequents'
        )
        fig.update_traces(
            hovertemplate=
            f'antecedents: %{{y}}<br>consequents: %{{x}}<br>{metric}: %{{z}}<extra></extra>'
        )
        fig.update_layout(
            plot_bgcolor='rgba(0, 0, 0, 0)', paper_bgcolor='rgba(0, 0, 0, 0)'
        )
        fig.update_layout(**layouts)
        
        return fig
