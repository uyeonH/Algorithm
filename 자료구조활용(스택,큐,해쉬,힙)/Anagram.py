'''
#input 
ABCDEGHKNOPQRUWXbcdfghikotuwxy
XbCdfGhiNoPuwUyABcDEgHKkOtQRxW
'''

import sys

sys.stdin = open("in1.txt", "r")

# 풀이3
a = input()
b = input()
str1 = [0] * 52
str2 = [0] * 52
# 소문자 -71
# 대문자 -65
for x in a:
    if x.isupper():
        str1[ord(x) - 65] += 1  # 아스키넘버
    elif x.islower():
        str1[ord(x) - 71] += 1
for x in b:
    if x.isupper():
        str2[ord(x) - 65] += 1  # 아스키넘버
    elif x.islower():
        str2[ord(x) - 71] += 1
for i in range(52):
    if str1[i]!=str2[i]:
        print("NO")
        break
else:
    print("YES")

'''
# 풀이2
a=input()
b=input()
sH=dict()
for x in a:
    sH[x]=sH.get(x,0)+1
for x in b:
    sH[x]=sH.get(x,0)-1
print(sH)
for x in a:
    if sH.get(x)!=0:
        print("NO")
        break
else:
    print("YES")
'''

'''
# 풀이1
n = input()
m = input()
str1 = dict()
str2 = dict()

# dict - 누적용
for x in n:
    str1[x] = str1.get(x,0)+1 # key값이 있으면 그 val값을, 없으면 0을 리턴하는 함수
for x in m:
    str2[x] = str2.get(x,0)+1 # key값이 있으면 그 val값을, 없으면 0을 리턴하는 함수
for i in str1.keys():
    if i in str2.keys():
        if str1[i]!=str2[i]:
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")
'''
