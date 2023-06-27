from flask import Flask, make_response, render_template, send_from_directory
import sqlite3

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/static/css/<path:filename>')
def serve_css(filename):
    return send_from_directory(app.static_folder + '/css', filename)

@app.route('/')
def listar_projetos():
    conn = sqlite3.connect('projetos.db')
    cursor = conn.cursor()

    cursor.execute("SELECT id, nome_do_projeto, status FROM projetos")
    projetos = cursor.fetchall()

    conn.close()

    response = make_response(render_template('lista_projetos.html', projetos=projetos))
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'

    return response

if __name__ == '__main__':
    app.run()

