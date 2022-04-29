from janome.tokenizer import Tokenizer
import random

janome = Tokenizer()

OPTION = {
      '--random': True,
#     '--single': False, # ひとつしか選ばない (DAはオフ)
      '--order': True, # 順序も入れ替える
      '--short': False, # 短い類義語を選ぶ
#     '--pyfirst': False, #Pythonを先に出力する (yk使用)
#     '--change-subject': 0.0, # 助詞の「が」をランダムに「は」に変える
#     '--drop': 0.0, # パラメータをドロップする
#     '--partial': False, #不完全なコードでも出力する
}

class ノード(object):  # 抽象的なクラス

    def emit(self, out):
        pass

    def stringfy(self):
        out = []
        self.emit(out)
        
        if OPTION['--order']:
            print(''.join(out))
            s = ''.join(out)
            s_li=str(s).split('/')
            while '_' in s_li:
                symbol_ind = s_li.index('_')
                before_ind = symbol_ind-1
                after_ind = symbol_ind+1
                z = [s_li[before_ind], s_li[after_ind]]
                random.shuffle(z)
                s_li[before_ind] = z[0]
                s_li[after_ind] = z[1]
                #print(z)
                del s_li[symbol_ind]
                #print(s_li[1:])
            return '/'.join(s_li[1:])
        else:
            return ''.join(out)

    def __repr__(self):
        return f"<{self.__class__.__name__}> " + self.stringfy()

class 文(ノード):
    ws: list  # 文節のリスト

    def __init__(self, *ws):
        self.ws = ws

    def emit(self, out):
        for w in self.ws:
            out.append('/')
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

class order(ノード):
    w: str

    def __init__(self, w):
        self.w = w
    
    def emit(self, out):
        out.append(self.w)    

class 未定義(ノード):
    w: str

    def __init__(self, w):
        self.w = w
    
    def emit(self, out):
        out.append(f'@{self.w}')


def synonyms_split(word): #'[sort|ソート]' -> ['sort', 'ソート']
    word = word[1:-1].split('|')
    return word

def random_choice(length: int): #indexをランダムに選択
    return random.randint(0, length-1)

def choice_synonym(s:str): #類義語を選択
    word_list = sorted(synonyms_split(s), key=lambda x: len(x))
    if OPTION['--short']:
        ind = 0
    if OPTION['--random']:
        ind = random_choice(len(word_list))
    return(word_list[ind])

def parse(s: str):
    '''
    janome で解析した結果から、文オブジェクトを返す
    https://note.nkmk.me/python-janome-tutorial/
    '''
    buf_pos = []
    buf_phrase = []
    
    if OPTION['--short'] or OPTION['--random']:
        while '[' and '|' and ']' in s: #類義語の処理
            first = s[:s.find('[')]
            word = str(choice_synonym(s[s.find('['):s.find(']')+1]))
            second = s[s.find(']')+1:]
            s = first + word + second
    
    # wakati = [token.surface for token in janome.tokenize(s)]   # 分かち書きのリスト
    wakati = [token.base_form for token in janome.tokenize(s)]   # 基本形 (標準形) のリスト

    pos = [token.part_of_speech.split(',')[0] for token in janome.tokenize(s)]   # 品詞のリスト
    pos2 = [token.part_of_speech.split(',')[1] for token in janome.tokenize(s)]
    # pos3 = [token.part_of_speech.split(',')[2] for token in janome.tokenize(s)]

    print('@@wakati', wakati)
    print('@@pos   ', pos)
    print('@@pos2  ', pos2)
    # print('@@pos3  ', pos3)

    for idx in range(len(wakati)):
        if wakati[idx] == '_': #'_'：語順入れ替え可能な文節間に挿入された記号
            x = order(wakati[idx])
            buf_pos.append(x)
            x = 文節(*buf_pos)
            buf_phrase.append(x)
            buf_pos = []
        elif pos[idx] == '名詞':
            x = 名詞(wakati[idx])
            buf_pos.append(x)
        elif pos[idx] == '動詞':
            x = 動詞(wakati[idx])
            buf_pos.append(x)
        elif pos[idx] == '助詞':
            x = 助詞(wakati[idx])
            buf_pos.append(x)
            x = 文節(*buf_pos)
            buf_phrase.append(x)
            # print(buf_phrase)
            buf_pos = []
        else:
            x = 未定義(wakati[idx])
            buf_pos.append(x)

    if buf_pos != []:
        x = 文節(*buf_pos)
        buf_phrase.append(x)

    s = 文(*buf_phrase)


    return s

s = parse('データフレームdfを_[逆順に|大きい順に][sortする|ソートする|並べる]')# 語順入れ替え可能な文節間に'_'を挿入
#s2 = parse('データフレームdfを逆順にソートして、df2とする')

print(s.stringfy())
#print(s2.stringfy())
