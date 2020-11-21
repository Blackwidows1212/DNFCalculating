from PublicReference.base import *
from math import *

芙蕾雅等级 = 100 + 5


class 芙蕾雅主动技能(主动技能):
    技能施放时间 = 0.0
    脱手 = 1
    数据 = []
    数据2 = []
    数据3 = []

    def 等效百分比(self, 武器类型):
        等效倍率 = 0.0
        if len(self.数据) >= self.等级 and len(self.数据) > 0:
            等效倍率 += self.数据[self.等级] * self.攻击次数
        if len(self.数据2) >= self.等级 and len(self.数据2) > 0:
            等效倍率 += self.数据2[self.等级] * self.攻击次数2
        if len(self.数据3) >= self.等级 and len(self.数据3) > 0:
            等效倍率 += self.数据3[self.等级] * self.攻击次数3
        return 等效倍率 * (1 + self.TP成长 * self.TP等级) * self.倍率


class 芙蕾雅技能0(被动技能):
    名称 = '单兵推进器'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10
    关联技能 = ['交叉射击', '聚合弹', '凝固汽油弹', '轻火力速射']
    关联技能2 = ['爆裂弹']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 + (10 + self.等级) / 100, 3)

    def 加成倍率2(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 + (2 * self.等级) / 100, 3)


class 芙蕾雅技能1(被动技能):
    名称 = '兵器研究'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10
    冷却关联技能 = ['交叉射击', 'M18阔剑地雷', 'C4飞弹', 'G18冰冻手雷', 'G35感电手雷', 'G61重力地雷', 'G96热压手雷', '爆裂弹', '聚合弹', '开火', '镭射狙击',
              '凝固汽油弹', '轻火力速射']

    def 加成倍率(self, 武器类型):
        return (1.1 + (self.等级 - 10) * 0.02) if self.等级 >= 10 else (1 + self.等级 * 0.01)

    def 独立攻击力倍率(self, 武器类型):
        return (1.1 + (self.等级 - 10) * 0.02) if self.等级 >= 10 else (1 + self.等级 * 0.01)

    def CD缩减倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 - 0.01 * self.等级, 3)


class 芙蕾雅技能2(被动技能):
    名称 = '手雷精通'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10
    关联技能 = ['G35感电手雷', 'G18冰冻手雷']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 + 0.1 * self.等级, 3)


class 芙蕾雅技能3(被动技能):
    名称 = '弹药改良'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10
    关联技能 = ['所有']
    技能加成描述 = ''
    加成数值 = 1.0

    def 加成倍率(self, 武器类型):
        return self.加成数值

    自定义描述 = 1
    def 技能描述(self, 武器类型):
        return self.技能加成描述

class 芙蕾雅技能4(芙蕾雅主动技能):
    名称 = 'M18阔剑地雷'
    所在等级 = 20
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((芙蕾雅等级 - 所在等级) / 学习间隔), 等级精通) + 1
    数据 = [0, 645, 709, 774, 841, 905, 972, 1037, 1101, 1168, 1233, 1299, 1364, 1429, 1495, 1560, 1626, 1691, 1756, 1822,
          1887, 1953, 2018, 2083, 2149, 2214, 2280, 2345, 2410, 2476, 2541, 2607, 2672, 2737, 2803, 2868, 2933, 2999,
          3064, 3130, 3195, 3260, 3326, 3391, 3457, 3522, 3587, 3653, 3718, 3784, 3849, 3914, 3980, 4045, 4111, 4176,
          4241, 4307, 4372, 4438, 4503, 4569, 4634, 4699, 4765, 4830, 4896, 4961, 5026, 5092, 5157]
    攻击次数 = 3
    CD = 6.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5


