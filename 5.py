#while문
'''
특정 조건을 만족할 때 코드를 반복 실행하는 조건문

조건이 참일 때 = 반복 실행
조건이 거짓일 때 = 반복 종료

while->한 칸 띄어쓰기->조건:
       한 블록 들여쓰기->실행 코드
'''
'''
#while문
print('a가 0보다 같거나 크면 실행, 작으면 정지')

a=int(input('a:'))

while a>=0:
    print('실행')
    a=int(input('a:'))
'''
'''
#무한루프
a=10

while a>0:
    print('실행')
'''
'''
#n번 반복하기
n=int(input('n:'))

while n:
    print(n)
    n=n-1
'''

#~까지 반복하기
'''
#(1)1 ~ 10까지 숫자 반복하기
n=1
while n<=10:
    print(n)
    n=n+1
'''
'''
#(2)yes를 입력하면 반복하기
text='yes'

while text=='yes':
    text=input('yes 입력 시 반복')

print('종료')
'''

#(3)e 또는 E가 입력될 때까지 반복하기
text=input('e 또는 E 입력 시 종료')

while text!='e' and text!='E':
    text=input('e 또는 E 입력 시 종료')

print('종료')
