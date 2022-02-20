from dataclasses import field
from random import randint
from cmath import sqrt
from operator import truediv
from pickletools import read_uint1

# print('Hello World')
# a=int(input('nhap chieu cao hinh chu nhat :  '))
# n=int(input('nhap chieu rong cua hinh chu nhat: '))
# s=0
# print('dien tich hinh chu nhat la : ',a*n)
# #comment ?
# for i in range(1,n+1):
#     s+=i
# print(s)
# # define 0 keo, 1 bua, 2 bao
# print('0 keo, 1 bua, 2 bao')
# a=int(input('nguoi choi nhap '))
# b=randint(0,2)
# print('may tinh nhap ',b)
# if a==b:
#     print('equal')
# elif a>b:
#     if a-b==1:
#         print('win')
#     else:
#         print('lose')
# else:
#     if a-b==-1:
#         print('lose')
#     else:
#         print('win')
#loop

# for i in 'Hello Wordl':
#     print(i,'\t',end='')
# else: print('\n')

# m=int(input('Nhap gia tri bat dau:'))
# n=int(input('Nhap gia tri ket thuc:'))
# s=0
# for i in range(m,n+1):
#     if i%3==0 or i%5==0:
#         s=s+i
# print('Tong các so chia het cho 3 hoac 5 tu',m, 'den', n, 'la',s)

# n=5
# d=0
# while n>0 :
#     i=1
#     while i<n : 
#         print(end=' ')
#         i=i+1
#     j=0
#     while j<=d: #d=2 , d=4
#         print(end='*')
#         j=j+1
#     n=n-1  ## n=2 , n=1 , n=0
#     d=d+2  # d=2 , d=4 , d=6
#     print('\n')

# function
# def hello():
#   print('Hello World')
# def abs_int(a):
#     if a>=0:
#         return a
#     else:
#         return -a
    
# print(abs_int(-5))

# def cal_val():
#     global x # bien cuc bo
#     x=10
#     print(x) 

# def my_func(): 
#     pass

# def UCLN(a,b):
#     while a!=b:
#         if a>b:
#             a=a-b
#         else:
#             b=b-a
#     return a
# print('UCLN',UCLN(25,15))    

# def min(a,b):
#     if a<b:
#         return a
#     else:
#         return b
# print(min(min(3,5),7)) 
# # de quy
# def giaithua(a):
#     if a==0:
#         return 1
#     else:
#         return giaithua(a-1)*a
# print(giaithua(5))

# def SNT(n):
#     if n==1:
#         return False
#     for i in range(2,int(n/2)):
#         if n%i==0:
#             return False
#     return True
# if SNT(5)==True:
#     print(1)
# else:
#     print(0)

# def solution(nums):
#     leftsum=0
#     rightsum=sum(nums)
#     for i,num in enumerate(nums):
#         rightsum -= num
#         if leftsum==rightsum:
#             return i
#         leftsum += num
#     return -1
# print(solution([2, 3, -1, 8, 4])) # 3
# print(solution([1, -1, 4])) # 2
# print(solution([2, 5])) # -1
# def solution1(nums):
#     leftsum=0
#     rightsum=sum(nums)
#     for i,num in enumerate(nums):
#         rightsum =rightsum - num
#         leftsum =leftsum + num
#         print(i,num, leftsum, rightsum)
# solution1([2, 3, -1, 8, 4])

#string
# str1='ahihi '
# str2='chao cau ^^'
# str3= str1 + str2
# print('do dai ->',str3,len(str3))
# check=str1 in str3 # in or not in
# print(check)
# print(str3[-17],'a ?')  #->a '{a}hihi chao cau ^^'
# print(str1.strip())  # xoa khoang trang dau hoac cuoi
# print(str1.lower()) #in thuong
# print(str1.upper()) #in hoa
# print(str1.find('hi')) #tim kiem
# print(str1.replace('hi','ho')) # thay doi
# print(str3.split(' ')) # tach chuoi
# print("^".join(str1))  # noi chuoi trong mang =))
# print('%s minh %s %0.1f'%(str1,str2,123.55)) # %s %f #df #d
# print(str3[0:len(str3):1]) #string start / end / step
# print(str3[::-1]) # khong viet tu mac dinh dau duoi ^^

# List
# list1 = ['vatly', 'hoahoc', 1997, 2000];
# print ("list1[0]: ", list1[0])
# print ("list1[-2]: ", list1[-2]) 
# print ("list1[0:3]: ", list1[0:3]) 
# print ("list1[1:]: ", list1[1:])
# print ("list1[-3:3]: ", list1[-3:3])
# a=[1,2,3]
# b=[4,5,6]
# c=a+b
# print(c)
# print(a*3)
# min=min(c)
# max=max(c)
# s=sum(c)
# c.append(7) # noi vao duoi cua list
# c.extend((8,9)) # sao chep phan tu o trong h=(a,b) noi vao duoi cua c
# #print(c.count(1)) # count element appear in list
# # print(c.index(2)) # return index of the first element in list
# c.insert(len(c),10) # insert element at index of list and put else elements after index  
# c.pop(5) # delete element
# c.remove(4)
# c.sort(reverse=True) # True lon - be False be-lon  mac dinh False
# c.reverse() # dao nguoc list
# print(c)
# c.clear()
# arr=[]
# n=int(input('N: '))
# for i in range(n):
#     print('a[',i,']= ',end='')
#     arr.append(int(input()))
# print(arr)
# dd=[]
# for i in range(n):
#     dd.append(sum(arr[:i+1]))
# print(dd)

