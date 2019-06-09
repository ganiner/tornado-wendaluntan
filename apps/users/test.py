# -*- coding:utf-8 -*-
#@Auhor : Agam
#@Time  : 2019-06-09
#@Email : agamgn@163.com
import json

import requests
web_url="http://127.0.0.1:8888"
def test_sms():
    url="{}/code/".format(web_url)
    data={
        "mobile":"18765422122"
    }
    res=requests.post(url,json=data)

    print(json.loads(res.text))


def test_register():
    url="{}/register/".format(web_url)
    data={
        "mobile":"18765422122",
        "code":"",
        "password":"ganin"
    }
    res=requests.post(url,json=data)

    print(json.loads(res.text))

if __name__ == '__main__':
    test_sms()