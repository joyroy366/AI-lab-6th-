n=[11,22,33,44,55,66,77,88,99]
print(n)
tamp=n[0]
n[0]=n[-1]
n[-1]=tamp
print(n)