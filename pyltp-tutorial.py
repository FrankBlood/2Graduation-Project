# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from pyltp import Segmentor
segmentor = Segmentor()
segmentor.load('E:\\Python\\pyltp\\ltp_data\\cws.model')
words = segmentor.segment('中华人民共和国成立了。我今天高兴地去和志伟约午饭。')
print '\t'.join(words)
segmentor.release()