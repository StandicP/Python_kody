print(20*"=")
print("BMI KALKULAČKA")
print(20*"=")

print("Zadejte své jméno:")
jmeno = input()

print("Zadejte svou váhu v kilogramech:")
vaha = float(input())

print("Zadejte svou výšku v metrech:")
vyska = float(input())

bmi = round(vaha/(vyska**2), 1)

if bmi<18.5:
    kategorie = "podvýživa."
elif bmi>=18.5 and bmi<25:
    kategorie = "zdravá váha."
elif bmi>=25 and bmi<30:
    kategorie = "mírná nadváha."
elif bmi>=30 and bmi<40:
    kategorie = "obezita."
else:
    kategorie = "těžká obezita."

print(jmeno, "tvé BMI je", bmi, ", což spadá do kategorie", kategorie)
print(20*"=")