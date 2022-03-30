def rev(z):
    r=[]
    for i in range(len(z)):
        r.append(z[len(z)-1-i])
        print(r)
    return r
        

n=int(input())
for i in range(n):
    z=list(map(int,input().split()))
    print(rev(z))
