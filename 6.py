# for문
'''
특정 범위만큼 코드를 반복 실행하는 조건문

열거형 데이터를 하나씩 변수 값에 대입하며 실행

for 변수 in 열거형:
    실행 코드
'''
#range()함수
'''
숫자의 범위와 증감 값을 정하면 규칙적인 수들의 집합으로 만들어주는 함수

range (a)     -> 0 ~ a-1
range (a,b)   -> a ~ b-1
range (a,b,c) -> a~b-1, c씩 증가

* a,b,c는 모두 정수(int)만 가능

 range(11)
 - 0부터 10(11-1)까지 1씩 증가
 - 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

 range(1,11)
 - 1부터 10(11-1)까지 1씩 증가
 - 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

 range(1,11,2)
- 1부터 10(11-1)까지 2씩 증가
- 1, 3, 5, 7, 9
'''
#range() 연습

list(range(5))
#0, 1, 2, 3, 4

list(range(1,11))
#1, 2, 3, 4, 5, 6, 7, 8, 9, 10

list(range(3,10,3))
#3, 6, 9

list(range(5,0,-1))
#5, 4, 3, 2, 1

list(range(10,-11,-5))
#10, 5, 0, -5, -10

#for문

for i in range(10):
    print(i)


#1에서 n까지 출력

n=int(input('n:'))
for i in range(1,n+1):
    print(i)

#a에서 b까지 출력

a,b=map(int,input('a b:').split())

for i in range(a,b+1):
    print(i)
    
#n에서 0까지 출력

n=int(input('n:'))

for i in range(n,-1,-1):
    print(i)
