import re
import csv
import sys
import pegtree as pg

from naming import type_augmentation
from multiese2_test import test_code
from multiese2_da import multiese_da, encode_text_code

# naming


GRAMMAR = '''

Sentense = { (Block / . )* }

Block = {
    { (!LF .)+ #Code } LF
    QUOTE LF
    { (!QUOTE (!LF .)* LF)+ #Doc }
    QUOTE LF
    #Pair
}

QUOTE = '\\'\\'\\'' _ / '"""' _
LF = '\\r'? '\\n' / !.

'''

parse_as_tree = pg.generate(pg.grammar(GRAMMAR))

# prefix

BEGIN = '([^A-Za-z0-9]|^)'
#END = ('(?![A-Za-z0-9\\[\\{]|$)')
END = ('(?![A-Za-z0-9]|$)')
VARPAT = re.compile(BEGIN+r'([a-z]+)(\d?)'+END)

PREFIX = {
    's': ('文字列', ''),
    'element': ('[文字列|オブジェクト|]', ''),
    'obj': ('[オブジェクト|]', ''),
    'alist': ('リスト', ''),
    'atuple': ('タプル', ''),
    'aset': ('セット', ''),
    'adict': ('辞書', ''),
    'ty': ('型', '型'),
    'fin': ('[ファイル[入力|]|入力[|ストリーム]]', ''),
    'fout': ('[ファイル[出力|]|出力[|ストリーム]]', ''),
    'iterable': ('[[リスト|タプル|配列]|列|イテラブル|]', ''),
}


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


def type_augmentation(doc, prefixdic):
    names = [_ta(x[1], x[2], prefixdic) for x in VARPAT.findall(doc + ' ')]
    doc = re.sub(VARPAT, r'\1@\2\3@', doc + ' ')  # @s@
    for old, new in names:
        if old != new:
            doc = doc.replace(f'@{old}@', new)
    return doc.replace('@', '').strip()


def _split(s):
    if ';' in s:
        return s.split(';')
    if ',' in s and '|' not in s:
        return [x.strip() for x in s.split(',')]
    return s.split('|')


def read_settings(docs, settings):
    ss = []
    settings['option'] = {}
    for line in docs:
        if line.startswith('@'):
            name, _, argument = line.strip().partition('(')
            if argument.endswith(')'):
                argument = argument[:-1]
            if name == '@alt':
                key, _, other = argument.partition('|')
                if key in other:
                    argument = other
                argument = argument.replace('_', '')
                settings['alt'][key] = f'[{argument}]'
            elif name == '@X':
                settings['X'] = _split(argument)
            elif name == '@Y':
                settings['Y'] = _split(argument)
            elif name == '@prefix':
                t = _split(argument)
                if len(t) == 2:
                    t.append('')
                settings['prefix'][t[0]] = tuple(t[1:])
                #print('@', settings['prefix'])
            else:
                settings['option'][name] = argument
        else:
            if line.count('[') != line.count(']') or line.count('{') != line.count('}'):
                print('SyntaxError:', line)
            ss.append(line)
    return ss


def replace_with_rules(s, altdic, prefixdic):
    s = type_augmentation(s, prefixdic)
    for old, new in altdic.items():
        if old in s:
            #print('=>', old, new)
            s = s.replace(old, new)
    return s


def augment_doc(code, docs, altdic, prefixdic):
    docs2 = []
    for i, doc in enumerate(docs):
        doc = replace_with_rules(doc, altdic, prefixdic)
        docs2.append(doc)
    return code, docs2


T5PREFIX = 'trans: '


def make_triple(ss, code, docs, settings):
    option = settings['option']
    altdic = settings['alt']
    prefixdic = settings['prefix']
    code, docs = augment_doc(code, docs, altdic, prefixdic)
    test_with = option.get('@test', '$$')
    result = test_code(code, test_with)
    for doc in docs:
        text = multiese_da(doc)
        ss.append((T5PREFIX + doc, code, T5PREFIX + text, test_with, result))
        print(encode_text_code(doc, code), result)


def scaleXY(ss, code, docs, settings):
    if '__X__' not in code:
        make_triple(ss, code, docs, settings)
        return
    for x, y in zip(settings['X'], settings['Y']):
        codeX = code.replace('__X__', x)
        docYs = [doc.replace('__Y__', y) for doc in docs]
        make_triple(ss, codeX, docYs, settings)


def new_altdic():
    return {
        'に変換する': 'に[変換|]する',
        'に設定する': '[に設定する|に変更する|に[セット|指定]する|にする]',
        'に代入する': '[に[代入|]する|とする]',
        'が_': '[が|は]',
        'で_': '[で|として|を[用いて|使って]]',
        'の中の': '[[|の][中|内]の|の]', 'の中に': '[[|の][中|内]に|に]', '中で': '[[の|][中|内]で|で]',
        '全ての': '[全ての|すべての|全|]',
        'の名前': '[名|の名前]',
        'まとめて': '[まとめて|一度に|]',
        '一つ': '[ひとつ|一つ]', '二つ': '[ふたつ|二つ]',
        '１': '[一|１|1]', '２': '[二|２|2]', '３': '[三|３|3]',
        'かどうか': '[か[|どうか][調べる||[確認|判定|テスト]する]|]',
        '、': '[、|]',
        '求める': '[求める|計算する|算出する]',
        '見る': '[見る|確認する|調べる]',
        '使う': '[使う|用いる|使用する]',
        '得る': '[使う|見る|求める]',
        '新たに': '[新しく|新たに|]',
        '作る': '[[作る|作成する]|[|新規]生成する|[用意|準備]する]',
        '作って': '[[作って|作成して]|[|新規]生成して|[用意|準備]して]',
        'プリントする': '[表示する|出力する|プリントする]',
        'コピーする': '[コピーする|複製する]'
    }


def read_corpus(filename):
    ss = []
    settings = {'alt': new_altdic(), 'prefix': PREFIX.copy()}
    with open(filename) as f:
        tree = parse_as_tree(f.read())
        for t in tree:
            code = str(t[0]).strip()
            docs = str(t[1]).splitlines()
            docs = read_settings(docs, settings)
            scaleXY(ss, code, docs, settings)
    return ss


def main():
    tuples = []
    for file in sys.argv[1:]:
        tuples.extend(read_corpus(file))
    with open('kogi_trans.tsv', 'w') as f:
        f = csv.writer(f, delimiter="\t")
        for tuple in tuples:
            f.writerow(tuple)


if __name__ == '__main__':
    main()
