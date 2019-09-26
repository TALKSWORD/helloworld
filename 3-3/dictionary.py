class Node:
    def __init__(self, char, end, frequency):
        self.char = char
        self.end = end
        self.frequency = frequency
        self.nextNode = []
        self.nextChar = []

    def set_end(self, end):
        self.end = end

    def ser_frequency(self, frequency):
        self.frequency = frequency

    def frequency_one_plus(self):
        self.frequency = self.frequency + 1

    def add_next(self, node):
        self.nextNode.append(node)
        self.nextChar.append(node.getchar())

    def getchar(self):
        return self.char


class TrieTree:
    def __init__(self):
        self.root = Node("", False, 0)

    def insert(self, word):
        root = self.root
        for c in word:
            if c not in root.nextChar:
                node = Node(c, False, 0)
                root.add_next(node)
                root = node
            else:
                root = root.nextNode[root.nextChar.index(c)]
        root.set_end(True)
        root.frequency_one_plus()

    def search(self, word):
        root = self.root
        for c in word:
            if c not in root.nextChar:
                return False
            else:
                root = root.nextNode[root.nextChar.index(c)]
        return True
        # if root.end is True:
        #     return True
        # else:
        #     return False

    def print_all(self, rt, s):
        root = rt
        for node in root.nextNode:
            if node.end is not True:
                self.print_all(node, s+node.getchar())
            else:
                # s += node.getchar()
                # print(s+node.getchar()+"\t\t"+str(node.frequency))
                f.write(s+node.getchar()+"\n")
                self.print_all(node, s+node.getchar())


def divide():
    tree = TrieTree()
    with open('F:\\dictionary.txt', encoding='utf-8') as f:
        data = f.read().split()
        for ss in data:
            tree.insert(ss)
        f.close()
    with open('F:\\division.txt', 'w+') as w:
        with open('F:\\199801_sent.txt') as f:
            s = ""
            read_data = f.readlines()
            for line in read_data:
                for c in line:
                    if tree.search(s+c) is True:
                        s += c
                    else:
                        w.write(s+"/")
                        # print(s+"/", end="")
                        s = c
                w.write("\n")
                # print()
            f.close()
        w.close()


if __name__ == '__main__':
    divide()
    # tree = TrieTree()
    # with open('F:\\199801_seg.txt') as f:
    #     read_data = f.read()
    #     a = read_data.split()
    #     start = False
    #     ss = ""
    #     for s in a:
    #         index = s.index('/')
    #         if s.find('[') != -1:
    #             tree.insert(s[s.index('[')+1:index])
    #         else:
    #             tree.insert(s[0:index])
    #     with open('F:\\dictionary.txt', 'w+', encoding='utf-8') as f:
    #         tree.print_all(tree.root, "")

    # if start is True:
    #     if s.find(']') != -1:
    #         start = False
    #     ss += s[0:index]
    #     tree.insert(ss)
    # else:
    #     if s.find('[') != -1:
    #         start = True
    #         index_l = s.index('[')
    #         ss += s[index_l:index]
    #     else:
    #         tree.insert(s[0:index])

    # tree.insert('你好')
    # tree.insert('你好')
    # tree.insert('你好中国')
    # tree.insert('史纪元')
    # tree.insert('史前巨像')
    # tree.insert('史记')
    # tree.print_all(tree.root, "")

