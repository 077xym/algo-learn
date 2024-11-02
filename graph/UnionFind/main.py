class UnionFind:
    node_to_set = {}
    set_to_node = {}

    def __init__(self, S):
        for i in range(len(S)):
            self.node_to_set[S[i]] = i
            self.set_to_node[i] = [S[i]]

    def find(self, u):
        return self.node_to_set[u]

    def union(self, u, v):
        set_u = self.node_to_set[u]
        set_v = self.node_to_set[v]
        node_set_v = self.set_to_node[set_v]
        self.set_to_node.pop(set_v)
        for n in node_set_v:
            self.node_to_set[n] = set_u
            self.set_to_node[set_u].append(n)

    def print_cur_set(self):
        for s in self.set_to_node.keys():
            print('set {}: nodes: {}\n'.format(s, self.set_to_node[s]))