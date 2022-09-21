import ssl
import smtplib
from os import getenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

E_TICKETS_EMAIL = getenv("E_TICKETS_EMAIL")
E_TICKETS_PASSWORD = getenv("E_TICKETS_EMAIL_PASSWORD")

def send_email_function(sender_email, sender_password, receiver_email, email_text, subject):
    try:
        msg = MIMEMultipart()
        msg['From'] = E_TICKETS_EMAIL
        msg['To']   = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(email_text, 'html') )

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', context=context) as smtp:
            smtp.login(E_TICKETS_EMAIL, E_TICKETS_PASSWORD)
            smtp.send_message(msg)

        return True

    except:
        return False

def send_email_register(first_name, last_name, receiver_email):
    email_text = f"""<h3 style="font-size:30px;">Olá, Seja bem vindo(a) a plataforma E-Tickets!</h3>

    <p style="font-size:20px;">Nesse e-mail simples e rápido, venho trazer abaixo suas Credências de Acesso a Plataforma!!!</p>
    
    <p style="font-size:15px;"><b>Username</b>: {(first_name+last_name).lower()}</p>
    <p style="font-size:15px;"><b>Password</b>: É a senha que você criou no site :)</p>

    <p style="font-size:20px;"><b>Att, Equipe da E-Tickets!!!</b></p>
    <p>Qualquer dúvida, basta entrar em contato com o link de suporte no site da E-Tickets ou acessar o <a href='www.google.com'>server do discord</a> da E-Tickets!!</p>
    
    """

    send_email_function(E_TICKETS_EMAIL, E_TICKETS_PASSWORD, receiver_email, email_text, 'Conta Registrada com Sucesso!!')
    
    return None

def send_email_purchase(first_name, ticket_name, price, valid_date, receiver_email):
    email_text = f"""<h3 style="font-size:30px;">Olá, Recebemos sua requisição da sua compra Ticket!!</h3>

    <p style="font-size:20px;">Caro {first_name.capitalize()}, Obrigado pela sua escolha na E-Tickets!</p>
    <p style="font-size:20px;">Você já pode conferir o link abaixo para efeturar o pagamento da compra ou apontar a camera para a leitura do QR Code para efetuar a compra do seu Ticket.</p>
    <p style="font-size:20px;">Lembrando, você comprou o ticket: {ticket_name} no preço de: {price}, essa transação é válida até: {valid_date.replace('-03:00', '').replace('T', ' ')} :)</p>

    <p>PICPAY QR CODE HERE</p>
    
    <p style="font-size:20px;"><b>Att, Equipe da E-Tickets!!!</b></p>
    <p>Qualquer dúvida, basta entrar em contato com o link de suporte no site da E-Tickets ou acessar o <a href='www.google.com'>server do discord</a> da E-Tickets!!</p>
    
    """

    send_email_function(E_TICKETS_EMAIL, E_TICKETS_PASSWORD, receiver_email, email_text, f'Pix Gerado do ticket - {ticket_name}!!')

    return None
