# for i in [9, 8, 7, 6, 5]:
#     print("i =", i)

# for i in range(5):
#     print("i =", i)

# for i in range(1, 11, 2): #range(시작값, 종료값, 증가값)
#     print("i =", i)

# sum = 0
# for i in range(3):
#     print("i =", i)
#     sum += i
# print("합계: ", sum)

# for i in range(3):
#     print("i =", i, end="   ") #end="" print내용을 일렬로 출력

# sum = 0
# n =10
# for i in range(1, n+1):
#     print("i =",i)
#     sum += i
# print("합계: ", sum)

# for i in range(1, 10):
#     print(f"{i}단")
#     for j in range(1, 10):
#         print(f"{i}*{j}={i*j}", end=" ")
#     print("\n")

# import turtle
# t = turtle.Turtle()
# t.shape("turtle")
# s = turtle.textinput("", "몇각형을 원하시나요?")
# n = int(s)
# for i in range(n):
#     t.forward(100)
#     t.left(360/n)
# turtle.done()

# import turtle
# t = turtle.Turtle()
# t.shape("turtle")

# for i in range(10, 4,-2):
#     t.forward(100)
#     t.left(120)
# turtle.done()

# TARGET = 2000
# money = 1000
# year = 0
# rate = 0.07
# while money < TARGET:
#     money += money*rate
#     year += 1
# print(year,"년")

# i = 10
# sum = 0
# while i >= 1:
#     sum += i
#     i -= 1
# print("합:", sum)

# sum = 0
# num = 0
# answer = "yes"
# while answer == "yes":
#     num = int(input("숫자를 입력하세요: "))
#     sum += num
#     answer = input("계속?(yes/no)")
# print("합계: ", sum)

import random
num = random.randint(1, 100)
answer = 0
total = 0
print("1 부터 100 사이의 값을 맞추시오")
while answer != num:
    answer = int(input("숫자를 입력하시오: "))
    if answer == num:
        print("정답!")
    elif answer > num:
        print("너무 높음!")
    elif answer < num:
        print("너무 낮음!")

