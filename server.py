# -*- coding:utf-8 -*-
#@Auhor : Agam
#@Time  : 2019-06-09
#@Email : agamgn@163.com
import tornado
from peewee_async import Manager
from tornado import web

from MxForm.urls import urlpattern
from MxForm.settings import settings, database

if __name__ == '__main__':
    # 集成json到wtforms
    import wtforms_json
    wtforms_json.init()

    app = web.Application(urlpattern, debug=True, **settings)
    app.listen(8888)

    object=Manager(database)
    database.set_allow_sync(False)

    app.object=object

    tornado.ioloop.IOLoop.current().start()