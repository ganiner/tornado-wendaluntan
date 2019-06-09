# -*- coding:utf-8 -*-
#@Auhor : Agam
#@Time  : 2019-06-09
#@Email : agamgn@163.com
from datetime import datetime

from MxForm.settings import database
from peewee import *

class BaseModel(Model):
    add_time = DateTimeField(default=datetime.now, verbose_name="添加时间")
    class Meta:
        database = database