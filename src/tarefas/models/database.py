from os import getenv
from pathlib import Path

import mysql.connector as mc
from dotenv import load_dotenv
from mysql.connector import Error


class Database:
    """
    Classe que gerencia conexões e operações com um banco de dados MySQL.
    """

    def __init__(self):
        load_dotenv()

        self.host = getenv('DB_HOST')
        self.username = getenv('DB_USER')
        self.password = getenv('DB_PASSWORD')
        self.database = getenv('DB_NAME')

        self.connection = None
        self.cursor = None

    def conectar(self):
        """Estabelece uma conexão com o banco de dados MySQL."""

        try:
            self.connection = mc.connect(
                host=self.host,
                database=self.database,
                user=self.username,
                password=self.password
            )

            if self.connection.is_connected():
                self.cursor = self.connection.cursor(dictionary=True)
                print('Conexão ao banco de dados realizada com sucesso!')

        except Error as e:
            print(f'Erro de conexão: {e}')
            self.connection = None
            self.cursor = None

    #metoto 
    def desconectar(self):
        """Encerra a conexão com o banco de dados e o cursor, se existirem."""

        if self.cursor:
            self.cursor.close()

        if self.connection and self.connection.is_connected():
            self.connection.close()

        print('Conexão encerrada com sucesso!')

    def executar(self, sql, params=None):
        """Executa uma instrução no banco de dados."""

        if not self.connection or not self.cursor:
            print('Conexão ao banco de dados não estabelecida.')
            return None

        try:
            self.cursor.execute(sql, params)

            if self.cursor.description:
                return self.cursor.fetchall()

            self.connection.commit()
            return self.cursor.rowcount

        except Error as e:
            print(f'Erro de execução: {e}')
            self.connection.rollback()
            return None


BASE_DIR = Path(__file__).resolve().parent.parent
SQL_PATH = BASE_DIR / 'data' / 'tarefas.sql'


def init_db(sql_filepath=None):
    """Função responsável por inicializar o schema (database) no banco de dados."""

    load_dotenv()

    conexao = None
    cursor = None

    # Localiza o arquivo SQL
    if sql_filepath is None:
        sql_filepath = SQL_PATH

    sql_filepath = Path(sql_filepath).resolve()

    print(f'Caminho do arquivo SQL: {sql_filepath}')
    print(f'Arquivo existe: {sql_filepath.exists()}')

    try:
        conexao = mc.connect(
            host=getenv('DB_HOST'),
            user=getenv('DB_USER'),
            password=getenv('DB_PASSWORD')
        )

        cursor = conexao.cursor()

        # Leitura do arquivo de criação do banco
        with open(sql_filepath, 'r', encoding='utf-8') as arquivo:
            sql = arquivo.read()

        # Executa os comandos SQL individualmente
        comandos = sql.split(';')

        for comando in comandos:
            if comando.strip():
                cursor.execute(comando)

        conexao.commit()

        print('Schema e tabelas inicializados com sucesso!')

    except Error as e:
        print(f'Erro no banco de dados: {e}')

        if conexao:
            conexao.rollback()

    except FileNotFoundError:
        print('O arquivo especificado não pôde ser encontrado.')

    finally:
        if cursor:
            cursor.close()

        if conexao and conexao.is_connected():
            conexao.close()


""" Área 51
Tudo o que for escrito nessa área
será lido e executado como string.
"""


if __name__ == '__main__':
    db = Database()
    db.conectar()

    print(db.executar('SELECT * FROM tarefa;'))

    db.desconectar()