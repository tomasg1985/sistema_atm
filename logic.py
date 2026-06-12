import sqlite3
from colorama import Fore, Style, init
init()

conexion = sqlite3.connect("banco.db")
cursor = conexion.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS banco(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        saldo REAL NOT NULL,
        contrasena TEXT NOT NULL
    )
''')


mensaje_exito = "Transaccion exitosa"
mensaje_error = "Transaccion fallida"

def extraer_monto(saldo, monto):
    
    """
    Simula la extracción de dinero de una cuenta.

    Parámetros:
    saldo (int/float): Saldo actual disponible.
    monto (int/float): Cantidad a extraer (debe ser positiva).

    Retorna:
    tuple: (nuevo_saldo, mensaje, exito)
        - nuevo_saldo (int/float): Saldo actualizado si la operación es exitosa, de lo contrario el saldo original.
        - mensaje (str): Mensaje informativo para el usuario.
        - exito (bool): True si la extracción fue exitosa, False en caso contrario.

    Ejemplo:
        >>> extraer_monto(5000, 1000)
        (4000, "Transaccion exitosa", True)
        >>> extraer_monto(5000, 6000)
        (5000, "Transaccion fallida", False)
    """
    try:
        if monto > 0 and monto <= saldo:
            nuevo_saldo = saldo - monto
            
            cursor.execute('UPDATE banco SET saldo = ?', (nuevo_saldo,))
            conexion.commit()
            
            print(f"{Fore.GREEN}Operacion realizada con éxito" + Style.RESET_ALL)
            return (nuevo_saldo, mensaje_exito, True)
        else:
            return (saldo, mensaje_error, False)
        
    except sqlite3.Error as e:
        conexion.rollback()
        print(f"{Fore.RED}Error de sistema...{e}" + Style.RESET_ALL)
        return (saldo, mensaje_error, False)
    

def depositar(saldo, monto):
    
    """
    Simula el depósito de dinero en una cuenta.

    Parámetros:
    saldo (int/float): Saldo actual disponible.
    monto (int/float): Cantidad a depositar (debe ser positiva).

    Retorna:
    tuple: (nuevo_saldo, mensaje, exito)
        - nuevo_saldo (int/float): Saldo actualizado si la operación es exitosa,de lo contrario el saldo original.
        - mensaje (str): Mensaje informativo para el usuario.
        - exito (bool): True si el depósito fue exitoso, False en caso contrario.

    Ejemplo:
        >>> depositar(5000, 1000)
        (6000, "Transaccion exitosa", True)
        >>> depositar(5000, -500)
        (5000, "Transaccion fallida", False)
    """
    try:
        if monto > 0:
            nuevo_saldo = monto + saldo
            
            cursor.execute('UPDATE banco SET saldo = ?', (nuevo_saldo,))
            conexion.commit()
            
            print(f"{Fore.GREEN}Operacion realizada con éxito" + Style.RESET_ALL)
            return (nuevo_saldo, mensaje_exito, True)
        
        else:
            print(f"{Fore.RED}Operacion fallida" + Style.RESET_ALL)
            return (saldo, mensaje_error, False)
        
    except sqlite3.Error as e:
        conexion.rollback()
        print(f"{Fore.RED}Error al realizar la operacion por fallas del sistema {e}" + Style.RESET_ALL)
        return (saldo, mensaje_error, False)

def cambiar_contrasena(contrasena_actual, nueva_contrasena, confirmacion):

    """
    Cambia la contraseña de un usuario tras validar la actual y la coincidencia.

    Parámetros:
    contrasena_actual (str): Contraseña vigente.
    nueva_contrasena (str): Nueva contraseña propuesta.
    confirmacion (str): Repetición de la nueva contraseña para verificación.

    Retorna:
    tuple: (nueva_contrasena, mensaje, exito)
        - nueva_contrasena (str o None): La nueva contraseña si es válida, None en caso de error.
        - mensaje (str): Mensaje explicativo del resultado.
        - exito (bool): True si el cambio fue exitoso, False en caso contrario.

    Ejemplo:
        >>> cambiar_contrasena("1234", "5678", "5678")
        ("5678", "Contraseña actualizada con éxito", True)
        >>> cambiar_contrasena("1234", "", "")
        (None, "La contraseña no puede estar vacía", False)
        >>> cambiar_contrasena("1234", "5678", "0000")
        (None, "Las contraseñas no coinciden", False)
        >>> cambiar_contrasena("1234", "1234", "1234")
        (None, "La nueva contraseña debe ser diferente a la actual", False)
    """

    if not nueva_contrasena:
        return(None, "La contraseña no puede estar vacía", False)
        
    if nueva_contrasena == contrasena_actual:
        return(None, "La nueva contraseña debe ser diferente a la actual", False)

    if nueva_contrasena != confirmacion:
        return(None, "Las contraseñas no coinciden", False)

    return(nueva_contrasena, "Contraseña actualizada con éxito", True)