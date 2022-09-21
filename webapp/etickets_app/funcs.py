import streamlit as st
import streamlit_authenticator as stauth

from pandas import DataFrame
from datetime import datetime

from .layout import (
    app_header,
    progress_bar,
    app_spaces_between,
)

from .utils import (
    ElasticCon,
    PicPayRequest,
    user_buy_terms,
    send_email_register,
    send_email_purchase,
    user_register_checkout,
    user_payment_validation,
)

_ELASTIC_Q = ElasticCon()

def app_login():
    name, pswd, email = _ELASTIC_Q.get_secrets()

    authenticator = stauth.Authenticate(
        email, name, pswd,
        "tickets_buys", "abcdef", cookie_expiry_days=30
    )

    name, authentication_status, email = authenticator.login("Login na E-Tickets!!")
    
    authenticator.logout("Logout", "sidebar")

    return name, authentication_status, email


def order_tickets(df, ticket_order_name):
    st.sidebar.header('Carrinho de Tickets')
    df_order = df[df['title'] == ticket_order_name].reset_index(drop=True)

    ticket_order_quantity = st.sidebar.slider(
        "Quantidade de Tickets que deseja comprar", 
        0, int(df_order.quantity.max())
    )

    total_price = float(float(df_order.price.str.replace(',', '.')) * ticket_order_quantity)
    product_id  = df_order['id'][0]
    ticket_name = df_order['title'][0] 

    st.sidebar.write('\n\n\n')
    st.sidebar.write(f'Comprando: {ticket_order_quantity} Tickets, você paga: R$ {total_price}!!')

    return total_price, product_id, ticket_name


def get_parsed_products_data(data) -> DataFrame:
    product_id = [r['_id'] for r in data]
    product_title = [r['_source']['title'] for r in data]
    product_price = [r['_source']['price'] for r in data]
    product_quantity = [r['_source']['quantity'] for r in data]
    data_dict = {
        "id": product_id,
        "title": product_title,
        "price": product_price,
        "quantity": product_quantity
    }

    return DataFrame(data_dict)


def app_sidebar(authentication_status, email):
    st.sidebar.title("Faça sua compra já!")
    st.sidebar.write("___")

    if authentication_status:

        data = _ELASTIC_Q.get_tickets_showroom(clean_json=False)

        if data:
            df = get_parsed_products_data(data)
            ticket_order_name = st.sidebar.selectbox("Tickets que deseja comprar", df['title'])
            app_spaces_between()

            if ticket_order_name:
                total_price, product_id, ticket_name = order_tickets(df,ticket_order_name)

                buy_tickets = st.sidebar.checkbox("Listar Carrinho!")

                app_spaces_between()

                if buy_tickets:
                    if not total_price:
                        st.sidebar.write('Antes de listar o seu carrinho, selecione a quantidade de tickets você quer comprar :)')
                        app_spaces_between()
                    
                    else:
                        st.sidebar.header('Antes de prosseguir ao pagamento, por favor, informe os seguintes dados para gerar o Pix!')
                        auth_user = user_buy_form(buy_tickets, email, total_price, product_id)

                        try:
                            if auth_user['auth']:
                                if user_buy_terms():
                                    picpay = PicPayRequest(
                                            picpay_token='picpay_token_da_conta_do_picpay',
                                            seller_token='seller_token_da_conta_do_picpay',
                                            url_callback='https://seusite.com/notification.com',
                                            url_return='url_do_site_na_web'
                                        )
                                
                                    request_dict = picpay.get_picpay_request(auth_user)

                                    payment_successfull = st.sidebar.button('Gerar QR Code')

                                    # Update List Itens Quantity Here

                                    if payment_successfull:
                                        _ = progress_bar()

                                        send_email_purchase(auth_user['first_name'], ticket_name, total_price, auth_user['expires_date'], email)
                                    
                                        st.sidebar.success('QR Code gerado e enviado para seu E-Mail !!')
                                        exit

                                app_spaces_between()

                        except:
                            st.sidebar.write('Por Favor, preencha corretamente as lacunas do (CPF e Celular), após isso, você vai ser direcionado ao link para acessar os termos de compra do seu Ticket!')
                            st.sidebar.write('Qualquer dúvida, basta enviar sua dúvida para o seguinte e-mail: www.e-tickets-help@etickets.com, Att, Equipe E-Tickets!')
                            app_spaces_between()
                            return None
        else:
            st.sidebar.write("Não encontrei nenhum ticket a venda no momento!")
            return None

    else:
        st.sidebar.write("Você precisa estar conectado a sua conta para comprar um Ticket!")
        user_register_form()
        return None

    return None


