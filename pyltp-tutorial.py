# -*- coding: utf-8 -*-

from pyltp import Segmentor, Postagger, Parser, NamedEntityRecognizer, SementicRoleLabeller

segmentor = Segmentor()
segmentor.load('E:/Python/pyltp/ltp_data/cws.model')
words = segmentor.segment('中华人民共和国成立了。我今天高兴地去和志伟约午饭。')
print '\t'.join(words)
segmentor.release()

postagger = Postagger()
postagger.load('E:/Python/pyltp/ltp_data/pos.model')
postags = postagger.postag(words)
print '\t'.join(postags)
postagger.release()

parser = Parser()
parser.load('E:/Python/pyltp/ltp_data/parser.model')
arcs = parser.parse(words, postags)
print "\t".join("%d:%s" % (arc.head, arc.relation) for arc in arcs)
parser.release()

recognizer = NamedEntityRecognizer()
recognizer.load('E:/Python/pyltp/ltp_data/ner.model')
netags = recognizer.recognize(words, postags)
print "\t".join(netags)
recognizer.release()

labeller = SementicRoleLabeller()
labeller.load('E:/Python/pyltp/ltp_data/srl/')
roles = labeller.label(words, postags, netags, arcs)

for role in roles:
    print role.index, "".join(
            ["%s:(%d,%d)" % (arg.name, arg.range.start, arg.range.end) for arg in role.arguments])
labeller.release()
