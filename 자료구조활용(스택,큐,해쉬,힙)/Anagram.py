'''
#input 
ABCDEGHKNOPQRUWXbcdfghikotuwxy
XbCdfGhiNoPuwUyABcDEgHKkOtQRxW
'''

import sys

sys.stdin = open("in4.txt", "r")
n = input()
m = input()
str1 = dict()
str2 = dict()

# dict - 누적용
for x in n:
    str1[x] = str1.get(x,0)+1 # key값이 있으면 그 val값을, 없으면 0을 리턴하는 함수
for x in m:
    str2[x] = str2.get(x,0)+1
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
