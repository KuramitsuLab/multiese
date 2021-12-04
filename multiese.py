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
            generated = generate_node(node, code, option.get(
                'max', 3), option)   # max 個 generate する
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
    parser.add_argument('-a', '--append', default=None)  # 既存のファイルに追記する
    parser.add_argument('--max', type=int, default=3)
    parser.add_argument('--verbose', action='store_true')    # デバッグ用の出力
    parser.add_argument('--type-none', action='store_true')    # 型情報をつけない
    # 型情報を先頭につける (e.g.: データフレームdf)
    parser.add_argument('--type-prefix', action='store_true')
    # 型情報を後ろにつける (e.g.: dfデータフレーム)
    parser.add_argument('--type-suffix', action='store_true')
    parser.add_argument('--partial', action='store_true')      # partial
    # 助詞の「が」と「は」をランダムに入れ替える
    parser.add_argument('--change-ga', action='store_true')
    parser.add_argument('--prefix', default=None)  # 強制的にタスクをつける
    parser.add_argument('--task', default=None)
    parser.add_argument('--without-context', action='store_true')  # コンテストをつけない
    parser.add_argument('--without-reorder', action='store_true')  # 順序を入れ替えない
    parser.add_argument('--drop-rate', type=float,
                        default=0.1)  # 0.0 にするとドロップしない

    # parser.add_argument('--files', nargs='*')
    args = parser.parse_args()
    option = vars(args)   # vars(args) => dict
    if args.verbose:
        print(option)
    for filename in args.files:
        pairs = []
        read_multiese_file(filename, pairs)
    pairs = generate_multiese(pairs, option)
    if args.append is not None:
        with open(args.append, 'a') as f:
            write_multiese_tsv(pairs, option, file=f)
    elif args.out is not None:
        with open(args.out, 'w') as f:
            write_multiese_tsv(pairs, option, file=f)
    else:
        write_multiese_tsv(pairs, option, file=sys.stdout)
