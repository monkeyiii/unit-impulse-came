# 欢迎使用pycharm
# 请在“哔”声后开始操作
# 模板开发时间:2022/8/20 9:12
import datetime
i = datetime.datetime.now()


def yeartype(year):
    return int(year%4 ==0 or (year%100 != 0 and year%400 == 0))


def birthgap(month, day):
    monthlength = [0,31,28+yeartype(i.year),31,30,31,30,31,31,30,31,30,31]
    gap = monthlength[i.month] - i.day
    if month > i.month:
        for j in range(i.month+1, month):
            gap += monthlength[j]
        gap += day

    if month == i.month and day > i.day:
        gap = day-i.day

    if month < i.month or (month == i.month and day <= i.day):
        for k in range(i.month+1, 13):
            gap += monthlength[k]
        monthlength[2] = 28+yeartype(i.year+1)
        for m in range(1, month):
            gap += monthlength[m]
        gap += day
    return gap


print(birthgap(2, 11))



