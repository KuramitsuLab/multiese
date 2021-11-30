import random

def optional_random(option, factor=0):
    r = option.get('random', random.random())
    factor = 10**(factor+1)
    return (int(r * factor) % 1000) / 1000

def alt(s, option=None, factor=0):  # alternative の略
    choice = s.split('|') if isinstance(s, str) else s
    if len(choice) == 1:
        return choice[0]
    if option is None:
        r = random.random()
    else:
        r = optional_random(option, factor)
    return choice[int(r * len(choice)) % len(choice)]


def random_seed(option, seed=0):
    r = option.get('random', random.random())
    return int(seed + 100 * r)

def optional_choice(option, s, seed=0):
    return alt(s, random_seed(option, seed))

if __name__ == '__main__':
    option = {
        'random': random.random()
    }
    print(option)
    for i in range(10):
        print(f'factor={i}', alt("A|B|C", option, factor=i), optional_random(option, factor=i))