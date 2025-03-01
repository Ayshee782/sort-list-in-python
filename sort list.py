#Write a program that takes five numbers as input from the user and stores them in a list.

a=list(map(int,input("enter 5 number=").split()))

print(a)
a.sort()
print("after sort=",a)
