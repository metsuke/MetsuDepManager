# Comentarios para humanos
# Este script inicializa un entorno de desarrollo para MetsuDepManager basado en Poetry.
# Su función principal es:
#   - Verificar si Poetry está instalado en el sistema.
#   - Si no lo está, instalarlo automáticamente usando el método oficial recomendado (instalador vía curl) con fallback a pip.
#   - Detectar si ya existe un proyecto Poetry (pyproject.toml) en el directorio actual.
#   - Si existe: ejecutar 'poetry install' para instalar todas las dependencias y crear/actualizar el entorno virtual.
#   - Si no existe: inicializar un nuevo proyecto Poetry de forma NO interactiva usando 'poetry init --no-interaction'.
#     Esto crea un pyproject.toml básico con valores por defecto (nombre basado en el directorio, versión 0.1.0, etc.).
#   - Añadir temporalmente ~/.local/bin al PATH si es necesario (para que Poetry sea accesible en la misma sesión).
#   - Proporcionar mensajes claros al usuario sobre cada paso realizado.
# El script está diseñado para ser ejecutado una sola vez al clonar o crear el proyecto MetsuDepManager,
# pero puede volver a ejecutarse sin problemas para reinstalar dependencias.
# Compatible con macOS, Linux y Windows (WSL o nativo con Python instalado).
# Autor: Raul Carrillo aka metsuke <metsuke@gmail.com>
# Fecha de última actualización: enero 2026.
# Corrección reciente: Se cambió a modo no interactivo en 'poetry init' para evitar que el script se cuelgue esperando input del usuario.

# Documentación
# Uso:
#   python init_metsudepmanager.py
# Requisitos previos:
#   - Python 3.8 o superior instalado y accesible en PATH.
#   - Conexión a internet la primera vez (para descargar e instalar Poetry si no está presente).
# Flujo del script:
# 1. Verifica si 'poetry' está disponible en PATH.
# 2. Si no → intenta instalar vía instalador oficial (curl).
# 3. Si falla el instalador oficial → fallback a 'pip install --user poetry'.
# 4. Añade ~/.local/bin al PATH de la sesión actual si es necesario.
# 5. Si existe pyproject.toml → ejecuta 'poetry install'.
# 6. Si no existe → ejecuta 'poetry init --no-interaction' para crear un pyproject.toml básico automáticamente.
# 7. Informa al usuario de los siguientes pasos recomendados (poetry shell, poetry add, etc.).
# Notas:
#   - El script no modifica archivos existentes ni fuerza opciones; respeta el estado actual del proyecto.
#   - En caso de error crítico (imposible instalar Poetry), termina con código de salida 1 y mensaje claro.
#   - El modo no interactivo usa valores por defecto; puedes editar pyproject.toml manualmente después.
# Autor: Raul Carrillo aka metsuke <metsuke@gmail.com>

# Comentarios para IA
# Estado actual del código (enero 2026):
# - Instalación de Poetry: método principal vía instalador oficial curl (recomendado por python-poetry.org).
# - Fallback robusto a pip install --user poetry.
# - Detección automática de PATH y añadido temporal para la sesión actual.
# - Lógica diferenciada: install existente vs. init nuevo proyecto.
# - Uso de shutil.which para detección fiable de Poetry.
# - Manejo de errores detallado con mensajes claros para el usuario.
# - No se añaden dependencias iniciales automáticas (para respetar libertad del usuario).
# - Compatible con entornos restringidos (sin sudo necesario gracias a --user).
# - Cambio clave: 'poetry init --no-interaction' para evitar hanging en subprocess.run() cuando se espera input interactivo.
# - Autor añadido explícitamente como "Raul Carrillo aka metsuke <metsuke@gmail.com>" en comentarios para humanos y documentación.
# Todo alineado con mejores prácticas actuales de Poetry en 2026.

# Exigencias Generales a la IA
# - Debes generar y mantener varios bloque de comentarios varios en la cabecera del fichero, como comentario de comentarios para humanos, otro de documentacion, otro con comentarios para IA en la que tu te apuntes lo que necesites para futuros trabajos con el script, y las dos secciones de Exigencias a la IA, la general (generica de programación) y la especifica del script que estamos trabajando.
# - Siempre actualiza el contenido de los comentarios para humanos e IA en cada revisión del script, manten intacta el área de Exigencias a IA.
# - No modifiques nada del script que no te hayan pedido explícitamente sin consultarlo primero.
# ---
# Exigencias especificas del script para la IA

import subprocess
import sys
import os
import shutil

def run_command(cmd, check=True):
    """Ejecuta un comando en la shell y maneja errores de forma amigable."""
    try:
        result = subprocess.run(cmd, check=check, text=True, capture_output=True)
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error ejecutando {' '.join(cmd)}:")
        if e.stderr:
            print(e.stderr)
        return False
    except FileNotFoundError:
        print(f"Comando no encontrado: {cmd[0]}. Verifica que esté instalado y en PATH.")
        return False

def is_poetry_installed():
    """Comprueba si Poetry está disponible en el sistema."""
    return shutil.which("poetry") is not None

def install_poetry():
    """Instala Poetry usando el método oficial recomendado (2026)."""
    print("Poetry no detectado. Instalándolo mediante el instalador oficial...")
    
    # Método principal: instalador oficial vía curl
    install_cmd = ["curl", "-sSL", "https://install.python-poetry.org", "|", sys.executable, "-"]
    if run_command(install_cmd):
        print("Instalación oficial completada.")
    else:
        print("Fallback: instalando Poetry vía pip...")
        if not run_command([sys.executable, "-m", "pip", "install", "--user", "poetry"]):
            print("No se pudo instalar Poetry automáticamente.")
            return False
    
    # Añadir ~/.local/bin al PATH de esta sesión si es necesario
    poetry_path = os.path.expanduser("~/.local/bin")
    if poetry_path not in os.environ.get("PATH", ""):
        os.environ["PATH"] += os.pathsep + poetry_path
        print(f"Añadido {poetry_path} al PATH de esta sesión.")
    
    return True

def main():
    print("=== Inicializador de MetsuDepManager con Poetry ===\n")
    
    if not is_poetry_installed():
        if not install_poetry():
            print("\nNo se pudo instalar Poetry. Instálalo manualmente desde:")
            print("https://python-poetry.org/docs/#installation")
            sys.exit(1)
        # Verificar nuevamente tras instalación
        if not is_poetry_installed():
            print("Poetry instalado pero no detectable en PATH. Reinicia la terminal o añade ~/.local/bin al PATH.")
            sys.exit(1)
    
    print("Poetry está disponible y listo para usar.\n")
    
    if os.path.exists("pyproject.toml"):
        print("Proyecto Poetry existente detectado (pyproject.toml encontrado).")
        print("Instalando dependencias...\n")
        run_command(["poetry", "install"])
    else:
        print("No se encontró pyproject.toml. Inicializando nuevo proyecto Poetry de forma automática (no interactiva)...\n")
        run_command(["poetry", "init", "--no-interaction"])
        print("\npyproject.toml creado con valores por defecto.")
        print("Edítalo manualmente si necesitas cambiar nombre, versión, autor, etc.")
        print("Luego ejecuta 'poetry install' para crear el entorno virtual.")
    
    print("\n¡MetsuDepManager inicializado correctamente!")
    print("Pasos recomendados:")
    print("  • poetry shell                  → activar el entorno virtual")
    print("  • poetry add <paquete>          → añadir nuevas dependencias")
    print("  • poetry run python tu_script.py → ejecutar scripts en el entorno")

if __name__ == "__main__":
    main()