#리스트 만들기
li=[]
li=list()

#리스트 인덱스
li=['a','b','c']

li[0]
li[1]
li[2]

li[2]='d'

#리스트 활용

li=['a','b','c','d','e']

li.index('c')        #위치 찾기

liappend('f')        #추가하기1
li.insert(0,'aa')    #추가하기2

li.remove('aa')      #삭제하기1
del li[2]            #삭제하기2

'b' in li            #확인하기

len                  #전체 개수

li.count('a')        #개수 세기



num=[1,2,3,4,5,9,7,6,8,10]

sum(num)             #합 구하기
min(num)             #최소값
max(num)             #최대값

num.reverse()        #역순 만들기

num.sort()                      #오름차순 정렬
num.sort(reverse=True)          #내림차순 정렬
