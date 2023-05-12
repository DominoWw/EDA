
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
    



def find_min_max(L:list) -> tuple:
    if len(L) == 1:
        return L[0], L[0]
    
    elif L==None:
        return None, None
    elif len(L)>1:
        m=len(L)//2
        min1,max1= find_min_max(L[0:m])
        min2,max2= find_min_max(L[m:])


        if (min1 or min2) and (max1 or max2):
            return min(min1,min2), max(max1,max2)
        else:
            return None, None


def find_lowest_even_odd(L:list) -> tuple:
    if L==None:
        return None,None
    elif len(L)==1:
        if L[0]%2 == 1:
            return None,L[0]
        else:
            return L[0], None



    else:
        m=len(L)//2
        even1, odd1=find_lowest_even_odd(L[0:m])
        even2,odd2=find_lowest_even_odd(L[m:])


        if odd1 and odd2:
            odd_final=min(odd1,odd2)
        elif odd1==None:
            odd_final=odd2
        elif odd2==None:
            odd_final=odd1

        if even1 and even2:
            even_final=min(even1,even2)
        elif even1==None:
            even_final=even2
        elif even2==None:
            even_final=even1 

        return even_final,odd_final


def sum_list(L:list)->int:
    if L==None:
        return None
    if len(L)==1:
        return L[0]
    
    m=len(L)//2
    left=sum_list(L[0:m])
    right=sum_list(L[m:])

    return left+right

def sum_multiple_5(L:list)->int:
    if L==None:
        return None
    if len(L)==1:
        if L[0]%5==0:
            return L[0]
        else:
            return 0
        
    m=len(L)//2
    left=sum_multiple_5(L[0:m])
    right=sum_multiple_5(L[m:])

    return left+right

def get_words_len_lower_2(L:list)->list:
    if L==None:
        return
    if len(L)==1:
        if len(L[0])<=2:
            return L[0]
        
    m=len(L)//2
    left=get_words_len_lower_2(L[0:m])
    right=get_words_len_lower_2(L[m:])

    return left+right



print(get_words_len_lower_2(["anfdjk", "sd", "ddadds", "dd", "f", " "]))