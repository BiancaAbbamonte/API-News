import smtplib
from email.mime.text import MIMEText
from resumo import obter_resumo_noticias

def send_email():
    servidor_email = smtplib.SMTP('smtp.gmail.com', 587)

    servidor_email.starttls()

    servidor_email.login('email_login', 'gmail code')

    # Criação do conteúdo
    conteudo = obter_resumo_noticias()
    mensagem = MIMEText(conteudo, 'plain', 'utf-8')
    mensagem['Subject'] = 'Resumo das Notícias de Negócios'
    mensagem['From'] = 'email_from'
    mensagem['To'] = 'email_to'


    servidor_email.sendmail(
        'email_from',
        ['email_to'],
        mensagem.as_string()
    )

    servidor_email.quit()