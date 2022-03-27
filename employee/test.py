# def outer(func):
#     def inner(num1,num2):
#         if num1<num2:
#             return func(num2,num1)
#         else: return func(num1,num2)
#     return inner
#
# @outer
# def devision(num1,num2):
#     a=(num1//num2)
#     return a
#
# print(devision(20,10))

# l=[1,9,8,9]
# print(l[0:4])
dic={'mango':'fruit','banna':'fruit','Bringal':'vegitable','tomato':'vegitable','apple':'fruit'}
final_dict={}
for dict_key,dict_val in dic.items():
    if dict_val not in final_dict:
        final_dict[dict_val]=[dict_key]
    else:
        for k,v in final_dict.items():
            if dict_val==k:
                v.append(dict_key)

print(final_dict)


dic_val={}
str1='sureshkadam'
for item in str1:
    if item in dic_val:
        dic_val[item]+=1

    else:dic_val[item]=1

print(dic_val)


def gen_fun():
    yield 1
    yield 2






import sys
sys.exit(0)
print('Hello Word')

# "Python program to print the duplicate elements of an array
Input= [1, 2, 3, 4, 2, 7, 8, 8, 3]
# In the above array, the first duplicate will be found at index 4
# which is the duplicate of the element (2) present at index 1.
# So, duplicate elements in the above array are 2, 3 and 8."
duplicate_val=[]

for item in Input:

    if (Input.count(item))>1:
        duplicate_val.append((item,Input.count(item)))
        Input.remove((item))

# print(duplicate_val)
# Input : str1 = 'aabcddekll12@'
#         str2 = 'bb22ll@55k'
# Output : 5
# (i.e. matching characters :- b, l, 2, @, k)"

str1 = 'aabcddekll12@'
str2 = 'bb22ll@55k'
l=[]
a=[]
d={}
final='aabcddekll12@bb22ll@55k'
for str_val in final:#22112211221111111221001
    if str_val not in l:
        l.append(str_val)
        a.append((str_val,final.count(str_val)))
    # else:print(str_val,end='')
for i,v in enumerate(a):
    if (a[i][1])==1:
        print(a[i][0],end='   ')

# print(a)
#     if str_val in str2 and str_val not in final_str_val and :
#         final_str_val+=str_val+','
#
# print(final_str_val)






# if item not in final_list:
    #     final_list.append(item)
    #
    # else:
    #     duplicate_val.append(item)

# n=8







