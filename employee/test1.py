from abc import ABC,abstractmethod

class Person(ABC):
    @abstractmethod
    def personmethos(self):
        pass

class Student(Person):

    def personmethos(self):
        print('This is Student')


class Teacher(Person):

    def personmethos(self):
        print('This is Teacher ')

class Factory:

 # def __init__(self,type):
 #     self.type=type
 @staticmethod
 def build_factor(person):
     if person=='student':
         return Student()

     if person=='teacher':
         return Teacher()

     return [-1]


# if __name__ == '__main__':
     # choice=input('Enter type')
     # f=Factory()
     # f.build_factor(choice).personmethos()

# l=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# list_val=[]
# for i,v in enumerate(l):
#     if i%2==1:
#         list_val+=(l[i][::-1])
#         print(l[i])
#     else:
#         list_val+=(l[i])
#         print((l[i][0:]))
# print(list_val)
name:1
# from types import

# quick sort

# l=[1,2,1,3,6,5]
def sort_function(l):
    lens=len(l)
    if lens <= 1:
        return l
    else:
        piovt=l.pop()

    left=[]
    right=[]
    for i in l:
        if i<piovt:
            left.extend([i])
        else:right.extend([i])

    return sort_function(left)+[piovt]+sort_function(right)

print(sort_function([1,2,4,2,3]))