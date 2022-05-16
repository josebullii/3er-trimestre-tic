#Crea un función “ConvertirEspaciado”, que reciba como parámetro un texto y
#devuelve una cadena con un espacio adicional tras cada letra. Por ejemplo,
#“Hola, tú” devolverá “H o l a , t ú “. Crea un programa principal donde se use
#dicha función.

def ConvertirEspaciado(texto):
    textoEspaciado = ""
    
    for i in texto:
        textoEspaciado = textoEspaciado + (i + (" "))
    return textoEspaciado

#Inicio del programa
texto = input("Introduzca el texto al que quiere agregar espacios: ")
print("El texto espaciado es: ", end="")
print(ConvertirEspaciado(texto), end = "")