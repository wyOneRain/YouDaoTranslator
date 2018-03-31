import config
import hashlib
import time
import requests

class Translator:
    def __init__(self):
        self.API_ul = "http://openapi.youdao.com/api"
        self.appKey = config.appKey
        self.appSercret = config.secretKey
        self.Trans_from = config.trans_from
        self.Trans_to = config.trans_to

    def getJsonData(self,queryText):
        '''
        将数据url编码
        :param queryText: 待翻译的文字
        :return: 返回url编码过的数据
        '''
        salt = str(int(round(time.time() * 1000))) #产生产生随机数 ,其实固定值也可以,比如"2"
        
        #http://ai.youdao.com/docs/doc-trans-api.s#p02
        #签名生成方法：将sign_text进行md5
        sign_text = self.appKey + queryText + salt +self.appSercret
        sign = hashlib.md5(sign_text.encode('utf-8')).hexdigest()

        payload = {
            'q': queryText,
            'from': self.Trans_from,
            'to': self.Trans_to,
            'appKey': self.appKey,
            'salt': salt,
            'sign': sign
        }
        data = requests.get(self.API_ul,payload);

        data = data.json()['translation']
        return data[0]

