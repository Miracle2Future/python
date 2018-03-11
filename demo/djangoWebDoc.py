#-*-coding:utf-8-*-

'''
django 2.0 实战操作手册

1.创建一个新项目：
django-admin startproject `projectname`
mysite
├── db.sqlite3
├── manage.py                               #   管理Django程序
└── mysite                                  #   对整个程序进行配置
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-35.pyc
    │   ├── settings.cpython-35.pyc
    │   ├── urls.cpython-35.pyc
    │   └── wsgi.cpython-35.pyc
    ├── settings.py                         #   配置文件
    ├── urls.py                             #   URL对应关系
    └── wsgi.py                             #   遵循WSGI规范， uwsgi + nginx

2.运行django功能：
    在创建新项目目录中运行：
    python manage.py runserver 127.0.0.1:`8001`

3.创建app

    python manage.py startapp 'appname'

    app目录：
            mirations   数据库操作记录 数据修改表结构
                        python manage.py makemigrations 迁移数据
                        python manage.py migrate        迁移数据到数据库
            admin       Django后台管理
            apps        配置当前app
            models      ORM,写指定的类，通过命令可以创建数据库结构
            tests       测试
            views       写业务逻辑代码

    1.配置模板的路径
        TEMPLATES = [
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [os.path.join(BASE_DIR,'templates')],
                'APP_DIRS': True,
                'OPTIONS': {
                    'context_processors': [
                        'django.template.context_processors.debug',
                        'django.template.context_processors.request',
                        'django.contrib.auth.context_processors.auth',
                        'django.contrib.messages.context_processors.messages',
                    ],
                },
            },
        ]

    2.配置静态目录
        STATIC_URL = '/static/'
        STATICFILES_DIRS = (
            os.path.join(BASE_DIR,'static'),
        )
'''