class 芙蕾雅技能5(芙蕾雅主动技能):
    名称 = 'G35感电手雷'
    所在等级 = 25
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((芙蕾雅等级 - 所在等级) / 学习间隔), 等级精通) + 1
    数据 = [0, 525, 577, 631, 683, 738, 790, 844, 896, 950, 1003, 1057, 1109, 1163, 1216, 1269, 1322, 1375, 1428, 1482,
          1535, 1588, 1641, 1695, 1748, 1801, 1854, 1907, 1961, 2014, 2067, 2120, 2174, 2227, 2280, 2333, 2386, 2440,
          2493, 2546, 2599, 2653, 2706, 2759, 2812, 2865, 2919, 2972, 3025, 3078, 3131, 3185, 3237, 3291, 3343, 3398,
          3450, 3504, 3556, 3610, 3663]
    攻击次数 = 1
    数据2 = [0, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14,
           14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14,
           14, 14, 14, 14, 14, 14, 14]
    攻击次数2 = 18
    CD = 3.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    基础释放次数 = 3
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if (self.等级 < 18):
            return 1.0
        else:
            return round(1 + 0.01 * (self.等级 - 18), 3)
    
    def 等效CD(self, 武器类型):
        # 经过测试,手雷恢复速度无法享受技能冷却恢复加成
        return round(self.CD, 1)


class 芙蕾雅技能6(芙蕾雅主动技能):
    名称 = '交叉射击'
    所在等级 = 25
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((芙蕾雅等级 - 所在等级) / 学习间隔), 等级精通) + 1
    数据 = [0, 1265, 1394, 1522, 1651, 1779, 1907, 2035, 2164, 2292, 2421, 2549, 2678, 2806, 2934, 3063, 3191, 3319, 3448,
          3576, 3704, 3833, 3961, 4090, 4218, 4347, 4475, 4603, 4732, 4860, 4988, 5117, 5245, 5374, 5502, 5631, 5759,
          5887, 6015, 6144, 6272, 6400, 6529, 6657, 6786, 6914, 7043, 7171, 7299, 7428, 7556, 7684, 7813, 7941, 8070,
          8198, 8327, 8455, 8583, 8712, 8840, 8968, 9096, 9225, 9353, 9482, 9610, 9739, 9867, 9995, 10124]
    攻击次数 = 3
    CD = 8.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5


class 芙蕾雅技能7(芙蕾雅主动技能):
    名称 = '爆裂弹'
    所在等级 = 30
    等级上限 = 20
    基础等级 = 10
    数据 = [0, 630, 731, 831, 931, 1032, 1132, 1232, 1333, 1434, 1534, 1635, 1735, 1835, 1936, 2036, 2137, 2238, 2338,
          2439, 2539]
    攻击次数 = 1
    CD = 5.0


class 芙蕾雅技能8(芙蕾雅主动技能):
    名称 = 'G18冰冻手雷'
    所在等级 = 30
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((芙蕾雅等级 - 所在等级) / 学习间隔), 等级精通) + 1
    数据 = [0, 634, 699, 763, 827, 891, 956, 1021, 1084, 1149, 1213, 1278, 1343, 1406, 1471, 1535, 1600, 1664, 1728, 1793,
          1857, 1922, 1986, 2050, 2115, 2180, 2243, 2308, 2372, 2437, 2500, 2565, 2630, 2694, 2759, 2822, 2887, 2952,
          3016, 3080, 3144, 3209, 3274, 3338, 3402, 3467, 3531, 3596, 3659, 3724, 3789, 3853, 3918, 3981, 4046, 4111,
          4175, 4239, 4303, 4368, 4433]
    攻击次数 = 1
    基础释放次数 = 3
    CD = 4.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    def 等效CD(self, 武器类型):
    # 经过测试,手雷恢复速度无法享受技能冷却恢复加成
        return round(self.CD, 1)


class 芙蕾雅技能9(芙蕾雅主动技能):
    名称 = '聚合弹'
    所在等级 = 35
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((芙蕾雅等级 - 所在等级) / 学习间隔), 等级精通) + 1
    数据 = [0, 7877, 8676, 9475, 10274, 11073, 11872, 12671, 13470, 14270, 15069, 15868, 16667, 17466, 18265, 19064,
          19863, 20662, 21461, 22260, 23060, 23859, 24658, 25457, 26256, 27055, 27854, 28654, 29453, 30252, 31051,
          31850, 32649, 33448, 34247, 35046, 35845, 36644, 37444, 38243, 39042, 39841, 40640, 41439, 42238, 43037,
          43836, 44635, 45434, 46234, 47033, 47832, 48631, 49430, 50229, 51029, 51828, 52627, 53426, 54225, 55024,
          55823, 56622, 57421, 58220, 59019, 59818, 60618, 61417, 62216, 63015]
    攻击次数 = 1
    CD = 18.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5


