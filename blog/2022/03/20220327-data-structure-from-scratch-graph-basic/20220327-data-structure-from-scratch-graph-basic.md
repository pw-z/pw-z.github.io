# 图论基础知识总结及相关应用实践

*Posted on 2022.03.27 by [Zhang Pengwei](http://pwz.wiki) under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)* 


![](graph_eg.png "图结构示例")  


...SUMMARY  AND TOC HERE

---
- [图的存储结构及实现](#图的存储结构及实现)
- [图的遍历](#图的遍历)
  - [BFS](#bfs)
  - [DFS](#dfs)
- [图的经典应用](#图的经典应用)
- [热点习题及实践](#热点习题及实践)


## 图的存储结构及实现

`邻接矩阵`、`邻接表`是图的两种基本存储结构。

邻接矩阵直接用二维数组实现即可，在N*N的二维数组中，用Array[I][J]存储I点与J点的关系，可以用01表示有无关系，或用数字表示权值等。无向图的邻接矩阵是一个对称矩阵。

邻接矩阵存储稀疏图太浪费空间，由此引入邻接表。邻接表逻辑上由顶点表与边表构成，顶点表存储所有顶点，每个顶点对应一张边表，存储依附于该顶点的边。

以下基于邻接表实现一个基本的图结构：
```python
class Vertex:
    """
    顶点表元素，其中直接用self.edge存储对应边表
    """

    def __init__(self, key: str):
        self.key = key
        self.edge = {}  # 边表字典，key=所指向的节点id，value=权重

    def addNeighbor(self, key, cost):
        self.edge[key] = cost

    def __str__(self):
        desc = ''
        if len(self.edge) > 0:
            for edge in self.edge.items():
                desc += f'({self.key}, {edge[0]}, {edge[1]})\n'
            desc = desc[:-1]  # 去除多余的换行
        else:
            desc = f'({self.key}, -, -)'
        return desc


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
        ver.addNeighbor(b, cost)

    def delete_vertex(self, v_id: int):
        """根据id号删除顶点"""
        pass

    def remove_edge(self, a, b):
        """移除a、b两节点之间的边"""
        pass

    def print_graph(self):
        """打印所有节点及节点间关系"""
        for ver in self.vertexList.values():
            print(ver)


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
```


## 图的遍历

图的遍历即【从某顶点出发不重复地访问图中所有顶点】，是各种相关算法的基础，主要有两种：
* 广度优先搜索（breadth first search，简称BFS）
* 深度优先搜索（depth first search，简称DFS）

### BFS

BFS可类比二叉树的`层序遍历`，需要一个队列存储本层所访问的节点，方便进行下一层的处理。注意图不像二叉树按序遍历就可以实现每个节点的唯一访问，图中不同节点相互关联，访问时需要标记每个节点是否被访问过。

算法思路：
1. 对每个连通分量分别处理
   1. 访问顶点，入队列
   2. 从队列取出一个顶点，访问其所有邻接顶点
   3. 将每个访问过的顶点依次入队列
2. 重复上述过程，直到队空

代码实现：
```python
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
                        v = g.get_vertex(key=vertex_)
                        ver_queue.append(v)


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

"""
try new component____________________
visit 1
visit 2
visit 3
visit 4
visit 6
visit 7
visit 5
try new component____________________
try new component____________________
try new component____________________
try new component____________________
try new component____________________
try new component____________________
try new component____________________
visit 8
visit 9
visit 10
visit 11
try new component____________________
try new component____________________
try new component____________________
try new component____________________
visit 12
visit 13
visit 15
visit 14
try new component____________________
try new component____________________
try new component____________________
"""
```

### DFS

DFS可类比二叉树的`先根序遍历`， 沿着一条路径向下访问，直到走到“叶子”节点（不再有未访问的邻接顶点），向上回溯，重复这个过程直到所有顶点都被遍历。

算法思路：
1. 对每个连通分量分别处理
   1. 有未访问的邻接顶点，则向下探索，向下时将本层状态压栈
   2. 走到叶子节点了，向上回溯，重复步骤1
2. 重复上述过程直到所有节点遍历完毕


代码实现（递归）：
```python
from graph import Graph
from graph import Vertex


def dfs(g: Graph):
    """depth first search 图的深度优先搜索"""

    all_vertex = g.get_all_vertex()
    count = len(all_vertex)
    is_visited = [False for _ in range(count+1)]  
    # 换个写法，列表坐标作为key标记对应顶点，
    # 这样做的前提是，顶点的key是int类型的（或可兼容的）
    print(is_visited)

    def dfs_recursive(v: Vertex):
        print('visit ' + v.key)          # 访问
        is_visited[int(v.key)] = True    # 标记
        for vertex_ in v.get_all_neighbor():  
        # 返回的是邻接顶点的key，str类型，不是Vertex类型
            if not is_visited[int(vertex_)]:
                v_ = g.get_vertex(vertex_)
                dfs_recursive(v_)             # 递归向下遍历

    for vertex in all_vertex:
        print('try new component' + '_' * 20)
        if not is_visited[int(vertex.key)]:
            dfs_recursive(vertex)


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

    dfs(g)


    """
    try new component____________________
    visit 1
    visit 2
    visit 3
    visit 4
    visit 7
    visit 6
    visit 5
    try new component____________________
    try new component____________________
    try new component____________________
    try new component____________________
    try new component____________________
    try new component____________________
    try new component____________________
    visit 8
    visit 9
    visit 10
    visit 11
    try new component____________________
    try new component____________________
    try new component____________________
    try new component____________________
    visit 12
    visit 13
    visit 15
    visit 14
    try new component____________________
    try new component____________________
    try new component____________________
    """
```




代码实现（非递归）：
```python


```

## 图的经典应用

## 热点习题及实践

