import random

Functions = globals()

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
            sentence_or = sentence + optional_choice(option, '、または、|、もしくは、')
            pairs_andor.append((sentence_and, code_and))
            pairs_andor.append((sentence_or, code_or))
    return pairs_andor

def alt(s, random_seed):
    choice = s.split('|') if isinstance(s, str) else s
    return choice[random_seed % len(choice)]

def random_seed(option, seed=0):
    r = option.get('random', random.random())
    return int(seed + 100 * r)

def optional_choice(option, s, seed=0):
    return alt(s, random_seed(option, seed))

def perform_if(pairs, option):
    ## pairs.extends(perform_not(pairs, option)) # @@not を加える
    pairs_if = []
    for sentence, code in pairs:
        code_if = f'if {code} :'
        sentence, _ = remove_whether(sentence)
        sentence_if = optional_choice(option, 'もし|もし|') + sentence
        if sentence.endswith('い'):   # 形容詞のとき
            sentence_if += optional_choice(option, 'ならば|なら|場合|とき')
        else:
            sentence_if += optional_choice(option, 'ならば|なら|の場合|のとき')
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
    if s.endswith(s) and len(s)>2:
        return s[-2] in 'けせてねれえげべ'
    return False

def transform_verb_and_then(s, random_seed):
    if s.endswith('する'):
        return s[:-2]+alt('して、|し、', random_seed)
    if s.endswith('ずる'): #論ずる　
        return s[:-2]+alt('じて、|じ、', random_seed)
    if isGroup2Verb(s):  # グループ２ # ラ行と区別が難しい
        return s[:-1]+alt('、|、|て、', random_seed)
    if s.endswith('く'):  # 書く 
        return s[:-1]+alt('き、|いて、', random_seed)
    if s.endswith('す'):  # 探す 
        return s[:-1]+alt('し、|して、', random_seed)
    if s.endswith('つ'):  # 勝つ 
        return s[:-1]+alt('ち、|って、', random_seed)
    if s.endswith('ぬ'):  # 死ぬ 
        return s[:-1]+alt('に、|んて、', random_seed)
    if s.endswith('む'):  # 読む 
        return s[:-1]+alt('み、|んで、', random_seed)
    if s.endswith('る'):  # 切る   ラ行
        return s[:-1]+alt('り、|って、', random_seed)
    if s.endswith('う'):  # 笑う 
        return s[:-1]+alt('い、|って、', random_seed)
    if s.endswith('ぐ'):  # 防ぐ 
        return s[:-1]+alt('ぎ、|いで、', random_seed)
    if s.endswith('ぶ'):  # 遊ぶ 
        return s[:-1]+alt('び、|んで、', random_seed)
    return None

def transform_verb_and_noun(s, noun, random_seed=0):
    if s.endswith('する'):
        return s[:-2]+alt('した|された', random_seed) + noun
    if s.endswith('ずる'): #論ずる　
        return s[:-2]+alt('じた、|じられた、', random_seed) + noun
    if isGroup2Verb(s):  # グループ２ # ラ行と区別が難しい
        return s[:-1]+alt('た|られた', random_seed) + noun
    if s.endswith('く'):  # 書く 
        return s[:-1]+alt('いた、|かれた、', random_seed) + noun
    if s.endswith('す'):  # 探す 
        return s[:-1]+alt('した、|された、', random_seed) + noun
    if s.endswith('つ'):  # 勝つ 
        return s[:-1]+alt('った|たれた', random_seed) + noun
    if s.endswith('ぬ'):  # 死ぬ 
        return s[:-1]+alt('んだ|なれた', random_seed) + noun
    if s.endswith('む'):  # 読む 
        return s[:-1]+alt('んだ|まれた', random_seed) + noun
    if s.endswith('る'):  # 切る   ラ行
        return s[:-1]+alt('った|られた', random_seed) + noun
    if s.endswith('う'):  # 笑う 
        return s[:-1]+alt('った|われた、', random_seed) + noun
    if s.endswith('ぐ'):  # 防ぐ 
        return s[:-1]+alt('いだ|がれた', random_seed) + noun
    if s.endswith('ぶ'):  # 遊ぶ 
        return s[:-1]+alt('んだ|ばれた', random_seed) + noun
    return None

def perform_noun(pairs, option): # 名詞に変える
    pairs_noun = []
    for sentence, code in pairs:
        sentence_and_noun = transform_verb_and_noun(sentence, '', random_seed(option))
        if sentence_and_noun:
            noun = optional_choice(option, option.get('action-with', '結果') + '|値|結果') 
            pairs_noun.append((sentence_and_noun + noun, code))
    return pairs_noun


def perform_let(pairs, option):  # 代入文に変える
    pairs_let = []
    for sentence, code in pairs:
        code_let = f'X = {code}'
        sentence_and_then = transform_verb_and_then(sentence, random_seed(option))
        if sentence_and_then:
            sentence_let = sentence_and_then + 'X' + optional_choice(option, 'にする|とする|に代入する')
            pairs_let.append((sentence_let, code_let))
            noun = optional_choice(option, option.get('action-with', '結果'))
            sentence = transform_verb_and_noun(sentence, noun, 0)
        sentence_let = sentence + 'をX' + optional_choice(option, 'にする|とする|に代入する')
        pairs_let.append((sentence_let, code_let))
        if sentence.endswith('かどうか'):
            ## 小さいかどうか　=> 小さいとき、Xを真とする
            s, _ = remove_whether(sentence)
            sentence_let = s + 'とき、Xを真' + optional_choice(option, 'にする|とする', seed=1)
            pairs_let.append((sentence_let, code_let))
    return pairs_let

def perform_let_self(pairs, option):
    pairs_let_self = []
    return pairs

def perform_inplace(pairs, option):
    pairs_inplace = []
    return pairs

def perform_dot(pairs, option):
    pairs_dot = []
    return pairs

def perform_it(pairs, option):
    pairs_it = []
    return pairs

def perform_option(pairs, option):
    pairs_option = []
    return pairs

def perform_check(pairs, option):
    pairs_check = []
    for sentence, code in pairs:
        sentence_check = sentence + optional_choice(option, 'を表示する|を確認する|を調べる|を見る')
        pairs_check.append((sentence_check, code))
    return pairs_check

def perform_get(pairs, option):
    pairs_get = []
    for sentence, code in pairs:
        sentence_get = sentence + optional_choice(option, 'を取得する|を得る|を抽出する')
        pairs_get.append((sentence_get, code))
    return pairs_get

def perform_calc(pairs, option):
    pairs_calc = []
    for sentence, code in pairs:
        sentence_calc = sentence + optional_choice(option, 'を計算する|を求める|を算出する')
        pairs_calc.append((sentence_calc, code))
    return pairs_calc

def perform_filter(actions, pairs, option):
    actions = actions.split('.')   # e.g.: @@if.not
    for action in actions:
        if 'action-with' in option:
            del option['action-with']
        if action.endswith(']'): # argument
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