# multi arr
# a=[[12,5,3,5],[23,6,4],[1,8,20,32,2]]
# row=len(a)
# for i in range (row):
#     col=len(a[i])
#     for j in range(col):
#         print(a[i][j],end=' ')
# else: print('\n')
# a=[]
# row=int(input('Nhap so hang:'))
# col=int(input('Nhap so cot:'))
# for i in range(row):
#     gt_row=[]
#     for j in range(col):
#          print(f'a[{i}][{j}]=')
#          gt_row.append(int(input()))
#     a.append(gt_row)
# print(a)  # matrix with row x col
# another case
# how to use -> print(dir(list | tuple | set | dict))
# a=[]
# row=int(input('Nhap so hang:'))
# for i in range(row):
#     col=int(input('Nhap so cot:'))
#     gt_row=[]
#     for j in range(col):
#          print(f'a[{i}][{j}]=',end='')
#          gt_row.append(int(input()))
#     a.append(gt_row)
# print(a) # free size of col
# a=[[12,5,7,3],[2,8,4,2]]
# tong=0
# for i in range(len(a)):
#    for j in range(len(a[i])):
#        tong=tong+a[i][j]
# print(tong)

# kieu du lieu
# tuple = ()
# tup1=(2,'abc',3,'def',5)
# tup2=(1,4,5,3)
# print(tup1+tup2)
# print(tup2*2)
# print(2 in tup1)
#set = set()
# set1={4,3,5,2,1,6,2}
# print(set1)
# set2={1,4,7,12}
# print(1 in set2)
# print(set1 & set2)
# print(set1 | set2)
# print(set1 -  set2)
# # dict = {key: value, key: value}, auto dict={} | dict=dict()
# dic={'name':'bali','age':'20'}
# print(dic['name'])
# dic={'easy':'ez game','cute':'dep vai ^^','song':'dong chi ten linh len do =))'}
# str=input('input key : ')
# print(dic.get(str,'can not find! :(('))

# Comprehensions  phim tat ?? =))
# list
# a=[int(x) for x in input().split()]  # nhap khong gioi han ?
# b=[x*x for x in a if x%2==0]  # tao list b voi cac phan tu ^2 if %2=0
# print(a)
# print(b)
# matrix=[[j*j+i for j in range(3)] for i in range(3)]
# row=3
# matrix1=[[int(x) for x in input().split()] for i in range(row)]

# set comprehensions {}
# names=[ 'Arnold', 'BILL', 'alice', 'arnold', 'MARY', 'J', 'BIII' , 'maRy']
# name_convert={x.capitalize() for x in names if len(x)>1}
# print(name_convert)

# # dict comprehensions
# char_dict = {'A' : 4,'z': 2, 'D': 8, 'a': 5, 'Z' : 10 }
# str={k.lower() : char_dict.get(k.lower(), 0) + char_dict.get(k.upper(), 0)
#  for k in char_dict.keys()}
# print(str)

# FILE

# file2=open('ahihi.txt','a')
# file2.write('\nminh la bali')
# file2.close()
# file=open('ahihi.txt','r')
# # df=file.read() # so am la doc het mac dinh ()
# # print(df)
# file.seek(5) # di chuyen con tro ve vi tri 5
# print(file.read())
# #df2=file.readline()  # read a line
# file.close()
# Example
# f1=open('trai.txt','r')
# f2=open('khcach.txt','w')
# n=len(f1.readlines())
# f1.seek(0)
# for i in range(n):
#     a=f1.readline().split()
#     d=math.sqrt(a[0]**2+a[1]**2)
#     f2.write('%.2f \n'%(d))
# f1.close()
# f2.close()

# Class and object

class hcn:
    def __init__(self,cd,cr):
        self.cd=cd
        self.cr=cr
    def show(self):
        print('chieu dai:',self.cd)
        print('chieu rong :',self.cr)
    def chuvi(self):
        return (self.cd+self.cr)*2
    def dientich(self):
        return self.cd*self.cr

hcn1=hcn(3,4)
hcn1.show()
print('chu vi : ',hcn1.chuvi())
print('dien tich : ',hcn1.dientich())
class hv (hcn):
    def __init__(self,a):
        self.a=a
    def show(args):
        print('canh :',args.a)
    def chuvi(args):
        return args.a*2
    def dientich(args):
        return args.a**2
hv1=hv(3)
hv1.show()

class hocsinh:
    def _init_(self,ten,lop,diem,truong):
        self.ten=ten
        self.lop=lop
        self.diem=diem
        self.truong=truong
    def show(args):
        print('Ten :',args.ten)
        print('Lop :',args.lop)
        print('Diem :',args.diem)
        print('Truong',args.truong)
        print('-----------------------')

def nhap(n):
    global a
    for i in range (n):
        a[i]=hocsinh(0,0,0,0)
        print('input hoc sinh thu ',i+1)
        a[i].ten=input('ten :')
        a[i].lop=input( 'lop :')
        a[i].diem=float(input('diem :'))
        a[i].truong=input('truong :')
def xuat(n):
    global a
    for i in range(n):
        a[i].show()

nhap(1)
xuat(1)