
from time import sleep


class Game:
    order = '菜单输入'

    def startGame(self):
        controller = '控制器'
        scene = Scene()
        while True:
            # 一个线程进行输入处理
            # 一个线程进行屏幕绘制以及逻辑判断
            scene.repaint()
            sleep(scene.speed)
            # 此处有逻辑...


class Scene:
    size = '尺寸信息'
    speed = 5  # '刷新速度'
    snake = '蛇'
    food = '食物'

    def __init__(self):
        print('初始化')

    def repaint(self):
        print('重绘场景')

    def generateFood(self):
        print('生成食物')


class Food:
    x, y = '坐标'


class Snake:
    class Node:
        x, y = '坐标'

    head = '蛇头'
    tail = '蛇尾'
    node_list = ['身体节点']
    direction = '方向'

    def eat(self, foo: Food):
        print('吃掉食物，身体变长')


