
#factorial integers
def fact(numero):
    if numero<0:
        return "error"
    else:
        if numero == 0:
            return 1
        else:
            return numero * fact(numero-1)
        
        
#sum of integers 
def devnat(numero):
    if numero<0:
        return "error"
    else:
        if numero==0:
            return 0
        else:
            return numero + devnat(numero-1)

#multiplication of integers
def sumdos(a,b):
    if a<0 or b<0:
        return "error"
    elif a==0 or b==0:
        return 0 
    
    else:

        if b==1:
            return a
        else:
            return a+sumdos(a,b-1)


def sumlist(a:list):
    if len(a)==0:
        return None
    else:
        if len(a)==1:
            return a[0]
        else:
            return a[0] + sumlist(a[1:])
        
def digit(a:int):
    if a==0:
        return 0
    else:
        return a % 10 + digit(a//10)  

print(fact(3))
print(devnat(4))
print(sumdos(1,0))
print(sumdos(-1,2))
print(sumdos(3,4))

l1 = [1,1,1,2,2,2]
print(sumlist(l1))

print(digit(45454))