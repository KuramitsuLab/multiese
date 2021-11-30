import sys
import argparse
import random
from parser import multiese_parser
from action import perform_filter


def read_multiese_file(filename: str, pairs: list = None):
    if pairs is None:
        pairs = []  # [('日本語', 'コード') .. ] こういう順番で入ります
    with open(filename) as f:
        code = None  # コード
        sentences = []  # 自然言語文
        for line in f.readlines():
            line = line.strip()
            if line.startswith('#'):
                continue  # #で始まる行はスキップ
            if line == '':
                if code is not None:  # もしコード が nullなら
                    for sentence in sentences:
                        pairs.append((sentence, code))
                code = None
                sentences = []  # 自然言語文
                continue
            line = line.split('#')[0]  # #以降はコメントとして捨てる
            # if code is None and ord(line[0])>127 and '=' in line:
            #     key, value = [s.strip() for s in line.split('=')]
            #     tokibi.update_synonyms(synonyms, key, value)
            #     continue
            if code is None:
                code = line
            else:
                sentences.append(line)
        if code is not None:
            for sentence in sentences:
                pairs.append((sentence, code))
    return pairs


def generate_node(node, code, max, option):
    ss = [node.generate(0.0, option)]   # seed=0.0 がdefault
    for _ in range(max*3):
        if len(ss) >= max:
            break
        s = node.generate(random.random(), option)   # seed に乱数を与える
        if s not in ss:
            ss.append(s)
    return [(s, code) for s in ss]


def generate_multiese(pairs, option={}):
    generated_pairs = []
    for sentence, code in pairs:
        actions = code.split('@@')   # e.g.: @@if
        code = actions[0]
        code = code.strip()
        actions[0] = ''
        node = multiese_parser(sentence)
        # print('@@', repr(node))
        for action in actions:
            generated = generate_node(node, code, option.get('max', 3), option)   # max 個 generate する
            generated = perform_filter(action, generated, option)
            generated_pairs.extend(generated)
    return generated_pairs


def write_multiese_tsv(pairs, option, file=sys.stdout):
    if option.get('pyfirst', True):
        for sentence, code in pairs:
            print(code, sentence, sep='\t', file=file)
    else:
        for sentence, code in pairs:
            print(sentence, code, sep='\t', file=file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Multiese')
    parser.add_argument('files', nargs='+', help='files')
    parser.add_argument('--pyfirst', action='store_true')
    parser.add_argument('-o', '--out', default=None)
    parser.add_argument('--max', type=int, default=3)
    parser.add_argument('--nontype', action='store_true')
    parser.add_argument('--partial', action='store_true')
    parser.add_argument('--change_subject', action='store_true')
    #parser.add_argument('--files', nargs='*')
    args = parser.parse_args()
    option = vars(args)   # vars(args) => dict
    print(option)
    for filename in args.files:
        pairs = []
        read_multiese_file(filename, pairs)
    pairs = generate_multiese(pairs, option)
    if args.out is not None:
        with open(args.out, 'w') as f:
            write_multiese_tsv(pairs, option, file=f)
    else:
        write_multiese_tsv(pairs, option, file=sys.stdout)


'''
import tokibi
from expression import *

OPTIONS = ('bool')

def read_terakoya(filename, synonyms, dataset=None):
    if dataset is None:
        dataset = []
    with open(filename) as f:
        code = None
        options = OPTIONS
        desc = []
        for line in f.readlines():
            line = line.strip()
            if line.startswith('#'):
                continue
            if line == '':
                if code is not None:
                    dataset.append((code, tuple(desc), options))
                code = None
                options = OPTIONS
                desc = []
                continue
            line = line.split('#')[0]
            if code is None and ord(line[0])>127 and '=' in line:
                key, value = [s.strip() for s in line.split('=')]
                tokibi.update_synonyms(synonyms, key, value)
                continue
            if code is None:
                lines = line.split('@')
                code = lines[0]
                options = tuple(s.strip() for s in lines[1:])
            else:
                desc.append(line)
        if code is not None:
            dataset.append((code, tuple(desc), options))
    return dataset

def emit_tsv(doc, code, file):
    if tokibi.OPTION['--pyfirst']:
        print(f'{code}\t{doc}', file=file)
    else:
        print(f'{doc}\t{code}', file=file)

条件 = tokibi.parse('[もし|]X[ならば]|X[とき|場合]|')
条件2 = tokibi.parse('[もし|]X[ならば]|Xの[とき|場合]|')

def emit(code, docs, buffers, options):
    for doc in docs:
        if doc.endswith('かどうか'):
            tokibi.randomize()
            cond = doc[:-4]
            buffers.append((cond+tokibi.alt('かどうか|か否か|か|か'), code))
            if cond.endswith('る') or cond.endswith('い') or cond.endswith('た'):
                doc = tokibi.choice(条件.apply({'X': doc[:-4]}).generate())
            else:
                doc = tokibi.choice(条件2.apply({'X': doc[:-4]}).generate())
            buffers.append((doc, f'if {code}:'))
        else:
            buffers.append((doc, code))
    
def dispatch_emit(code, docs, buffers, options):
    if 'option' not in options:
        # @option は出力しない
        emit(code, docs, buffers, options)
    if len(options) > 0:
        symbols = globals()
        for option in options:
            local_options = option.split(':')
            option = local_options[0]
            fname = f'emit_{option}'
            if fname in symbols:
                app = symbols[fname]
                local_buffers = []
                is_extendable = app(code, docs, local_buffers, tuple(local_options[1:]) + options)
                buffers.extend(local_buffers)
                if is_extendable:
                    docs.extend([f'{x[1]}#{x[0]}' for x in local_buffers])
            else:
                print(f'undefined {option}')

def write_tsv(datasetset, synonyms, file=sys.stdout):
    for code, desc, options in datasetset:
        buffers = []
        for d in desc:
            try:
                exp, mcode, _ = tokibi.parse2(d, code, synonyms=synonyms)
                docs = exp.generate()
                dispatch_emit(mcode, docs, buffers, options)
            except RuntimeError:
                pass
        if tokibi.OPTION['--pyfirst']:
            for doc,code in buffers:
                print(f'{code}\t{doc}', file=file)
        else:
            for doc,code in buffers:
                print(f'{doc}\t{code}', file=file)
  

def parse_value(s):
    if s.isdecimal():
        return int(s)
    else:
        try:
            return float(s)
        except ValueError:
            return s == 'True'
'''
