from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def mostrar_libros():
    url_api = "https://api-libros-biblia.onrender.com/"
    response = requests.get(url_api)
    if response.status_code == 200:
        libros = response.json()
        print(libros)
        return render_template('libros.html', libros=libros)
    else:
        return "Error al obtener los libros"

if __name__ == '__main__':
    app.run(debug=True)
