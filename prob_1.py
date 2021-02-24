def multiples_of_under(of , under):
    L=[]
    for i in range(of,under,of):
        L.append(i)
    return L

def sum(L):
    s=0
    for i in range (len(L)):
        s+=L[i]
    return s

M=multiples_of_under(5, 1000)
P=multiples_of_under(3, 1000)
N=multiples_of_under(15,1000)
x=sum(M) + sum(P) - sum(N)
print(x)