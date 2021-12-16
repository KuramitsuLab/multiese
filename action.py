import random
from choice import alt


def remove_whether(sentence):
    if sentence.endswith('かどうか'):
        return sentence[:-4], 'かどうか'
    if sentence.endswith('か否か'):
        return sentence[:-4], 'か否か'
    if sentence.endswith('か'):
        return sentence[:-1], 'か'
    return sentence, ''


def transform_not(code):
    if '==' in code:
        return code.replace('==', '!=')
    if '!=' in code:
        return code.replace('!=', '==')
    if ' is ' in code and not 'is not' in code:
        return code.replace(' is ', ' is not ')
    if ' in ' in code and not 'not in' in code:
        return code.replace(' in ', ' not in ')
    if 'True' in code:
        return code.replace('True', 'False')
    if 'False' in code:
        return code.replace('False', 'True')
    return f'not {code}'


def perform_not(pairs, option):
    pairs_not = []
    for sentence, code in pairs:
        code_not = transform_not(code)
        sentence, whether = remove_whether(sentence)
        if sentence[-1] == 'い':
            # e.g.: a が 0 と等しい
            if 'くない' in sentence:
                sentence_not = sentence.replace('くない', 'い') + whether
            else:
                sentence_not = sentence[:-1] + 'くない' + whether
        else:
            # e.g.: a が偶数
            if 'でない' in sentence:
                sentence_not = sentence.replace('でない', '') + whether
            else:
                sentence_not = sentence + 'でない' + whether
        pairs_not.append((sentence_not, code_not))
    return pairs_not


def perform_andor(pairs, option):
    pairs_andor = []
    if option.get('partial', True):
        for sentence, code in pairs:
            code_and = f'{code} and'
            code_or = f'{code} or'
            sentence, _ = remove_whether(sentence)
            sentence_and = sentence + '、かつ、'
            sentence_or = sentence + alt('、または、|、もしくは、')
            pairs_andor.append((sentence_and, code_and))
            pairs_andor.append((sentence_or, code_or))
    return pairs_andor


def perform_if(pairs, option):
    # pairs.extends(perform_not(pairs, option)) # @@not を加える
    pairs_if = []
    for sentence, code in pairs:
        code_if = f'if {code} :'
        sentence, _ = remove_whether(sentence)
        sentence_if = alt('もし|もし|') + sentence
        if sentence.endswith('い'):   # 形容詞のとき
            sentence_if += alt('ならば|なら|場合|とき')
        else:
            sentence_if += alt('ならば|なら|の場合|のとき')
        pairs_if.append((sentence_if, code_if))
    return pairs_if


def perform_while(pairs, option):
    pairs_while = []
    for sentence, code in pairs:
        code_while = f'while {code} :'
        sentence, _ = remove_whether(sentence)
        if sentence.endswith('い'):
            sentence_while = sentence + '間'
        else:
            sentence_while = sentence + 'の間'
        pairs_while.append((sentence_while, code_while))
    return pairs_while


def isGroup2Verb(s):
    if s.endswith(s) and len(s) > 2:
        return s[-2] in 'えけせてねれえげべ得見'
    return False


def transform_verb_and_then(s):
    if s.endswith('する'):
        return s[:-2]+alt('して、|し、')
    if s.endswith('ずる'):  # 論ずる　
        return s[:-2]+alt('じて、|じ、')
    if isGroup2Verb(s):  # グループ２ # ラ行と区別が難しい
        return s[:-1]+alt('、|、|て、')
    if s.endswith('く'):  # 書く
        return s[:-1]+alt('き、|いて、')
    if s.endswith('す'):  # 探す
        return s[:-1]+alt('し、|して、')
    if s.endswith('つ'):  # 勝つ
        return s[:-1]+alt('ち、|って、')
    if s.endswith('ぬ'):  # 死ぬ
        return s[:-1]+alt('に、|んて、')
    if s.endswith('む'):  # 読む
        return s[:-1]+alt('み、|んで、')
    if s.endswith('る'):  # 切る   ラ行
        return s[:-1]+alt('り、|って、')
    if s.endswith('う'):  # 笑う
        return s[:-1]+alt('い、|って、')
    if s.endswith('ぐ'):  # 防ぐ
        return s[:-1]+alt('ぎ、|いで、')
    if s.endswith('ぶ'):  # 遊ぶ
        return s[:-1]+alt('び、|んで、')
    return None


def transform_verb_and_noun(s):
    if s.endswith('する'):
        return s[:-2]+alt('した|した|された')
    if s.endswith('ずる'):  # 論ずる　
        return s[:-2]+alt('じた|じた|じられた、')
    if isGroup2Verb(s):  # グループ２ # ラ行と区別が難しい
        return s[:-1]+alt('た|た|られた')
    if s.endswith('く'):  # 書く
        return s[:-1]+alt('いた|いた|かれた')
    if s.endswith('す'):  # 探す
        return s[:-1]+alt('した|した|された')
    if s.endswith('つ'):  # 勝つ
        return s[:-1]+alt('った|った|たれた')
    if s.endswith('ぬ'):  # 死ぬ
        return s[:-1]+alt('んだ|んだ|なれた')
    if s.endswith('む'):  # 読む
        return s[:-1]+alt('んだ|んだ|まれた')
    if s.endswith('る'):  # 切る   ラ行
        return s[:-1]+alt('った|った|られた')
    if s.endswith('う'):  # 笑う
        return s[:-1]+alt('った|った|われた、')
    if s.endswith('ぐ'):  # 防ぐ
        return s[:-1]+alt('いだ|いだ|がれた')
    if s.endswith('ぶ'):  # 遊ぶ
        return s[:-1]+alt('んだ|んだ|ばれた')
    return None


