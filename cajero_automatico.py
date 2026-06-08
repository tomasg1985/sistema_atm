cliente = {
    "nombre": "Tomas",
    "saldo" : 80000
}

cajero_encendido = True

while cajero_encendido:
    
    print("=========================")
    print("Sistema de cajero automatico")
    print("=========================")
    print()
    print("1- Extracción")
    print("2- Deposito")
    print("3- Consulta de saldo")
    print("4- Cambio de contraseña")
    print("5- Salir")
    
    menu_cajero = input("Ingrese la operacion que desea efectuar: ")
    
    if menu_cajero == "":
        print("No ingresaste ninguna opción, verifica e intentalo nuevamente")
        continue
    
    match menu_cajero:
        case "1":
            
            print("=========================")
            print("Extracción de efectivo")
            print("=========================")
            print()
            
            monto_extraccion = input("Indique el monto a extraer (Escriba '0' para salir del sistema): ")
            
            if monto_extraccion == "":
                print("No ingresaste ningun monto, verifica e intentalo nuevamente")
                continue
            
            if monto_extraccion == "0":
                print("Saliendo del sistema...")
                print("Hasta luego vuelva pronto")
                break
            
            monto_numerico = int(monto_extraccion)
            
            if monto_numerico <= cliente["saldo"]:
                cliente["saldo"] -= monto_numerico
                print(f"Su nuevo saldo en cuenta es: AR${cliente["saldo"]}")
            else:
                print("No puedes retirar ese monto tu saldo es insuficiente.")
                
            
        case "2":
            print()
            
        case "3":
            print("=========================")
            print("Consultar saldo")
            print("=========================")
            print()
        
            print(f"El saldo disponible en cuenta es: AR${cliente["saldo"]}")
        case "4":
            print()
        
        case "5":
            cajero_encendido = False
            print("ADIOS...")
        
        case _:
            print("Opcion invalida, ingrese alguna opcion del menu")