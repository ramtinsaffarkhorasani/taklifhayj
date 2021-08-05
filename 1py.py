a=int(input())
if a<0:
    print("nemishe")
hour=int(a/3600)
a=a-hour*3600
minaute=int(a/60)
a=a-(minaute*60)
print(hour)
print(minaute)
print(a)
