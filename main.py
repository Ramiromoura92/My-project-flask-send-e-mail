from flask import Flask, redirect, render_template, request
from flask_mail import Mail,Message

class Mensagem:

    def __init__(self, nome, email, subject, message) :
        self.nome = nome
        self.email = email
        self.subject = subject
        self.message = message



app = Flask(__name__)


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'ramiro.teste.2022@gmail.com'
app.config['MAIL_PASSWORD'] = '########'
app.config['MAIL_DEFAULT_SENDER'] = 'ramiro.teste.2022@gmail.com'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/index')
def index():

    return render_template ('index.html')

@app.route('/enviado')
def enviado():

    return render_template ('enviado.html')

@app.route('/falha')
def falha():

    return render_template ('falha.html')


@app.route('/enviando', methods = ['POST',])
def enviar_email():
    try:
        nome = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        content = request.form['message']

        content = f"{nome} precisa de ajuda, {content}"
        enviar = Message(subject)
        enviar.body =  content
        enviar.recipients=[email]
        response = mail.send(enviar)
        
        return redirect ('/enviado')
    except:
        return redirect ('/falha')






app.run(debug=True)
