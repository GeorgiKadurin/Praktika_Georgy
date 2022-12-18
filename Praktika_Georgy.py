from math import *

#Ülesanne 1.
n=float(input("Sisesta arv: "))
try:
    if n>0:
        print("Arv on positiivne")
    else:
        print("Negatiivne arv")
except:
    print("Vale arvukogum")
try:
    if n%2==1:
        print("Paaritu arv")
    else:
        print("Paarisarv")
except:
    print("Vale arvukogum")
    print()
    print()
    
#Ülesanne 2.
a=int(input("Arv 1 "))
b=int(input("Arv 2 "))
c=int(input("Arv 3 "))
try:
    if (a,b,c)>0:
        print("Paarisarv")
        if a+b+c==180:
            if a==b and b==c:
                print("Võrdkülgne kolmnurk")
            elif a==b or a==c or b==c:
                print("Võrdse puusaga kolmnurk")
            else:
                print("Mitmekülgne kolmnurk")
    else:
        print("Paaritu arv")
except:
    print("Vale arvukogum")
    print()
    print()

#Ülesanne 3.
Küsimus=input("Nädalapäev? ")
try:
    if Küsimus.lower()=="jа":
        number=input("Sisesta arv 1-7: ")
        if number.isdigit() and 1 <=int(number) <=7:
            päeva=["Esmaspäev", "Teisipäev", "Kolmapäev", "Neljapäev", "Reede", "Laupäev", "Pühapäev"]
            print(f"день недели: {päeva[int(number)-1]}")
        else:
            print("Viga!")
except:
    print("Ok")
    print()
    print()

#Ülesanne 4.
päev=int(input("Millal sinu sünnipäev on?: "))
kuu=input("Sünnikuu?: ")
if kuu=="Detsember":
	sodiaagimärk="strelets" if (päev<22) else "kaljukits"
elif kuu=="Jaanuar":
	sodiaagimärk="kaljukits" if (päev<20) else "veevalaja"
elif kuu=="Veebruar":
	sodiaagimärk="veevalaja" if (päev<19) else "kala"
elif kuu=="Märts":
	sodiaagimärk="kala" if (päev<21) else "jäär"
elif kuu=="Aprill":
	sodiaagimärk="jäär" if (päev<20) else "sõnni"
elif kuu=="Mai":
	sodiaagimärk="sõnni" if (päev<21) else "kaksikud"
elif kuu=="Juuni":
	sodiaagimärk="kaksikud" if (päev<21) else "vähk"
elif kuu=="Juuli":
	sodiaagimärk="vähk" if (päev<23) else "lõvi"
elif kuu=='August':
	sodiaagimärk="lõvi" if (päev<23) else "neitsi"
elif kuu=="September":
	sodiaagimärk="neitsi" if (päev<23) else "kaalud"
elif kuu=="Oktoober":
	sodiaagimärk="kaalud" if (päev<23) else "skorpion"
elif kuu=="November":
	sodiaagimärk="skorpion" if (päev<22) else "strelets"
print("Sinu sodiaagimärk :",sodiaagimärk)
print()
print()

#Ülesanne 5(iseseisev).
