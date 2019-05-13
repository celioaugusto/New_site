

from flask import Flask
from flask_mail import Mail, Message


app = Flask(__name__)

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 587,
    "MAIL_USE_TLS": True,
    "MAIL_USE_SSL": False,
    "MAIL_USERNAME": 'celioaugustoss@gmail.com',
    "MAIL_PASSWORD": 'Tricolor6331'
}

app.config.update(mail_settings)
mail = Mail(app)


def send_mail(name, email, tel, msg):
    if __name__ == '__main__':
        with app.app_context():
            msg = Message(subject=name,
                          sender=app.config.get("MAIL_USERNAME"),
                          recipients=['celio.souza@starline.inf.br'], # replace with your email for testing
                          body='Contato: {}\n Email: {}\n Telefone: {}\n Mensagem: {}'.format(name, email, tel, msg))

            mail.send(msg)