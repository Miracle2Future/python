#!/usr/bin/env python3
# coding: utf-8

import requests		
from wxpy import *
import json
robot = Bot()				
def talks_robot(info = '你好啊'):
   api_url = 'http://www.tuling123.com/openapi/api'
   apikey = '12a59232e9a645e38d93694fdc6d9fa9'
   data = {'key': apikey,
               'info': info}
   req = requests.post(api_url, data=data).text
   replys = json.loads(req)['text']
   return replys

@robot.register()
def reply_my_friend(msg):
   message = '{}'.format(msg.text)
   replys = talks_robot(info=message)
   return replys
robot.start()
embed()
