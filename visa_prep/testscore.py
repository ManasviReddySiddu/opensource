def f(N,X,Y):
    if Y%X==0 and Y<=N*X:
        return "YES"
    else:
        return "NO"
N,X,Y=map(int,input().split())
print(f(N,X,Y))
