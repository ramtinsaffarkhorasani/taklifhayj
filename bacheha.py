a= int(input("tedad nafarat"))
b= []

for i in range(a):
    nomre = float(input("nomre"))
    b.append(nomre)
    
print("miangin", sum(b) / a)
print("bishtarin", max(b))
print('kamtarin', min(b))