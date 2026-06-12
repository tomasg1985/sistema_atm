# 🏧 Simulación de Cajero Automático (ATM) con Motor Relacional SQL

Una aplicación financiera transaccional desarrollada en **Python** que modela el comportamiento lógico, matemático y de seguridad de un cajero automático real. Este ecosistema implementa persistencia local mediante **SQLite**, gestionando transacciones financieras de forma atómica y aplicando control de excepciones riguroso junto con validaciones de tipo estrictas.

---

### 🚀 Innovaciones y Características Técnicas

*   **Persistencia de Estados Financieros (SQLite):** Migración de variables volátiles en memoria hacia un motor de base de datos embebido, permitiendo que el saldo disponible y los parámetros de seguridad persistan entre sesiones de ejecución.
*   **Transacciones Atómicas y Tolerancia a Fallos:** Implementación de bloques de control (`try/except sqlite3.Error`) con rutinas de reversión transaccional (`conexion.rollback()`) ante fallos del sistema físico de disco, asegurando que el saldo nunca quede en un estado corrupto.
*   **Encapsulamiento mediante Tuplas de Control:** Las operaciones críticas (`extraer_monto`, `depositar`) devuelven estructuras inmutables de tres elementos (Saldo Actualizado, Mensaje de Estado, Flag Booleano de Éxito) para garantizar flujos de datos predecibles y seguros.
*   **Validación de Tipos y Programación Defensiva:** Módulo de sanitización nativa (`validar_monto`) que aísla las entradas de texto de la terminal (`str`) y audita su composición mediante inspección digital (`.isdigit()`) antes de realizar castéos numéricos.
*   **Seguridad y Reglas de Negocio:** Lógica criptográfica básica para la actualización de credenciales, controlando de forma temprana campos vacíos, redundancias de clave respecto a la actual y errores de confirmación binaria.

---

### 🛠️ Stack Tecnológico

*   **Lenguaje:** Python 3.x
*   **Motor de Persistencia:** [SQLite3](https://python.org) (Mapeo de datos relacionales en archivo local)
*   **Librerías UX:** `colorama` (Feedback jerarquizado por colores en la consola de comandos)

---

### 🗄️ Modelo Relacional de Datos

Al iniciar el sistema por primera vez, el motor SQL inicializa de manera automática la siguiente tabla para el control de la cuenta bancaria simulada:

```sql
CREATE TABLE IF NOT EXISTS banco(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    saldo REAL NOT NULL,
    contrasena TEXT NOT NULL
);
```

---

### 📂 API del Núcleo Lógico transaccional (`logic.py`)

Las reglas financieras del ATM han sido documentadas bajo estándares de producción mediante *Docstrings* interactivos que incluyen ejemplos de pruebas conceptuales (*doctests*):

| Función | Tipo de Operación | Descripción Técnica y Mecanismos de Control |
| :--- | :--- | :--- |
| `extraer_monto()` | **UPDATE / Escritura** | Valida la suficiencia de fondos frente al saldo actual. Actualiza la entidad SQL y mitiga errores mediante cláusulas de guarda. |
| `depositar()` | **UPDATE / Escritura** | Audita que el monto sea un valor positivo flotante o entero, actualiza el registro físico en disco y confirma la transacción (`commit`). |
| `cambiar_contrasena()`| **Lógica de Seguridad** | Evalúa de forma estricta la concordancia de cadenas y restringe el uso de contraseñas previas idénticas para mitigar riesgos. |
| `validar_monto()` | **Sanitización de Datos** | Filtra entradas de usuario por consola. Bloquea caracteres alfabéticos o montos menores o iguales a cero, impidiendo excepciones en ejecución. |

---

### ⚙️ Instalación y Configuración Local

Sigue estos comandos detallados en tu terminal para probar la simulación en tu computadora:

1. **Clonar el repositorio con persistencia relacional:**
   ```bash
   git clone https://github.com
   cd sistema_atm
   ```

2. **Instalar el formateador visual de consola:**
   ```bash
   pip install colorama
   ```

3. **Ejecutar el orquestador principal:**
   ```bash
   python app.py
   ```
   *(Nota: El motor creará el archivo binario de base de datos `banco.db` de forma automática al momento de inicializar el programa).*

---

### 📄 Licencia

Este software se distribuye bajo los términos de la Licencia MIT. Libre para fines educativos, académicos y desarrollo profesional continuo.
