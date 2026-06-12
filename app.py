from logic import *
from validaciones import *
from colorama import Fore, Back, Style, init

init(autoreset=True)

cajero_encendido = True

cliente = {
    "nombre": "Tomas",
    "saldo": 80000,
    "contrasena": "1234"
}

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

    menu_cajero = input("Ingrese la operacion que desea efectuar: ").strip()

    if menu_cajero == "":
        print(Fore.RED + "No ingresaste ninguna opción, verifica e intentalo nuevamente")
        continue

    match menu_cajero:
        case "1":  # Extracción
            print("=========================")
            print("Extracción de efectivo")
            print("=========================")
            print()

            monto_extraccion = input("Indique el monto a extraer (Escriba 'Fin' para salir del sistema): ").strip()

            if monto_extraccion == "":
                print(Fore.RED + "No ingresaste ningún monto, verifica e inténtalo nuevamente")
                continue

            if monto_extraccion.lower() == "fin":
                print(Fore.YELLOW + "Saliendo del sistema...")
                print(Fore.YELLOW + "Hasta luego, vuelva pronto")
                break

            monto_valido, es_valido = validar_monto(monto_extraccion)

            if not es_valido:
                print(Fore.RED + "Monto inválido. Debe ser un número entero positivo.")
                continue

            # Llamar a la función de extracción
            nuevo_saldo, mensaje, exito = extraer_monto(cliente["saldo"], monto_valido)

            if exito:
                cliente["saldo"] = nuevo_saldo
                print(Fore.GREEN + mensaje)
                print(Fore.GREEN + f"Su nuevo saldo en cuenta es: AR${cliente['saldo']}")
            else:
                print(Fore.RED + mensaje)

        case "2":  # Depósito
            print("=========================")
            print("Depósito de efectivo")
            print("=========================")
            print()

            monto_deposito = input("Indique el monto a depositar (Escriba 'Fin' para salir): ").strip()

            if monto_deposito == "":
                print(Fore.RED + "No ingresaste ningún monto, verifica e inténtalo nuevamente")
                continue

            if monto_deposito.lower() == "fin":
                print(Fore.YELLOW + "Operación cancelada. Volviendo al menú principal...")
                continue

            monto_valido, es_valido = validar_monto(monto_deposito)

            if not es_valido:
                print(Fore.RED + "Monto inválido. Debe ser un número entero positivo.")
                continue

            nuevo_saldo, mensaje, exito = depositar(cliente["saldo"], monto_valido)

            if exito:
                cliente["saldo"] = nuevo_saldo
                print(Fore.GREEN + mensaje)
                print(Fore.GREEN + f"Su nuevo saldo en cuenta es: AR${cliente['saldo']}")
            else:
                print(Fore.RED + mensaje)

        case "3":  # Consulta de saldo
            print("=========================")
            print("Consultar saldo")
            print("=========================")
            print()
            print(Fore.CYAN + f"El saldo disponible en cuenta es: AR${cliente['saldo']}")

        case "4":  # Cambio de contraseña
            print("=========================")
            print("Cambio de contraseña")
            print("=========================")
            print()

            contrasena_actual = input("Ingrese su contraseña actual: ").strip()

            if contrasena_actual != cliente["contrasena"]:
                print(Fore.RED + "Contraseña actual incorrecta. Operación cancelada.")
                continue

            nueva_contrasena = input("Ingrese la nueva contraseña: ").strip()
            confirmacion = input("Confirme la nueva contraseña: ").strip()

            nueva, mensaje, exito = cambiar_contrasena(contrasena_actual, nueva_contrasena, confirmacion)

            if exito:
                cliente["contrasena"] = nueva
                print(Fore.GREEN + mensaje)
            else:
                print(Fore.RED + mensaje)

        case "5":  # Salir
            cajero_encendido = False
            print(Fore.YELLOW + "ADIOS...")

        case _:
            print(Fore.RED + "Opción inválida, ingrese alguna opción del menú")

conexion.close()
print(f"{Fore.GREEN}Conexión cerrada. ¡Hasta luego!{Style.RESET_ALL}")