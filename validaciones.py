def validar_monto(monto_str):
    
    """
    Valida que el texto ingresado represente un número entero positivo.

    Parámetros:
    monto_str (str): Cadena ingresada por el usuario.

    Retorna:
    tuple: (monto, es_valido)
        - monto (int o None): El número entero si es válido, None en caso contrario.
        - es_valido (bool): True si el monto es un entero positivo, False si no.

    Ejemplo:
        >>> validar_monto("1500")
        (1500, True)
        >>> validar_monto("0")
        (None, False)
        >>> validar_monto("abc")
        (None, False)
    """
    
    if monto_str.isdigit():
        monto_numero = int(monto_str)
        if monto_numero > 0:
            return(monto_numero, True)
        else:
            return (None, False)
    else:
        return (None, False)