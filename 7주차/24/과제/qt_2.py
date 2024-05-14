# 문제 2. 사용자로부터 정수를 입력받아 '양수', '음수, '0'을 구분
num = int(input("정수를 입력하세요: "))
if num == 0:
    print("0")
elif num > 0:
    print("양수")
elif num < 0:
    print("음수")
else:
    print("err")