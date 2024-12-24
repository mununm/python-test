#문자열 인덱스
'''
text='abc'

print(text[0]) #text[-3] == text[0]
print(text[1]) #text[-2] == text[1]
print(text[2]) #text[-1] == text[2]
#print(text[3])
#print(text[2.0])
'''
#문자열 슬라이스

text='abcde fgh ijk'

'''
print(text[2:5])
print(text[1:8])
print(text[-5:-1])
print(text[5:])
print(text[:5])
print(text[:])
'''
print(text[0:8:2])
print(text[1:8:2])
print(text[8:0:-1])
print(text[::-1])

#문자열 메서드

#1.출력 지정 : format(a,b,c,...)
text='abcde {} {}'
print(text,format('ABC',123))

#2.대체하기 : replace(a,b)
text='abcde ABC ABC'
print(text,replace('A','K'))

#3.자르기 : split(a)
text='abcde A/B/C A.B.C'
a,b,c=text.split('/')
print(a)
print(b)
print(c)

#4.합치기 : a.join
text='abcde'
print('/'.join(text))

#5.개수 확인하기 : count(a)
text='abcde ABC ABC'
print(text.count('a'))
print(text.count('A'))
print(text.count('1'))

#6.제거하기 : strip(a)/lstrip(a)/rstrip(a)
text=' abcde  '
print(text.strip())
print(text.lstrip())
print(text.rstrip())

#7.인덱스 찾기 : find(a)/rfind(a)/index(a)/rindex(a)
text='ABC ABC'
print(text.find('A'))
print(text.rfind('A'))
print(text.index('A'))
print(text.rindex('A'))

#8.확인하기 : isalpha()/isdigit()/isalnum()/isupper()/islower
text1='ABCabc123'
text2='123'
text3='ABC'
text4='abc'

print()text1.isalpha())
print()text1.isdigit())
print()text1.isalnum())
print()text1.isupper())
print()text1.islower())

#9.대/소문자 만들기 : upper()/lower()
text='ABCabc'
print(text.upper())
print(text.lower())

#10.0 채우기 : zfill()
y='2020'
m='3'
d='1'

print(y.zfill('4'))
print(m.zfill('2'))
print(d.zfill('2'))
