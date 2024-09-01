numbers=int(input("Ender the number :"))
value=0
if numbers == 0 or numbers ==1:
    print(f"{numbers} is not a prime number")
elif numbers>1:
    for i in range(2,numbers):
        if (numbers %i )==0:
            value=1
            break
if value==1:
    print(f"{numbers} is not a prime number")
else:
    print(f"{numbers} is a prime number")
