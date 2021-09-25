from equip import *


class Hero:
    name = ''   # 角色名
    hp = 0      # 生命值
    mp = 0      # 法力值
    atk = 0     # 攻击力

    def __init__(self):
        self.name = '未命名的普通英雄'
        self.hp = 100
        self.mp = 100
        self.atk = 50

    def battleCry(self): # 战吼技能 遇到敌人后自动释放
        print("battleCry")

    def activeSkill(self): # 主动技能 手动释放
        print("activeSkill")

    # def passiveSkill(self): # 被动技能 默认增益
    #     print("passiveSkill")


# 人族攻高
class HumanHero(Hero):

    level = 1   # 初始等级
    exp = 0     # 经验值
    equip = ''  # 初始装备为空
    kind = "人族"

    temp_hp = 100  # 初始血槽
    temp_mp = 100  # 初始蓝槽
    need_exp = 10  # 升级所需要的经验

    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.mp = 100
        self.atk = 60
        self.equip = DefaultEquip()

    def update(self,exp):  # 根据传入的经验值进行升级
        self.exp += exp
        while self.exp > self.need_exp:
            self.level +=1
            self.hp += 20
            self.temp_hp = self.hp
            self.atk += 5
            self.exp -= self.need_exp
            self.need_exp += 10
            print("\033[0;30;46m您升级了！\033[0m  当前等级：" + str(self.level) + "   当前生命值：" + str(self.hp) + "   当前攻击力：" + str(self.atk) + "   下一级所需经验：" + str(int(self.need_exp)))
        return self

    def recover(self):
        self.temp_hp = self.hp
        self.temp_mp = self.mp
        return self

    def battleCry(self): # 人族战吼：对敌人造成60%攻击力的伤害
        return self.atk*0.6

    def activeSkill(self): # 人族主动技能：对敌人造成160%攻击力的伤害
        if self.temp_mp>40:
            self.temp_mp = self.temp_mp - 40
            return self.atk*1.5
        else:
            return 0


# 兽人血厚
class BeastHero(Hero):

    level = 1   # 初始等级
    exp = 0     # 经验值
    equip = ''  # 初始装备为空
    kind = "兽族"

    temp_hp = 150  # 初始血槽
    temp_mp = 100  # 初始蓝槽
    need_exp = 10  # 升级所需要的经验

    def __init__(self,name):
        self.name = name
        self.hp = 150
        self.mp = 100
        self.atk = 50
        self.equip = DefaultEquip()

    def battleCry(self): # 兽人战吼：对敌人造成50%攻击力的伤害
        return self.atk*0.5

    def activeSkill(self): # 兽人主动技能：对敌人造成150%攻击力的伤害
        if self.temp_mp>40:
            self.temp_mp = self.temp_mp - 40
            return self.atk*1.5
        else:
            return 0

    def update(self,exp):  # 根据传入的经验值进行升级
        self.exp += exp
        while self.exp > self.need_exp:
            self.level +=1
            self.hp += 20
            self.temp_hp = self.hp
            self.atk += 5
            self.exp -= self.need_exp
            self.need_exp += 10
            print("\033[0;30;46m您升级了！\033[0m  当前等级：" + str(self.level) + "   当前生命值：" + str(self.hp) + "   当前攻击力：" + str(self.atk) + "   下一级所需经验：" + str(int(self.need_exp)))
        return self

    def recover(self):
        self.temp_hp = self.hp
        self.temp_mp = self.mp
        return self