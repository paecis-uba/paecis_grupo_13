import os
import subprocess
import sys
import argparse

def setup_environment(venv_dir, requirements_path):
    # Verificar si ya existe el entorno virtual
    if not os.path.exists(venv_dir):
        print(f"Creando entorno virtual en '{venv_dir}'...")
        try:
            subprocess.check_call([sys.executable, "-m", "venv", venv_dir])
            print("Entorno virtual creado exitosamente.")
        except subprocess.CalledProcessError as e:
            print(f"Error al crear el entorno virtual: {e}")
            sys.exit(1)

    # Ruta al ejecutable pip dentro del entorno virtual
    pip_executable = os.path.join(venv_dir, "bin", "pip") if os.name != "nt" else os.path.join(venv_dir, "Scripts", "pip.exe")

    # Verificar si el archivo requirements.txt existe
    if not os.path.exists(requirements_path):
        print(f"Error: No se encontró el archivo requirements.txt en {requirements_path}")
        sys.exit(1)

    # Instalar dependencias desde requirements.txt
    try:
        print("Instalando dependencias desde requirements.txt...")
        subprocess.check_call([pip_executable, "install", "-r", requirements_path])
        print("¡Dependencias instaladas correctamente!")
    except subprocess.CalledProcessError as e:
        print(f"Error al instalar dependencias: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Configura automáticamente un entorno virtual e instala dependencias.")
    parser.add_argument(
        "--venv_dir",
        type=str,
        default=os.path.join(os.path.dirname(__file__), "../venv"),
        help="Ruta donde se creará el entorno virtual (por defecto: ../venv en el directorio principal)."
    )
    parser.add_argument(
        "--requirements",
        type=str,
        default=os.path.join(os.path.dirname(__file__), "../requirements.txt"),
        help="Ruta al archivo requirements.txt (por defecto: ../requirements.txt en el directorio principal)."
    )
    args = parser.parse_args()

    setup_environment(venv_dir=os.path.abspath(args.venv_dir), requirements_path=os.path.abspath(args.requirements))
