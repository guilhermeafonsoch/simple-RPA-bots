import rpa as r
import pyautogui as p
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd

r.init()
r.url('https://www.melhorcambio.com/dolar-hoje')

p.sleep(4)
janela = p.getActiveWindow()
janela.maximize()
dolar_comercial = r.read('//*[@id="comercial"]')
r.close()

#texto do email
texto_email = 'A cotação do dolar está aqui para voce ' + dolar_comercial + ' ' + str(pd.Timestamp('today'))

#email remetente, senha, destinatário
remetente = 'ch.afonso.gui@gmail.com'
senha = 'vermelhoazul'
destinatário = 'eduardo.goncalves.2002@gmail.com'

# Setup the MIME
message = MIMEMultipart()
message['From'] = remetente
message['To'] = destinatário
#message['To'] = para02
message['Subject'] = 'Cotação do dolar'   #Título do e-mail

# Corpo do E-mail com anexos
message.attach(MIMEText(texto_email, 'plain'))

# Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587)  # Usuário do Gmail com porta
session.starttls()  # Habilita a segurança
session.login(remetente, senha)  # Login e senha de quem envia o e-mail
texto = message.as_string()
session.sendmail(remetente, destinatário, texto)
session.quit()

