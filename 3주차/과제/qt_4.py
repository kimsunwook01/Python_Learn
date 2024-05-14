# 변수 2개 생성 후 10과 20 저장. 이 2개의 변수 값을 서로 바꾸기

# 변수 2개 선언 후 10 20 저장
numA = 10
numB = 20
# 결과 출력
print(f"바꾸기 전:   a = {numA} b = {numB}")
# 변수 2개 값 바꾸기
numA, numB = numB, numA
# 결과출력
print(f"바꾸기 후:   a = {numA} b = {numB}")