from time import strftime

from flask import Flask, render_template, request, jsonify
from send import app, mail, Message




def send_mail(name, email, tel, msg):
        with app.app_context():
            msg = Message(subject=name,
                          sender=app.config.get("MAIL_USERNAME"),
                          recipients=['celio.souza@starline.inf.br'], # replace with your email for testing
                          body='Contato: {}\n Email: {}\n Telefone: {}\n Mensagem: {}'.format(name, email, tel, msg))

            mail.send(msg)


def get_time():
    time = strftime("%Y-%m-%dT%H:%M")
    return time

def write_to_disk(name, email, tel, msg):
    data = open('file.log', 'a')
    timestamp = get_time()
    data.write(
        'DateStamp= {}, Name= {},  Email= {}, Celular = {}\n, Mensagem = {} '.format(timestamp, name, email, tel, msg))
    data.close()



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    email = request.form['email']
    name = request.form['name']
    celular = request.form['celular']
    msg = request.form['msg']

    if name and email and celular and msg:
        send_mail(name, email, celular, msg)



    else:
        return jsonify({'error': 'Missing data!'})




if __name__ == '__main__':
    app.run(debug=True)
