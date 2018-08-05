# Write your solution for 1.1 here!
a=0
for i in range (101):
    a=a+i
print (a)
a=0
for b in range(101):
    if b % 2 == 0:
        a=a+b
        
    else:
        print("odd")
print(a)
