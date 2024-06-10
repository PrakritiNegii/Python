""" Program to print the following pattern:
    *
    * *
    * * *
    * * * * * 
    * * * * * * * * 
    * * * * * * * * * * * * * 
"""
n = int(input("Specify the number of lines: "))
i=0
a=0
b=1
while i!=n:
    c=a+b
    print("* "*c)
    a=b
    b=c
    i=i+1