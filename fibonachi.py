a= int(input("addadd ra vared kon")
x = []

for i in range(n):
    if (i == 0 or i == 1):
        b.append(1)
    
    else:
        b.append(b[i-1]+b[i-2])

b= list(map(str, b))        
c = ', '.join(b)
print(b)