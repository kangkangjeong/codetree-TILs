n,m=tuple(map(int,input().split()))

t=[[0 for _ in range(m)] for _ in range(n)]

cnt=1

for i in range(m+n-1):
    for j in range(i+1):
        try :
            t[j][i-j]=cnt
        except:
            pass
        else:
            cnt+=1

for k in t:
    print(*k)