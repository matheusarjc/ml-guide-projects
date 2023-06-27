from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def listar_projetos():
    conn = sqlite3.connect('projetos.db')
    cursor = conn.cursor()

    cursor.execute("SELECT id, nome_do_projeto, status FROM projetos")
    projetos = cursor.fetchall()

    conn.close()

    return render_template('lista_projetos.html', projetos=projetos)

if __name__ == '__main__':
    app.run()