class 芙蕾雅技能10(芙蕾雅主动技能):
    名称 = 'C4飞弹'
    所在等级 = 35
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((芙蕾雅等级 - 所在等级) / 学习间隔), 等级精通) + 1
    数据 = [0, 7178, 7906, 8635, 9363, 10091, 10819, 11547, 12276, 13004, 13732, 14460, 15188, 15917, 16645, 17373, 18101,
          18829, 19558, 20286, 21014, 21742, 22470, 23200, 23928, 24656, 25384, 26112, 26841, 27569, 28297, 29025,
          29754, 30482, 31210, 31938, 32666, 33395, 34123, 34851, 35579, 36307, 37036, 37764, 38492, 39220, 39949,
          40678, 41406, 42134, 42862, 43590, 44319, 45047, 45775, 46503, 47231, 47960, 48688, 49416, 50144, 50873,
          51601, 52329, 53057, 53786, 54514, 55242, 55970, 56699, 57427]
    攻击次数 = 1
    CD = 20.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, 类型):
        if 类型 == 0:
            self.数据 = [i * 1.16 for i in self.数据]
        elif 类型 == 1:
            self.数据 = [i * 1.25 for i in self.数据]


class 芙蕾雅技能11(芙蕾雅主动技能):
    名称 = '凝固汽油弹'
    所在等级 = 40
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((芙蕾雅等级 - 所在等级) / 学习间隔), 等级精通) + 1
    数据 = [0, 8539, 9405, 10271, 11137, 12004, 12870, 13736, 14603, 15469, 16335, 17201, 18067, 18934, 19800, 20666,
          21533, 22399, 23265, 24131, 24998, 25864, 26730, 27596, 28463, 29329, 30195, 31062, 31928, 32794, 33660,
          34526, 35393, 36259, 37125, 37992, 38858, 39724, 40591, 41457, 42323, 43189, 44055, 44922, 45788, 46654,
          47521, 48387, 49253, 50119, 50985, 51852, 52718, 53584, 54451, 55317, 56183, 57050, 57916, 58782, 59648,
          60514, 61381, 62247, 63113, 63980, 64846, 65712, 66578, 67444, 68311]
    攻击次数 = 1
    数据2 = [0, 44, 47, 52, 56, 61, 65, 70, 74, 79, 83, 87, 92, 96, 101, 105, 110, 114, 119, 122, 127, 131, 136, 141, 145,
           150, 154, 158, 162, 167, 171, 176, 180, 185, 190, 194, 198, 202, 207, 211, 216, 220, 225, 229, 233, 238, 242,
           247, 251, 256, 260, 265, 268, 273, 277, 282, 287, 291, 296, 300, 305, 308, 313, 317, 322, 326, 331, 336, 340,
           344, 348]
    攻击次数2 = 15
    CD = 20.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, 类型):
        if 类型 == 0:
            self.数据 = [x * 1.31 for x in self.数据]
            self.攻击次数2 = 0
            self.CD *= 0.94
        elif 类型 == 1:
            self.数据 = [x * 1.40 for x in self.数据]
            self.攻击次数2 = 0
            self.CD *= 0.94


