#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request
import urllib.error
import urllib.parse
import base64
import time

class login:
    def __init__(self,Username,Password):
        self.Url = 'https://gw.buaa.edu.cn:801/include/auth_action.php'
        Password = base64.b64encode(Password.encode(encoding='utf-8'))
        Password = urllib.parse.quote(Password)
        self.Data = 'action=login&username='+Username+'&password={B}'+Password+'&ac_id=22&user_ip=&nas_ip=&user_mac=&save_me=1&ajax=1'
        self.Data = self.Data.encode(encoding='utf-8')
    def auto_login(self):
        request_data = urllib.request.Request(url=self.Url,data=self.Data)
        response_data = urllib.request.urlopen(request_data)
        print (str(response_data.read(),encoding='utf-8'))
        
#####################################################
def internet_on():
    try:
        urllib.request.urlopen('https://www.baidu.com/', timeout=1)
        return True
    except urllib.error.URLError as err:
        return False

#####################################################
if __name__ == '__main__':
    while True:
        if not internet_on():
            Buaa = login(Username='by222222',Password='111111') # 111111替换为密码，by222222替换为学号
            Buaa.auto_login()
            print ('User login!')
        time.sleep(60*2)
