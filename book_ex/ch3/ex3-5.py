from konlpy.tag import Komoran
import os

komoran = Komoran(userdic=os.path.join(os.getcwd(),'book_ex', 'ch3', 'user_dic.tsv'))
text = "우리 챗봇은 엔엘피를 좋아해."
pos = komoran.pos(text)
print(pos)