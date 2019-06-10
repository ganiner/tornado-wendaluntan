# -*- coding:utf-8 -*-
#@Auhor : Agam
#@Time  : 2019-06-09
#@Email : agamgn@163.com
from tornado.web import url
from apps.users.handler import SmsHandler, RegisterHandler, LoginHandler

urlpattern=(
    url("/code/",SmsHandler),
    url("/register/",RegisterHandler),
    url("/login/",LoginHandler),
)