n=int(input("Enter a number: "))
count=0
while n>0:
    n=n//10
    count+=1
print(f"{count} is the total no. of digits in given number")