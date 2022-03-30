from graph import Graph

def BFS(g: Graph):
    """图的广度优先遍历"""
    is_visited = {}  # 标记顶点是否被访问过，key=顶点id，value=1为被访问过
    ver_queue = []
    for vertex in g.get_all_vertexs():
        


