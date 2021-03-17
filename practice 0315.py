# aa=[0,0,0,0]
# hap = 0
#
# aa[0] = int(input("1번째 숫자 :"))
# aa[1] = int(input("2번째 숫자 :"))
# aa[2] = int(input("3번째 숫자 :"))
# aa[3] = int(input("4번째 숫자 :"))
#
# hap = aa[0] + aa[1] + aa[2] + aa[3]
#
# print("합계 ==> %d" % hap)

# aa=[]
# for i in range (0,100) :
#     aa.append(0)
#
# len(aa)
#
# print(len(aa))

# 소스코드 7-3 스스로 문제 해결
# aa=[]
# for i in range(0,10) :
#     aa.append(0)
#
# hap = 0
# i=0
#
# while i<10 :
#     aa[i] = int(input( str(i+1) + "번째 숫자 :"))
#     i+=1
# hap = aa[0] + aa[1] + aa[2] + aa[3] + aa[4] + aa[5] + aa[6] + aa[7] + aa[8] +aa[9]
#
# print("합계 == : %d " %hap)

#소스코드 7-4

# aa=[]
# bb=[]
# value=0
#
# for i in range(0,200) :
#     aa.append(value)
#     value+=3
#
# for i in range(0,200) :
#     bb.append(aa[199-i])
#
# print(" bb[0]는 %d, bb[199]는 %d 입력됨 " % (bb[0], bb[199]))

# aa=[10,20,30,40]
# print(aa[0:3])
# print(aa[2:4])
# print(aa[2:])
# print(aa[:2])

# aa=[10,20,30]
# bb=[40,50,60]
# print(aa+bb)
# print(aa*3)
#
# aa=[10,20,30]
# aa[1]=200
# print(aa)

# aa=[10,20,30]
# del (aa[1])
# print(aa)

# aa=[10,20,30,40,50]
# aa[1:4]=[]
# print(aa)

# 소스코드 7-5

myList=[30,10,20]
print("현재 리스트: %s" %myList)

myList.append(40)
print("append(40) 후의 리스트 : %s " %myList)

print("pop()으로 추출한 값 : %s" %myList.pop())
print("pop() 후의 리스트 : %s" %myList)

myList.sort()
print("sort() 후의 리스트 : %s " %myList)

myList.reverse()
print("reverse() 후의 리스트 : %s " %myList)

print("20 값의 위치 : %d" %myList.index(20))

myList.insert(2,222)
print("insert(2,222) 후의 리스트 : %s" %myList)

myList.remove(222)
print("remove(222)후의 리스트 : %s" %myList)

myList.extend([77,88,77])
print("extend([77,88,77]) 후의 리스트 : %s" %myList)

print("77값의 개수 : %d" % myList.count(77))