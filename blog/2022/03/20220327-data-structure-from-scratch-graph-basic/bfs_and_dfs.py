from graph import Graph
from graph import Vertex


def bfs(g: Graph):
    """breadth first search 图的广度优先搜索"""
    is_visited = {}  # 标记顶点是否被访问过，key=顶点id，value=1为被访问过
    ver_queue = []
    all_vertex = g.get_all_vertex()  # 顶点表 list[Vertex,Vertex,Vertex,,,]
    if len(all_vertex) == 0:
        return

    for vertex in all_vertex:  # 对每一个联通分量进行处理
        print('try new component' + '_'*20)
        if vertex.key not in is_visited.keys():
            ver_queue.append(vertex)  # 将该联通分量的第一个顶点入队
            print('visit ' + vertex.key)  # 访问顶点
            is_visited[vertex.key] = 1  # 标记顶点被访问过

            while len(ver_queue) > 0:
                cur = ver_queue.pop(0)  # 当前处理的顶点
                for vertex_ in cur.get_all_edge():
                    if is_visited.get(vertex_) is None:
                        print('visit ' + vertex_)
                        is_visited[vertex_] = 1
                        # 访问过后将该顶点入队列，等待后续访问其相邻节点
                        # 由于此处vertex_是字符串，队列里需要存入Vertex类
                        # 前面构造Vertex类的时候图省事，此处只好再从g中取下
                        # 妈的有这几句话的功夫前面都改好了
                        # 算了就这样吧，啊我好懒
                        v = g.get_vertex(key=vertex_)
                        ver_queue.append(v)


def dfs(g: Graph):
    """depth first search 图的深度优先搜索"""
    is_visited = {}


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
    g.add_edge(12, 15)
    g.add_edge(15, 14)
    g.add_edge(14, 12)

    bfs(g)






        


