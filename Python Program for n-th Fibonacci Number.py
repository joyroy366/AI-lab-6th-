fibArray=[0,1]
sum=0
num=int(input("Enter the number :"))
for i in range(num):
    sum=fibArray[i]+fibArray[i+1]
    fibArray.append(sum)
print("Fibonacci value:",fibArray)

