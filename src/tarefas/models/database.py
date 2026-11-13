from os import getenv
import mysql.connector as mc
from dotenv import load_dotenv
from mysql.connector import Error

class Database:
    def __init__(self):
        load_dotenv()
        self.host = getenv('DB_HOST', 'localhost')
        self.username = getenv('DB_USER', 'root')
        self.password = getenv('DB_PASSWORD', '')
        self.database = getenv('DB_NAME', 'tarefas')
        self.connection = None
        self.cursor = None

    def conectar(self):
        try:
            self.connection = mc.connect(
                host=self.host,
                database=self.database,
                user=self.username,
                password=self.password
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor(dictionary=True)
        except Error as e:
            print(f'Erro de conexão: {e}')
            self.connection = None
            self.cursor = None

    def desconectar(self):
        if self.cursor:
            self.cursor.close()
        if self.connection and self.connection.is_connected():
            self.connection.close()

    def __enter__(self):
        self.conectar()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.desconectar()

    def executar(self, sql, params=None):
        if not self.connection or not self.cursor:
            return None
        try:
            self.cursor.execute(sql, params)
            if self.cursor.description:
                return self.cursor.fetchall()
            self.connection.commit()
            return self.cursor.rowcount
        except Error as e:
            print(f'Erro de execução: {e}')
            if self.connection:
                self.connection.rollback()
            return None