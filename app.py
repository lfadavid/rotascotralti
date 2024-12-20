import streamlit as st
import pandas as pd
from conversor_moedas import main

st.set_page_config(
    page_title="Cotralti T&L",
    page_icon="cotralti_logo.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

pg = st.navigation(
  {
                             
"𝗛𝗼𝗺𝗲":[st.Page("homepage.py", title="★ Cotralti Corporation")],
"𝗖𝗼𝗻𝘀𝘂𝗹𝘁𝗮𝘀 𝗻𝗮 𝗧𝗮𝗯𝗲𝗹𝗮 𝗦𝗽𝗶𝗰𝗲":[st.Page("consultarotas.py", title="🚵‍♂️ Consulta por Rotas"),
                         st.Page("rateiofrete.py", title="💲 Rateio de Frete por peso")],
"𝐔𝐭𝐢𝐥𝐢𝐭𝐚́𝐫𝐢𝐨𝐬":[st.Page("separadorpdf.py", title="📝Separador Arquivos PDF"),
            st.Page("juntarpdf.py", title="📝Juntar Arquivos PDF"),
            st.Page(main, title="🤑 Conversor de Moeda")]
  }
)

             
pg.run()