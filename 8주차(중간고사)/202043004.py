# 2024/04/24 기초프로그래밍 중간고사
# 컴퓨터공학과 202043004 김선욱

# # 문제 1. 한 개의 정수를 입력받아서 입력된 숫자가 ‘100보다 작음’, ‘100에서 1000 사이’, ‘1000보 다 큼’으로 구분하여 출력. 중첩 if문 사용
# num = int(input("한 개의 정수를 입력하시오: "))
# if num < 100:
#     print("100보다 작음")
# elif num >= 100:
#     if num > 1000:
#         print("1000보다 큼")
#     else:
#         print("100에서 1000사이")

# # 문제 2. 국어, 영어, 수학 점수를 실수로 입력받아 정수형 평균으로 학점을 출력
# print("과목별 점수를 입력하시오")
# language = float(input("국어 점수: "))
# english = float(input("영어 점수: "))
# math = float(input("수학 점수: "))
# avr = int((language + english + math)/3)
# print(f"평균{avr}점")
# if avr <= 100 and avr >=80:
#     print("A학점")
# elif avr >= 60 and avr <= 79:
#     print("B학점")
# elif avr < 60 and avr >= 0:
#     print("F학점")
# else:
#     print("올바른 점수를 입력하세요")

# # 문제 3. 랜덤하게 2개의 정수를 발생시켜서 첫 번째 정수가 두 번째 정수로 나누어 떨어지는 지를 검사. 난수가 발생되는 정수의 범위는 20에서 100 사이
# import random
# num1 = random.randint(20,100)
# num2 = random.randint(20,100)
# print(f"첫 번째 정수: {num1}\n두 번째 정수: {num2}")
# if num1 % num2 == 0:
#     print("첫 번째 정수가 두 번째 정수로 나누어 떨어진다.")
# else:
#     print("나누어 떨어지지 않는다.")

# 문제 4. 사용자로부터 실수를 입력받아서 정수로 변환 후 양수인지, 0인지, 음수인지를 출력
fnum = float(input("실수를 입력하세요: "))
fnum = int(fnum)
if fnum > 0:
    print("양수")
elif fnum < 0:
    print("음수")
else:
    print("0")
