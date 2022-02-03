# Oculid Backend Engineering Challenge

# Introduction

I build a web server to efficiently collect and organise data. In this project i used Python module `Django` to structure the project. This solution provide you to load the localy saved data easily to the server and also through APIs new data can be inject into the database. When tester upload the testing image it will convert that image into base64 and save it into database. All of the infomation for tester,picx and videos can be obtained from tester `test_id`.

## Prerequisites

1. Python 3
2. Dajngo 4.0.1
3. IDE
4. Postgresql Database

## Run Server

To run this application you should open this folder in any IDE (pycharm,VScode or Atom etc). After setting up in the IDE, execute following commands in the terminal:

```
python manage.py makemigrations oculid
```

```
python manage.py  migrate
```

After executing migrate all the tables from `models.py` of your django installed apps are created in your database file.

## setting up database

You can create database in postgresql and all of the information to access that database should be updated in `setting.py` .

## load data into the database

It's time to load data which is provided by oculid into the database table. In django application file `updatemodels.py` is responsible for injecting data into server. Eecute following command for loading the data:

```
python manage.py updatemodels
```

## Runserver

Run the server so in future you can update the data from APIs or also from django admin.

```
python manage.py runserver
```

## Post data through Django APIs

W ith the help of Djnago I created the form for tester so in future he/she can update data online and automatically saved into our server. In django application file `forms.py` and `views.py` is responsible for filling the form and saving it correctly.

All url information is availble in `urls.py`.

To add data just go to following apis and fill the form and submit .

```
localhost:8000/home
```

```
localhost:8000/picx
```

```
localhost:8000/video
```

```
localhost:8000/admin
```
