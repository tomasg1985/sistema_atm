# 🏧 Simulación de Cajero Automático (ATM)

Una aplicación interactiva desarrollada en **Python** que simula el flujo lógico y las operaciones financieras esenciales de un cajero automático real. Este proyecto destaca por su arquitectura altamente modular, segregación de responsabilidades y un sistema riguroso de validación de entradas para garantizar la estabilidad del sistema sin depender de librerías externas complejas.

---

### 🚀 Características Técnicas

*   **Arquitectura Modular Avanzada:** División estricta del sistema en módulos especializados (Presentación, Núcleo Lógico y Capa de Validación) para facilitar el mantenimiento y escalabilidad.
*   **Validación de Entradas Rigurosa:** Mecanismos integrados para sanitizar y controlar las acciones del usuario, mitigando desbordamientos, ingresos de tipos de datos incorrectos o transacciones inválidas.
*   **Operaciones Bancarias Simuladas:** Implementación completa del flujo transaccional clásico, incluyendo consulta de saldos, depósitos, retiros de efectivo y transferencias.
*   **Interfaz Optimizada (UX):** Entorno por línea de comandos interactivo potenciado con **Colorama** para ofrecer alertas visuales claras (Éxitos, Advertencias y Errores).

---

### 🛠️ Stack Tecnológico

*   **Lenguaje:** Python 3.x
*   **Librerías:** [Colorama](https://pypi.org) (Formateo estético y manejo de flujos de color en la terminal)

---

### 📂 Estructura y Modularización del Proyecto

El código fuente se encuentra distribuido de forma estratégica para cumplir con el principio de responsabilidad única:


| Archivo | Rol en el Sistema | Descripción Técnica |
| :--- | :--- | :--- |
| `app.py` | **Orquestador Principal** | Punto de entrada de la aplicación. Inicializa el entorno y coordina el flujo general del cajero. |
| `cajero_automatico.py` | **Capa de Presentación** | Gestiona la interfaz de usuario en consola, el renderizado de menús y la captura inicial de datos. |
| `logic.py` | **Motor de Negocio** | Procesa los cálculos matemáticos, transacciones financieras y la mutación de los estados de las cuentas. |
| `validaciones.py` | **Capa de Seguridad** | Módulo autónomo encargado de auditar que los montos, credenciales y operaciones cumplan con las reglas de negocio antes de ser procesados. |

---

### ⚙️ Instalación y Ejecución

Sigue estos pasos para clonar, configurar y ejecutar la simulación en tu entorno local:

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com
   cd sistema_atm
   ```

2. **Instalar las dependencias requeridas:**
   ```bash
   pip install colorama
   ```

3. **Iniciar el sistema:**
   ```bash
   python app.py
   ```

---

### 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo de origen para más detalles.
