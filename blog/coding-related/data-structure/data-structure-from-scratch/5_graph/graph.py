from re import S


class Vertex:
    """
    顶点表元素，其中直接用self.edge存储对应边表
    """

    def __init__(self, key: str):
        self.key = key
        self.edge = {}  # 边表字典，key=所指向的节点id，value=权重

    def add_neighbor(self, key: str, cost):
        self.edge[str(key)] = cost

    def __str__(self):
        desc = ''
        if len(self.edge) > 0:
            for edge in self.edge.items():
                desc += f'({self.key}, {edge[0]}, {edge[1]})\n'
            desc = desc[:-1]  # 去除多余的换行
        else:
            desc = f'({self.key}, -, -)'
        return desc

    def get_all_neighbor(self) -> list:
        return list(self.edge.keys())


# class Edge:
#     def __init__(self, from_, to_, cost=None):
#         self.from_ = from_
#         self.to_ = to_
#         self.cost = cost


class Graph:

    def __init__(self):
        self.vertexList = {}

    def insert_vertex(self, ver_id: str):
        """插入顶点"""
        self.vertexList[ver_id] = Vertex(ver_id)

    def add_edge(self, a, b, cost=0):
        """在a、b两节点之间添加一条边，默认无权重"""
        a, b = str(a), str(b)
        if a not in self.vertexList:
            print(f'{a} not found, add vertex first please')
            return
        if b not in self.vertexList:
            print(f'{b} not found, add vertex first please')
            return
        ver = self.vertexList.get(a)
        ver.add_neighbor(b, cost)

    def delete_vertex(self, v_id: str):
        """根据id号删除顶点"""
        pass

    def remove_edge(self, a, b):
        """移除a、b两节点之间的边"""
        pass

    def print_graph(self):
        """打印所有节点及节点间关系"""
        for ver in self.vertexList.values():
            print(ver)

    def get_all_vertex(self) -> list:
        return list(self.vertexList.values())

    def get_vertex(self, key: str) -> Vertex:
        for _ in self.vertexList.values():
            if _.key == key:
                return _


if __name__ == '__main__':
    g = Graph()
    for i in range(5):
        g.insert_vertex(str(i))
    g.add_edge(1, 2, 99)
    g.add_edge(1, 3, 88)
    g.add_edge(1, 4, 77)
    g.add_edge(2, 4, 66)
    g.print_graph()
    """output
    (0, -, -)
    (1, 2, 99 )
    (1, 3, 88 )
    (1, 4, 77 )
    (2, 4, 66 )
    (3, -, -)
    (4, -, -)
    """


