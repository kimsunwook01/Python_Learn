# 삼각형 한 변 길이를 side 변수로 선언. 변수의 초기값을 입력받아 삼각형 그리기
# turtle 라이브러리 받아오기
import turtle

# turtle 그리기
t = turtle.Turtle()
t.shape("turtle")

# 삼각형 한 변의 길이 변수 저장
side = 100

# 삼각형 그리기
t.forward(side)
t.right(-120)
t.forward(side)
t.right(-120)
t.forward(side)
t.right(-120)

# 화면을 끌 때가지 프로그램 작동 유지
turtle.mainloop()
