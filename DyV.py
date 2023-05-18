from random import randint
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
    if L is None or len(L)==0:
        return []
    if len(L)==1:
        w=L[0]
        if len(w)<=2:
            return [w]
        else:
            return []
        
    m=len(L)//2
    left=get_words_len_lower_2(L[0:m])
    right=get_words_len_lower_2(L[m:])

    return left+right

def merge_sort(L:list)->list:
    if len(L)==0 or L is None:
        return []
    if len(L)==1:
        return L
    

    
    m=len(L)//2
    left=merge_sort(L[0:m])
    right=merge_sort(L[m:])

    return merge_sort_merge(right,left)

def merge_sort_merge(L1:list, L2:list)->list:
    output=[]

    
    i=0
    j=0

    while i<len(L1) and j<len(L2):
        if L1[i] < L2[j]:
            output.append(L1[i])
            i+=1

        else:
            output.append(L2[j])
            j+=1

    if i==len(L1):
        while j<len(L2):
            output.append(L2[j])
            j+=1

    if j==len(L2):
        while i<len(L1):
            output.append(L1[i])
            i+=1


    return output
        

def quicksort_central(L:list):
        _quicksort_central(L,0,len(L)-1)


def _quicksort_central(L:list, left:int, right:int):
    m=(left+right)//2


    p=L[m]
    i=left
    j=right

    while i<=j:
        while L[i]<p:
            i+=1

        while L[j]>p:
            j-=1

        if i<=j:
            L[i],L[j]=L[j],L[i]
            i+=1
            j-=1



    if j>left:
        _quicksort_central(L,left, j)

    if i<right:
        _quicksort_central(L,i,right)


def my_merge_merge(L1:list, L2:list)->list:
    outcome=[]

    i=0
    j=0

    while i<len(L1) and j<len(L2):
        if L1[i]<L2[j]:
            outcome.append(L1[i])
            i+=1

        else:
            outcome.append(L2[j])
            j+=1


    while i<len(L1):
        outcome.append(L1[i])
        i+=1


    while j<len(L2):
        outcome.append(L2[j])
        j+=1

    return outcome


def my_merge(L:list)->list:
    if len(L)<1 or L==None:
        return []
    if len(L)==1:
        return L
    
    m=len(L)//2
    left=my_merge(L[:m])
    right=my_merge(L[m:])

    return my_merge_merge(left,right)



def quicksort_f(L:list)->list:
    if len(L)<2:
        return L
    
    lower, p, upper = partition_first(L)

    return quicksort_f(lower) + [p] + quicksort_f(upper)

def partition_first(L:list):
    left=[]
    right=[]

    p=L[0]

    for i in range(1,len(L)):
        if L[i]<p:
            left.append(L[i])

        else:
            right.append(L[i])

    return left, p, right



def quicksort_l(L:list)->list:
    if len(L)<2:
        return L
    
    left,p,right = partition_last(L)

    return quicksort_l(left) + [p] + quicksort_l(right)

def partition_last(L:list):
    left=[]
    right=[]

    p=L[len(L)-1]

    for i in range(0,len(L)-1):
        if L[i]<p:
            left.append(L[i])
        else:
            right.append(L[i])

    return left, p, right


def mid_quick(L:list)->None:
    if L and L[0]:
        m_q(L, 0, len(L)-1)

def m_q(L:list, left:int, right:int):

    
   

    

    i=left
    j=right
    m=(left+right)//2
    p=L[m]

    while i<=j:
        while L[i]<p:
            i+=1

        while L[j]>p:
            j-=1

        if i<=j:
            L[i],L[j]=L[j],L[i]
            i+=1
            j-=1

    if j>left:
        m_q(L,left,j)

    if i<right:
        m_q(L,i,right)


def quicksort_r(L:list)->None:
    if L and len(L)>1:
        q_r(L, 0, len(L)-1)

def q_r(L:list, left:int, right:int)-> None:
    i,j=left,right

    m=randint(i,j)
    p=L[m]

    while i<=j:
        while L[i]<p:
            i+=1

        while L[j]>p:
            j-=1

        if i<=j:
            L[i],L[j]=L[j],L[i]
            i+=1
            j-=1

    if j>left:
        q_r(L,left,j)

    if i<right:
        q_r(L,i,right)


def nm5(L:list)->int:
    if L and len(L)==1:
        if L[0]%5==0:
            return L[0]
        else:
            return 0
    
    if L and len(L)>1:
        m=len(L)//2
        left=L[m:]
        right=L[:m]
        return nm5(left) + nm5(right)









L=[1,3,10,2,4,7,9,23,5]

print(L)
quicksort_r(L)
print(L)

print(nm5(L))


