print("Indica el número de monedas que tienes de:")
dosEuros = int(input("- 2€: "))
unEuro = int(input("- 1€: "))
cincuentaCent = int(input("- 0.50€: "))
veinteCent = int(input("- 0.20€: "))
diezCent = int(input("- 0.10€: "))

euros = (dosEuros * 2) + (unEuro * 1)
centimos = (cincuentaCent * 0.50) + (veinteCent * 0.20) + (diezCent * 0.10)

total = euros + centimos

print("Tienes un total de", total, "€")