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
├── run.sh                       # Script de configuración y ejecución en Linux
└── run.bat                      # Script de configuración y ejecución en Windows
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

2. Uso del entorno virtual y ejecución de scripts
Dependiendo del sistema operativo que se esté utilizando, se deberá usar uno de los dos archivos disponibles para configurar y ejecutar el entorno virtual:

##### En sistemas Windows: `run.bat`
Si estás utilizando Windows, puedes ejecutar el script run.bat, el cual configurará el entorno virtual, instalará las dependencias necesarias y ejecutará el script principal o abrirá Jupyter Notebook dependiendo del parámetro que pases.

Pasos:
- Abre la terminal de Windows (CMD o PowerShell).
- Navega al directorio del proyecto.
- Ejecuta el archivo run.bat con el siguiente comando:

```bash
./run.bat
```

- Si la preferencia es abrir Jupyter Notebook en lugar de ejecutar el script principal, se puede utilizar:
```bash
./run.bat notebook
```

- Para ver la ayuda del script, puedes ejecutar:
```bash
.\run.bat --help
```
Esto mostrará el uso y las opciones disponibles.

3. En sistemas Linux/macOS: `run.sh`
Estando en Linux o macOS, se puede utilizar run.sh, el cual realiza la misma función que el archivo .bat pero para sistemas basados en Unix.

Pasos:
- Abrir la terminal.
- Navegar al directorio del proyecto.
- Si no posee permisos de ejecución, otórgalos con:
```bash
chmod +x run.sh
```
- Ejecutar el script:
```bash
./run.sh
```
Este comando configurará el entorno virtual, instalará las dependencias y ejecutará el script principal.

- Si la preferencia es abrir Jupyter Notebook en lugar de ejecutar el script principal, se puede utilizar:
```bash
./run.sh notebook
```

- Para ver la ayuda del script, puedes ejecutar:
```bash
./run.sh --help
```
----------------------------------------------------------------------------------------------------------------

4. Configurar el entorno virtual e instalar dependencias usando el script de Python
Se debe ejecutar el siguiente comando para crear el entorno virtual e instalar las dependencias:

```bash
python scripts/setup_env.py
```

Este script:
- Crea un entorno virtual llamado venv/.
- Instala las dependencias definidas en requirements.txt.

Si se desea hacerlo manualmente, se deben seguir estos pasos:
```bash
# Crear el entorno virtual
python -m venv venv

# Activar el entorno virtual
source venv/bin/activate      # En Linux/Mac
venv\Scripts\activate         # En Windows

# Instalar las dependencias
pip install -r requirements.txt
```

----------------------------------------------------------------------------------------------------------------

### Notebooks
Es posible explorar los análisis paso a paso en los notebooks dentro de la carpeta notebooks/. Asegurense de activar el entorno virtual antes de abrirlos utilizando el metodo anterior:

```bash
source venv/bin/activate
jupyter notebook
```
o si se quiere hacer automaticamente: 

```bash
#Windows
./run.bat notebook

#Linux/Mac
./run.sh notebook
```


###  Ejecución en diferentes entornos

#### **Google Colab**
Si se está utilizando Google Colab, se deberían instalar las dependencias manualmente y subir los datos necesarios:
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
