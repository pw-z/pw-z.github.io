from hero import *
from monster import *
import random
import time

# 初始化新游戏
def init_new_game():
    print("\033[1;30;41m==================开始新游戏==================\033[0m")
    print("1.人族英雄（攻高）            2.兽族英雄（血厚）")
    heroTypt = input("请选择英雄类型：")
    while (heroTypt!=str(1) and heroTypt!=str(2)):
        heroTypt = input("\033[0;31;m输入有误，请重新选择（只能是1或2）：\033[0m")
    else:
        heroName = input("请输入英雄名称：")
    if heroTypt==str(1):
        humanHero = HumanHero(heroName)
        print("您新建了人族英雄：" + humanHero.name)
        show_hero_info(humanHero)
        return humanHero
    else:
        beastHero = BeastHero(heroName)
        print("您新建了兽族英雄：" + beastHero.name)
        show_hero_info(beastHero)
        return beastHero

# 读取展示英雄信息
def show_hero_info(hero):
    print("\033[0;30;m--------------当前英雄信息--------------\033[0m")
    print("英雄名称：" + hero.name + "   种族：" + hero.kind + "\n"
          "生命值：" + str(hero.hp) + "   法力值：" + str(hero.mp) + "\n"
          "攻击力：" + str(hero.atk) + "")
    if hero.equip.name != 'default':
        print("装备：" + hero.equip.name + "   攻击：" + str(int(hero.equip.atk)))
    else:
        print("目前无装备")

# 主菜单响应
def handle_menu(hero):
    print("\033[0;30;42m-----------------绿明村中-----------------\033[0m")
    print("1.外出历练        2.角色状态")
    code = input("请选择操作：")
    if code==str(1):
        handle_map(hero)
    else:
        show_hero_info(hero)
        handle_menu(hero)

# 战斗处理
def handle_battle(hero, monster):
    print("您遇到了：" + monster.name + "  怪物生命值：" + str(int(monster.hp)) + "  怪物攻击力：" + str(int(monster.atk)))
    print("1.勇敢战斗      2.逃跑")
    code = input("请选择操作：")
    if code==str(2):
        x = abs(hero.level - monster.level)
        y = random.choice(range(1,10))
        if y<x:  # 差10级以上100%逃跑成功
            print("逃跑成功")
            return hero
        else:
            print("逃跑失败，即将进入战斗…")

    while monster.hp > 0:
        print("1.普通攻击  2.主动技能")
        code = input("请选择操作：")
        if code == str(1):
            tempatk = hero.atk+hero.equip.atk
            monster.hp -= tempatk
            print("您进行了普通攻击，对怪物造成" + str(int(tempatk)) + "点伤害,  怪物剩余生命值：" + str(int(monster.hp)))
            if monster.hp < 0:
                continue
        else:
            tempatk = hero.activeSkill()
            if tempatk != 0:
                monster.hp -= tempatk
                print("您发动了主动技能，对怪物造成" + str(tempatk) + "点伤害,  怪物剩余生命值：" + str(int(monster.hp)))
            else:
                print("\033[7;31;40m您没蓝了\033[0m，请使用普通攻击")
                continue
        hero.temp_hp -= monster.atk
        print("怪物发动攻击对您造成" + str(int(monster.atk)) + "点伤害,  您剩余生命值：" + str(int(hero.temp_hp)))
        if hero.temp_hp < 0:
            print("\033[7;31;40m您被拍死了，游戏结束\033[0m")
            exit(0)

    # 怪物死掉了才能到达这一步：
    hero.recover()    # 恢复
    if monster.name != "秦义绝":
        print("\033[0;36;47m战斗胜利！\033[0m获得经验：" + str(monster.exp) + "！ 您的生命值与魔法值已经恢复")
        hero.update(monster.exp)  # 判断升级
        # 装备掉落判断：
        if monster.equip != '' and monster.equip.name != 'default':
            if random.random() > 0.5:  # 0.5的几率掉落装备
                print("\033[1;30;45m怪物掉落了一件装备:\033[0m" + monster.equip.name + "  攻击力为：" + str(int(monster.equip.atk)) + "   您当前武器为：" + hero.equip.name + "   攻击力为：" + str(int(hero.equip.atk)))
                code = input("是否更换装备（y/n）：")
                if code == 'y':
                    hero.equip = monster.equip
                    print("更换装备成功，当前装备：" + hero.equip.name)
                else:
                    print("您已经放弃了这个装备。正在返回绿明村。")
                    return hero
            else:
                return hero
    else:
        print("\033[1;30;45m您战胜了秦义绝！天下终于太平了。\033[0m")
        print("\033[1;30;42m全剧终,即将自动退出游戏\033[0m")
        slow_print()
        exit(0)

# 地图探索
def handle_map(hero):
    while True:
        print("\033[0;30;42m-----------------绿明村头-----------------\033[0m")
        print("1.村头小树林   2.风之平原   3.红莲墓地   4.白青山脉   5.国师府邸   0.回到村中")
        code = input("请选择目的地：")
        if code == str(1):
            print("\033[0;30;42m----------------村头小树林----------------\033[0m")
            print("探索中…"+" ")
            slow_print()
            mm = monster_generator(random.choice(range(1, 3)))  # 随机生成一个[1，3]级别的怪物
            handle_battle(hero, mm)  # 处理战斗过程,如果没死，会返回新的hero，死了就结束了
        elif code == str(2):
            print("\033[0;30;42m-----------------风之平原-----------------\033[0m")
            print("探索中…"+" ")
            slow_print()
            mm = monster_generator(random.choice(range(1, 10)))  # 随机生成一个[1，10]级别的怪物
            handle_battle(hero, mm)  # 处理战斗过程,如果没死，会返回新的hero，死了就结束了
        elif code == str(3):
            print("\033[0;30;42m-----------------红莲墓地-----------------\033[0m")
            print("探索中…" + " ")
            slow_print()
            mm = monster_generator(random.choice(range(11, 30)))
            handle_battle(hero, mm)
        elif code == str(4):
            print("\033[0;30;42m-----------------白青山脉-----------------\033[0m")
            print("探索中…" + " ")
            slow_print()
            mm = monster_generator(random.choice(range(31, 50)))
            handle_battle(hero, mm)
        elif code == str(5):
            print("\033[0;30;42m-----------------国师府邸-----------------\033[0m")
            print("")
            code = input("您确定要现在挑战秦义绝吗?(y/n)")
            if code == 'y':
                qinyijue = QinYijue()
                handle_battle(hero,qinyijue)
        elif code == str(0):
            handle_menu(hero)
        else:
            print("输入有误")

# 怪物生成器
def monster_generator(level):
    # print("正在生成怪物")
    if random.random()>0.8:  # 0.2的几率生成精英怪
        m = MonsterPro(level)
        if random.random() > 0.4:  # 0.6的几率生成装备
            m.equip = Equip(m)   # 这样互相依赖貌似……
        return m
    else:
        m = Monster(level)
        return m

# 延迟打印以防止刷屏
def slow_print():
    for x in range(3, -1, -1):
        mystr = "探索中" + str(x) + "秒"
        print(mystr, end="")
        print("\b" * (len(mystr) * 2), end="", flush=True)
        time.sleep(0.2)

if __name__ == '__main__':
    hero = init_new_game()  # 开始新游戏：创建新角色
    handle_menu(hero)       # 提供主菜单，在主菜单进行接下来的操作