class 芙蕾雅技能12(芙蕾雅主动技能):
    名称 = '镭射狙击'
    所在等级 = 45
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((芙蕾雅等级 - 所在等级) / 学习间隔), 等级精通) + 1
    数据 = [0, 3040, 3349, 3657, 3966, 4274, 4583, 4892, 5200, 5509, 5817, 6126, 6435, 6743, 7052, 7360, 7669, 7978, 8286,
          8595, 8903, 9212, 9521, 9829, 10138, 10446, 10755, 11063, 11372, 11681, 11989, 12298, 12606, 12914, 13222,
          13531, 13839, 14148, 14457, 14765, 15074, 15382, 15691, 16000, 16308, 16617, 16925, 17234, 17543, 17851,
          18160, 18468, 18777, 19085, 19394, 19703, 20011, 20320, 20628, 20937, 21246, 21554, 21863, 22171, 22480,
          22787, 23096, 23404, 23713, 24022, 24330]
    攻击次数 = 5
    CD = 45.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self,类型):
        if 类型 == 0:
            self.数据 = [x * 0.26 for x in self.数据]
            self.攻击次数 = 24
            self.技能施放时间 = 3.0
        elif 类型 == 1:
            self.数据 = [x * 0.28 for x in self.数据]
            self.攻击次数 = 24
            self.技能施放时间 = 3.0

class 芙蕾雅技能13(被动技能):
    名称 = '弹药强化'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        return 1.105 + self.等级 * 0.015 if self.等级 > 0 else 1


class 芙蕾雅技能14(芙蕾雅主动技能):
    名称 = 'EMP磁爆'
    所在等级 = 50
    等级上限 = 40
    学习间隔 = 5
    等级精通 = 30
    基础等级 = min(int((芙蕾雅等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据 = [0, 10794, 13296, 15800, 18302, 20806, 23308, 25811, 28314, 30817, 33321, 35823, 38327, 40829, 43333, 45835,
          48338, 50841, 53344, 55846, 58350, 60852, 63356, 65860, 68362, 70865, 73368, 75871, 78373, 80877, 83379,
          85883, 88385, 90889, 93391, 95895, 98398, 100900, 103404, 105906, 108410, 110912, 113416, 115918, 118422,
          120924, 123427, 125930, 128433, 130937, 133439, 135943, 138445, 140949, 143451, 145954, 148457, 150960,
          153462, 155966, 158470, 160972, 163476, 165978, 168481, 170984, 173487, 175989, 178493, 180995, 183499]
    攻击次数 = 3
    数据2 = [0, 539, 664, 790, 915, 1039, 1164, 1290, 1415, 1540, 1666, 1791, 1916, 2040, 2165, 2291, 2416, 2541, 2667,
           2792, 2917, 3041, 3167, 3292, 3417, 3543, 3668, 3793, 3919, 4042, 4168, 4293, 4418, 4544, 4669, 4794, 4920,
           5044, 5169, 5294, 5420, 5545, 5670, 5796, 5921, 6045, 6170, 6295, 6421, 6546, 6671, 6797, 6922, 7047, 7171,
           7297, 7422, 7547, 7673, 7798, 7923, 8049, 8172, 8298, 8423, 8548, 8674, 8799, 8924, 9050, 9174]
    攻击次数2 = 20
    CD = 145.0


class 芙蕾雅技能15(芙蕾雅主动技能):
    名称 = 'G61重力地雷'
    所在等级 = 60
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((芙蕾雅等级 - 所在等级) / 学习间隔), 等级精通) + 1
    数据 = [0, 5672, 6247, 6823, 7399, 7975, 8550, 9125, 9701, 10276, 10851, 11428, 12003, 12579, 13154, 13729, 14305,
          14880, 15455, 16032, 16607, 17183, 17758, 18333, 18909, 19484, 20061, 20636, 21211, 21787, 22362, 22937,
          23513, 24088, 24665, 25240, 25815, 26391, 26966, 27542, 28117, 28692, 29269, 29844, 30420, 30995, 31570,
          32146, 32721, 33297, 33873, 34448, 35023, 35599, 36175, 36750, 37326, 37901, 38477, 39052, 39628, 40203,
          40779, 41354, 41930, 42505, 43081, 43656, 44232, 44807, 45383]
    攻击次数 = 1
    数据2 = [0, 189, 207, 227, 246, 265, 284, 304, 322, 342, 361, 380, 400, 419, 438, 457, 477, 495, 515, 533, 553, 572,
           591, 610, 630, 649, 668, 688, 706, 726, 744, 764, 783, 803, 821, 841, 859, 879, 899, 917, 937, 956, 975, 994,
           1014, 1032, 1052, 1070, 1090, 1109, 1128, 1148, 1167, 1186, 1205, 1224, 1244, 1263, 1282, 1301, 1320, 1339,
           1359, 1378, 1397, 1416, 1435, 1455, 1474, 1493, 1512]
    攻击次数2 = 29
    CD = 20.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    技能施放时间 = 3
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self,类型):
        if 类型== 0:
            self.数据 = [x * 2.16 for x in self.数据]
            self.技能施放时间 = 0.5
            self.攻击次数2 = 5
        elif 类型== 1:
            self.数据 = [x * 2.34 for x in self.数据]
            self.技能施放时间 = 0.5
            self.攻击次数2 = 5


class 芙蕾雅技能16(芙蕾雅主动技能):
    名称 = '轻火力速射'
    脱手 = 0
    所在等级 = 70
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((芙蕾雅等级 - 所在等级) / 学习间隔), 等级精通) + 1
    数据 = [0, 1061, 1169, 1277, 1384, 1492, 1600, 1708, 1815, 1923, 2031, 2139, 2246, 2354, 2461, 2569, 2677, 2785, 2892,
          3000, 3108, 3215, 3323, 3431, 3538, 3646, 3754, 3862, 3969, 4077, 4185, 4292, 4400, 4508, 4616, 4723, 4831,
          4938, 5046, 5154, 5262, 5369, 5477, 5585, 5692, 5800, 5908, 6016, 6123, 6231, 6339, 6446, 6554, 6662, 6769,
          6877, 6985, 7093, 7200, 7308, 7416, 7523, 7631, 7739, 7846, 7954, 8062, 8170, 8277, 8385, 8493]
    攻击次数 = 17
    CD = 30.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    技能施放时间 = 1
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self,类型):
        if 类型 == 0:
            self.数据2 = [x * 0.6 for x in self.数据]
            self.技能施放时间 = 1.5
            self.攻击次数2 = 6
            self.CD *= 0.95
        elif 类型 == 1:
            self.数据2 = [x * 0.82 for x in self.数据]
            self.技能施放时间 = 1.5
            self.攻击次数2 = 6
            self.CD *= 0.95


