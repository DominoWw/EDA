
#si visitas todos los nodos -> O(n)
#si buscas -> O(logn)

def find_max(L:list) -> int:
    if len(L)>1:
        m=len(L)//2
        l_iz=find_max(L[0:m])
        l_der=find_max(L[m:])
        return max(l_iz, l_der)

    
    elif len(L)==1:
        return L[0]
    




print(find_max([1,5,7,5,3,6,2,43,54,1,6,34,2]))