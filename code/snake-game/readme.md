# 贪吃蛇的实现

## 需求

* 场景下有一条蛇按照一定的速度朝着某个方向持续进行移动
* 蛇在移动过程中可以通过键盘输入控制蛇的方向
* 场景中随机出现食物，蛇吃掉食物后长度加一
* 蛇撞到场景边界或者撞到自己的身体则游戏结束

## 思路

* 用链表或者数组描述蛇，蛇处于游戏场景内，整个场景不断重新绘制形成动画效果
* 每一次绘制时蛇按照当前方向向前挪动一个单位，判断是否游戏结束，判断是否吃到食物
* 场景不断绘制的同时，应该有另一个线程来处理键盘输入从而控制蛇的行进方向


