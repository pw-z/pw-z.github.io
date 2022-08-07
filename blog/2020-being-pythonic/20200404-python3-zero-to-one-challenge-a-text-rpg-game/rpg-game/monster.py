import random
from equip import *

from hero import HumanHero

nameList1 = ['魔化大蜘蛛','魔化大老鼠','魔化大鸵鸟','腐败香菇蘑','冲角团教员','冲角团临时工','楼上的拖鞋','游荡的鬼魂','饥饿的小鬼']  # 场景1怪物名字
nameList2 = ['大地之熊','玄冰毒蚁','迅影斑斓豹','紫尾貂','堕落魔蛹','不死雪狐','八翼雷鹰王']  # 场景2怪物名字
nameList3 = ['魂灭先知','狂飙毁灭者','鬼剑圣人','火爆龙将','逆焰斗神','星辰玉龙','无双赤鬼']  # 场景3怪物名字


class Monster:
    name = ''   # 怪物名
    level = 0   # 等级
    exp = 0     # 经验
    hp = 0      # 生命值
    atk = 0     # 攻击力
    equip = ''

    def __init__(self, level):
        if level <= 10:
            self.name = str(level) + "级的" + random.choice(nameList1)
        elif level <= 30:
            self.name = str(level) + "级的" + random.choice(nameList2)
        else:
            self.name = str(level) + "级的" + random.choice(nameList3)
        self.level = level
        self.exp = (5 + 5*(level-1))    # 每 +1 级 +5 经验
        self.hp = (100 + 40*(level-1))*(random.random()+0.5)  # 每 +1 级 +40 血  //再乘上(0.5-1.5)倍随机量
        self.atk = (30 + 5*(level-1))*(random.random()+0.5)   # 每 +1 级 +5 攻击 //再乘上(0.5-1.5)倍随机量


class MonsterPro(Monster):  # 精英怪
    equip = ''

    def __init__(self, level):
        if level <= 10:
            self.name = str(level) +"级的精英"+ random.choice(nameList1)
        elif level <= 30:
            self.name = str(level) +"级的精英"+ random.choice(nameList2)
        else:
            self.name = str(level) +"级的精英"+ random.choice(nameList3)
        self.level = level
        self.equip = DefaultEquip()
        self.exp = (5 + 5*(level-1))*2    # 精英怪经验翻倍
        self.hp = ((100 + 40*(level-1))*2)*(random.random()+0.5)  # 精英怪血量翻倍 //再乘上(0.5-1.5)倍随机量
        self.atk = ((30 + 5*(level-1))*2)*(random.random()+0.5)  # 精英怪攻击翻倍 //再乘上(0.5-1.5)倍随机量


class QinYijue():
    name = "秦义绝"
    level = 100  # 等级
    exp = 0  # 经验
    hp = 9999  # 生命值
    atk = 500  # 攻击力
    equip = ''