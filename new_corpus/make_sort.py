import sys


def main():
    tuples = []
    for file in sys.argv[1:]:
        with open(file) as f:
            for line in f:
                tuples.append(line.strip())
    tuples.sort()
    for line in tuples:
        print(line)


if __name__ == '__main__':
    """
    python3 make_dic.py term.txt
    """
    main()
