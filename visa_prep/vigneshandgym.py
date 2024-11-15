def f(X,Y,Z):
    if Z>=X+Y:
        print(2)
    elif Z>=X:
        print(1)
    else:
        print(0)
X,Y,Z=map(int,input().split())
f(X,Y,Z)
