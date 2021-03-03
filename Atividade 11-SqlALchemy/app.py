from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///login.db'

db = SQLAlchemy(app)

# Define uma Tabela People
class People(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), index=True)
    peso = db.Column(db.String(255))
    altura = db.Column(db.String(255))
    classe = db.Column(db.String(255))

    def __init__(self, name, peso, altura, classe):
        self.name = name
        self.peso = peso
        self.altura = altura
        self.classe = classe

    def __repr__(self):
        return '<Nome: {}>'.format(self.name)


db.create_all()

@app.route('/')
def home():
    result = "<h1>Tabelas</h1><br><ul>"
    for table in db.metadata.tables.items():
        result += "<li>%s</li>" % str(table)
    result += "</ul>"
    return result


@app.route('/adc/')
def addPeople():
    result = "<h1>Adição de Usuários</h1><br><ul>"
    login = People(name='lixo', peso='0kg', altura='10cm', classe='null')
    db.session.add(login)
    db.session.commit()
    result += "<h4>Usuários Adicionados</h4>"
    return result

@app.route('/deletar/<int:id>')
def delPeople(id):
    result = "<h1>Exclusão de Registro</h1><br><ul>"
    people=People.query.get(id)
    db.session.delete(people)
    db.session.commit()
    result += '<p>Usuário -> Id=' + str(people.id) + ' Excluido!</p>'
    return result

@app.route('/mostrar/<int:id>')
def showPerson(id):
    people=People.query.get(id)
    result = "<h1>Consulta a Registro</h1><br><ul>"
    result += "<p> Id=" + str(people.id) + "</p>"
    result += "<p> Nome=" + people.name + "</p>"
    result += "<p> Peso=" + people.peso + "</p>"
    result += "<p> Altura=" + people.altura + "</p>"
    result += "<p> Classe=" + people.classe + "</p>"
    
    return result

@app.route('/listar')
def showPeople():
    people=People.query.order_by(People.id).all()
    result=  '<h1>Usuários</h1><br><ul>'
    for people in people:
        result += '<p>'
        result += 'Id=' + str(people.id)
        result += " <br>Nome= " + people.name
        result += " <br>Peso= " + people.peso
        result += " <br>Altura= " + people.altura
        result += " <br>Classe= " + people.classe
        result += '</p>'
    return result

@app.route('/alterar/<int:id>')
def alterar(id):
    people =People.query.get(id)
    people.altura= '176cm'
    db.session.commit()
    return 'MUDANÇA CONFIRMADA'

if __name__ == '__main__':
    app.run()