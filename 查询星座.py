import 类
birthday2 = 类.Birthday(2010, 10, 1)

# i = 'a'
# print(birthday2.month)


def constellation(birthday):   # 查询星座
    i = 'a'
    j = 'b'
    if birthday.month == 3 and birthday.day >= 21:
        i = 'Aries/'  # i作为星座字符串,白羊
        j = '白羊'
    elif birthday.month == 4 and birthday.day <= 19:
        i = 'Aries/'
        j = '白羊'
    elif birthday.month == 4 and birthday.day >= 20:
        i = 'Taurus/'  # 金牛
        j = '金牛'
    elif birthday.month == 5 and birthday.day <= 20:
        i = 'Taurus/'
        j = '金牛'
    elif birthday.month == 5 and birthday.day >= 21:
        i = 'Gemini/'  # 双子
        j = '双子'
    elif birthday.month == 6 and birthday.day <= 21:
        i = 'Gemini/'
        j = '双子'
    elif birthday.month == 6 and birthday.day >= 22:
        i = 'Cancer/'  # 巨蟹
        j = '巨蟹'
    elif birthday.month == 7 and birthday.day <= 22:
        i = 'Cancer/'
        j = '巨蟹'
    elif birthday.month == 7 and birthday.day >= 23:
        i = 'Leo/'  # 狮子
        j = '狮子'
    elif birthday.month == 8 and birthday.day <= 22:
        i = 'Leo/'
        j = '狮子'
    elif birthday.month == 8 and birthday.day >= 23:
        i = 'Virgo/'  # 处女
        j = '处女'
    elif birthday.month == 9 and birthday.day <= 22:
        i = 'Virgo/'
        j = '处女'
    elif birthday.month == 9 and birthday.day >= 23:
        i = 'Libra/'  # 天秤
        j = '天秤'
    elif birthday.month == 10 and birthday.day <= 23:
        i = 'Libra/'
        j = '天秤'
    elif birthday.month == 10 and birthday.day >= 24:
        i = 'Scorpio/'  # 天蝎
        j = '天蝎'
    elif birthday.month == 11 and birthday.day <= 22:
        i = 'Scorpio/'
        j = '天蝎'
    elif birthday.month == 11 and birthday.day >= 23:
        i = 'Sagittarius/'  # 射手
        j = '射手'
    elif birthday.month == 12 and birthday.day <= 21:
        i = 'Sagittarius/'
        j = '射手'
    elif birthday.month == 12 and birthday.day >= 22:
        i = 'Capricorn/'  # 摩羯
        j = '摩羯'
    elif birthday.month == 1 and birthday.day <= 19:
        i = 'Capricorn/'
        j = '摩羯'
    elif birthday.month == 1 and birthday.day >= 20:
        i = 'Aquarius/'  # 水瓶
        j = '水瓶'
    elif birthday.month == 2 and birthday.day <= 18:
        i = 'Aquarius/'
        j = '水瓶'
    elif birthday.month == 2 and birthday.day >= 19:
        i = 'Pisces/'  # 双鱼
        j = '双鱼'
    elif birthday.month == 3 and birthday.day <= 20:
        i = 'Pisces/'
        j = '双鱼'
    return i, j


(f, g) = constellation(birthday2)
print(f)  # f为 英文/ 格式
print(g)  # g为 中文  格式
