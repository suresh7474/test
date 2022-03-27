






#
# l=[1,5,7,9]
# original_val=[]
# final_list=[]
# for val1 in range(max(l)):
#     for j in l:
#         if val1==j:
#             print(val1,j)
#             break
#     else:final_list.append(val1)
#
# print(final_list)
#
#
# data='suresh'
#
# print(data[::-1])
# l1=['a','b','c']
# print(''.join(l1))

import unittest


# l=[1,2,3,4]
# flag=False
# tem=0
# for list_ in l:
#     if tem < list_:
#         tem=list_
#         flag=True
#     else:flag=False
#
# if flag==True:
#     print('This is continous list')
# else:print('This is not continous list')


# l=[1,3,4,3,32,5]
# count=0
# for i in l:
#     if count< i:
#         count=i
#
# l.remove(count)
#
# count=0
# for i in l:
#     if count< i:
#         count=i
# print(count)

# l.sort()
# print(l[-2])
# l1=max(l)
# l.remove(l1)
# print(max(l))
# list1=set(l)
# list1.remove(max(list1))
# print(max(list1))








    # if len(l)==item:
    #     print(l)
    #
    # else:print(item)



























# l=[1,2,4,1,4,2]
def quick_sort(l):
    le=len(l)
    if le<=1:
        return l
    else:
        povit=l.pop()

    left=[]
    right=[]
    for item in l:
        if item < povit:
            left.append(item)
        else:
            right.append(item)
    return quick_sort(left)+[povit]+quick_sort(right)

q=quick_sort([1,2,4,5,6,3,45,6,])
print(q[-2])
import sys
sys.exit(0)












l1=[1,2,3,4,5]
l2=l1#[1,2,3,4,5,6]

l2.append(6)

# print(l1)#[1,2,3,4,5]
# print(l2)#[1,2,3,4,5,6]


# l={x:x*2 for x in range(10)}
# print(l)


l1=[1,2,4,60,500,]

count=0
second_largest=0
for list_val in l1:
    if len(l1):
        second_largest=count

    if count <=list_val:
        count=list_val

# print(count)
print(second_largest)

# a=' I am python developer'.split()
# str_list=''
# for i,v in enumerate(a):
#     if i<2 :
#         str_list+=v+" "
#
#     else:str_list+=v[::-1]+' '
#
# print(str_list)
import time
original_count=0
counts=0
final_val=[]
for i in range(1,100):#1,2,3,5,7,
    for j in range(2,100):
        if i%j==0 and counts<2:
            counts+=1
        elif counts>1:
            counts=0
            break
    else:
        counts=0
        final_val.append(i)
        original_count+=1
# t2=time.ctime()
print(final_val)
# l=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163 ,167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293]
# l3=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293]
# count1=0
# for i in l:
#     count1+=1
# print(count1)

# print(s,original_count)
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97

s='Suresh'
print(s.replace('r',''))

# l=[1,2,3,100,20]
# l.remove(max(l))
# m
d={1:10,2:20}



