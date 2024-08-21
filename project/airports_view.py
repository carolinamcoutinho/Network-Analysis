import pandas as pd
import networkx as nx
from pyvis.network import Network
import streamlit as st
import streamlit.components.v1 as components

rotas = pd.read_csv(r'../data/flights_names.csv')
rotas = rotas[['OriginAirport', 'DestAirport']]

# Função para gerar o grafo e salvar em um arquivo HTML
import streamlit as st
import streamlit.components.v1 as components

# Função para gerar o grafo e salvar em um arquivo HTML
def gerar_grafo(rotas_df):
    G = nx.Graph()
    
    # Adicionar arestas ao grafo
    for _, row in rotas_df.iterrows():
        G.add_edge(row['OriginAirport'], row['DestAirport'])
    
    # Criar uma rede Pyvis
    net = Network(height="1000px", width="100%", bgcolor="#222222", font_color="white")
    net.from_nx(G)

    # Ajustar as opções de física para movimentação mais lenta
    net.set_options("""
    var options = {
      "nodes": {
        "shape": "icon",
        "icon": {
          "face": "FontAwesome",
          "code": "\uf072",
          "size": 50,
          "color": "#f5a623"
        }
      },
      "physics": {
        "enabled": true,
        "barnesHut": {
          "gravitationalConstant": -20000,
          "springLength": 200,
          "springConstant": 0.04,
          "damping": 0.09
        },
        "minVelocity": 0.75
      }
    }
    """)
    
    # Salvar a visualização em um arquivo HTML temporário
    net.save_graph("aeroportos.html")

# Streamlit app
st.title("Visualização de Rotas de Aeroportos")

# Gerar o grafo
gerar_grafo(rotas)

# Inserir o arquivo HTML gerado pelo Pyvis
HtmlFile = open("aeroportos.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
components.html(source_code, height=1000)

#Para visualização rodar no terminal: streamlit run airports_view.py
