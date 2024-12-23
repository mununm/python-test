#숫자형
print("숫자형")
'''
1.정수형 int             -연산이 가능하다
2.실수형 float           -숫자를 다루는 내장함수들 사용 가능
3.복소수 complex 등등    ex) round(), range(), pow() 등
a//b : a를 b로 나눈 몫
a%b : a를 b로 나눈 나머지
a**b : a의 b제곱
'''
#정수형 int
a=10
b=5
#실수형 float
c=2.0
d=0.5
print('int와 int의 연산')
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
print('int와 float의 연산')
print(b+c)
print(b-c)
print(b*c)
print(b/c)
print(b//c)
print(b%c)
print(b**c)
#논리형
'''                      -참과 거짓을 나타내는 자료형
                      
1.bool                -주로 비교&논리 연산자로 만들어진다
  ->True 참/False 거짓
                      -조건문에 많이 활용된다
비교 연산자     논리 연산자
== : 같다       x or y : x나 y 둘 중 하나만 참이면 참
!= : 같지 않다  x and y : x, y 모두 참이어야 함
                not x : x가 참이면 거짓, x가 거짓이면 참
'''
print()
print("논리형")
x=10
y=-10

print(x>0)
print(y>0)
print()
print(x>y)
print(x<y)
print()
print(x==10)
print(x==y)
print(x!=y)
print()
print(x>0 or y>0)
print(x>0 and y>0)
print()
print(x>0)
print(not x>0)
#문자열형
print()
print("문자열형")
'''
1.str -> 다른 언어와 달리 문자와 문자열을 따로 구분하지 않는다.
''또는""에 감싸져 있다.
연산이 불가능하다. (예외 : 문자 + 문자, 문자*정수)
문자열을 다루는 다양한 메소드들이 존재한다.
ex) split(), join(), upper(), lower(), replace() 등
'''
a=5
b='5'
c=5.0

print(a+a) #int+int
print()
print(b+b) #str+str
print(a*b) #int*str
print()
'''
print(a+b) #int+str
print(b+c) #str*float
'''

print('안녕하세요')
print("안녕하세요")
#print("안녕하세요')
#군집 자료형
print()
print("군집 자료형")
'''
                 -여러 데이터를 모은 집합 형태 자료형
1.리스트 list    -데이터를 순차적으로 저장 -> 열거형
2.튜플 tuple     -값을 변경할 수 없는 열거형 집합
3.세트 set       -순서가 없고 중복이 허용되지 않는 집합
4.사전 dictionary-키와 값의 쌍으로 구성된 집합
'''
#자료형 변환
print()
print("자료형 변환")
'''
파이썬은 사용자가 자료형을 결정하지 않기 때문에 편리하기도 하지만
데이터가 사용자의 의도와 다른 자료형이 될 수도 있다.
이때는 각 데이터들의 자료형을 원하는 것으로 변경해야 한다.
ex) input()사용, 정수와 실수의 사용 등

자료형 변환 (typecasting) 방법 : 원하는 자료형 함수에 값을 넣는다.
ex) str(10), int('10'), int(12.5), list('hello') 등
'''
#input()으로 숫자 입력 받기

a=int(input('숫자를 입력하세요'))

print(a+a)

'''
#실수 <-> 정수
num=5.0
range(int(num))
'''

a=input('숫자 하나 입력')
b=int(a)
c=float(a)

print(type(a))
print(type(b))
print(type(c))
