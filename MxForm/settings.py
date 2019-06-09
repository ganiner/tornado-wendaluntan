# -*- coding:utf-8 -*-
#@Auhor : Agam
#@Time  : 2019-06-09
#@Email : agamgn@163.com
import peewee_async

settings={
    "static_path":"",
    "static_url_prefix":"/static/",
    "template_path":"templates",
    "db":{
        "host":"127.0.0.1",
        "user":"root",
        "password":"916149",
        "name":"",
        "port":3306
    },
    "redis": {
        "host": "127.0.0.1"
    }
}

database = peewee_async.MySQLDatabase(
    'mxforum', host="127.0.0.1", port=3306, user="root", password="916149"
)