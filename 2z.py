# Примеры:
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

a=int(input("enter number1 "))
b=int(input("enter number2 "))
c=int(input("enter number3 "))
d=int(input("enter number4 "))
e=int(input("enter number5 "))

list=[a,b,c,d,e]
max=a #list[0]-a
for i in list: 
  if i>max:
    max=i
print("max number", max)

# if b>max:
#     max=b
# if c>max:
#     max=c
# if  d>max:
#     max=d
# if e>max:
#     max=e
# print("max number", max)

#my_list=[4,8,2,0,9,6]
#for i in range (len(my_list)):
#print(my_list[i])

#my_list=[]
#for i in range(5):
# number= int(input(f"enter {i+1} number:"))
# my_list.append(number)
#max=my_list[0] 
# for item in my_list: 
#   if item>max:
#     max=item
# print("max number", max)