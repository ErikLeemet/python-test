u = int(input("esimene arv: "))
t = int(input("teine arv: "))
b = int(input("kolmas arv: "))
if u > t and u > b:
    print(u)
elif t > b:
    print(t)
else:
    print(b)
