# -*- coding:utf-8 -*-
#@Auhor : Agam
#@Time  : 2019-06-09
#@Email : agamgn@163.com
import os

import peewee_async

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
settings={
    "static_path":"",
    "static_url_prefix":"/static/",
    "template_path":"templates",
    "secret_key":"AxfO2V3I9NetpO",
    "jwt_expire": 7 * 24 * 3600,
    "MEDIA_ROOT": os.path.join(BASE_DIR, "media"),
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