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
├── scripts/                     # Scripts de Python (setup_env.py y main_script.py)
├── venv/                        # Entorno virtual (no incluido en el repositorio)
├── requirements.txt             # Lista de dependencias del proyecto
├── README.md                    # Documentación del proyecto
├── .gitignore                   # Archivos y carpetas a ignorar
└── run.sh                       # Instala las dependencias y el entorno virtual, lo activa y ejecuta el script.
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

3. Ejecutar el proyecto con run.sh
Se puede configurar el entorno y ejecutar el análisis principal utilizando el script run.sh:
```bash
./run.sh
```

Este script realiza las siguientes acciones:

- Configura el entorno virtual e instala las dependencias si no se han instalado aún.
- Activa el entorno virtual.
- Ejecuta el script principal main_script.py o abre Jupyter Notebook dependiendo del parámetro que se pase (main_script.py se ejecuta por default).

Si se quiere abrir Jupyter Notebook, ejecuta:
```bash
./run.sh notebook
```
Si necesitan ver la ayuda ejecuten este comando:
```bash
./run.sh --help
```

----------------------------------------------------------------------------------------------------------------

### Notebooks
Es posible explorar los análisis paso a paso en los notebooks dentro de la carpeta notebooks/. Asegurense de activar el entorno virtual antes de abrirlos utilizando el metodo anterior:

```bash
python scripts/main_script.py
```
o de forma manual: 

```bash
source venv/bin/activate
jupyter notebook
```


###  Ejecución en diferentes entornos

#### **Google Colab**
Si usas Google Colab, instala las dependencias manualmente y sube los datos necesarios:
```python
!pip install -r requirements.txt

from google.colab import files
uploaded = files.upload()  # Se puede subir los archivos directamente desde tu computadora
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

No es necesario subir estos archivos/carpeta al repositorio.

----------------------------------------------------------------------------------------------------------------
