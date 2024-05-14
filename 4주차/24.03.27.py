# x = int(input("피젯수 입력  : "))
# y = int(input("젯수 입력    : "))
# q = x//y
# r = x%y
# print(f"{x}를 {y}로 나눈 몫: {q}")
# print(f"{x}를 {y}로 나눈 나머지: {r}")
# print(f"{x} ÷ {y} = {q}...{r}")

# print(2**5)

# total_sales = 0
# milk_price = 2000
# cola_price = 3000
# krice_price = 3500
# milk_sale = int(input("우유 판매 개수:   "))
# cola_sale = int(input("콜라 판매 개수:   "))
# krice_sale = int(input("김밥 판매 개수:   "))
# total_sales += milk_sale*milk_price
# total_sales += cola_sale*cola_price
# total_sales += krice_sale*krice_price
# print(f"오늘 총 매출은 {total_sales}원 입니다.")

# # 삼각형의 넓이 구하기
# a = int(input("삼각형의 밑변:   "))
# b = int(input("삼각형의 높이:   "))
# w = (a*b)/2
# print(f"삼각형의 넓이:  {w}")

# score1 = int(input("국어성적:    "))
# score2 = int(input("수학성적:    "))
# score3 = int(input("영어성적:    "))
# avg = (score1 + score2 + score3)/3
# print(f"평균 성적은 {avg:.2f}점입니다.")

# print("산수 퀴즈에 오신 것을 환영합니다.\n")
# num = int(input("2 + 5 = "))
# print(7 == num)
# num = int(input("7 - 6 = "))
# print(1 == num)
# num = int(input("2 ** 3 = "))
# print(8 == num)
# num = float(input("3.0 / 1.5 = "))
# print(2.0 == num)

score = 0

ans = input("가장 쉬운 프로그래밍 언어는? ")
check = (ans=="파이썬")
print(check)

score += int(check)
ans = input("거듭제곱을 계산하는 연산자는? ")
check = (ans=="**")
print(check)

score += int(check)
ans = input("파이썬에서 출력시에 사용하는 함수이름은? ")
check = (ans=="print")
print(check)

score += int(check)
print(f"점수 = {score}")