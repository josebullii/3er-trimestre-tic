#Crea un función “ConvertirEspaciado”, que reciba como parámetro un texto y
#devuelve una cadena con un espacio adicional tras cada letra. Por ejemplo,
#“Hola, tú” devolverá “H o l a , t ú “. Crea un programa principal donde se use
#dicha función.

def ConvertirEspaciado(texto):
    for i in texto:
        if texto[i] != " ":
            texto = texto[i] + " "

#Inicio del programa

texto = input("Escriba un texto: ")
ConvertirEspaciado(texto)