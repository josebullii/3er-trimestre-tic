edadJuan = int(input("Dime la edad de Juan: "))
edadJose = int(input("Dime la edad de Jose: "))

#Intercambio de las edades
edadAux = edadJose
edadJose = edadJuan
edadJuan = edadAux

#if condicional
if edadJose>=18:
    print("La edad de Jose es", edadJose, " y es mayor de edad")
else:
    print("La edad de Jose es", edadJose, "y es menor de edad")

if edadJuan>=18:
    print("La edad de Juan es", edadJuan, "y es mayor de edad")
else:
    print("La edad de Juan es", edadJuan, "y es menor de edad")