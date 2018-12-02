    
"""    
assignment
write a program that prints (1 to 100)
if it is a multiple of 3, print(fizz)
if it is a multiple of 5 print(buzz)
if it is a multiple of 3 and 5 print(fizz buzz)
""" 

x = 1
while (x<=100):
    if (x%3==0):
        print (x, "multiple of 3, " "fizz")
    if (x%5==0):
        print (x, "multiple of 5, " "buzz")
    if (x%3 and 5==0):
        print  (x, "multiple of 3 and 5, " "fizz buzz")
    else:
        print(x)
        x+=1 
    
