# Installation 
Create venv 
```angular2html
python3 -m venv venv
```
Activate venv
```angular2html
source venv/bin/activate
```
Install requirements.txt
```angular2html
pip3 install -r requirements.txt
```
# Running Commands
Migrate project 
```angular2html
python3 manage.py makemigrations
```
```angular2html
python3 manage.py migrate
```
Run project
```angular2svg
python3 manage.py runserver
```