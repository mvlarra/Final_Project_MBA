from .RulesGraphManager import RulesGraphManager

import numpy as np


class CrossSellingProducts:
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
    
    def get_cross_selling_products(
        self, min_support=0.01, max_support_ratio_diff=1.5, min_confidence=0.5
    ):
        df_report = self.rules.copy()
        df_report = df_report[df_report['support'] >= min_support]
        df_report = df_report[df_report['confidence'] >= min_confidence]
        
        df_report['support_ratio_diff'] = (
            df_report[['antecedent support', 'consequent support']].max(axis=1
                                                                       ) /
            df_report[['antecedent support', 'consequent support']].min(axis=1)
        )
        df_report = df_report[df_report['support_ratio_diff'] <
                              max_support_ratio_diff]
        
        df_report = df_report.sort_values(
            ['confidence', 'support_ratio_diff'], ascending=[False, True]
        )
        df_report['consequent confidence'] = np.nan
        df_report['consequent support'] = np.nan
        
        for idx, row in df_report.iterrows():
            the_couple = (self.rules['antecedents'] == row['consequents'])
            the_couple &= (self.rules['consequents'] == row['antecedents'])
            
            other_idx = the_couple.idxmax()
            consequent_confidence = self.rules.at[other_idx, 'confidence']
            consequent_support = self.rules.at[other_idx, 'antecedent support']
            
            df_report.loc[idx, 'consequent confidence'] = consequent_confidence
            df_report.loc[idx, 'consequent support'] = consequent_support
        
        df_report = df_report.rename(
            {'confidence': 'antecedent confidence'}, axis=1
        )
        df_report['confidence_mean'] = round(
            (
                df_report['antecedent confidence'] +
                df_report['consequent confidence']
            ) / 2, 2
        )
        valid_confidence = (df_report['confidence_mean'] >= min_confidence)
        df_report = df_report.loc[valid_confidence]
        
        COLUMNS = [
            'antecedents', 'consequents', 'antecedent support',
            'consequent support', 'antecedent confidence',
            'consequent confidence', 'support', 'support_ratio_diff',
            'confidence_mean'
        ]
        
        df_report = df_report[COLUMNS].sort_values(
            ['confidence_mean', 'support'], ascending=False
        )
        
        return df_report.reset_index(drop=True).dropna()
    
    def get_graph_features(self, csp_rules):
        """
        return df_nodes, df_edges
        """
        MyRGM = self.RulesGraphManager(csp_rules)
        df_nodes, df_edges = MyRGM.get_graph_features()
        
        return df_nodes, df_edges
