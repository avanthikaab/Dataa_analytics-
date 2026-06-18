# a= input("enter a number ")
# b= input("enter the second number ")

# print(type(a))

# n=int(a)
# m=int(b)

# sum = n+m
# diff = n-m
# mul=n*m
# div=n/m
# f=n//m
# ex=n**m
# print(sum ,diff ,mul ,div ,f ,ex )

# del n
# print(n)

# a=5
# b=6
# temp=a
# a=b
# b=temp

# print(a,b)

# a=6
# b=5
# a,b=b,a
# print(a,b)
# x=1,2,3,4
# print(type(x))

# y=2+3j
# print(type(y))

# y=int(input("enter the number"))

# for i in range(1,11,1):
#     print(f"{i}x{y}={i*y}")

# for i in range(1,y+1):
#     for j in range(y-i):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#             print(k,end="   ")
#     print()

# row=y
# for i in range(y+1):
#      print(" "*(row-i)+ "* " *i)

# x=[1,2,3]
# for i in x:
#     print(i)

# x= int(input("enter the number"))
# i=1
# while i<11:
#     if i==5:
#         i=i+1
#         continue
#     else:
#         print(f"{i}x{x}={i*x}")
#     i=i+1

# if x%5==0:
#     print(f"{x} multiple of 5")
# else:
#     print(f"{x}not a multiple of 5")

# if x%2==0:
#     print(f"{x} is even")
# else:
#     print(f"{x} is odd")

# if x%2==0:
#     print(f"{x} is multiple of 2")
# elif x%3==0:
#     printf(f"{x} is multiple of 3")
# else:
#     print(f"{x} either multiple of 2 nor 3")

# if x>=0:
#     if x==0:
#         print(f"x is zero")
#     else:
#         printf("x is positive")
# else:
#     print("x is negative")

# x=input(" enter a string  ")
# rev=""

# for i in x:
#     rev=i+rev
# print(rev)

# x= input("enter the string ")
# y = input(" enter another string ")

# print(x+ y)
# print(len(x+y))

# print(x in y)

# print(x.upper())
# print(x.lower())
# print(x+y.title())
# print(x.swapcase())
# print(x.capitalize())

# print(x.find("y"))
# print(y.index("t"))
# print(x.startswith("py"))
# print(y.endswith("on"))
# print(y.count("y"))
# print(x.replace("p","r"))
# print(x.strip())
# print(y.split("o"))
# print(y.join("['th', 'n'0]"))

# l=[1,2,3,4]
# print(l[-1])
# print(l[3])
# l.append(9)
# print(l)
# l.extend([7,8,9])
# print(l)
# print(len(l))


# num=int(input("enter the number"))
# rev=0

# while num>0:
#     x=num%10
#     rev=rev*10+x
#     num= num//10
# print(rev)

# l=[1,2,3,4]
# l.remove(2)
# print(l)
# print(l.pop())
# del l[0]
# print(l)
# print(l.clear())
# print(l.index(2))

# print(l.count(2))
# print(2 in l)


# l=[]
# n=int(input(" enter the size of list "))

# for i in range(n):
#     x=int(input("enter the values "))
#     l.append(x)
# print(l)

# for j in range(n):
#     for i in range(n-1):
#        if  l[i] > l[i+1]:
#          temp=l[i]
#          l[i]=l[i+1]
#          l[i+1]=temp

# print(l)
# l.sort(reverse=True)
# print(l)

# l.sort()
# print(l)
# l.reverse()
# print(l)
# sorted(l)

# h=l.copy()
# print(h)
# a= input(" enter a string ")
# b=list(a)
# print(b)
# print(b*2)

# a=input("enter the string ")
# l=["A","E","I","O","U","e","a","o","u","i"]
# v=0
# c=0
# for i in a:
#     if i.isalpha()== True:
#         if i in l:
#             v+=1
#         else:
#             c+=1

# print(f"the number of vowels is {v} and consonants {c} ")

# print(ord("b"))
# # print(chr(65))
# s= None
# for i in a:
#     if i =='z':
#         n='a'
#     elif i=='Z':
#         n='A'
#     else:
#         n=chr(ord(i)+1)       
    
