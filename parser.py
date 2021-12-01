import pegtree as pg
from pegtree import ParseTree
from pegtree.visitor import ParseTreeVisitor
from choice import update_choice_dic
import tree as ntree
import pprint

peg = pg.grammar('multiese.pegtree')
parser = pg.generate(peg)


def fix(tree):
    a = [tree.epos_]
    for t in tree:
        fix(t)
        a.append(t.epos_)
    for key in tree.keys():
        a.append(fix(tree.get(key)).epos_)
    tree.epos_ = max(a)
    return tree


class MultieseParser(ParseTreeVisitor):
    def __init__(self):
        ParseTreeVisitor.__init__(self)

    def parse(self, s: str):
        tree = parser(s)
        node = self.visit(tree)
        return node

    def acceptChunk(self, tree: ParseTree):
        s = str(tree)
        node = ntree.parse(s)
        return ntree.系列(*node.flatten()).simplify()

    def acceptSeq(self, tree: ParseTree):
        ns = []
        # print(repr(tree))
        for t in tree:
            node = self.visit(t)
            node.flatten(ns)
        return ntree.系列(*ns)

    def acceptBlock(self, tree: ParseTree):
        # print(repr(tree))　(1+2)*3
        return ntree.グループ(self.visit(tree[0]))

    def acceptChoice(self, tree: ParseTree):
        ns = []
        for t in tree:
            ns.append(self.visit(t))
        node = ntree.Choice(ns)
        if ns[0].__class__.__name__ != '助詞':
            # ntree.update_choice_dic(node.stringfy())  # 類義語辞書を更新する
            update_choice_dic(node.stringfy())  # 類義語辞書を更新する
        return node

    def acceptExpression(self, tree: ParseTree):
        s = str(fix(tree))
        return ntree.コード(s)

    def acceptSymbol(self, tree: ParseTree):
        s = str(fix(tree))
        return ntree.コード(s)

    def acceptAnnotation(self, tree: ParseTree):
        name = str(tree[0])  # アノテーション種類
        ns = [self.visit(t) for t in tree[1:]]
        return ntree.annotation(name, ns)


mult = MultieseParser()


def multiese_parser(s: str):
    return mult.parse(s)


def test_for_nobu(s):
    print(s)
    print('=>', repr(mult.parse(s)))
    print()


if __name__ == '__main__':
    test_for_nobu('データフレームdfを降順にソートする')
    test_for_nobu('望遠鏡で泳ぐ子犬を見た')
    test_for_nobu('望遠鏡で{泳ぐ子犬}を見た')
    test_for_nobu('望遠鏡で[子犬|とうきび]を見た')
    test_for_nobu('@type(df, データフレーム)について、望遠鏡で子犬を見てない')  # 否 見た 80%
    test_for_nobu('@type(df)の先頭を見る')  # Keyword
    test_for_nobu('望遠鏡で{子犬が泳ぐ}様子を見たら、math.pi+1を実行する')
