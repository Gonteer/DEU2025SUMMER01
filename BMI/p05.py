#BMI(허세지수) 프로그램 v0.5

datas = [] #누적 데이터 보관 리스트

def pandan(bmi) :
    
    if bmi >= 2.5 :
        return '허세작렬'
    elif bmi >= 2.0 :
        return '고도허세'
    elif bmi >= 1.5 :
        return '과한허세'
    elif bmi >= 1.0 :
        return '정상'
    else :
        return '저허세'
    

while True :
    
    salary = int(input('당신의 월급은?'))
    car = int(input('당신의 차량 가격은?'))

    bmi = car / (salary * 6)

    datas.append([salary,car,bmi]) #리스트에 계속 데이터 누적하기

    #사용자가 원하는 만큼 입력 받도록 하는 기능 추가
    t = input("계속하시겠습니까?(y/n)")
    if t == 'n':
        print('프로그램 종료')
        break
    else :
        print()

print('월급\t차량가격\tBMI\t상태')
for i in datas :
    print(i[0],'\t',i[1]'\t',round(i[2],2),'\t',pandan(i[2]))
    
