from flask import Flask, render_template, request, current_app
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123123@localhost/lexus'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    cliente = db.Column(db.String(200), unique=True)
    vendedor = db.Column(db.String(200))
    avaliacao = db.Column(db.Integer)
    comentarios = db.Column(db.Text())

    def __init__(self, cliente, vendedor, avaliacao, comentarios):
        self.cliente = cliente
        self.vendedor = vendedor
        self.avaliacao = avaliacao
        self.comentarios = comentarios

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        cliente = request.form['cliente']
        vendedor = request.form['vendedor']
        avaliacao = request.form['avaliacao']
        comentarios = request.form['comentarios']
        # print(cliente, vendedor, avaliacao, comentarios)
        if cliente == '' or vendedor == '':
            return render_template('index.html', mensagem='Preencha todos os campos')
        if db.session.query(Feedback).filter(Feedback.cliente == cliente).count() == 0:
            data = Feedback(cliente, vendedor, avaliacao, comentarios)
            db.session.add(data)
            db.session.commit()
            return render_template('success.html')
        return render_template('index.html', mensagem='A avaliação já foi feita')

if __name__ == '__main__':
    app.run()