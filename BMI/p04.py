#BMI(허세지수) 프로그램 v0.4
while True :
    
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

    #사용자가 원하는 만큼 입력 받도록 하는 기능 추가
    t = input("계속하시겠습니까?(y/n)")
    if t == 'n':
        print('프로그램 종료')
        break
    else :
        print()
