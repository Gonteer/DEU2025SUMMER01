#BMI(허세지수) 프로그램 v0.3
salary = int(input('당신의 월급은?'))
car = int(input('당신의 차량 가격은?'))

bmi = car / (salary * 6)

print('당신의 허세지수는', bmi, '입니다')

print('그리고 당신은',end=' ')
if bmi >= 2.5 :
    print('허세작렬',end=' ')
elif bmi >= 2.0 :
    print('고도허세',end=' ')
elif bmi >= 1.5 :
    print('과한허세',end=' ')
elif bmi >= 1.0 :
    print('정상',end=' ')
else :
    print('저허세',end=' ')
print('입니다.')
