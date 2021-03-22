### Home Automation using Python/Django 

## Building

It is best to use the python `venv` tool to build locally:

```sh
$ python -m venv venv
$ venv/Scripts/activate
```

## requirements.txt

Install libraries using pip.
Use freeze command to automatically generate a list of requirements.

```
$ pip install django,djangorestframework,psycopg2,pytest,pytest-django
$ pip list
$ pip freeze > requirements.txt 
```
requirements.txt should have the following lines:

```
asgiref==3.3.1
atomicwrites==1.4.0
attrs==20.3.0
colorama==0.4.4
Django==3.1.7
djangorestframework==3.12.2
iniconfig==1.1.1
packaging==20.9
pluggy==0.13.1
psycopg2==2.8.6
py==1.10.0
pyparsing==2.4.7
pytest==6.2.2
pytest-django==4.1.0
pytz==2021.1
sqlparse==0.4.1
toml==0.10.2
```