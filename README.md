## Instalação

* python3 -m pip install --upgrade pip
* python3 -m venv env (PS> virtualenv env)
* source env/bin/activate (PS> .\env\Scripts\activate.bat)
* pip3 install -r requirements.txt
* export set FLASK_APP=football.webapp (PS> $env:FLASK_APP="football.webapp")
* export FLASK_ENV=development (default é production)
* python3 -m flask run --host=0.0.0.0 (PS> flask run)

* Criar o arquivo .env na raiz (/Users/rogerioluz/Documents/football) com as seguintes informações:

    * SECRET_KEY = b'sua chave secreta'
    * ADMIN_USERNAME = 'Seu usuario administrador'
    * ADMIN_PASSWORD = 'Uma senha'