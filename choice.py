import random


def optional_random(option, factor=-1):
    r = option.get('random', random.random())
    if factor == -1:
        factor = random.randint(0, 5)
    factor = 10**(factor+3)
    return (int(r * factor) % 1000) / 1000


def random_seed(option, seed=0):
    r = option.get('random', random.random())
    return int(seed + 100 * r)


def optional_choice(option, s, seed=0):
    return alt(s, option, random_seed(option, seed))


def alt(s, option=None, factor=-1):  # alternative の略
    choice = s.split('|') if isinstance(s, str) else s
    if len(choice) == 1:
        return choice[0]
    if option is None:
        r = random.random()
    else:
        r = optional_random(option, factor)
    return choice[int(r * len(choice)) % len(choice)]


ChoiceDic = {}


def isChoiceString(s):
    return s.startswith('[') and s.endswith(']')


def update_choice_dic(choice):
    if isChoiceString(choice):
        choice = choice[1:-1]
        ss = choice.split('|')
        s = ss[0]
        if s not in ChoiceDic:
            ChoiceDic[s] = choice
        else:
            ChoiceDic[s] = ChoiceDic[s] + '|' + choice


if __name__ == '__main__':
    option = {
        'random': random.random()
    }
    print(option)
    for i in range(10):
        print(f'factor={i}', alt("A|B|C", option, factor=i),
              optional_random(option, factor=i))
