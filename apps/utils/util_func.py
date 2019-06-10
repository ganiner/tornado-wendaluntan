# -*- coding:utf-8 -*-
#@Auhor : Agam
#@Time  : 2019-06-10
#@Email : agamgn@163.com
from datetime import datetime, date

def json_serial(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError("Type {}s not serializable".format(type(obj)))