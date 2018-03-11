#-*-coding:utf-8-*-
import random,time
import urllib
import urllib3

def createPhoneCode(session):
    '''
    生成4位数字验证码
    :param session: 
    :return: 
    '''
    chars=['0','1','2','3','4','5','6','7','8','9']
    x = random.choice(chars),random.choice(chars),random.choice(chars),random.choice(chars)
    verifyCode = "".join(x)
    session["phoneVerifyCode"] = {"time":int(time.time()), "code":verifyCode}
    return verifyCode

def sendTelMsg(msg, phoneID):
    '''
    发送给外部短信接口
    :param msg:
    :param phoneID:
    :return:
    '''
    SendTelMsgUrl="http://www.810086.com.cn/jk.aspx"
    params = {"zh":"china", "mm":"china@10086",
           "hm":phoneID,"nr":msg,"sms_type":88}
    postData=urllib.urlencode(params)
    req = urllib2.Request(SendTelMsgUrl, postData)
    req.add_header('Content-Type', "application/x-www-form-urlencoded")
    respone = urllib2.urlopen(req)
    res = respone.read()
    return res

