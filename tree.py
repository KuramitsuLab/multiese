import itertools
from janome.tokenizer import Tokenizer
import argparse
import random
from choice import ChoiceDic, alt
import sys

# オプション


class ノード(object):  # 抽象的なトップクラス

    def emit(self, out, option):
        pass

    def stringfy(self):
        out = []
        self.emit(out, {})
        return ''.join(out)

    def generate(self, random=0.0, option={}):
        out = []
        option['random'] = random
        self.emit(out, option)
        return ''.join(out)

    def flatten(self, ns=None):
        if ns is None:
            ns = []
        ns.append(self)
        return ns

    def simplify(self):
        """シンプルにしてノードを返す
        """
        return self


class 字句(ノード):  # 抽象的な字句
    w: str

    def __init__(self, w):
        self.w = w

    def emit(self, out, option):
        out.append(self.w)

    def __repr__(self):  # repr
        return f"[{self.__class__.__name__} {repr(self.w)}]"


class 系列(ノード):  # 系列
    ws: list  # 系列のリスト

    def __init__(self, *ws):
        self.ws = ws

    def emit(self, out, option):
        for w in self.ws:
            w.emit(out, option)

    def stringfy(self):
        ss = [w.stringfy() for w in self.ws]
        if sum(1 for s in ss if isChoiceString(s)) == 0:
            return ''.join(ss)
        # Choice が含まれる場合は展開する
        prod = [toChoiceTuple(s) for s in ss]
        sss = []
        for t in itertools.product(*prod):
            sss.append(''.join(t))
        return '[' + '|'.join(sss)+']'

    def flatten(self, ns=None):
        if ns is None:
            ns = []
        for w in self.ws:
            w.flatten(ns)
        return ns

    def simplify(self):
        if len(self.ws) == 1:
            return self.ws[0]
        return self

    def __repr__(self):
        s = ' '.join(map(repr, self.ws))
        return f"[{self.__class__.__name__} {s}]"


class グループ(ノード):  # 外からみると、字句として扱えるが、中には系列が入っている
    node: str

    def __init__(self, node):
        self.node = node

    def emit(self, out, option):
        self.node.emit(out, option)

    def __repr__(self):  # repr
        return f"[{self.__class__.__name__} {repr(self.node)}]"

# Choice


def isChoiceString(s):
    return s.startswith('[') and s.endswith(']')


def deChoiceString(s):
    if isChoiceString(s):
        return s[1:-1]
    return s


def toChoiceTuple(s):
    if isChoiceString(s):
        return tuple(s[1:-1].split('|'))
    return (s,)


# ChoiceDic = {}


# def update_choice_dic(choice):
#     if isChoiceString(choice):
#         choice = choice[1:-1]
#         ss = choice.split('|')
#         # print('@', ss, choice)
#         for s in ss:
#             if s == '':
#                 continue
#             if s not in ChoiceDic:
#                 ChoiceDic[s] = choice
#             else:
#                 ChoiceDic[s] = ChoiceDic[s] + '|' + choice

# def choice_dic(w, option):
#     '''
#     ChoiceDic に登録されている候補を読んで
#     字句列を返す
#     '''
#     if w in ChoiceDic:
#         s_choice = ChoiceDic[w].split('|')
#         print(s_choice)
#         r = option.get('random', random.random())
#         idx = int(len(s_choice) * r)
#         return s_choice[idx]
#     else:
#         return w   # ChoiceDic に登録されていなければ、そのまま返す

def change_sub(w, option):
    ChangeSub = ['が', 'は']
    if w in ChangeSub:
        r = option.get('random', random.random())
        idx = int(len(ChangeSub) * r)
        return ChangeSub[idx]
    else:
        return w   # ChangeSub に登録されていなければ、そのまま返す


class Choice(ノード):  # 系列が入っている字句として扱えるが、中には系列が入っている
    nodes: list

    def __init__(self, nodes):
        self.nodes = nodes

    def emit(self, out, option):
        s = deChoiceString(self.stringfy())
        out.append(alt(s, option, factor=2))

        # s = deChoiceString(self.stringfy())
        # s_choice = s.split('|')
        # r = option.get('random', random.random())
        # s_idx = int(len(s_choice) * r)
        # out.append(s_choice[s_idx % len(s_choice)])

    def stringfy(self):
        ss = [deChoiceString(node.stringfy()) for node in self.nodes]
        return '[' + '|'.join(ss) + ']'

    def __repr__(self):  # repr
        s = ' '.join(map(repr, self.nodes))
        return f"[{self.__class__.__name__} {s}]"

# アノテーション


class Annotation(ノード):  # 本来ならアノテーションごとに作った方がよい
    name: str
    nodes: list

    def __init__(self, name, nodes):
        self.name = name
        self.nodes = nodes

    def emit(self, out, option):
        pass  # がんばれ

    def __repr__(self):  # repr
        s = ' '.join(map(repr, self.nodes))
        return f"[{self.__class__.__name__} {self.name} {s}]"


