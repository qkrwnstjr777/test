# ss="파이썬만세"
# print(ss[0])
# print(ss[1:3])
# print(ss[3:])

# ss='파이썬'+'만세'
# print(ss)
# ss='파이썬'*3
# print(ss)

# ss='파이썬abcd'
# print(len(ss))

# ss='파이썬짱!'
#
# sslen=len(ss)
# for i in range(0,sslen) :
#     print(ss[i]+'$',end='')

# 소스코드 8-1 스스로 문제해결

# ss='파이썬은완전재미있어요'
#
# sslen=len(ss)
# for i in range(0,sslen,2) :
#     print(ss[i]+'#',end='')

# 소스코드 8-2

## 변수 선언 부분
# inStr,outStr="",""
# count, i=0,0
#
# ## 메인 코드
# inStr=input("문자열을 입력하세요 :")
# count=len(inStr)
#
# for i in range(0,count):
#     outStr+=inStr[count-(i+1)]
#
# print("내용을 거꾸로 출력-->%s" %outStr)