import re
import csv
import sys
import pegtree as pg

##
# Multiese Parser

GRAMMAR = '''

Sentense = { (Block / . )* }

// { (!LF .)+ #Code } LF

Code = {
    (!LF .)+ (LF [ \t]+ (!LF .)+ )* #Code
}

Block = {
    Code LF
    QUOTE LF
    { (!QUOTE (!LF .)* LF)+ #Doc }
    QUOTE LF
    #Pair
}

QUOTE = '\\'\\'\\'' _ / '"""' _
LF = '\\r'? '\\n' / !.

'''

parse_as_tree = pg.generate(pg.grammar(GRAMMAR))


# Document Settings

# auto_augmentation

BEGIN = '([^A-Za-z0-9]|^)'
END = ('(?![A-Za-z0-9]|$)')
VARPAT = re.compile(BEGIN+r'([A-Za-z_]+)(\d?)'+END)


def _ta(name, number, prefixdic):
    prefix, suffix = prefixdic.get(name, ('', ''))
    if prefix == '' and suffix == '':
        if name.endswith('func'):
            prefix = '関数'
            suffix = '関数'
    if '|' not in prefix:
        prefix = f'[{prefix}|]'
    if suffix != '' and '|' not in suffix:
        suffix = f'[{suffix}|]'
    var = f'{name}{number}'
    if suffix == '':
        return var, f'{prefix}{var}'
    return var, f'[{prefix}{var}|{var}{suffix}]'


def _split(s):
    if ';' in s:
        return s.split(';')
    if ',' in s and '|' not in s:
        return [x.strip() for x in s.split(',')]
    return s.split('|')


class Corpus(object):
    def __init__(self, corpus):
        self.corpus = corpus
        self.prefixDic = {}
        self.altDic = {}

    def extend_type(self, doc):
        names = [_ta(x[1], x[2], self.prefixDic)
                 for x in VARPAT.findall(doc + ' ')]
        doc = re.sub(VARPAT, r'\1@\2\3@', doc + ' ')  # @s@
        for old, new in names:
            if old != new:
                doc = doc.replace(f'@{old}@', new)
        return doc.replace('@', '').strip()

    def extend_alt(self, doc):
        doc = self.extend_type(doc)
        for old, new in self.altDic.items():
            if old in doc:
                #print('=>', old, new)
                doc = doc.replace(old, new)
        return doc

    def make_pair(self, code, docs):
        self.corpus.append((code, [self.extend_alt(doc) for doc in docs]))

    def multiplex(self, code, docs):
        if '__X__' in code:
            for x, y in zip(self.X, self.Y):
                codeX = code.replace('__X__', x)
                self.make_pair(codeX, [doc.replace('__Y__', y)
                                       for doc in docs])
        else:
            self.make_pair(codeX, docs)

    def parse_argument(self, name, argument):
        if name == '@alt':
            if '=' in argument:
                key, _, argument = argument.partition('=')
            else:  # old-style
                key, _, other = argument.partition('|')
                if key in other:
                    argument = other
                argument = argument.replace('_', '')
            if not argument.startswith('['):
                argument = f'[{argument}]'
            self.altDic[key] = argument
        elif name == '@prefix':
            t = _split(argument)
            if len(t) == 2:
                t.append('')
            self.prefixDic[t[0]] = tuple(t[1:])
        elif name == '@X':
            self.X = _split(argument)
        elif name == '@Y':
            self.Y = _split(argument)

    def parse_settings(self, docs):
        ss = []
        for line in docs:
            line = line.strip()
            if line.startswith('@'):
                name, _, argument = line.strip().partition('(')
                if argument.endswith(')'):
                    argument = argument[:-1]
                self.parse_argument(name, argument)
            elif len(line) > 0:
                if line.count('[') != line.count(']') or line.count('{') != line.count('}'):
                    print('SyntaxError:', line)
                ss.append(line)
        return ss

    def read(self, filename):
        #settings = {'alt': new_altdic(), 'prefix': PREFIX.copy()}
        self.altDic = {}
        self.prefixDic = {}
        with open(filename) as f:
            tree = parse_as_tree(f.read())
            for t in tree:
                code = str(t[0]).strip()
                docs = self.parse_settings(str(t[1]).splitlines())
                self.multiplex(code, docs)


# Main

def main():
    tuples = []
    corpus = Corpus(tuple)
    for filename in sys.argv[1:]:
        corpus.read(filename)
    # with open('kogi_trans.tsv', 'w') as f:
    #     f = csv.writer(f, delimiter="\t")
    #     for tuple in tuples:
    #         f.writerow(tuple)


if __name__ == '__main__':
    main()
