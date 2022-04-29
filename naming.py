
from importlib import import_module
import re
BEGIN = '([^A-Za-z0-9]|^)'
END = ('(?![A-Za-z0-9]|$)')
VARPAT = re.compile(BEGIN+r'([a-z]+)(\d?)'+END)

PREFIX = {  # これは使われていない
    's': ('文字列', ''),
    'alist': ('リスト', ''),
    'atuple': ('タプル', ''),
    'aset': ('セット', ''),
    'element': ('[|文字列|[リスト|タプル|辞書|セット]]', ''),
    'obj': ('[オブジェクト|]', ''),
    'adict': ('辞書', ''),
    'key': ('[キー|]', ''),
    'filename': ('[ファイル[名|パス]|文字列]', ''),
    'adate': ('日付', ''),
    'dt': ('日時', ''),
    'df': ('データフレーム', ''),
    'args': ('引数[|列|リスト]', ''),
    'colname': ('', '[行|カラム]'),
}


def _ta(name, number):
    prefix, suffix = PREFIX.get(name, ('', ''))
    if prefix == '' and suffix == '':
        if name.endswith('func'):
            prefix = '関数'
    return f'{name}{number}', f'{prefix}{name}{number}{suffix}'


def type_augmentation(doc):
    names = [_ta(x[1], x[2]) for x in VARPAT.findall(doc)]
    doc = re.sub(VARPAT, r'\1@\2\3@', doc)  # @s@
    for old, new in names:
        if old != new:
            doc = doc.replace(f'@{old}@', new)
    return doc.replace('@', '')


def _replace_vars(s, oldnews):
    s = re.sub(VARPAT, r'\1@\2\3@', s)  # @s@
    for old, new in oldnews:
        s = s.replace(f'@{old}@', new)
    return s.replace('@', '')


def _check_variables(doc, code):
    names = [(x[1], x[2]) for x in VARPAT.findall(doc)]
    ss = set(name[0] for name in names if names[1] != '')
    if len(ss) == 0:
        return doc, code
    d = {name: [] for name in ss}
    for name in names:
        if name[0] in ss:
            d[name[0]].append(name[1])
    oldnews = []
    for key in d:
        order_names = d[key]
        sorted_names = list(sorted(order_names))
        if order_names != sorted_names:
            print('diff', key, order_names, sorted_names)
            oldnews += [(key+s1, key+s2)
                        for s1, s2 in zip(order_names, sorted_names) if s1 != s2]
    doc = _replace_vars(doc, oldnews)
    code = _replace_vars(code, oldnews)
    return doc, code


def special_token(variable_name, d):
    if 'name' in variable_name:
        suffix = d.get('name', 0)
        d['name'] = suffix + 1
        return f'<name{suffix}>'
    if variable_name in ['s', 's2', 's3', 's4']:
        suffix = d.get('str', 0)
        d['str'] = suffix + 1
        return f'<str{suffix}>'
    if variable_name in ['df', 'df2', 'df3', 'df4']:
        suffix = d.get('df', 0)
        d['df'] = suffix + 1
        return f'<df{suffix}>'
    if variable_name in ['n', 'n2', 'n3', 'x', 'y', 'z']:
        suffix = d.get('num', 0)
        d['name'] = suffix + 1
        return f'<num{suffix}>'
    suffix = d.get('var', 0)
    d['var'] = suffix + 1
    return f'<var{suffix}>'


if __name__ == '__main__':
    print(type_augmentation('df1のcolname2をs3とsとs2に置き換える'))
