import streamlit as st
import socket
import requests
import os


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
# containers
# columns

with open ('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

hostname = socket.gethostname()
public_ip = requests.get('https://api.ipify.org').text
username = os.getlogin()

coluna_esquerda, coluna_direita = st.columns([1, 1.5])

coluna_esquerda.header("Cotralti :blue[T&L.] ", divider='green')

coluna_esquerda.write(f"### Olá, :red[😁**{username}**]") # markdown
coluna_esquerda.write(f"#### Seu IP, :red[**{public_ip}**]") # markdown

    
st.markdown("𝑨𝒄𝒆𝒔𝒔𝒆 𝒏𝒐𝒔𝒔𝒐 𝒔𝒊𝒕𝒆 𝒑𝒂𝒓𝒂 𝒄𝒐𝒏𝒉𝒆𝒄𝒆𝒓 𝒏𝒐𝒔𝒔𝒐𝒔 𝒔𝒆𝒓𝒗𝒊𝒄̧𝒐𝒔 :red[http://cotralti.com.br]")
botao_dashboards = coluna_esquerda.button("Juntar PDFs 📃 ")
botao_indicadores = coluna_esquerda.button("Separar PDFs 📕")


if botao_dashboards:
    st.switch_page("juntarpdf.py")
if botao_indicadores:
    st.switch_page("separadorpdf.py")


container = coluna_direita.container(border=True)
container.image("cotraltiimage.jpg")
st.write("""
         &copy; 2024 - Luis Felipe A. David. Todos os direitos reservados
         """)