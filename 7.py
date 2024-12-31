#continue/break/pass
'''
continue
- 해당 단계만 건너뛰고 다음 단계로 간다

break
- 제어문을 중단하고 빠져나간다          ->제어문과 함께 다양하게 활용되는 명령문

pass
- 아무 작업도 하지 않는다
'''
'''
#continue
for i in range(1,11):
    if i ==5:
        continue
    print(i)

#break
for i in range(1,11):
    if i ==5:
        break
    print(i)

#pass
for i in range(1,11):
    if i ==5:
        pass
    print(i)
'''
#비워두기

n= int(input('n:'))

if n>0:
    pass
else:
    pass
