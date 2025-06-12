nums=[2, 3, 2, 5, 3, 2, 6]
frequency={}
for num in nums:
    if num in frequency:
        frequency[num]+=1
    else:
        frequency[num]=1
for key in frequency:
    count=frequency[key]
    print(f"{key} → {count} time{'s' if count > 1 else ''}")