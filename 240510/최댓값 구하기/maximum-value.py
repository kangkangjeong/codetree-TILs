a,b,c=map(int,input().split(' '))
def abc(a,b,c):
    d=list()
    d.append(a)
    d.append(b)
    d.append(c)
    d.sort(reverse=True)
    print(d[0])

abc(a,b,c)