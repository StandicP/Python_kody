print(20*"=")
print("PŘEPOČET JEDNOTEK")
print(20*"=")

kg_pocet=int(input("Zadej počet kg: "))
km_pocet=int(input("Zadej počet km: "))
l_pocet=int(input("Zadej počet l: "))

print(20*"=")

kg_vysledek=round((kg_pocet*2.2), 1)
print(kg_pocet, "kg je po přepočtu:", kg_vysledek, "lb")
km_vysledek=round((km_pocet*0.62), 1)
print(km_pocet, "km je po přepočtu:", km_vysledek, "mil")
l_vysledek=round((l_pocet*0.26), 1)
print(l_pocet, "l je po přepočtu:", l_vysledek, "gal")

print(20*"=")