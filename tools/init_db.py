# -*- coding:utf-8 -*-
#@Auhor : Agam
#@Time  : 2019-06-09
#@Email : agamgn@163.com
from peewee import MySQLDatabase

from MxForm.settings import database
from apps.community.models import CommunityGroup, CommunityGroupMember
from apps.users.model import User

database = MySQLDatabase(
    'mxforum', host="127.0.0.1", port=3306, user="root", password="916149"
)

def init():
    #生成表
    database.create_tables([User])
    database.create_tables([CommunityGroup,CommunityGroupMember])
    # database.create_tables([Post, PostComment, CommentLike])
    # database.create_tables([Question, Answer])

if __name__ == "__main__":
    init()