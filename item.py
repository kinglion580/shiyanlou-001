a = [(80000, 0.45, 13505), (35000, 0.30, 2755),(55000, 0.35, 5505),(9000, 0.25, 1005),(4500, 0.2, 555),(1500, 0.1, 105),(0, 0.03, 0)]                                                        

for item in a:
    print(item)
    for i in range(3):
        print(item[i],end=' ')

print("-------------")
print(item[0])
print(item[1])
print(item[2])
