import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Cotralti Transportes e Logistica",
    page_icon="cotralti_logo.png",
    layout="wide",
    initial_sidebar_state="expanded"
)
pg = st.navigation(
  {
                             
"𝗛𝗼𝗺𝗲":[st.Page("homepage.py", title="★ Cotralti Corporation")],
"𝗖𝗼𝗻𝘀𝘂𝗹𝘁𝗮𝘀 𝗻𝗮 𝗧𝗮𝗯𝗲𝗹𝗮 𝗦𝗽𝗶𝗰𝗲":[st.Page("consultarotas.py", title="① Consulta por Rotas"),
                         st.Page("rateiofrete.py", title="② Rateio de Frete por peso")],
"𝐔𝐭𝐢𝐥𝐢𝐭𝐚́𝐫𝐢𝐨𝐬":[st.Page("separadorpdf.py", title="📝Separador Arquivos PDF"),
                                 st.Page("juntarpdf.py", title="📝Juntar Arquivos PDF")]
  }
)               
pg.run()