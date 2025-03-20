import streamlit as st
import pandas as pd

# Ocultar elementos visuais desnecessários
st.markdown("""
    <style>
        #GithubIcon, h1 > div > a, h2 > div > a, h3 > div > a, 
        h4 > div > a, h5 > div > a, h6 > div > a {
            display: none !important;
            visibility: hidden;
            opacity: 0;
        }
        [data-testid=stSidebar] [data-testid=stImage] {
            text-align: center;
            display: block;
            margin: auto;
            width: 50%;
        }
    </style>
""", unsafe_allow_html=True)

st.header("Consulta por :blue[Rotas]", divider='green')

# Carregar dados e otimizar tipos
df = pd.read_excel("Base Rotas.xlsx", index_col=4)
df = df.astype({"Cidade": "string", "Tabela de Fat.": "string"})

# Carregar estilos adicionais
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Layout das seleções
col1, col2 = st.columns(2)

cidade = col1.selectbox("Cidade", df["Cidade"].unique(), index=None, help="Selecione a Cidade.")
tabela_de_fat = col2.multiselect("Tabela de Fat.", df["Tabela de Fat."].unique(), help="Selecione a rota.")

# Filtrar os dados com base nas seleções
if cidade:
    df = df.query("Cidade == @cidade")
    st.success("Encontramos a cidade selecionada!")
elif tabela_de_fat:
    df = df.query("`Tabela de Fat.` in @tabela_de_fat")
    st.success("Encontramos a rota selecionada!")  

# Exibir os dados filtrados
colunas = ["Tabela de Fat.", "Saída Spice", "Cidade", "Região", "Dias de Entrega", "Lead Time"]
st.dataframe(df[colunas], use_container_width=True, column_config={"Lead Time": st.column_config.ProgressColumn("Tempo de Entrega", format="D+%d", min_value=1, max_value=5)})

st.write("&copy; 2024 - Luis Felipe A. David. Todos os direitos reservados")
