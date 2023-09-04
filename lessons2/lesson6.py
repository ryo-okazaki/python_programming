count = 0

while count < 5:
    print(count)
    count += 1

count1 = 0
while count < 5:
    if count1 >= 5:
        break
    
    if count1 == 2:
        count1 += 1
        continue
    
    print(count1)
    count1 += 1