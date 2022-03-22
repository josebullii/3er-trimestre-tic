edadJuan = int(input("Dime la edad de Juan: "))
edadJose = int(input("Dime la edad de Jose: "))

#Intercambio de las edades
edadAux = edadJose
edadJose = edadJuan
edadJuan = edadAux

print("Juan tiene", edadJuan, "años y Jose tiene", edadJose, "años")