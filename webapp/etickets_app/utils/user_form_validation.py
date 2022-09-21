import streamlit as st
from re import findall, match


def user_register_checkout(first_name, last_name, email, pswd):
    first_name = first_name.strip().capitalize()
    last_name = last_name.strip().capitalize()
    email = email.strip()

    try:
        if len(first_name) <= 3 or len(set(findall('\w', first_name))) <= 3:
            st.sidebar.error('Providencie um nome válido!', color="red")
            return False
        
        if len(last_name) <= 3 or len(set(findall('\w', last_name))) <= 3:
            st.sidebar.error('Providencie um nome válido')
            return False
        
        if len(pswd) <= 8 or len(set(list(pswd))) <= 4:
            st.sidebar.error('A sua senha deve conter pelo menos 8 caracteres e um símbolo.')
            return False

        if len(email) <= 10 or len(set(list(email))) <= 7 or not '@' in email or '.' not in email:
            st.sidebar.error('Providencie um EMAIL válido!')
            return False

        else:
            return True

    except:
        st.sidebar.error('Providencia suas credencias válidas!')
        return False

def user_payment_validation(cpf, phone):
    cpf = cpf.strip()
    phone = phone.strip()

    try:
        cpf = match('[0-9]+', cpf)[0]
        phone = match('[0-9]+', phone)[0]

        if len(cpf) < 11:
            st.sidebar.error('Providencie um cpf válido')
            return False

        if len(phone) < 9:
            st.sidebar.error('Providencie um número de celular válido')
            return False

        else:
            return True

    except:
        st.sidebar.error('Providencia suas credencias válidas!')
        return False


def user_buy_terms():
    terms = """
        <div>
            <p>Para melhorar a sua experiência, por favor, concorde com os termos descritos nesse link: <a href="www.google.com">Termos</a></p>
        </div>
    """ 
    
    st.sidebar.write(terms, unsafe_allow_html=True)
    
    accept_terms = st.sidebar.checkbox('Concordar e continuar')

    if accept_terms:
        return True
    else: 
        return False