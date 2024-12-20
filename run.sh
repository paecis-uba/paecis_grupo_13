#!/bin/bash

# Función para mostrar ayuda
function show_help {
    echo "Uso: $0 [opción]"
    echo ""
    echo "Opciones:"
    echo "  notebook    Abre Jupyter Notebook."
    echo "  (vacío)     Ejecuta el script principal (main_script.py)."
    echo "  --help      Muestra esta ayuda."
}

# Mostrar ayuda si se pasa --help
if [ "$1" == "--help" ]; then
    show_help
    exit 0
fi

# Configurar entorno virtual e instalar dependencias
python scripts/setup_env.py

# Activar entorno virtual
source venv/bin/activate

# Abrir Jupyter Notebook o ejecutar el script principal
if [ "$1" == "notebook" ]; then
    echo "Abriendo Jupyter Notebook..."
    jupyter notebook
else
    echo "Ejecutando el script principal..."
    python scripts/main_script.py
fi
