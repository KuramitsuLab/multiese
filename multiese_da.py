import re
import random
import pegtree as pg


GRAMMAR = '''

Sentense = { (Chunk/ Punc)* #Chunk }

S = ' '*

ChunkGroup = {
    Chunk* #Chunk
}

Chunk = 
  / Order
  / Choice
  / Text

Order = {
  "{"
  ChunkGroup ("|" ChunkGroup )*
  "}"
  #Order
}

Choice = {
  "["
  ChunkGroup ("|" ChunkGroup )*
  "]"
  #Choice
}

Text = 
    / '`' { (!'`' . )+ #Text } '`'
    / { (!PUNC .)+ #Text } S
    / { &"|" #Text }

Punc = { PUNC #Text }
PUNC = [` {}\[\]|/] S

'''

parse_as_tree = pg.generate(pg.grammar(GRAMMAR))


class Chunk(object):
    chunks: tuple

    def __init__(self, chunks):
        self.chunks = chunks

    def __repr__(self):
        return ' '.join(repr(x) for x in self.chunks)

    def emit(self, **kw):
        return ''.join(c.emit(**kw) for c in self.chunks)


class Text(object):
    text: str

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return repr(self.text)

    def emit(self, **kw):
        return self.text


def zipf(k, n):
    return (1/(k+1)) / sum(1 / (i+1) for i in range(n))


def random_rank(n):
    acc = 0
    r = random.random()
    for i in range(n):
        acc += zipf(i, n)
        if r < acc:
            return i
    return n-1


class Choice(object):
    chunks: tuple

    def __init__(self, chunks, pos):
        self.chunks = chunks
        self.pos = pos

    def __repr__(self):
        return '['+('|'.join(repr(x) for x in self.chunks))+']'

    def emit(self, **kw):
        choice = kw.get('choice', 0.5)
        if choice > 1.0 or choice < 0.0:
            return self.chunks[-1].emit(**kw)
        r = random.random()
        if r < choice:
            n = len(self.chunks)
            n = random_rank(n)
            return self.chunks[n].emit(**kw)
        return self.chunks[0].emit(**kw)


class Order(object):
    chunks: tuple

    def __init__(self, chunks, pos):
        self.chunks = chunks
        self.pos = pos

    def __repr__(self):
        return '{'+(' | '.join(repr(x) for x in self.chunks))+'}'

    def emit(self, **kw):
        shuffle = kw.get('shuffle', 0.5)
        r = random.random()
        if shuffle > 1.0:
            # 常にシャッフル
            chunks = list(self.chunks[::-1])
        elif r < shuffle:
            chunks = list(self.chunks)
            random.shuffle(chunks)
        else:
            chunks = self.chunks
        return ''.join(c.emit(**kw) for c in chunks)


class ParsedResult(object):
    def __init__(self):
        self.c = 0
        self.result = None

    def count(self):
        self.c += 1
        return self.c-1

    def __repr__(self):
        return repr(self.result)

    def emit(self, **kw):
        return self.result.emit(**kw)


def _traverse_tree(tree, c):
    if tree == 'Text':
        return Text(str(tree))
    ss = []
    for t in tree:
        ss.append(_traverse_tree(t, c))
    if len(ss) > 0:
        if tree == 'Chunk':
            if len(ss) == 1:
                return ss[0]
            return Chunk(tuple(ss))
        if tree == 'Order':
            if len(ss) == 1:
                return ss[0]
            return Order(tuple(ss), c.count())
        if tree == 'Choice':
            if len(ss) == 1:
                ss.append(Text(''))
            return Choice(tuple(ss), c.count())
    return Text('')


def multiese_da(s, choice=0.9, shuffle=0.5):
    tree = parse_as_tree(s)
    c = ParsedResult()
    c.result = _traverse_tree(tree, c)
    # print(repr(c.result))
    return c.emit(shuffle=shuffle, choice=choice)


BEGIN = '([^A-Za-z0-9]|^)'
#END = ('(?![A-Za-z0-9\\]\\}]|$)')
END = ('(?![A-Za-z0-9]|$)')
VARPAT = re.compile(BEGIN+r'([a-z]+\d?)'+END)


def _replace(doc, oldnews):
    doc = re.sub(VARPAT, r'\1@\2@', doc)  # @s@
    for old, new in oldnews:
        doc = doc.replace(old, new)
    return doc.replace('@', '')


def encode_text_code(text, code, choice=0.9, shuffle=0.5):
    text = multiese_da(text, choice=choice, shuffle=shuffle) + ' '
    names = [x[1] for x in VARPAT.findall(text) if x[1] in code]
    d = {}
    oldnews = []
    for name in names:
        if name not in d:
            d[name] = f'<e{len(d)}>'
            oldnews.append((f'@{name}@', d[name]))
    text = _replace(text, oldnews).strip()
    code = _replace(code+' ', oldnews).strip()
    return text, code


VERBS = [
    ('する', 'して', 'した', 'したい', 'します'),
    ('探す', '探して', '探した', '探したい', '探します'),
]

if __name__ == '__main__':
    print(multiese_da('[sub]を 探す'))
    print(multiese_da('{Aと|[||B]subを}探す'))
    print(multiese_da('[Aと|subを]探す'))
    print(multiese_da('sにおいて{startからend [|まで ] [|の間] で | subを } 探す'))
    print(multiese_da(
        'sにおいて{startからend [|まで ] [|の間] で | subを } 探す', choice=1.0, shuffle=1.0))
