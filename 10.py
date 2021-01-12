name = input("Enter name: ")
print("Tere " +  name)
home = input(" Where do you live: ")
if home == "saaremaa":
    print("tere tulemast saarlane")
else:
    print("et saa elad " + home)
age = int(input("Sisestage vanus: "))
if age < 18:
    print("oled liiga noor")
elif age > 18:
    print("Te võite autot juhtida")
else:
    print("õnnitlen teid saades 18 aastaseks")
