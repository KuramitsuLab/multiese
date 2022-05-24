import sys
import csv


def main():
    tuples = []
    for file in sys.argv[1:]:
        with open(file) as f:
            for line in f:
                term, sep, desc = line.strip().partition('とは、')
                if sep != '':
                    if term.startswith('[') and term.endswith(']'):
                        for t in term[1:-1].split('|'):
                            tuples.append((t, desc))
                    else:
                        tuples.append((term, desc))
    with open('kogi_dic.tsv', 'w') as f:
        f = csv.writer(f, delimiter="\t")
        for term, desc in tuples:
            f.writerow((f'dic: {term}', desc))
    with open('termdic.py', 'w') as f:
        f.write('''
def load_term():
    return {
''')
        for term, desc in tuples:
            f.write(f'\t\t"{term}": "{desc}",\n')
        f.write('''
def load_term():
    }
''')


if __name__ == '__main__':
    """
    python3 make_dic.py term.txt
    """
    main()
