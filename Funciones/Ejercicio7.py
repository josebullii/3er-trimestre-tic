#Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una 
#contraseña y te devuelve Verdadero si el nombre de usuario es “usuario1” y la 
#contraseña es “asdasd”. Además recibe el número de intentos que se ha 
#intentado hacer login y si no se ha podido hacer login incremente este valor.
#Crear un programa principal donde se pida un nombre de usuario y una 
#contraseña y se intente hacer login, solamente tenemos tres oportunidades para 
#intentarlo.

def Login(usuario, contraseña):
    
    if (usuario == "usuario1") and (contraseña == "asdasd"):
        return True
    else:
        return False
    
    
#Inicio del programa

intentos = 0

while intentos < 3:
    
    usuario = input("Introduce el nombre de usuario: ")
    contraseña = input("Introduce la contraseña: ")
    
    if Login(usuario, contraseña) == True:
        print("Iniciando...")
        exit()
    
    else:
        print("Usuario y/o contraseña incorrectos\n")
        intentos = intentos + 1
        
if intentos == 3:
    print("No dispone de más intentos")


            