import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Cotralti T&L",
    page_icon="cotralti_logo.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

pg = st.navigation(
  {
                             
"𝗛𝗼𝗺𝗲":[st.Page("homepage.py", title="★ Cotralti Corporation")],
"𝗖𝗼𝗻𝘀𝘂𝗹𝘁𝗮𝘀 𝗻𝗮 𝗧𝗮𝗯𝗲𝗹𝗮 𝗦𝗽𝗶𝗰𝗲":[st.Page("consultarotas.py", title="🚵‍♂️ Consulta por Rotas")],

  }
)

             
pg.run()