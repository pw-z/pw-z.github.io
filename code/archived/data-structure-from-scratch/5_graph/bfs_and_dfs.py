from functools import wraps

from graph import Graph
from graph import Vertex


# def print_start_and_end(func):
#     @wraps(func)
#     def wrap(*args, **kwargs):
#         print('BFS -> ', end='')
#         func(*args, **kwargs)
#         print('END')
#
#     return wrap


# @print_start_and_end
def bfs(g: Graph):
    """breadth first search 图的广度优先搜索"""
    all_vertex = g.get_all_vertex()  # 顶点表 list[Vertex,Vertex,Vertex,,,]
    is_visited = {}  # 标记顶点是否被访问过，key=顶点id，value=1为被访问过
    ver_queue = []

    print('BFS -> ', end='')
    for vertex in all_vertex:  # 外层循环：遍历所有联通分量
        # print('try new component' + '_' * 20)
        if vertex.key not in is_visited.keys():

            # 处理联通分量第一个顶点，初始化队列
            print(vertex.key + ' -> ', end='')
            is_visited[vertex.key] = 1
            ver_queue.append(vertex)

            # 中层循环：遍历该联通分量
            while len(ver_queue) > 0:
                cur = ver_queue.pop(0)  # 当前处理的顶点
                # 内层循环：遍历某顶点所有邻接顶点
                for vertex_ in cur.get_all_neighbor():
                    if is_visited.get(vertex_) is None:
                        # 访问过后将该顶点入队列，等待后续访问其相邻节点
                        # 由于此处vertex_是字符串，队列里需要存入Vertex类
                        # 前面构造Vertex类的时候图省事，此处只好再从g中取下
                        # print('visit ' + vertex_)
                        print(vertex_ + ' -> ', end='')
                        is_visited[vertex_] = 1
                        ver_queue.append(g.get_vertex(key=vertex_))
    print('END')


def dfs(g: Graph):
    """depth first search 图的深度优先搜索"""

    all_vertex = g.get_all_vertex()
    # 换个写法记录是否被访问过，列表坐标作为key标记对应顶点
    # 这样做的前提是，顶点的key是int类型的（或可兼容的）
    is_visited = [False for _ in range(len(all_vertex) + 1)]

    def dfs_recursive(v: Vertex):
        # print('visit ' + v.key)  # 访问
        print(v.key + ' -> ', end='')
        is_visited[int(v.key)] = True  # 标记
        for vertex_ in v.get_all_neighbor():  # 返回的是邻接顶点的key，str类型，不是Vertex类型
            if not is_visited[int(vertex_)]:
                dfs_recursive(g.get_vertex(vertex_))  # 递归向下遍历

    print('DFS_Recur -> ', end='')
    for vertex in all_vertex:
        # print('try new component' + '_' * 20)
        if not is_visited[int(vertex.key)]:
            dfs_recursive(vertex)
    print('END')


def dfs_unrecursive(g: Graph):
    """depth first search 图的深度优先搜索 非递归实现"""
    # 注意对比以下非递归实现与BFS的细微区别（queue vs stack）

    all_vertex = g.get_all_vertex()
    is_instack = [False for _ in range(len(all_vertex) + 1)]
    ver_stack = []

    print('DFS_unRecur -> ', end='')
    for vertex in all_vertex:
        if not is_instack[int(vertex.key)]:

            is_instack[int(vertex.key)] = True  # 标记
            ver_stack.append(vertex)
            while len(ver_stack) > 0:
                vertex_ = ver_stack.pop()
                # pop不传参则默认处理最后一个元素 （index = -1）
                # print('visit ' + vertex_.key)
                print(vertex_.key + ' -> ', end='')
                for v_str in vertex_.get_all_neighbor():
                    if not is_instack[int(v_str)]:
                        ver_stack.append(g.get_vertex(v_str))
                        is_instack[int(v_str)] = True  # 标记
    print('END')


if __name__ == '__main__':
    g = Graph()
    for i in range(1, 12):
        g.insert_vertex(str(i))

    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(5, 6)
    g.add_edge(5, 7)
    g.add_edge(3, 7)

    g.add_edge(8, 9)
    g.add_edge(8, 10)
    g.add_edge(9, 11)
    g.add_edge(11, 10)
    g.add_edge(10, 8)

    bfs(g)
    print('*' * 50)
    dfs(g)
    print('*' * 50)
    dfs_unrecursive(g)
