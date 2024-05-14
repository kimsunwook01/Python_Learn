# 삼각형의 밑변, 높이를 입력받아 넓이 구하기

# 밑변과 높이 입력
base = int(input("삼각형의 밑변:    "))
height = int(input("삼각형의 높이:    "))

# 넓이 계산
width = (base*height)/2

# 결과 출력. 소수점 첫째 자리까지
print(f"삼각형의 넓이:  {width:.1f}")