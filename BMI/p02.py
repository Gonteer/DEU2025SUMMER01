#BMI(허세지수) 프로그램 v0.2
salary = int(input('당신의 월급은?'))
car = int(input('당신의 차량 가격은?'))

bmi = car / (salary * 6)

print('당신의 허세지수는', bmi, '입니다')

if bmi >= 1.5 :
    print('그리고 당신은 허세 입니다.')
else :
    print('그리고 당신은 보통 입니다.')
