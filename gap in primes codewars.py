def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            break
    return n

def gap(g, m, n):
    l = []
    for j in range(m,n+1):
        if is_prime(j)!=None:
            l.append(is_prime(j))
    for i in range(len(l)):
        compare = l[i:i+2]
        if len(compare) > 1:
            if compare[1]-compare[0]==g:
                return compare
    return None        
        
        