# 型情報
# --type-prefix
# --type-suffix
# --type-none
# --type-random  (default) ユーザはどう書くかわからない

TypeDic = {
    's': '文字列', 'df': 'データフレーム|表データ'
}


def name_key(s):
    if len(s) > 1 and (s[-1].isdigit() or s[-1] == '_'):
        return s[:-1]
    return s


class 型情報(ノード):
    name: str  # 変数名
    desc: str  # 型情報

    def __init__(self, name, desc):
        self.name = name
        self.desc = deChoiceString(desc)

    def emit(self, out, option):
        name = self.name
        key = name_key(name)  # df2 => df を読みにいく
        if self.desc != '':
            TypeDic[key] = self.desc  # 更新
        if key in TypeDic:
            desc = alt(TypeDic[key], option, factor=3)  # 複数バージョンに対応
            # print('@@', TypeDic[key], desc, option['random'])
        else:
            desc = ''

        if option.get('type_none', False) or option.get('nontype', False):
            out.append(name)
        elif option.get('type_prefix', False):
            out.append(f'{desc}{name}')
        elif option.get('type_suffix', False):
            out.append(f'{name}{desc}')
        else:
            ss = [name, f'{desc}{name}', f'{name}{desc}']
            out.append(alt(ss, option, factor=4))

    def __repr__(self):  # repr
        return f"[{self.__class__.__name__} {self.name} {self.desc}]"

# Prefix


class Task(ノード):
    name: str  # 変数名

    def __init__(self, name=''):
        self.name = name

    def emit(self, out, option):
        task = option['task'] if option.get(
            'task', None) != None else self.name
        if 'prefix' in option and option['prefix'] != None:
            if task == '':
                task = option['prefix']
            else:
                task = option['prefix'] + '-' + task
        if task != '':
            out.append(task + ': ')


DefaultTask = Task('')


class Context(ノード):
    name: str  # 変数名

    def __init__(self, name=''):
        self.name = name

    def emit(self, out, option):
        if option.get('context_random', True):
            if random.random() < 0.5:
                out.append('#' + self.name + ' ')
        elif option.get('context', True):
            out.append('#' + self.name + ' ')


# アノテーション


def annotation(name: str, nodes):
    if name == 'type':
        if len(nodes) == 1:
            return 型情報(nodes[0].stringfy(), '')
        return 型情報(nodes[0].stringfy(), nodes[1].stringfy())
    if name == 'task':
        return Task(nodes[0].stringfy())
    if name == 'context':
        return Context(nodes[0].stringfy())

    return Annotation(name, nodes)


class 文(系列):
    def emit(self, out, option):
        # 変更するところだけ定義する
        for w in self.ws:
            w.emit(out, option)


class 文節(系列):
    pass


# 末端(字句)

class 名詞(字句):
    def emit(self, out, option):
        if self.w in ChoiceDic:
            w = ChoiceDic[self.w]
        else:
            w = self.w
        out.append(alt(w, option, factor=5))
        # out.append(choice_dic(self.w, option))


class 助詞(字句):
    def emit(self, out, option):
        if option.get('change_ga', True):
            out.append(change_sub(self.w, option))
        else:
            out.append(self.w)


class 助動詞(字句):
    pass


class 形容詞(字句):
    pass


class 連体詞(字句):
    pass


class 副詞(字句):
    pass


class 接続詞(字句):
    pass


class 動詞(字句):
    def emit(self, out, option):
        if self.w in ChoiceDic:
            w = ChoiceDic[self.w]
        else:
            w = self.w
        out.append(alt(w, option, factor=5))
        # out.append(choice_dic(self.w, option))


class コード(字句):
    pass


class 記号(字句):
    pass


class 未定義(字句):
    pass

# post_processing


def post_processing(series: 系列):
    return series


def join_s_verb(wakati, pos):
    '''
    名詞 (サ変接続) の後ろに動詞があった場合、
    ひとまとめにして動詞句として返す
    '''
    s_verb = None
    if len(pos) > 1:
        if pos[1] == '動詞':
            s_verb = ''.join(wakati[0:2])
    return s_verb


def join_verb_attached(wakati, pos, pos2, s_verb=None):
    '''
    動詞の後ろに助動詞や接続助詞があった場合、
    ひとまとめにして動詞句として返す
    '''
    flag_idx = len(pos)
    for idx in range(1, len(pos)):
        if pos[idx] == '助動詞' or pos2[idx] == '接続助詞':
            pass
        else:
            flag_idx = idx
            break
    if s_verb != None:
        wakati[0] = s_verb
    verb_attached = ''.join(wakati[0:flag_idx])
    skipped = flag_idx - 1    # join した助詞/助動詞の数

    return verb_attached, skipped


janome = Tokenizer()


