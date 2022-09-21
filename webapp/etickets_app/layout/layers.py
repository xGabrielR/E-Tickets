from time import sleep
import streamlit as st

def app_header():
    st.title("E-Tickets, Compre seu ticket Já!")
    st.write('____')

    ticket_input = st.text_input("Informe o título do Ticket")
    st.write(' ')

    st.header("🎫 | Top 3 Tíckets Disponíveis!")

    return ticket_input

def app_spaces_between():
    st.sidebar.write('___')
    st.sidebar.write('\n\n')
    
    return None

def progress_bar():
    progress = st.sidebar.progress(0)
    for per in range(100):
        sleep(.01)
        progress.progress(per+1)

    return progress