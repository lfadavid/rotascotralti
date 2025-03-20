import streamlit as st
import socket
import requests
import os
import getpass


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
public_hostname = socket.getfqdn(socket.gethostbyname(socket.gethostname()))
username = getpass.getuser()
ip_address = public_ip  # Substitua pelo IP desejado
hostname, _, _ = socket.gethostbyaddr(ip_address)

coluna_esquerda, coluna_direita = st.columns([1, 1.5])

coluna_esquerda.header("Cotralti :blue[T&L.] ", divider='green')

coluna_esquerda.write(f"#### Olá, :red[😁**{public_hostname}**]") # markdown
coluna_esquerda.write(f"##### Seu IP, :red[**{public_ip}**]") # markdown

    
st.markdown("𝑨𝒄𝒆𝒔𝒔𝒆 𝒏𝒐𝒔𝒔𝒐 𝒔𝒊𝒕𝒆 𝒑𝒂𝒓𝒂 𝒄𝒐𝒏𝒉𝒆𝒄𝒆𝒓 𝒏𝒐𝒔𝒔𝒐𝒔 𝒔𝒆𝒓𝒗𝒊𝒄̧𝒐𝒔 :red[http://cotralti.com.br]")

container = coluna_direita.container(border=True)
container.image("cotraltiimage.jpg")
st.write("""
         &copy; 2024 - Luis Felipe A. David. Todos os direitos reservados
         """)