def perform_noun(pairs, option):  # 名詞に変える
    pairs_noun = []
    for sentence, code in pairs:
        sentence_and_noun = transform_verb_and_noun(sentence)
        if sentence_and_noun:
            noun = option.get('action-with', '結果')
            noun = alt(noun + '|結果', option, factor=3)
            pairs_noun.append((sentence_and_noun + noun, code))
    return pairs_noun


def perform_let(pairs, option):  # 代入文に変える
    pairs_let = []
    for sentence, code in pairs:
        code_let = f'X = {code}'
        sentence_and_then = transform_verb_and_then(sentence)
        if sentence_and_then:
            sentence_let = sentence_and_then + 'X' + alt('にする|とする|に代入する')
            pairs_let.append((sentence_let, code_let))
            noun = alt(option.get('action-with', '結果'))
            sentence = transform_verb_and_noun(sentence) + noun
        sentence_let = sentence + 'をX' + alt('にする|とする|に代入する')
        pairs_let.append((sentence_let, code_let))
        if sentence.endswith('かどうか'):
            # 小さいかどうか　=> 小さいとき、Xを真とする
            s, _ = remove_whether(sentence)
            sentence_let = s + 'とき、Xを真' + alt('にする|とする')
            pairs_let.append((sentence_let, code_let))
    return pairs_let


def perform_let_self(pairs, option):
    pairs_let_self = []
    for sentence, code in pairs:
        name = code[:code.find('.')]
        code_let_self = f'{name} = {code}'
        sentence_and_then = transform_verb_and_then(sentence)
        if sentence_and_then:
            sentence_let_self = sentence_and_then + name + alt('にする|とする|に代入する')
            pairs_let_self.append((sentence_let_self, code_let_self))
            sentence_let_self = sentence_and_then + alt('置き換える|再代入する')
            pairs_let_self.append((sentence_let_self, code_let_self))
            noun = alt(option.get('action-with', '結果'))
            sentence = transform_verb_and_noun(sentence) + noun
        sentence_let_self = sentence + 'を' + name + alt('にする|とする|に代入する')
        pairs_let_self.append((sentence_let_self, code_let_self))
        sentence_let_self = sentence + alt('で置き換える|を再代入する')
        pairs_let_self.append((sentence_let_self, code_let_self))
    return pairs_let_self


def perform_inplace(pairs, option):
    pairs_inplace = []
    for sentence, code in pairs:
        if code[-2] == '(':
            # e.g.: df.dropna()
            code_inplace = code[:-1] + 'inplace=True)'
        else:
            # e.g.: df.drop('price', axis=1)
            code_inplace = code[:-1] + ', inplace=True)'
        sentence_and_then = transform_verb_and_then(sentence)
        if sentence_and_then:
            sentence_inplace = sentence_and_then + alt('インプレースする|置き換える|書き換える')
            pairs_inplace.append((sentence_inplace, code_inplace))
            noun = alt(option.get('action-with', '結果'))
            sentence = transform_verb_and_noun(sentence) + noun
        sentence_inplace = sentence + alt('でインプレースする|で置き換える|で書き換える')
        pairs_inplace.append((sentence_inplace, code_inplace))
    return pairs_inplace


def perform_then(pairs, option):
    pairs_then = []
    if option.get('partial', True):
        for sentence, code in pairs:
            verb = transform_verb_and_then(sentence)
            if verb:
                pairs_then.append((verb, code+'.'))
    return pairs_then


def starts_with_var(s, var):
    if s.startswith(var) and s[len(var)] in 'のをに':
        return True
    return False


def perform_it(pairs, option):
    pairs_dot = []
    if option.get('partial', True):
        for sentence, code in pairs:
            pos = code.find('.')
            var = code[:pos]
            #print('@', sentence, var)
            if not starts_with_var(sentence, var):
                continue
            code = code[pos:]
            it = option.get('action-with', 'それ')
            sentence = sentence[len(var):]
            if sentence.startswith('の'):
                sentence = alt(['そ', '']) + sentence
            else:
                sentence = alt([it, '']) + sentence
            pairs_dot.append((sentence, code))
    return pairs_dot


def perform_check(pairs, option):
    pairs_check = []
    for sentence, code in pairs:
        verb = transform_verb_and_then(sentence)
        if not verb:
            sentence_check = sentence + alt('を表示する|を確認する|を調べる|を見る')
            pairs_check.append((sentence_check, code))
    return pairs_check


def perform_get(pairs, option):
    pairs_get = []
    for sentence, code in pairs:
        verb = transform_verb_and_then(sentence)
        if not verb:
            sentence_get = sentence + alt('を取得する|を得る|をえる|を抽出する')
            pairs_get.append((sentence_get, code))
    return pairs_get


def perform_calc(pairs, option):
    pairs_calc = []
    for sentence, code in pairs:
        verb = transform_verb_and_then(sentence)
        if not verb:
            sentence_calc = sentence + alt('を計算する|を求める|を算出する')
            pairs_calc.append((sentence_calc, code))
    return pairs_calc


Functions = globals()


def perform_filter(actions, pairs, option):
    actions = actions.split('.')   # e.g.: @@if.not
    for action in actions:
        if 'action-with' in option:
            del option['action-with']
        if action.endswith(']'):  # argument
            action, argument = action[:-1].split('[')
            option['action-with'] = argument
        if action.endswith('?'):
            action = action[:-1]
            join = True
        else:
            join = False
        f = f'perform_{action.strip()}'
        if f in Functions:
            new_pairs = Functions[f](pairs, option)
            if join:
                pairs.extend(new_pairs)
            else:
                pairs = new_pairs
    return pairs


if __name__ == '__main__':
    print(Functions)
    perform_filter('not.if', [], {})
