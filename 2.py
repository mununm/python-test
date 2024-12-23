#한 줄에 하나씩 숫자 입력하기
a=int(input('a입력:'))
b=int(input('b입력:'))
c=int(input('c입력:'))

print(a,b,c,a+b+c)

#한 줄에 여러 개의 숫자 입력받기
a,b,c=map(int,input('a b c값 입력').split())

print(a,b,c,a+b+c)

#문자1.split(문자2) : 문자2를 기준으로 문자1을 자른다.
text=input('날짜 입력 yyyy.mm.dd')
y,m,d=text.split('.')

print(text,y,m,d)

#map(함수, 집합 형태-iterable객체)
a,b,c=map(int,['1','2','3',])
print(a,b,c,a+b+c)

#하나씩 적용
#a,b,c=map(int,input('a b c값 입력').split())
text=input('a b c값 입력')
text=text.split()
a,b,c=map(int,text)

print(a,b,c,a+b+c)




'''
#숫자 출력하기
x=3
y=5
print(x,y,x+y)
print('3과 5의 합은 8이다.')

#숫자와 문자 함께 출력하기 (1) 콤마 & 형변환
print("str(x)'과'str(y)'의 합은'str(x+y)'이다.'")

#숫자와 문자 함께 출력하기 (2) end=''
print(x,end='')
print('과'end='')
print(y,end='')
print('의 합은'end='')
print(x+y,end='')
print('이다.')

#*숫자와 문자 함께 출력하기 (3) format()*
print('()과 ()의 합은 ()이다.'.format(x,y,x+y))
'''




#연산자 우선순위
#산술 연산자  >  관계 연산자  >  논리 연산자
'''
 a**b 지수       <  작다         not x   x가 참이면 거짓 x가 거짓이면 참
                 <= 작거나 같다
 a*b  곱하기     >  크다         x and y x, y 모두 참이어야 함
 a/b  나누기     >= 크거나 같다
 a//b 몫         == 같다         x or y x나y 둘 중 하나만 참이면 참
 a%b  나머지     != 같지 않다

 a+b  더하기
 a-b  빼기
 
ex) 2*5>2+5 and not 3*3>10 ->True
'''





#반올림 : round(a), round(a,b)
print(round(3.33))
print(round(3.66))
print(round(3.66,1))

#절대값 : abs(a)
print(abs(3))
print(abs(-3))

#제곱 : pow(a,b)
print(pow(3,2))
print(3**2)

#나눗셈 : divmod(a,b)
x,y=divmod(7,2)
print(x)
print(y)

#최대값 : max(a,b,c,d,...)
print(max(7,5,1,3))

#최소값 : min(a,b,c,d,...)
print(min(7,5,1,3))

#합 : sum(집합 형태 : lterable)
print(sum([7,5,1,3]))
                 
