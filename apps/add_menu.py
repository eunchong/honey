# coding: utf-8
from __future__ import unicode_literals
from decorators import on_command

import requests
import random

@on_command(['메뉴추가', 'add_menu'])
def run(robot, channel, user, tokens):
    '''점심 메뉴 추가!!!!'''
    with open('/root/honey/apps/menu.list', 'a') as file:
        file.write("%s\n"%tokens[0])
    return channel, "%s 메뉴 추가 완료!!"%tokens[0]

