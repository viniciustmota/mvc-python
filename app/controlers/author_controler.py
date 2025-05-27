from app import app
from flask import Flask, render_template, request, redirect, url_for
from app.services import author_service

@app.route('/', methods=["GET"])
def author():
    print("pag home")
    autores=author_service.listar()
    return render_template('author.html', autores=autores)

@app.route('/add_author', methods=["POST"])
def add_author():
    nome = request.form.get('nome')
    author_service.inserir(nome)
    return redirect(url_for('author'))

@app.route('/delete_author/<int:author_id>', methods=["POST"])
def delete_author(author_id):
    author_service.excluir(author_id)
    return redirect(url_for('author'))
