import streamlit as st
import etickets_app.funcs as app
from warnings import filterwarnings

filterwarnings('ignore')
st.set_page_config(page_title="| E-Tickets - Seu ticket na hora!", page_icon="🎫")

if __name__ == '__main__':
    try:
        name, authentication_status, email = app.app_login()

        ticket_input = app.app_header()

        app.app_sidebar(authentication_status, name)

        html_tickets = app.get_tickets(ticket_input)

        st.write(html_tickets, unsafe_allow_html=True)

    except:
        st.title('E-Tickets, compre seu Ticket Já!')
        st.write('___')
        st.write('Servidores em manutenção, assim de uma possível retomada, enviaremos um e-mail! 😊👍')