class 芙蕾雅技能17(被动技能):
    名称 = '制空掌握'
    所在等级 = 75
    等级上限 = 30
    基础等级 = 11
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 3)


class 芙蕾雅技能18(芙蕾雅主动技能):
    名称 = '开火'
    所在等级 = 75
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((芙蕾雅等级 - 所在等级) / 学习间隔), 等级精通) + 1
    数据 = [0, 7474, 8232, 8990, 9748, 10507, 11265, 12023, 12781, 13540, 14298, 15056, 15814, 16572, 17331, 18089, 18847,
          19605, 20364, 21122, 21880, 22638, 23396, 24155, 24913, 25671, 26429, 27188, 27946, 28704, 29462, 30220,
          30979, 31737, 32495, 33253, 34012, 34770, 35528, 36286, 37044, 37803, 38561, 39320, 40078, 40836, 41594,
          42352, 43111, 43869, 44627, 45385, 46144, 46902, 47660, 48418, 49177, 49935, 50693, 51451, 52210, 52968,
          53726, 54484, 55242, 56001, 56759, 57517, 58275, 59034, 59792]
    攻击次数 = 6
    CD = 45.0
    脱手 = 0
    技能施放时间 = 1
    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self,类型):
        if 类型 == 0:
            self.数据 = [x * 1.35 for x in self.数据]


class 芙蕾雅技能19(芙蕾雅主动技能):
    名称 = 'G96热压手雷'
    所在等级 = 80
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((芙蕾雅等级 - 所在等级) / 学习间隔), 等级精通) + 1
    数据 = [0, 38800, 42736, 46673, 50608, 54545, 58481, 62418, 66353, 70290, 74226, 78163, 82099, 86035, 89971, 93908,
          97844, 101780, 105716, 109653, 113589, 117525, 121461, 125398, 129334, 133270, 137206, 141143, 145079, 149016,
          152951, 156888, 160824, 164761, 168696, 172633, 176569, 180506, 184441, 188378, 192314, 196251, 200187,
          204122, 208059, 211996, 215932, 219867, 223804, 227741, 231677, 235612, 239549, 243486, 247422, 251359,
          255294, 259230, 263167, 267104, 271039, 274975, 278912, 282849, 286784, 290720, 294657, 298594, 302529,
          306465, 310402]
    攻击次数 = 1
    CD = 45.0
    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self,类型):
        if 类型 == 0:
            self.数据 = [x * 1.29 for x in self.数据]
            self.CD *= 0.9


