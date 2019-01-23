# Ordinal Number.
nums = [str(i) for i in range(1,9)]
ordinal = ['st','nd','rd','th']
for i in nums:
    if i=='1':
        print(i+ordinal[0])
    elif i == '2':
        print(i + ordinal[1])
    elif i == '3':
        print(i + ordinal[2])
    else:
        print(i + ordinal[3])

