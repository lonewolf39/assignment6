#1 calculate area of square

def area():
    r=float(input("enter the radius of sphere"))
    a=(4*3.14*(r**2))
    return a
print("area of sphere is:",area())

#2 prints all the perfect numbers between 1 and 1000

def perfect(num):
    x=0
    for i in range(1,num):
        if(num%i==0):
            x=x+i
    if(x==num):
        print(num)
for i in range(1,1001):
    perfect(i)
    
#3 print multiplication table of a user defined number
    
n=int(input("enter number"))
def table(n):
    for i in range(1,11):
        print("{}*{}=".format(n,i),(n*i))
table(n)

#4 calculate power of a number using recursion

a=int(input("enter a"))
b=int(input("enter b"))

def fun(b):
    
    if(b==0):
        return 1
    else:
        return a*fun(b-1)
    
print(fun(b))
    

