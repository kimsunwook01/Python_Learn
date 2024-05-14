# 3개의 정수를 입력받아 if else문을 이용해 가장 작은 값을 결정
num1, num2, num3 = eval(input("세개의 정수를 입력하시오: "))
if num1 < num2:
    if num1 < num3:
        print(f"제일 작은 정수는 {num1}입니다.")
elif num2 < num1:
    if num2 < num3:
        print(f"제일 작은 정수는 {num2}입니다.")
    elif num3 < num2:
        print(f"제일 작은 정수는 {num3}입니다.")
elif num1 == num2 and num2 == num3:
    print(f"정수의 값이 모두 같은 {num1}입니다.")
else:
    print("잘못된 입력")