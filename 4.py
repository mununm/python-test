#if문
'''
특정 조건을 만족할 때와 만족하지 않을 때를 나누어 코드를 실행하는 조건문

조건이 참일 때 = 실행
조건이 거짓일 때 = 실행하지 않음

if->한 칸 띄어쓰기->조건:
    한 블록 들여쓰기->실행 코드
'''
'''
#if
num=int(input('숫자 하나 입력:'))

if num>0 :
    print('{}은(는) 양수입니다.'.format(num))
'''
'''
#if ~ else
num=int(input('숫자 하나 입력:'))

if num%2==0:
    print('{}은(는) 짝수입니다.'.format(num))
else :
    print('{}은(는) 홀수입니다.'.format(num))
'''
'''
#if ~ elif
age=int(input('나이 입력:'))

if age<=7:
    print('유아입니다.')
elif age<=19:
    print('청소년입니다.')
elif age>=20:
    print('성인입니다.')
'''

#if ~ elif ~ else
text=input('알파벳 입력:')

if text.isupper():
    print('대문자')
elif text.islower():
    print('소문자')
else :
    print('대/소문자 구분 불가능')
