from graph import Graph
from graph import Vertex


def bfs(g: Graph):
    """breadth first search 图的广度优先搜索"""
    is_visited = {}  # 标记顶点是否被访问过，key=顶点id，value=1为被访问过
    ver_queue = []
    all_vertex = g.get_all_vertex()  # 顶点表 list[Vertex,Vertex,Vertex,,,]

    for vertex in all_vertex:  # 对每一个联通分量进行处理
        print('try new component' + '_' * 20)
        if vertex.key not in is_visited.keys():
            ver_queue.append(vertex)  # 将该联通分量的第一个顶点入队

            while len(ver_queue) > 0:
                cur = ver_queue.pop(0)  # 当前处理的顶点
                print('visit ' + cur.key)
                is_visited[cur.key] = 1
                for vertex_ in cur.get_all_neighbor():
                    if is_visited.get(vertex_) is None:
                        # 访问过后将该顶点入队列，等待后续访问其相邻节点
                        # 由于此处vertex_是字符串，队列里需要存入Vertex类
                        # 前面构造Vertex类的时候图省事，此处只好再从g中取下
                        ver_queue.append(g.get_vertex(key=vertex_))
                        is_visited[vertex_] = 1


def dfs(g: Graph):
    """depth first search 图的深度优先搜索"""

    all_vertex = g.get_all_vertex()
    # 换个写法记录是否被访问过，列表坐标作为key标记对应顶点
    # 这样做的前提是，顶点的key是int类型的（或可兼容的）
    is_visited = [False for _ in range(len(all_vertex) + 1)]

    def dfs_recursive(v: Vertex):
        print('visit ' + v.key)  # 访问
        is_visited[int(v.key)] = True  # 标记
        for vertex_ in v.get_all_neighbor():  # 返回的是邻接顶点的key，str类型，不是Vertex类型
            if not is_visited[int(vertex_)]:
                dfs_recursive(g.get_vertex(vertex_))  # 递归向下遍历

    for vertex in all_vertex:
        print('try new component' + '_' * 20)
        if not is_visited[int(vertex.key)]:
            dfs_recursive(vertex)


def dfs_unrecursive(g: Graph):
    """depth first search 图的深度优先搜索 非递归实现"""

    all_vertex = g.get_all_vertex()
    count = len(all_vertex)
    is_visited = [False for _ in range(count + 1)]

    ver_stack = []

    for vertex in all_vertex:  # 外循环：对连通分量遍历处理
        print('try new component' + '_' * 20)
        if not is_visited[int(vertex.key)]:
            ver_stack.append(vertex)  # 该分量首个顶点入栈（存Vertex类，不是str）
            while len(ver_stack) > 0:
                vertex_ = ver_stack.pop()
                # pop不传参则默认处理最后一个元素 （index = -1）
                print('visit ' + vertex_.key)  # 访问
                is_visited[int(vertex_.key)] = True  # 标记
                for v_str in vertex_.get_all_neighbor():
                    if not is_visited[int(v_str)]:
                        ver_stack.append(g.get_vertex(v_str))


if __name__ == '__main__':
    g = Graph()
    for i in range(1, 16):
        g.insert_vertex(str(i))

    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(3, 4)
    g.add_edge(3, 6)
    g.add_edge(6, 2)
    g.add_edge(6, 5)
    g.add_edge(4, 7)

    g.add_edge(8, 9)
    g.add_edge(8, 10)
    g.add_edge(9, 10)
    g.add_edge(10, 11)

    g.add_edge(12, 13)
    g.add_edge(12, 14)
    g.add_edge(12, 15)
    g.add_edge(15, 14)
    g.add_edge(14, 12)

    # bfs(g)
    # print('*' * 50 + '\n' + '*' * 50)
    dfs(g)
    print('*' * 50 + '\n' + '*' * 50)
    dfs_unrecursive(g)
