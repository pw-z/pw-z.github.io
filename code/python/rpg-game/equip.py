import random

nameList1 = ['脚趾甲','牙齿','胳膊','鼻涕','头盖骨','汗毛','大眼睛','小拇指']
nameList2 = ['匕首','长剑','短斧','铃铛','乾坤袋','金枪']
nameList = [nameList1,nameList2]

class Equip:
    name = ''
    level = 0
    atk = 0

    def __init__(self, monster):
        self.name = monster.name + "的" + random.choice(random.choice(nameList))
        self.level = monster.level
        self.atk = monster.atk*0.5


class DefaultEquip():
    name = "default"
    atk = 0

    def __init__(self):
        self.atk = 0