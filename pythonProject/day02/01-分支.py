a = 10
if a > 3:
    print('我是if语句的结构体')
    print('我也是if语句的结构体')

print('我和if是平级')

# # 单分支
# age = int(input('请输入你的年龄'))
# if age > 18:
#     print('成年了，可以上网')
#
# # 双分支
# high = int(input('请输入你的身高'))
# if high > 18:
#     print('可以进动物园了')
# else:
#     print('需要买票')

# 写法1 多分支
# score = int(input('输入你的成绩：'))
# if score >= 90 and score <= 100:
#     print('优秀')
# elif score >= 80 and score <90:
#     print("良好")
# elif score >= 70 and score <80:
#     print("良")
# elif score >= 60 and score <70:
#     print("及格")
# elif score >= 0 and score < 60:
#     print('不及格')
# else:
#     print('打')


# 写法2 python独有
score = int(input('输入你的成绩：'))
if 90<=score<=100:
    print('优秀')
elif 80<=score<90:
    print("良好")
elif 70<=score<80:
    print("良")
elif 60<=score<70:
    print("及格")
elif 0<=score<60:
    print('不及格')
else:
    print('打')

# 写法3  实际开发
score = int(input('输入你的成绩：'))
if score<=0 or score>=100:
    print('打')
elif score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 70:
    print("良")
elif score >= 60:
    print('及格')
else:
    print('不及格')