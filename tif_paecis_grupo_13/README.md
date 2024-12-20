# tif_paecis_grupo_13
### Entrega que corresponde al grupo 13 del Módulos Programa de actualización en Estrategias Computacionales para la Investigación Social - C-1 (PAECIS). 
### El grupo está conformado por Tomás Deglise, Vladyslav Dodonov y Natalia Rossetti


### Estructura del proyecto: 

```python

PAECIS_GRUPO_13/
├── data/
│   ├── external/                # Datos externos proporcionados
│   ├── processed/               # Datos procesados listos para análisis
│   ├── raw/                     # Datos sin procesar descargados
├── notebooks/                   # Notebooks organizados por pasos
├── scripts/                     # Scripts de Python (setup_env.py, main_script.py, etc.)
├── venv/                        # Entorno virtual (no incluido en el repositorio)
├── requirements.txt             # Lista de dependencias del proyecto
├── README.md                    # Documentación del proyecto
└── .gitignore                   # Archivos y carpetas a ignorar
```
----------------------------------------------------------------------------------------------------------------

### Instrucciones para configurar el entorno

#### Requisitos previos
- Tener instalado Python 3.8 o superior.
- Tener acceso a una terminal o entorno de línea de comandos.


1. Clonar el repositorio
Ejecuta los siguientes comandos para clonar el repositorio y navegar a su directorio:

```bash
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio
```

2. Configurar el entorno virtual e instalar dependencias
Ejecuta el siguiente comando para crear el entorno virtual e instalar las dependencias:

```bash
python scripts/setup_env.py
```

Este script:
- Crea un entorno virtual llamado venv/.
- Instala las dependencias definidas en requirements.txt.

Si deseas hacerlo manualmente, sigue estos pasos:
```bash
# Crear el entorno virtual
python -m venv venv

# Activar el entorno virtual
source venv/bin/activate      # En Linux/Mac
venv\Scripts\activate         # En Windows

# Instalar las dependencias
pip install -r requirements.txt
```

3. Ejecutar el script principal
Una vez configurado el entorno, puedes ejecutar el script principal con:

```bash
python scripts/main_script.py
```
Esto ejecutará el análisis principal del proyecto.

----------------------------------------------------------------------------------------------------------------

### Notebooks
Puedes explorar los análisis paso a paso en los notebooks dentro de la carpeta notebooks/. Asegúrate de activar el entorno virtual antes de abrirlos:

```bash
source venv/bin/activate
jupyter notebook
```
----------------------------------------------------------------------------------------------------------------

### Archivos ignorados
En el archivo .gitignore, ya está configurado para ignorar:

```bash
# Python cache files
__pycache__/
*.py[cod]

# Virtual environment
venv/
scripts/venv/

# Jupyter Notebook checkpoints
.ipynb_checkpoints/

# Logs and temporary files
*.log
*.tmp

# Automated file to create directories
/create_files.py
```

No necesitas subir estos archivos/carpeta al repositorio.
----------------------------------------------------------------------------------------------------------------
