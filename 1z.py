#1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
# *Примеры:*
# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8,9 -> нет
#a=int(input("enter number"))
print ("enter number")
a=int(input())
print ("enter number square")
b=int(input())

if a==b*b or b==a**2:
    print("yes")
else:
    print("no")
