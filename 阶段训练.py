#1
hello='hello hust'
print (hello)

#2
a=eval(input("请输入a:"))
b=eval(input("请输入b:"))
info='''
	1.乘法运算
	2.加法运算
	3.减法运算
	4.除法运算
	5.退出
	'''
while True:
	print(info)
	choice = int(input('your choice:'))
	if isinstance(a,(int,float)) and isinstance(b,(int,float)):

		if choice==1:
				print('a*b=',a*b)
		elif choice==2:
			print('a+b=',a+b)
		elif choice==3:
			print('a-b=',a-b)
		elif choice==4:
			if b!=0:
				print('a/b=',a/b)
			else:
				print("除数不能为0")
		elif choice==5:
			break
		else:
			print('input successful choice ')
	else:
		print('类型错误')
		print(type(a))
		print(type(b))
		break

#3  年龄计算
age = bool(input("Age of the dog: "))

print()

if age < 0:
  print("This can hardly be true!")

elif age == 1:

  print("about 14 human years")

elif age == 2:

  print("about 22 human years")

elif age > 2:

   human = 22 + (age -2)*5

   print("Human years: ", human)

###

   input('press Return>')

#4  求100以内的质数
for i in range(2,101):
    isSUshu = True
    for j in range(1,i):
        if i % j ==0 and j !=1:
            isSUshu = False
            break
    if isSUshu:
        print(i)
    else:continue

#5  函数：肥胖与否？
def fun_bmi(person, height, weight):
    """
    功能：根据身高和体重计算BMI指数
    :param person: 姓名
    :param height: 身高，单位：米
    :param weight: 体重，单位：千克
    """
    print(person + "的身高：" + str(height) + "米\t 体重：" + str(weight) + "千克")
    bmi = weight / (height * height)  # 用于计算BMI指数，公式为“体重/身高的平方”
    print(person + "的BMI指数为：" + str(bmi))

    # 判断身材是否合理
    if bmi < 18.5:
        print("您的体重过轻")
    if 18.5 <= bmi < 24.9:
        print("正常范围，注意保持")
    if 24.9 <= bmi < 29.9:
        print("您的体重过重")
    if bmi > 18.5:
        print("肥胖")

#6  一个book类


class book:  # 定义 book 类
	author = ''  # 定义 author 属性
	name = ''  # 定义 name 属性
	pages = 0  # 定义 pages 属性
	price = 0  # 定义 price 属性
	press = ''  # 定义 press 属性


a = book()  # book 类实例化
print(a)  # 查看对象 a
print(a.author)  # 访问 author 属性
print(a.pages)  # 访问 pages 属性
print(a.price)  # 访问 price 属性

a.author = 'Tutu'  # 设置 author 属性
a.pages = 300  # 设置 pages 属性
a.price = 25  # 设置 price 属性
print(a.author)  # 重新访问 author 属性
print(a.pages)  # 重新访问 pages 属性
print(a.price)  # 重新访问 price 属性
b = book()  # 将 book 类实例化生成 b 对象
print(b.author)  # 访问 b 对象的 author 属性
print(b.price)  # 访问 b 对象的 price 属性
b.author = 'Butter'  # 设置 b 对象的 author 属性
b.price = 15  # 设置 b 对象的 price 属性

print(b.price)  # 访问 b 对象的 price 属性
print(a.price)  # 访问 a 对象的 price 属性，没有发生改变
print(b.author)  # 访问 b 对象的 author 属性
print(a.author)  # 访问 a 对象的 author 属性，没有发生改变
print(b.pages)  # 访问 b 对象的 pages 属性
print(a.pages)  # 访问 a 对象的 pages 属性

#7 见预习作业：超市货物管理系统




