import datetime

i = datetime.datetime.now()


class Birthday:
    def __init__(self, year=-1, month=1, day=1):  # 构造方法
        self.year = year
        self.month = month
        self.day = day

    def say_birthday(self):
        print(self.year, self.month, self.day)

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def inquiry(self):   # 查询离下个生日差多远
        a = 1

    def constellation(self):   # 查询星座
        c = 1

    def luck(self):   # 查询运势
        b = 1


b = ""
s1 = Birthday(b, 4, 30)
a = s1.year
if a == "":
    print('空')
print(a)
s1.say_birthday()

