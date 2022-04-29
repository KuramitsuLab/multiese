#環境設定
from janome.tokenizer import Tokenizer


class ノード(object):  # 抽象的なクラス
    pass

    def emit(self, out):
        pass

    def stringfy(self): #全てのノードに共通の変更があればここを書き換える
        out = [] #空のリストをもつ
        self.emit(out) #入れていく
        return ''.join(out) #joinしてstr型にする


class 文(ノード):
    ws: list  # 文節のリスト

    def __init__(self, *ws):
        self.ws = ws

    def emit(self, out):
        for w in self.ws:
            w.emit(out)


class 文節(ノード):
    ws: list

    def __init__(self, *ws):
        self.ws = ws

    def emit(self, out):
        for w in self.ws:
            w.emit(out)


class 名詞(ノード):
    w: str

    def __init__(self, w):
        self.w = w

    def emit(self, out):
        # 類義語に置き換える処理を書けばよい
        out.append(self.w)
        # print(out)


class 助詞(ノード):
    w: str

    def __init__(self, w):
        self.w = w

    def emit(self, out):
        out.append(self.w)

class 動詞(ノード):
    w: str

    def __init__(self, w):
        self.w = w

    def emit(self, out):
        out.append(self.w)

class その他(ノード):
    w: str

    def __init__(self, w):
        self.w = w

    def emit(self, out):
        out.append(self.w)


def parse(s: str):
    # Janome で解析し、文オブジェクトを返す
    # 偶数の
    # s = 文(文節(名詞('我輩'), 助詞('を')) ,文節(名詞('猫'), 助詞('と')), 文節(動詞('する')))
    # t_list = list(token.surface for token in t.tokenize(s)) #['偶数', 'の']

    t = Tokenizer()
    token = list(t.tokenize(s))


    # 文節区切りでリストにする(格助詞が来たら文節区切り)
    work = [[] for i in range(len(token))]  #一応トークンの数だけ空のリストを用意しておく
    p = 0
    for tok in token:
        work[p].append(tok)
        # work[p].append(tok.surface)     #tok.surfaceよりも、ここはtokを入れておくと読めないけど後々の処理が楽なのでしょうか...?
        if tok.part_of_speech.split(',')[1] == "格助詞": #格助詞が来たら次のリストに移動する
            p += 1
    #print(work)

    # Step1：   [['吾輩', 'を'], ['猫', 'と'], ['する'], [], []]
    # Step2：   [文節(['吾輩', 'を']), 文節(['猫', 'と']), 文節(['する']), [], []]
    
    #   --------メモ---------
    # work = [[] for i in range(len(token))]
    # p = 0
    # for tok in token:
    #     # print(tok)
    #     if tok.part_of_speech.startswith('名詞'):
    #         work[p].append(tok.surface) #後からtokのみにする
    #         # 名詞(tok.surface)
    #     elif tok.part_of_speech.startswith('助詞'):
    #         work[p].append(tok.surface)
    #         # 助詞(tok.surface)
    #     elif tok.part_of_speech.startswith('動詞'):
    #         work[p].append(tok.surface)
    #         # 動詞(tok.surface)
    #     else:
    #         work[p].append(tok.surface)
    #         # その他(tok.surface)
    #     if tok.part_of_speech.split(',')[1] == "格助詞":
    #         p += 1
    #   --------メモ---------
    

    # 文節クラスに文節リストを順に入れる
    q = 0
    while len(work[q]) > 0:
        文節(work[q])
        #q += 1
    # Step2：   [文節(['吾輩', 'を']), 文節(['猫', 'と']), 文節(['する']), [], []]
    # Step3：   [文節([名詞('我輩'), 助詞('を')]), 文節([名詞('猫'), 助詞('と']), 文節([動詞('する')]), [], []]

        #  文節クラスから得た出力結果を品詞分解する
        for word in work[q]: #FIXME：文節の出力からリストの中身は持ってくる
            print(word)
            if word.part_of_speech.startswith('名詞'):
                名詞(word.surface)
            elif word.part_of_speech.startswith('助詞'):
                助詞(word.surface)
            elif word.part_of_speech.startswith('動詞'):
                動詞(word.surface)
            else:
                その他(word.surface)
        q += 1  #次のリストを処理する
    return s #ここ何返していいか分からないです



s = parse('吾輩を猫とする')
print(s)
#   これをしたの形に変換する

# s = 文(文節(名詞('我輩'), 助詞('を')) ,文節(名詞('猫'), 助詞('と')), 文節(動詞('する')))
# print(s.stringfy())

# 吾輩を猫とする