# Create new app from scratch
* Git init
* Git branch -m main
* Git remote origin https://github.com/Ivanmdelaf/TaskManager.git
* Como vamos a trabajar con Python debemos crear un entorno virtual, la caja donde se guardan las versiones con las que vamos a trabajar.

* Python3 -m venv .venv -> py -m venv .venv
* source .venv/bin/activate -> .venv\Scripts\activate

* Creamos un fichero main.py
* Creamos un fichero task_manager.py
* Creamos un fichero readme.md
* Creamos un fichero .gitignore
    * Dentro metemos .venv/
# Para hacer llamadas a una API por Http tenemos que instalar el modulo request.
* Hay que recordar que antes de instalar nada, hay que tener activo el entorno virtual.
* pip install requests
* python.exe -m pip install --upgrade pip -> Sugerido por la línea de comandos.
* pip freeze > requirements.txt

* pip install openai
* pip freeze > requirements.txt

* pip install dotenv