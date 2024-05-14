# # 산수 문제 출제
# import random
# x = random.randint(1, 100)
# y = random.randint(1, 100)
# answer = int(input(f"{x} + {y} = "))
# flag = (answer == (x+y))
# print(flag)

# # 배송비 계산
# area = input("배송지(현재는 한국과 미국만 가능: ")
# price = int(input("상품의 가격: "))
# if area == '한국':
#     if price >= 20000:
#         print(f"배송비 = {price}")
#     else :
#         print(f"배송비 = {price + 3000}")
# else :
#     if price >= 100000 :
#         print(f"배송비 = {price}")
#     else :
#         print(f"배송비 = {price + 8000}")

# # 리히터 규모
# scal = float(input("리히터 규모를 입력하십시오: "))
# if scal < 2.0:
#     print("지진계에 의해서만 탐지 가능")
# elif scal >= 2.0 and scal <= 3.9:
#     print("물건들이 흔들리거나 떨어진다")
# elif scal >= 4.0 and scal <= 6.9:
#     print("빈약한 건물에 큰 피해")
# elif scal >= 7.0 and scal <= 7.9:
#     print("지표면에 균열")
# elif scal >= 8.0 and scal <= 9.0:
#     print("대부분의 구조물 파괴")

# # 도형 그리기
# import turtle
# t = turtle.Turtle()
# t.shape("turtle")
# s = turtle.textinput("", "도형을 입력하시오: ")
# if s == "사각형":
#     w = int(turtle.textinput("", "가로: "))
#     h = int(turtle.textinput("", "세로: "))
#     t.forward(w)
#     t.left(90)
#     t.forward(h)
#     t.left(90)
#     t.forward(w)
#     t.left(90)
#     t.forward(h)
# elif s == "삼각형":
#     w = int(turtle.textinput("", "길이: "))
#     # h = int(turtle.textinput("", "각도: "))
#     t.forward(w)
#     t.right(-120)
#     t.forward(w)
#     t.right(-120)
#     t.forward(w)
#     t.right(-120)
# turtle.done()

# # 2개의 정수 받아 첫 번째 정수가 두 번째 정수로 나누어 떨어지는지 검사(약수 검사)
# num1 = int(input("정수를 입력하시오: "))
# num2 = int(input("정수를 입력하시오: "))
# if num1 % num2 == 0:
#     print("약수입니다.")
# else :
#     print("약수가 아닙니다.")

# # 정수를 입력받아 양수, 0, 음수 검사하여 출력
# num = int(input("정수를 입력하세요: "))
# if num > 0:
#     print("양수")
# elif num == 0:
#     print("0")
# elif num < 0:
#     print("음수")
# else:
#     print("err")

# # 문자 하나 입력 받아 그것이 R 또는 r 이면 Rectangle 출력. T 또는 t면 Triangle. C 또는 c이면 Circle 출력. 그 외 Unknown 출력
# char = input("문자 하나 입력: ")
# if char == 'R' or 'r':
#     print("Rectangle")
# elif char == 'T' or 't':
#     print("Triangle")
# elif char == 'C' or 'c':
#     print("Circle")
# else:
#     print("Unknown")

# # 연습문제 7번. 코드 간결하게
# temp = int(input("온도를 입력: "))
# if temp < 0:
#     state = "얼음"
# else:
#     state = "기체"
# print(state)

# 연습문제 11번
score = 87
if score >= 90:
    grade = "A" 
elif score >= 80:
    grade = "B" 
elif score >= 70:
    erade = "C" 
elif score >= 60:
    grade = "D"