l = [1,4,2,5,3]

d = []
a= len(l)
while(True):
    if a %2 != 0:
        d.append(a)
        if a //2 == 1:
            d.append(1)
            break
        else:
            a = a//2 +1
    else:
        break
b = len(l)

sum = 0
for k in d:
    for i in range(b):
        for j in range(k):
            sum = sum +   l[i+j]      
            print(l[i+j], end= '   ')   
        print()
        if i + k>=b:
            break 
print(sum)