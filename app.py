
from flask import Flask, render_template, request, redirect, url_for
from src.tarefas.models.tarefa import Tarefa

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':

        titulo = request.form.get('tituloTarefa')
        data = request.form.get('dataConclusao') or None

        Tarefa.inserir(titulo, data)

        return redirect(url_for('index'))

    tarefas = Tarefa.listarTarefa()

    return render_template(
        'base.html',
        titulo="Lista de Tarefas",
        tarefas_da_pagina=tarefas,
        tarefa_a_editar=None
    )


@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_tarefa(id):

    print(f'ID recebido na rota: {id}')

    if request.method == 'POST':

        titulo = request.form.get('tituloTarefa')
        data = request.form.get('dataConclusao') or None

        print(f'Título recebido: {titulo}')
        print(f'Data recebida: {data}')

        resultado = Tarefa.atualizar(id, titulo, data)

        print(f'Resultado final: {resultado}')

        return redirect(url_for('index'))

    tarefa_selecionada = Tarefa.carregarPorId(id)

    if tarefa_selecionada is None:
        return redirect(url_for('index'))

    tarefas = Tarefa.listarTarefa()

    return render_template(
        'base.html',
        titulo="Editar Tarefa",
        tarefas_da_pagina=tarefas,
        tarefa_a_editar=tarefa_selecionada
    )


@app.route('/apagar/<int:id>')
def apagar_tarefa(id):

    Tarefa.apagar(id)

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
