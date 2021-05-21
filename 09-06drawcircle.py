import turtle as t
t.setup(500,400) #초기 원도의 크기 조정
t.speed(1) #1에서 10까지 거북이 속도 증가, 0이면 최고속도

t.pu() #이동에 선이 그려지지 않도록 penup
t.goto(0,-100) # 이동

t.pd()#이동에 선이 그려지도록 pendown 
t.hideturtle() #거북이는 보이지 않도록
t.fillcolor('aqua') # 내부 칠할 색 지정
t.begin_fill() # 칠하기 시작
t.circle(100) #원 그리기
t.end_fill() #칠하기 종료
