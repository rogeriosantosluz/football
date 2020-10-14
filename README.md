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

https://flask.palletsprojects.com/en/1.1.x/cli/

Directories are scanned upwards from the directory you call flask from to locate the files. 
The current working directory will be set to the location of the file, with the assumption that that is the top level project directory.


## WSGI

/etc/systemd/system/football.service

[Unit]
Description=uWSGI instance to serv football
After=network.target

[Service]
User=root
Group=root
WorkingDirectory=/opt/football
Environment="PATH=/opt/football/env/bin"
ExecStart=/opt/football/env/bin/uwsgi --ini wsgi.ini

[Install]
WantedBy=multi-user.target

## stop start status

root@lab-morphine:/opt/football# systemctl start football
root@lab-morphine:/opt/football# systemctl stop football
root@lab-morphine:/opt/football# systemctl status football


https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04

## NGINX

https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-18-04

