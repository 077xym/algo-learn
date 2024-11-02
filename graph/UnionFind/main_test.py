from main import UnionFind

if __name__ == '__main__':
    a = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    uf = UnionFind(a)

    uf.union("A", "B")
    uf.union("B", "D")
    uf.union("F", "G")

    uf.union("B", "G")
    uf.print_cur_set()


