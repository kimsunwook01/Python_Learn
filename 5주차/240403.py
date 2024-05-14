# # 예제: 배송비 계산
# price = int(input("상품의 가격: "))
# if price > 20000:
#     shipping_cost = 0
# else:
#     shipping_cost = 3000
# print(f"배송비는 {shipping_cost}원 입니다.")
# print("배송비는", shipping_cost,"원 입니다")
# print("배송비는 %d원 입니다." %shipping_cost)

# # 예제: 파이썬 카드 그리고 2만원 초과시 배송비 계산
# price = int(input("상품의 가격: "))
# card = input("카드의 종류를 입력하시오: ")
# shipping_cost = 3000
# if price > 20000 and card == "파이썬":
#     shipping_cost = 0
# print(f"배송비는 {shipping_cost}원 입니다.")

# #산술퀴즈 프로그램
# import random
# x = random.randint(1, 100)
# y = random.randint(1, 100)
# answer = int(input(f"{x} + {y} = "))
# if (x+y) == answer:
#     print("정답입니다")
# else:
#     print("오답입니다.")

# # 예제: 로그인
# id = "1q2w3e4r"
# s = input("아이디를 입력하시오: ")
# if id == s:
#     print("환영합니다.")
# else:
#     print("아이디를 찾을 수 없습니다.")

# # 배송비 계산 예제2
# country = input("배송지(한국과 미국만 가능): ")
# price = int(input("상품의 가격)"))

# if country == "한국":
#     if price >= 20000:
#         sh_cost = 0
#     else:
#         sh_cost = 3000
# else:
#     if price >= 100000:
#         sh_cost = 0
#     else:
#         sh_cost = 8000

# print(f"배송비는 {sh_cost}원 입니다.")


# 배송비 계산 예제3
# country = input("배송지(한국과 미국만 가능): ")
# price = int(input("상품의 가격)"))

# if country == "한국" and price >= 20000:
#     sh_cost = 0
# elif country == "한국" and price < 20000:
#     sh_cost = 3000

# print(f"배송비는 {sh_cost}원 입니다.")


# # 연속 if문 학점 결정 예제
# score = int(input("성적을 입력하시오: "))
# if score >= 90:
#     print("학점 A")
# elif score >= 80:
#     print("학점 B")
# elif score >= 70:
#     print("학점 C")
# elif score >= 60:
#     print("학점 D")
# else:
#     print("학점 F")