#     print(n,end=" ")

# t = 1,2,3
# print(t)
# x,y,z= t
# print(x,y,z)
# num= frozenset({1,2,3,4})
# print(num)
# print(type(num))
# a=set()
# print(type(a))
# b={1,2,2,3}
# print(b)
# print(len(b))
# b.add(5)
# print(b)
# b.update([7,8])
# print(b)

# b.remove(3)
# print(b)
# b.discard(2)
# print(b)
# b.pop()
# print(b)
# b.clear()
# print(b)

# a={1,2,3,4,5,6}
# b={0,1,2,3,8,6,7,10}
# c={2,4,6}
# print(a|b)
# print(a&b)
# print(a-b)
# print(a^b)

# print(a.issubset(c))
# print(a.issuperset(c))

# h=a.copy()
# print(h)

# print(sorted(b))
# print(max(a))
# print(min(b))
# print(sum(a))

# a= {"name":"avanthika","age":19}
# print(a)

# print(a["name"])
# print(a.get("name"))
# print(len(a))

# a["c"]=3
# print(a)
# a.update({"b":5})
# print(a)
# a.setdefault("d",4)
# print(a)

# a.pop("age")
# print(a)
 
# print(a.popitem())
# del a["b"]
# print(a)
# # a.clear()
# # print(a)

# print(a.keys())
# print(a.values())
# print(a.items())

# print(dict([(1,'a')]))

# print("a" in a)
# print("x" not in a)

# for k in a:
#     print(k)

# for v in a.values():
#     print(v)

# for k,v in a.items():
#     print(k,v)


# x=('apple',[1,2,3,4],2.5,7,{'a':25,'b':74})
# x[1][2]=10
# print(x)
# x[4]["a"]=75
# print(x)

# x=['name','age','qualification']
# y=['avanthika',24,'pg']

# d={}
# # for i in x:
# #     for j in y:
# #         d={i:j}
# #     print(d)

# for i in range(len(x)):
#     d.update({x[i]:y[i]})
# print(d)
# d={}
# x = input("enter a string : ")
# for i in x:
#     d.update({i:x.count(i)})
# print(d)

# x=3
# y=3
# print(x is y)

# x= 10 
# r ="defeven"if x%2==0 else "odd"
# print(r)

# a=5
# b=4
# max= a if a>b else b
# print(max)

# a=["hai" if i%2==0 else i for i in range(10)]
# print(a)

# a=3
# b=4
# c=10

# m=a if a>b&a>c else b if b>a&b>c else c

# print(m)

# def find_sq(num):
#     result = num*num
#     return result
# square=print(find_sq(3))

# def pow(a,b):
#     return a**b

# x=int(input("enter the number "))
# y=int(input("enter the power "))
# z= pow(x,y)
# print(z)

#  amst(a):
#     n=a
#     sum=0
#     while(a!=0):
#         rem=a%10
#         sum=sum+(rem**3)
#         a=a//10
#     if(n==sum):
#         return True
#     else:
#         return False
    
# num=int(input("enter a number : " ))
# b=(amst(num))
# print(b)

# import math
# squ = math.sqrt(4)
# print(squ)

# def name(**kargs):
#     print(kargs)

# name(name='anu')
# name(name='manu',age=24)

# sum = lambda a,b:a+b

# print(sum(5,3))

# check = lambda a: a%2
# res= check(12)
# if res==0:
#     print("even")
# else:
#     print("odd")

# a=[1,2,3,4]
# double=map(lambda x:x*2,a)
# res= list(double)
# print(res)

# even=list(filter(lambda x:x%2==0,a))
# print(even)

# from functools import reduce
# sum=reduce(lambda x,y:x+y,a)
# print(sum)

# import main
# print(main.sum(5,4)) 
try:
    f=open('sample.txt','x')
except:
    pass

f=open('sample.txt','w')
f.write("hai")
f.write("heyy\n")

for i in range(1,11,1):
    f.write(f"{i}x5={i*5}\n")
    
f=open('sample.txt','a')          
f.write("helllo")
print("hello")