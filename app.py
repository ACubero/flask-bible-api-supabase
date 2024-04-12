from flask import Flask, render_template
import requests
from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()
url = os.getenv('SUPABASE_URL')
key = os.getenv('SUPABASE_KEY')

app = Flask(__name__)

@app.route('/')
def mostrar_libros():
    supabase = create_client(url,key)
    response = supabase.table("books").select("*").execute()
    #print(response)
    if len(response.data) > 0:
        return render_template('libros.html', libros=response.data)
    else: 
        return "Error al obtener los libros"

if __name__ == '__main__':
    app.run(debug=False)


