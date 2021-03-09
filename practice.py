# a=100
# b=50
# result = a+b
#
# print(a,"+",b,"=",result)
# result=a-b
# print(a,"-",b,"=",result)
# result=a*b
# print(a,"*",b,"=",result)
# result=a/b
# print(a,"/",b,"=",result)

# c=500
# d=200
# result=c+d
# print(c,"+",d,"=",result)
# result=c-d
# print(c,"-",d,"=",result)
# result=c*d
# print(c,"*",d,"=",result)
# result=c/d
# print(c,"/",d,"=",result)

# first=543.21
# second=123.45
# result=first+second
# print(first,"+",second,"=",result)
#
#
# a=int(input("첫 번째 숫자를 입력 하세요 :"))
# b=int(input("두번째 숫자를 입력 하세요 :"))
# result=a+b
# print(a,"+",b,"=",result)
#
# a=int(input("첫번째 숫자를 입력하세요:"))
# b=int(input("두번째 숫자를 입력하세요:"))
# c=int(input("세번째 숫자를 입력하세요:"))
# result=a+b+c
# print(a,"+",b,"+",c,"=",result)
#
# from tkinter import *
#
# ## 변수 ##
# window=None
# canvas=None
# x1,y1,x2,y2=None,None,None,None #선의 시작점과 끝점
#
#
# ## 함수 ##
#
# def mouseClick(event):
#     global x1,y1,x2,y2
#     x1=event.x
#     y1=event.y
#
#
# def mouseDrop(event):
#     global x1,y1,x2,y2
#     x2=event.x
#     y2=event.y
#     canvas.create_line(x1,y1,x2,y2,width=1, fill="green")
#
# ## 메인 코드 ##
# window=Tk()
# window.title("그림판 프로그램")
# canvas=Canvas(window, height=500, width=500)
# canvas.bind("<Button-1>", mouseClick)
# canvas.bind("<ButtonRelease-1>",mouseDrop)
# canvas.pack()
# window.mainloop()


# a=int(input())
# b=int(input())
# result=a+b
# print(result)


# print("%d/%d=%5.1f" % (100,200,0.5))

# print("%d" % 123)
# print("%5d" % 123)
# print("%0.5d" % 123)
#
# print("%f" % 123.45)
# print("%7.1f" % 123.45)
# print("%7.3f" % 123.45)
#
# print("%s" % "Python")
# print("%10s" % "Python")

# print("{0:d} {1:5d} {2:05d}".format(123,123,123))

# print("한 행입니다. 또 한행입니다")
# print("한 행입니다.\n또 한행입니다.")

# print("\n줄바꿈\n연습")
# print("\t탭키\t연습")
# print("글자가\"강조\"되는 효과1")
# print("글자가 \'강조\'되는 효과2")
# print("\\\\\\역슬래쉬 세개 출력")
# print(r"\n\t\"\\를 그대로 출력")

