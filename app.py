import pandas as pd
import streamlit as st
import numpy


st.set_page_config(
                    page_title="Consulta por Rotas",
                    layout="wide", 
                    page_icon="cotralti_logo.png",
                    #initial_sidebar_state="collapsed" # inicia com barra de filtros fechada
)

st.header("Consulta por Cidade!", divider='gray')

DataFrame = pd.read_excel("Base Rotas.xlsx", index_col=4)#index_col=2
DataFrame["Cidade"] = DataFrame["Cidade"].astype("string")
DataFrame["Estado de Destino"]  = DataFrame["Estado de Destino"]

with open ('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


#Editar a Imagem da Cotralti e deixar ela centralizada
st.markdown(
    """
    <style>
        [data-testid=stSidebar] [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width:50%;
        }
    </style>
    """, unsafe_allow_html=True
)

hide_github_icon = """
#GithubIcon {
  visibility: hidden;
   display:none;
    opacity:0;
}
"""

st.sidebar.image("cotralti_logo.png",width=100,)
st.sidebar.markdown("""
                    #### Desenvolvido  por http://cotralti.com.br
                    """)

st.sidebar.header("Filtro")



cidade = st.sidebar.selectbox(
                key=1,
                label="Cidade",
                options=DataFrame["Cidade"].unique(),
                help="Selecione a Cidade e click nela",
                placeholder="Selecione a cidade",
                index=None
                
)
if cidade:
    if len(cidade) != None:
        DataFrame = DataFrame.query("Cidade== @cidade")
        st.success("Encontramos a cidade selecionada!")
       
colunas_aparecer = ["Tabela de Fat.", "Saída Spice","Cidade", "Região", "Dias de Entrega", "Lead Time", "Habitantes", "Imagem"]
st.dataframe(DataFrame[colunas_aparecer],use_container_width=True,
            column_config={ "Lead Time": st.column_config.ProgressColumn("Tempo de Entrega",format="D+%d", min_value=1, max_value=5),
                            "Imagem": st.column_config.ImageColumn("Cartão Postal", help="ok"),
                            "Habitantes":st.column_config.NumberColumn(step=".01"),
            })

st.write("""
         &copy; 2024 - Luis Felipe A. David. Todos os direitos reservados
         """)
