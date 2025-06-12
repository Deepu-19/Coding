n=int(input("Enter a number:"))
even=0
odd=0
even_digits=[]
odd_digits=[]
while n>0:
    digit=n%10
    if digit%2==0:
        even_digits.append(digit)
        even+=1
    else:
        odd_digits.append(digit)
        odd+=1
    n=n//10
print("Even Digits: ",even,", Even digits: ",even_digits)
print("Odd numbers: ",odd,", Odd digits: ",odd_digits)