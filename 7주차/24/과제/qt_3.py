# 문자 하나 입력 받아 그것이 R 또는 r 이면 Rectangle 출력. T 또는 t면 Triangle. C 또는 c이면 Circle 출력. 그 외 Unknown 출력
char = input("문자 하나 입력: ")
if char == 'R' or 'r':
    print("Rectangle")
elif char == 'T' or 't':
    print("Triangle")
elif char == 'C' or 'c':
    print("Circle")
else:
    print("Unknown")
