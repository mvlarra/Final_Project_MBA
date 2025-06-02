import pandas as pd
import os
import streamlit as st

@st.cache_data
def load_data():
    base_path = "data/processed"

    dataset_sample = pd.read_csv(os.path.join(base_path, "00_dataset_sample.csv"))
    Top_10_Mas_Vendidos = pd.read_csv(os.path.join(base_path, "Top_10_Mas_Vendidos.csv"))
    example_basket = pd.read_csv(os.path.join(base_path, "01_example_basket.csv"))
    monthly_transactions = pd.read_csv(os.path.join(base_path, "02_monthly_transactions.csv"))
    matriz_binaria = pd.read_csv(os.path.join(base_path, "matriz_binaria.csv"))
    rules = pd.read_csv(os.path.join(base_path, "summary_rules.csv"))
    df_bundle_products = pd.read_csv(os.path.join(base_path, "bundle_products.csv"))
    tabular = pd.read_csv(os.path.join(base_path, "tabular_bundle.csv"))
    Top_5_Rules_by_Score = pd.read_csv(os.path.join(base_path, "Top_5_Rules_by_Score.csv"))

    return (dataset_sample, Top_10_Mas_Vendidos, example_basket, monthly_transactions, matriz_binaria,
            rules, df_bundle_products, tabular, Top_5_Rules_by_Score)