def user_buy_form(buy_tickets, email, total_price, product_id) -> dict:
    if buy_tickets:
        c1, c2 = st.sidebar.columns((2))
        cpf = c1.text_input('Informe seu CPF (Apenas Números)')
        phone = c2.text_input('Informe seu Celular (Apenas Números)')

        app_spaces_between()
        
        if cpf and phone:
            user_info = _ELASTIC_Q.get_user_name_by_email(email)[0]

            if user_payment_validation(cpf, phone):
                html_payment = f"""
                    <div>
                        <p><b>Pro favor, verifique suas credenciais antes de pagar!</b></p>
                        <ul>
                            <li><b>Nome</b>: {user_info['first_name']} {user_info['last_name']}</li>
                            <li><b>Email</b>: {email}</li>
                            <li><b>CPF</b>: {cpf}</li>
                            <li><b>Celular</b>: {phone}</li>
                        </ul> 
                    </div>
                """

                st.sidebar.write(html_payment, unsafe_allow_html=True)

                return {"auth":True, "cpf":cpf, "phone":phone, 
                        "first_name":user_info['first_name'], "last_name":user_info['last_name'],
                        "email": user_info['email'], "product_id": str(product_id), 
                        "expires_date":datetime.now().strftime("%Y-%m-%dT%H:%m:%S")+'-03:00', "price": float(total_price) }
        else:
            return {'auth': None}

    else:
        return {'auth', None}


def user_register_form() -> bool:
    create_account = st.sidebar.checkbox('Criar Conta na E-Ticket?')
    st.sidebar.write('___')

    if create_account:
        st.sidebar.header('Informe as credenciais abaixo e clice em Registrar!')
        st.sidebar.write('\n\n')
        c1, c2 = st.sidebar.columns((2))
        first_name = c1.text_input('Informe seu Primeiro Nome')
        last_name = c2.text_input('Informe seu Último Nome')
        email = st.sidebar.text_input('Informe seu E-Mail')
        pswd = st.sidebar.text_input('Informe uma Senha', type="password")
        app_spaces_between()

        if user_register_checkout(first_name, last_name, email, pswd):
            finalize_account = st.sidebar.button('Registrar')

            app_spaces_between()
            
            if finalize_account:
                _, _, email_list = _ELASTIC_Q.get_secrets()
                
                if email in email_list:
                    st.sidebar.error(f'O Email: {email} já foi cadastrado !!!')
                    st.sidebar.write('___')
                    st.snow()

                else:
                    _ = progress_bar()

                    hash_pass = stauth.Hasher([pswd]).generate()[0];

                    _ELASTIC_Q.insert_new_user(first_name.capitalize(), last_name.capitalize(), email, hash_pass)
                    
                    send_email_register(first_name, last_name, email)

                    st.sidebar.success('Credenciais Validadas, VERIFIQUE SEU EMAIL! agora você ja pode fazer login!!!')
                    st.sidebar.write('___')
                    st.balloons()
                    
                return True
    
    return None


def get_tickets(ticket_text=False) -> str:
    if ticket_text:
        data = _ELASTIC_Q.search_tickets(ticket_text)
    else:
        data = _ELASTIC_Q.get_tickets_showroom()
    
    if data:
        base_row = ' '.join(
            [f"""
                <div class="ticket" style="display:flex;">
                    <img src="{row['img_url']}" width="110" height="110">
                    <div class="ticket-content" style="padding:10px;">
                        <p><b>{row['title']}</b></p>
                        <p>{row['description']}</p>
                        <p><b>Preço: R$ {row['price']} - Quantidade: {row['quantity']}</b></p>
                    </div>
                </div>""" for row in data]
            )
    else:
        base_row = """<div><p><b>Não encontrei nenhum Ticket a venda 😔</b></p></div>"""
        
    return base_row
