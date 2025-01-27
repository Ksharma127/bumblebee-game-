Adress=("24","buckingham mansions","353 west end lane","London","NW6 1LR")
houseno , housename, streetname,city,zipcode=Adress
print("Adress:",Adress)
print("city:",city)
print(Adress[2:5])
print(Adress[3])
print(Adress[4])
#tuples does not allow changing
for i in Adress:
    print(i)
    if i == "London":
        print("yes") 
    elif i == "24":
        print("yes")
    else:
        print("no")
