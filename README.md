# Gerenciador de tarefas

Este projeto servira para aprimorarmos nossa lógicas de 
programação ao mesmo tempo em que exploramos conceitos e técnicas 
de programação back-end e fullstack.Vamos utilizar e desenvolver conceitos de MVC(Model-View-controller), algumas particularidades Funcional, persistência de dados(MySQL), microframework Flask e gerenciador de pacotes 
do Python(ASTRAL uv).

Alguns passos iniciais para peparar o projeto:

1. Caso não esteja instalado, prepare o uv no seu os. Você encontra o script de instalação no site <https://docs.sastral.sh/uv/#installation>:
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

2.Faça a inicialização do projeto com o comando:
```bash
uv init
```
Até então utilizávamos um Layout de Pacote (Package Layout) denominado flat-laout. o uv adota um estrutura mais moderna chamda src-layout, que previne erros de importação comuns chamados `inport shadowing` (importação mascaradas).
3.Crie um ambiente virtual do Python:
```bash
uv venv
```
aitve o ambiente virtual:
```powershel
.venv/Scripts/Activate.ps1 #no poweshell do windows 
source .venv/Scripts/activate #no Git bash do windos 
souce  .venv/bin/activevate #no bash do linux 
```

4. Instale o flask
```bash
uv add flask
```
Será criado um arquivo uv.lock contendo as depedêndocias (requerimentos) e versões dos 
pacotes do seu projeto.

5. Crie um arquivo app.py contendo o código inicial do projeto
```python
 from flask import Flask

 app = Flask(__name__)

 @app.route('/test')
 def test():
    return 'Servidor online!'
```

6. Teste a plicação inciando o servidor do Flask 
```bash
uv run flask run
```