class 芙蕾雅技能20(芙蕾雅主动技能):
    名称 = '决战之日'
    所在等级 = 85
    等级上限 = 40
    学习间隔 = 5
    等级精通 = 30
    基础等级 = min(int((芙蕾雅等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据 = [0, 3047, 3754, 4460, 5167, 5874, 6581, 7288, 7994, 8701, 9408, 10115, 10822, 11529, 12236, 12941, 13648,
          14355, 15062, 15769, 16476, 17182, 17889, 18596, 19303, 20009, 20716, 21423, 22129, 22836, 23543, 24250,
          24957, 25664, 26371, 27076, 27783, 28490, 29197, 29904, 30611, 31318, 32024, 32731, 33438, 34145, 34851,
          35558, 36265, 36972, 37678, 38385, 39092, 39799, 40505, 41212, 41919, 42626, 43333, 44039, 44746, 45453,
          46160, 46866, 47573, 48280, 48987, 49693, 50400, 51107, 51814]
    攻击次数 = 40
    CD = 180.0


class 芙蕾雅技能21(被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    学习间隔 = 3
    等级精通 = 30
    基础等级 = min(int((芙蕾雅等级 - 所在等级) / 学习间隔 + 1), 等级精通)

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 芙蕾雅技能22(被动技能):
    名称 = '超卓之心'
    所在等级 = 95
    等级上限 = 11
    学习间隔 = 2
    等级精通 = 1
    基础等级 = min(int((芙蕾雅等级 - 所在等级) / 学习间隔 + 1), 等级精通)

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.045 + 0.005 * self.等级, 5)


class 芙蕾雅技能23(被动技能):
    名称 = '觉醒之抉择'
    所在等级 = 100
    等级上限 = 40
    学习间隔 = 5
    等级精通 = 30
    基础等级 = min(int((芙蕾雅等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10 + 0.05 * self.等级, 5)


芙蕾雅技能列表 = []
i = 0
while i >= 0:
    try:
        exec('芙蕾雅技能列表.append(芙蕾雅技能' + str(i) + '())')
        i += 1
    except:
        i = -1

芙蕾雅技能序号 = dict()
for i in range(len(芙蕾雅技能列表)):
    芙蕾雅技能序号[芙蕾雅技能列表[i].名称] = i

芙蕾雅一觉序号 = 0
芙蕾雅二觉序号 = 0
芙蕾雅三觉序号 = 0

for i in 芙蕾雅技能列表:
    if i.所在等级 == 50:
        芙蕾雅一觉序号 = 芙蕾雅技能序号[i.名称]
    if i.所在等级 == 85:
        芙蕾雅二觉序号 = 芙蕾雅技能序号[i.名称]
    if i.所在等级 == 100:
        芙蕾雅三觉序号 = 芙蕾雅技能序号[i.名称]

芙蕾雅护石选项 = ['无']
for i in 芙蕾雅技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        芙蕾雅护石选项.append(i.名称)

芙蕾雅符文选项 = ['无']
for i in 芙蕾雅技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1 and i.名称 != '爆裂弹':
        芙蕾雅符文选项.append(i.名称)

class 芙蕾雅角色属性(角色属性):
    实际名称 = '芙蕾雅'
    角色 = '神枪手(女)'
    职业 = '弹药专家'

    武器选项 = ['手弩', '步枪']

    类型选择 = ['魔法固伤', '物理固伤']

    类型 = '魔法固伤'
    防具类型 = '皮甲'
    防具精通属性 = ['智力', '力量']

    超负荷属性= 0

    主BUFF = 1.84

    远古记忆 = 0

    打桩模式 = 0

    # 守门人四属强 = [0,0,0,0]

    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(芙蕾雅技能列表)
        self.技能序号 = deepcopy(芙蕾雅技能序号)

    def 技能释放次数计算(self):
        技能释放次数 = []
        技能消耗时间 = 0.0
        爆裂弹间隔 = 0.115
        每轮空射次数 = 12 + floor(0.5 * min(self.技能栏[self.技能序号['单兵推进器']].等级, 20))
        每轮时间 = 爆裂弹间隔 * 每轮空射次数 + 1.05
        # 最大不脱手时间 = 0.0

        反应时间 = 0.0
        释放时间系数 = 0.0
        起落地时间 = 0.0
        CD延迟 = 0.0

        if(self.打桩模式 ==0):
            反应时间 = 1.5
            释放时间系数 = 1.0
            起落地时间 = 1.5
            CD延迟 = 0.0

        elif(self.打桩模式 ==1):
            反应时间 = 0.0
            释放时间系数 = 0.0
            起落地时间 = 1.0
            CD延迟 = 0.0

        elif(self.打桩模式 ==2):
            反应时间 = 3.0
            释放时间系数 = 2.0
            起落地时间 = 3.0
            CD延迟 = 2.0


        if (self.武器类型 != '手弩'):
            爆裂弹间隔 = 0.14
            每轮空射次数 = 4 + floor(0.5 * min(self.技能栏[self.技能序号['单兵推进器']].等级, 20))
            每轮时间 = 爆裂弹间隔 * 每轮空射次数 + 起落地时间

        爆裂弹位置 = self.技能序号['爆裂弹']

        # for i in self.技能栏:
        #     if i.是否有伤害 == 1 and i.脱手!=1 and i.技能施放时间 > 最大不脱手时间:
        #         最大不脱手时间 = i.技能施放时间
        for i in self.技能栏:
            if i.是否有伤害 == 1:
                if i.名称 == '爆裂弹':
                    技能释放次数.append(0)
                else:
                    if self.次数输入[self.技能序号[i.名称]] == '/CD':
                        # 技能无法释放次数 = int(最大不脱手时间/(i.等效CD(self.武器类型)+0.5))
                        # 技能释放次数.append(int((self.时间输入 - 反应时间) / (i.等效CD(self.武器类型) + i.技能施放时间*释放时间系数 + CD延迟) + 1 + i.基础释放次数)-技能无法释放次数)
                        技能释放次数.append(int((self.时间输入 - 反应时间) / (i.等效CD(self.武器类型) + i.技能施放时间*释放时间系数 + CD延迟) + 1 + i.基础释放次数))
                        if i.脱手 == 1:
                            技能消耗时间 += int((self.时间输入 - 反应时间) / (i.等效CD(self.武器类型) + i.技能施放时间*释放时间系数 + CD延迟) + 1 + i.基础释放次数) * 0.12 * 释放时间系数
                        else:
                            技能消耗时间 += int((self.时间输入 - 反应时间) / (i.等效CD(self.武器类型) + i.技能施放时间*释放时间系数 + CD延迟) + 1 + i.基础释放次数) * i.技能施放时间*释放时间系数
                    elif self.次数输入[self.技能序号[i.名称]] != '0':
                        技能释放次数.append(int(self.次数输入[self.技能序号[i.名称]]))
                        if i.脱手 == 1:
                            技能消耗时间 += int(self.次数输入[self.技能序号[i.名称]]) * 0.12 * 释放时间系数
                        else:
                            技能消耗时间 += int(self.次数输入[self.技能序号[i.名称]]) * i.技能施放时间 * 释放时间系数
                    else:
                        技能释放次数.append(0)
            else:
                技能释放次数.append(0)

        if self.次数输入[self.技能序号['爆裂弹']] == '/CD':
            技能释放次数[爆裂弹位置] = int(floor((self.时间输入 - 技能消耗时间) / 每轮时间) * 每轮空射次数)
            技能释放次数[爆裂弹位置] += max(floor((self.时间输入 - 技能消耗时间 - 每轮时间 * floor((self.时间输入 - 技能消耗时间) / 每轮时间) - 起落地时间/2) / 爆裂弹间隔), 0)
        else:
            技能释放次数[爆裂弹位置] = int(self.次数输入[self.技能序号['爆裂弹']]) * 每轮空射次数
        return 技能释放次数

    def 预处理(self):
        if self.超负荷属性 == 0:
            self.技能栏[self.技能序号['弹药改良']].加成数值 = 1.1
            self.技能栏[self.技能序号['弹药改良']].自定义描述 = 0
        if self.超负荷属性 == 1:
            self.技能栏[self.技能序号['弹药改良']].技能加成描述 = '火属性强化增加：36'
            self.火属性强化 += 36
        if self.超负荷属性 == 2:
            self.技能栏[self.技能序号['弹药改良']].技能加成描述 = '冰属性强化增加：36'
            self.冰属性强化 += 36          
        if self.超负荷属性 == 3:
            self.技能栏[self.技能序号['弹药改良']].技能加成描述 = '光属性强化增加：36'
            self.光属性强化 += 36        
        super().预处理()

class 芙蕾雅(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 芙蕾雅角色属性()
        self.角色属性A = 芙蕾雅角色属性()
        self.角色属性B = 芙蕾雅角色属性()
        self.一觉序号 = 芙蕾雅一觉序号
        self.二觉序号 = 芙蕾雅二觉序号
        self.三觉序号 = 芙蕾雅三觉序号
        self.护石选项 = deepcopy(芙蕾雅护石选项)
        self.符文选项 = deepcopy(芙蕾雅符文选项)

    def 界面2(self):
        super().界面2()

        self.超负荷属性选择=MyQComboBox(self.main_frame2)
        self.超负荷属性选择.addItems(['超负荷装填：无','超负荷装填：火','超负荷装填：冰','超负荷装填：光'])
        self.超负荷属性选择.resize(120,20)
        self.超负荷属性选择.move(325,420)
        
        self.打桩模式 = MyQComboBox(self.main_frame2)
        y=QLabel("打桩模式：", self.main_frame2)
        y.move(500, self.height() - 63)
        y.resize(70, 20)
        y.setStyleSheet(标签样式)
        self.打桩模式.addItems(['常规打桩','桩逼模式','手残模式'])
        self.打桩模式.move(570, self.height() - 63)
        self.打桩模式.resize(80, 20)

        # self.守门人属强输入 = []
        # self.守门人属强.resize(0,0)
        # 守门人属强x = self.守门人属强.geometry().x()
        # 守门人属强y = self.守门人属强.geometry().y()
        # y=QLabel("守门人(火冰暗光)：", self.main_frame2)
        # y.move(守门人属强x-100, 守门人属强y)
        # y.resize(100, 20)
        # y.setStyleSheet(标签样式)
        # for i in range(0,4):
        #     self.守门人属强输入.append(QLineEdit(self.main_frame2))
        #     self.守门人属强输入[i].setAlignment(Qt.AlignCenter)
        #     self.守门人属强输入[i].setStyleSheet(文本框样式白)
        #     self.守门人属强输入[i].resize(32, 22)
        #     self.守门人属强输入[i].move(守门人属强x + i*35, 守门人属强y)

    def 输入属性(self, 属性, x = 0):
        super().输入属性(属性, x)
        属性.打桩模式 = self.打桩模式.currentIndex()
        属性.超负荷属性 = self.超负荷属性选择.currentIndex()
        # 守门人适用于属强差
        # if (self.希洛克选择状态[9] + self.希洛克选择状态[10] + self.希洛克选择状态[11]) > 1:
        #     try:
        #         属性.火属性强化 += int(self.守门人属强输入[0].text())
        #     except:
        #         pass
        #     try:
        #         属性.冰属性强化 += int(self.守门人属强输入[1].text())
        #     except:
        #         pass    
        #     try:
        #         属性.暗属性强化 += int(self.守门人属强输入[2].text())
        #     except:
        #         pass    
        #     try:
        #         属性.光属性强化 += int(self.守门人属强输入[3].text())
        #     except:
        #         pass
    
