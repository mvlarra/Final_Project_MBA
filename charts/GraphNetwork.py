import networkx as nx
import plotly.graph_objects as go
import ast

def draw_graph(rules, metrica='lift', top_n=50, valor_minimo=1.2):
    G = nx.DiGraph()

    reglas_filtradas = rules[rules[metrica] >= valor_minimo]
    reglas_top = reglas_filtradas.nlargest(top_n, metrica)

    for _, row in reglas_top.iterrows():
        # Asegurarse que sean listas, usando ast.literal_eval si son strings
        try:
            antecedents = ast.literal_eval(row['antecedents']) if isinstance(row['antecedents'], str) else row['antecedents']
            consequents = ast.literal_eval(row['consequents']) if isinstance(row['consequents'], str) else row['consequents']
        except:
            continue  # saltar si hay error de parseo

        origen = ', '.join(antecedents)
        destino = ', '.join(consequents)
        texto_hover = f"{origen} → {destino}<br>Lift: {row['lift']:.2f}<br>Confianza: {row['confidence']:.2f}"

        G.add_node(origen)
        G.add_node(destino)
        G.add_edge(origen, destino, weight=row[metrica], text=texto_hover)

    pos = nx.spring_layout(G, seed=42)

    # Edges
    edge_x, edge_y, edge_text = [], [], []
    for u, v, data in G.edges(data=True):
        x0, y0 = pos[u]
        x1, y1 = pos[v]
        edge_x += [x0, x1, None]
        edge_y += [y0, y1, None]
        edge_text.append(data.get("text", ""))

    edge_trace = go.Scatter(
        x=edge_x,
        y=edge_y,
        line=dict(width=1.5, color='gray'),
        hoverinfo='none',
        mode='lines'
    )

    # Nodes
    node_x, node_y, texts = [], [], []
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        texts.append(node)

    node_trace = go.Scatter(
        x=node_x,
        y=node_y,
        mode='markers+text',
        hoverinfo='text',
        text=texts,
        textposition="top center",
        textfont=dict(size=10),
        marker=dict(
            color='darkorange',
            size=15,
            line_width=2
        )
    )

    fig = go.Figure(data=[edge_trace, node_trace])
    fig.update_layout(
        title=f"Red de productos relacionados (top {top_n}, {metrica} ≥ {valor_minimo})",
        title_x=0.5,
        showlegend=False,
        margin=dict(t=30, b=20, l=20, r=20),
        height=600
    )

    return fig
