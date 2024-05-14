# 키와 나이를 입력받아 140, 10 이상이면 '타도 좋습니다' 아닐 경우 '죄송합니다' 출력
height, old = eval(input("키와 나이를 입력하세요: "))
print(f"키{height}cm, 나이{old}살")
if height >= 140 and old >= 10:
    print("타도 좋습니다.")
else:
    print("죄송합니다.")