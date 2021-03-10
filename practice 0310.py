# ## 변수 선언 부분,
# money, c500, c100, c50, c10 = 0,0,0,0,0
#
# ##메인 코드 부분
# money = int(input("교환할 돈은 얼마?\n"))
#
# c500= money //50000
# money %= 50000
#
# c100 = money //10000
# money %= 10000
#
# c50 = money//5000
# money %= 5000
#
# c10 = money//1000
# money %= 1000
#
# print("\n 오만원짜리 ==> %d 개" % c500)
# print(" 만원짜리 ==> %d 개" % c100)
# print(" 오천원짜리 ==> %d 개" % c50)
# print(" 천원짜리 ==> %d 개" % c10)
# print(" 바꾸지 못한 잔돈 ==> %d 원\n" % money)


# # 관계연산자 참, 거짓
# a,b= 100,200
# print(a==b, a!=b, a>b, a<b, a>=b, a<=b)

# # 논리 연산자
#
# a=99
# (a>100) and (a<200)
# (a>100) or (a<200)
# not(a == 100)

# # 참 거짓 조건문
# if(1234) : print("참이면 보여요")
# if(0) : print("거짓이면 안보여요")

# # 윤년 계산 프로그램
#
# ## 변수 선언 부분
# year = 0
#
# ## 메인 코드 부분
# year=int(input("연도를 입력 하세요 :"))
#
# if(((year%4==0) and (year%100 !=0)) or (year%400==0)) :
#     print("%d 년은 윤년입니다." %year);
# else :
#     print("%d 년은 윤년이 아닙니다." % year);

# # 문자열을 숫자로 변환한 후 계산하는 식
# s1, s2, s3 = "111", "111.11", "99999999999"
#
# print(int(s1)+111.11)
# print(float(s2)+111.11)
# print(int(s3)+111.11)


# a,b=10,20;
# a//=b;
# print(a)


# 현금 교환 프로그램
# ## 변수 선언 부분
#
# money, p50, p10, p5, p1, c500, c100, c50, c10 = 0,0,0,0,0,0,0,0,0
#
# ## 메인 코드 부분
# money=int(input("교환할 돈은 얼마?\n"))
#
# p50=money//50000; money%=50000
# p10=money//10000; money%=10000
# p5=money//5000; money%=5000
# p1=money//1000; money%=1000
# c500=money//500; money%=500
# c100=money//100; money%=100
# c50=money//50; money%=50
# c10=money//10; money%=10
#
# print("오만원 %d장, 만원%d장, 오천원 %d장, 천원%d장" %(p50, p10, p5, p1))
# print("오벡원 %d, 백원%d, 오십원 %d, 십원%d" %(c500, c100, c50, c10))
# print("바꾸지 못한 돈 ==> %d원\n" %money)

# 챕터5 조건문

# a=99
# if a<100 :
#     print("100보다 작군요")

# a=200
#
# if a<100 :
#     print("100보다 작군요")
#     print("거짓이므로 안보인다")
#
# print("프로그램 끝")

# a=200
#
# if a<100 :
#     print("100보다 작군요.")
# else :
#     print("100보다 크군요.")

# a=int(input("정수를 입력하세요 :"))
#
# if a%2==0 :
#     print("짝수")
# else :
#     print("홀수")

# a= 75
#
# if a>50:
#     if a<100 :
#         print("50보다 크고 100보다 작군요")
#     else :
#         print("100보다 크군요")
# else :
#     print("50보다 작군요")

# 점수 문제

# score=int(input("점수를 입력 하세요 :"))
#
# if score>=95 :
#     print("A+")
# elif score>=90 :
#     print("A0")
# elif score>=85 :
#     print("B+")
# elif score>=80 :
#     print("B0")
# elif score>=75 :
#     print("C+")
# elif score>=70 :
#     print("C0")
# elif score>=65 :
#     print("D+")
# elif score >= 60:
#     print("D0")
# else :
#     print("F")
#
# print("학점입니다.")

# 리스트

# fruit = ['사과','배','딸기','포도']
# fruit.append('귤')
# if '딸기' in fruit :
#     print("딸기가있네요")

# import random
#
# numbers=[]
# for num in range(0,10) :
#     numbers.append(random.randrange(0,10))
#
# print("생성된 리스트",numbers)
#
# for num in range(0,10) :
#     if num not in numbers :
#         print("%d 숫자는 리스트에 없어요" %num)

# 챕터6 반복분

# for i in range(0,3,1) :
#     print("안녕하세요? for문을 공부중입니다.")

# i,hap = 0,0
# num1, num2, num3 = 0,0,0
#
# num1=int(input("값 입력 :"))
# num2=int(input("값 입력 :"))
# num3=int(input("값 입력 :"))
#
# for i in range (num1,num2+1,num3) :
#     hap+=i
# print("%d에서 %d까지 %d씩증가하는 값의 합 : %d 입니다." % (num1,num2,num3,hap))

# i,dan = 0,0
#
# dan = int(input(" 몇 단 ? "))
#
# for i in range(1,10,1) :
#     print("%dX%d = %2d" %(dan,i,dan*i))

# for i in range(0,3,1) :
#     for k in range(0,2,1) :
#         print("파이썬은 ... (i값: %d, k값 %d)" % (i,k))

# i,k=0,0
#
# for i in range(2,10,1):
#     print("## %d 단 ##" %i)
#     for k in range(1,10,1):
#         print("%d X %d = %2d 입니다." % (i,k,i*k))
#     print("")

## 구구단 가로로 출력

# 변수 선언 부분
# i, k, guguLine=0,0," "
#
# #메인 코드 부분
# for i in range(9,1,-1) :
#     guguLine=guguLine+(" # %d단 #" % i)
#
# print(guguLine)
#
# for i in range(1,10) :
#     guguLine=""
#     for k in range(9,1,-1) :
#         guguLine=guguLine+str("%2dX%2d=%2d"%(k,i,k*i))
#     print(guguLine)

# i,hap = 0,0
#
# i = 1
#
# while i < 11 :
#     hap+=i
#     i+=1
#
# print("1에서 10까지의 합 : %d" %hap)

# hap = 0
# a,b=0,0
#
# while True :
#     a=int(input("더할 첫번째 수 : "))
#     b=int(input("더할 두번째 수 : "))
#     hap=a+b
#     print("%d + %d = %d" %(a,b,hap))
#

# str = "abc"
# print(str[0])
# print(str[1])
# print(str[2])

##변수 선언부분
# i,k,heartNum=0,0,0
# numStr,ch,hearStr="","",""
#
# ##메인
# numStr=input("숫자를 여러 개 입력하세요 :")
# print("")
#
# i=0
# ch=numStr[i]
# while True :
#     heartNum=int(ch)
#
#     hearStr=""
#
#     for k in range(0,heartNum):
#         hearStr+="\u2665"
#         k+=1
#
#     print(hearStr)
#
#     i+=1
#     if(i>len(numStr)-1) :
#         break
#
#     ch=numStr[i]