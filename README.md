# flask-bible-api-supabase
Leer una api de libros de la Biblia

##Crear el entorno virtual
mkdir myproject
cd myproject
py -3 -m venv venv

##Activar en entorno virtual
.venv\Scripts\activate

##Después de activar el entorno virtual instalar el pip/Flask
pip install Flask

##Añadir la carpeta .venv al .gitignore

#Opcional
##Instalar WSL que es Linux en WIndows
https://learn.microsoft.com/es-es/windows/wsl/install
wsl --install

Crear el fichero requeriments.txt para incluir dentro todas las librerias
y dependencias

Para ver las dependencias hay que hacer pip freeze
hacer "pip freeze > requeriments.txt" para que se graben en el fichero

ENDPOINT es el punto final, o la ruta de la web

#Ejecutar el progama
python app.py