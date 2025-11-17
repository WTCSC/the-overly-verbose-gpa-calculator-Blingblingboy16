import time as t
n=int(input())
g=[]
for i in range(n):
    while 1:
        try:
            x=float(input())
            if 0<=x<=4:g.append(x);break
        except:0
print("calc");t.sleep(1)
p=sum(g)/n
print(p)
h=input()
k=n//2
s=g[:k]if h=="1"else g[k:]
q=sum(s)/len(s)
print(q)
print("+"if q>p else"-"if q<p else"=")
while 1:
    try:
        m=float(input())
        if 0<=m<=4:break
    except:0
if p>=m:print("ok")
else:
    a=[]
    for i in range(n):
        r=g[:];r[i]=4
        if sum(r)/n>=m:a.append(i+1)
    print(a or ">1")