def parse(s: str, post_processing=post_processing) -> 系列:
    '''
    janome で解析した結果から、系列を返す
    https://note.nkmk.me/python-janome-tutorial/
    '''
    buf_pos = []
    noun = []

    wakati = [token.surface for token in janome.tokenize(s)]   # 分かち書きのリスト
    # base = [token.base_form for token in janome.tokenize(s)]   # 基本形 (標準形) のリスト

    pos = [token.part_of_speech.split(',')[0]
           for token in janome.tokenize(s)]   # 品詞のリスト
    pos2 = [token.part_of_speech.split(',')[1] for token in janome.tokenize(s)]
    # pos3 = [token.part_of_speech.split(',')[2] for token in janome.tokenize(s)]

    s_verb = None
    skipped = 0

    for idx in range(len(wakati)):
        if pos[idx] == '名詞' or pos[idx] == '接頭詞':
            if pos2[idx] == 'サ変接続':
                s_verb = join_s_verb(wakati[idx:], pos[idx:])
                if s_verb is not None:
                    continue

            if idx == 0 or (pos[idx-1] != '名詞' and pos[idx-1] != '接頭詞'):
                noun.append(wakati[idx])

            try:
                if pos[idx+1] == '名詞' or pos[idx+1] == '接頭詞':
                    noun.append(wakati[idx+1])
                    continue
            except:
                pass

            x = 名詞(''.join(noun))
            buf_pos.append(x)
            noun = []

        elif pos[idx] == '動詞':
            if s_verb is not None:
                if len(wakati) != idx+1 and (pos[idx+1] == '助動詞' or pos2[idx+1] == '接続助詞'):
                    verb_attached, skipped = join_verb_attached(
                        wakati[idx:], pos[idx:], pos2[idx:], s_verb)
                    x = 動詞(verb_attached)
                else:
                    x = 動詞(s_verb)
                s_verb = None
            elif len(wakati) != idx+1 and (pos[idx+1] == '助動詞' or pos2[idx+1] == '接続助詞'):
                verb_attached, skipped = join_verb_attached(
                    wakati[idx:], pos[idx:], pos2[idx:])
                x = 動詞(verb_attached)
            else:
                x = 動詞(wakati[idx])
            buf_pos.append(x)

        elif pos[idx] == '助動詞':
            if skipped == 0:
                x = 助動詞(wakati[idx])
                buf_pos.append(x)
            else:
                skipped -= 1

        elif pos[idx] == '助詞':
            if skipped == 0:
                x = 助詞(wakati[idx])
                buf_pos.append(x)
            else:
                skipped -= 1

        elif pos[idx] == '副詞':
            x = 副詞(wakati[idx])
            buf_pos.append(x)
        elif pos[idx] == '連体詞':
            x = 連体詞(wakati[idx])
            buf_pos.append(x)
        elif pos[idx] == '形容詞':
            x = 形容詞(wakati[idx])
            buf_pos.append(x)

        elif pos[idx] == '接続詞':
            x = 接続詞(wakati[idx])
            buf_pos.append(x)

        elif pos[idx] == '記号':
            if pos2[idx] == '空白' or pos2[idx] == '句点':
                pass
            elif pos2[idx] == '一般' or '読点':   # 名詞で扱った方が良いかも？
                x = 記号(wakati[idx])
                buf_pos.append(x)
            else:
                x = 未定義(wakati[idx])
                buf_pos.append(x)
                # print('@@未定義', wakati[idx], pos[idx], pos2[idx])

        # ad hoc な実装
        # e.g.: A と B を表示する
        elif pos[idx] == 'フィラー':
            if wakati[idx] == 'と':
                x = 助詞(wakati[idx])
                buf_pos.append(x)

        elif pos[idx] == '感動詞':
            if wakati[idx] == 'こんにちは':
                x = 名詞(wakati[idx])
                buf_pos.append(x)

        else:
            x = 未定義(wakati[idx])
            buf_pos.append(x)
            # print('@@未定義', wakati[idx], pos[idx], pos2[idx])

    s = 系列(*buf_pos)

    return post_processing(s)


def read_txt(input_filename):
    '''
    テキストファイルを1行ずつ読み込んで
    parse した結果をプリント
    '''
    with open(input_filename) as f:
        for line in f.readlines():
            s = parse(line.strip())
            print(repr(s))
            print()


def read_str():
    s = parse('隣の客はよく柿食う客だ')
    print(repr(s), s.stringfy())

    s = parse('その写真は美しい')
    s2 = parse('美しい写真を眺める').simplify()
    s2 = parse('データフレームdfの先頭を表示する').simplify()

    # s = parse('データフレームdfを逆順にソートする')
    # s2 = parse('データフレームdfを逆順にソートして、df2とする')

    print(repr(s), s.stringfy())
    print(repr(s2), s2.stringfy())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='tree for Multiese')
    parser.add_argument('--files', nargs='*')

    args = parser.parse_args()

    if args.files != None:
        for filename in args.files:
            read_txt(filename)
    else:
        read_str()
