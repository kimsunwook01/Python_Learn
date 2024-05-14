# 문제1: 2~50 사이의 모든 짝수를 출력하는 반복 루프
# for i in range(2, 51, 2):
#     print(i, end=" ")

# 문제2: 리스트에 저장된 정수들의 합을 계산
# sum = 0
# for i in [11, 22, 23, 99, 81, 93, 35]:
#     sum += i
# print(f"정수들의 합은 {sum}")

# 문제3: 사용자가 입력한 정수의 모든 약수를 화면에 출력
# num = int(input("정수를 입력하시오: "))
# for i in range(1, num+1):
#     if num % i == 0:
#         print(i, end=" ")

# 문제4: 중첩 반복문을 사용하여 출력
# num = int(input("정수를 입력하시오: "))
# for i in range(1, num+1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()

# 문제5: 마일을 킬로미터로 변환하는 표 출력
# print("마일	        킬로미터")
# for i in range(1, 11):
#     km = 1.609 * i
#     print(f"{i}         {km}")