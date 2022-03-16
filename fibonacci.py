n=int(input("Type the the nth term "))
p = 5 ** 0.5
q = (((1+p)/2) ** n)
r = ((1-p)/2) ** n
s = q/p - r/p
t = s % 1
if t >= 0.5:
    print(s-t + 1)
else:
    print( s-t)
