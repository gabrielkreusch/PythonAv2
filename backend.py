import flask
from flask import request
from config import *
from modelo import Disciplina, EstudanteDisciplina, Pessoa

@app.route("/")
def inicio():
    return 'Sistema de cadastro de Estudantes e disciplinas.<br>' +\
           '<a href="/listar_pessoas">Listar pessoas</a><br/>' +\
           '<a href="/listar_disciplinas">Listar disciplinas</a><br/>' +\
           '<a href="/listar_estudante_disciplina">Estudantes das Disciplinas</a><br/>'

# PESSOAS #
@app.route("/listar_pessoas")
def listar_pessoas():
    return flask.render_template('listar_pessoas.html')

@app.route("/listar_pessoas_json")
def listar_pessoas_json():
    pessoas = db.session.query(Pessoa).all()
    pessoas_json = [x.json() for x in pessoas]
    resposta = jsonify(pessoas_json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route("/cadastrar_pessoa")
def cadastrar_pessoa():
    return flask.render_template('cadastrar_pessoa.html')

@app.route("/inserir_pessoa", methods=['post'])
def inserir_pessoa():
    resposta = jsonify({ "resultado": "ok"})
    pessoa_json = request.get_json()
    try:
        pessoa = Pessoa(**pessoa_json)
        db.session.add(pessoa)
        db.session.commit()
    except Exception as ex:
        resposta = jsonify({ "resultado": "erro"})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

# DISCIPLINAS #

@app.route("/listar_disciplinas")
def listar_disciplinas():
    return flask.render_template('/listar_disciplinas.html')

@app.route("/listar_disciplinas_json")
def listar_disciplinas_json():
    disciplinas = db.session.query(Disciplina).all()
    disciplinas_json = [x.json() for x in disciplinas]
    resposta = jsonify(disciplinas_json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route("/cadastrar_disciplina")
def cadastrar_disciplina():
    return flask.render_template('cadastrar_disciplina.html')

@app.route("/inserir_disciplina", methods=['post'])
def inserir_disciplina():
    resposta = jsonify({ "resultado": "ok"})
    disciplina_json = request.get_json()
    try:
        disciplina = Disciplina(**disciplina_json)
        db.session.add(disciplina)
        db.session.commit()
    except Exception as ex:
        resposta = jsonify({ "resultado": "erro"})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

# ESTUDANTEDISCIPLINA #

@app.route("/listar_estudante_disciplina")
def listar_estudante_disciplina():
    return flask.render_template('/listar_estudante_disciplina.html')

@app.route("/listar_estudante_disciplina_json")
def listar_estudante_disciplina_json():
    estudantes_disciplinas = db.session.query(EstudanteDisciplina).all()
    estudantes_disciplinas_json = [x.json() for x in estudantes_disciplinas]
    resposta = jsonify(estudantes_disciplinas_json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route("/cadastrar_estudante_disciplina")
def cadastrar_estudante_disciplina():
    return flask.render_template('cadastrar_estudante_disciplina.html')

@app.route("/inserir_estudante_disciplina", methods=['post'])
def inserir_estudante_disciplina():
    resposta = jsonify({ "resultado": "ok"})
    estudante_disciplina_json = request.get_json()
    try:
        estudante_disciplina = EstudanteDisciplina(**estudante_disciplina_json)
        db.session.add(estudante_disciplina)
        db.session.commit()
    except Exception as ex:
        resposta = jsonify({ "resultado": "erro"})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

app.run(debug=True)