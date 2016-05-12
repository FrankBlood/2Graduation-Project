#-*-coding:utf8-*-

import sys
import urllib2

reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == '__main__':
    url_get_base = 'http://api.ltp-cloud.com/analysis/?'
    api_key = 'L693Q726KenaGTMjoZBOFf8ELaOJIJMkvACvCopJ'
    text = '中华人民共和共成立了,导致我今天多吃了两碗饭。。'
    format = 'x'
    patterns = ['ws', 'pos', 'ner', 'dp', 'sdp', 'srl']
    for pattern in patterns:
        result = urllib2.urlopen("%sapi_key=%s&text=%s&format=%s&pattern=%s"\
                             %(url_get_base, api_key, text, format, pattern))
        content = result.read().strip()
        print content