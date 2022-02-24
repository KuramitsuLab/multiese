import random
import pegtree as pg

GRAMMAR = '''

Sentense = { (Chunk/ Punc)* #Chunk }

ChunkGroup = {
    Chunk* #Chunk
}

Chunk = 
  / Order
  / Choice
  / Text

Order = {
  "{"
  ChunkGroup ([|/] ChunkGroup)*
  "}"
  #Order
}

Choice = {
  "["
  ChunkGroup ("|" ChunkGroup )*
  "]"
  #Choice
}

Text = {
  (!PUNC .)+
  #Text
} / { 
  &']'
  #Text
}

Punc = { PUNC #Text }
PUNC = [{}\[\]|/]

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


class Choice(object):
    chunks: tuple

    def __init__(self, chunks, pos):
        self.chunks = chunks
        self.pos = pos

    def __repr__(self):
        return '['+('|'.join(repr(x) for x in self.chunks))+']'

    def emit(self, **kw):
        choice = kw.get('choice', 0.5)
        r = random.random()
        if r < choice:
            size = len(self.chunks)
            index = int(size * (r / choice)) % size
            #print(index, repr(self.chunks[index]))
            return self.chunks[index].emit(**kw)
        return self.chunks[0].emit(**kw)


class Order(object):
    chunks: tuple

    def __init__(self, chunks, pos):
        self.chunks = chunks
        self.pos = pos

    def __repr__(self):
        return '{'+(' | '.join(repr(x) for x in self.chunks))+'}'

    def emit(self, **kw):
        shuffle = kw.get('shuffle', 0.3)
        r = random.random()
        if r < shuffle:
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


def multiese_da(s, choice=0.5, shuffle=0.5):
    if '|' in s:
        tree = parse_as_tree(s)
        c = ParsedResult()
        c.result = _traverse_tree(tree, c)
        #print(repr(c.result), c.c, c.emit(choice=0.9))
        return c.emit(shuffle=shuffle, choice=choice)
    return s


if __name__ == '__main__':
    multiese_da(']a')
    multiese_da('subを探す')
    multiese_da('{Aと|[||B]subを}探す')
    multiese_da('[Aと|subを]探す')
    multiese_da('{sのstartからend[|まで]の間で|subを}探す')
