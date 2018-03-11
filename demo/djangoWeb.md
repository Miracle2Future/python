**django 实战操作手册**

**1.创建一个新项目：**
django-admin startproject `projectname`
.
├── db.sqlite3
├── manage.py
└── mysite
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-35.pyc
    │   ├── settings.cpython-35.pyc
    │   ├── urls.cpython-35.pyc
    │   └── wsgi.cpython-35.pyc
    ├── settings.py
    ├── urls.py
    └── wsgi.py

**2.运行django功能：**
    在创建新项目目录中运行：
    python manage.py runserver 127.0.0.1:`8001`
