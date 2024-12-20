@echo off

:: Mostrar ayuda si se pasa el parámetro --help
if "%1"=="--help" (
    echo.
    echo Uso del script:
    echo.
    echo run.bat [notebook]   : Abre Jupyter Notebook
    echo run.bat              : Ejecuta el script principal
    echo run.bat --help       : Muestra este mensaje de ayuda
    echo.
    exit /b
)

:: Configurar entorno virtual e instalar dependencias
python scripts/setup_env.py

:: Activar entorno virtual
call venv\Scripts\activate

:: Abrir Jupyter Notebook o ejecutar el script principal
if "%1"=="notebook" (
    echo Abriendo Jupyter Notebook...
    jupyter notebook
) else (
    echo Ejecutando el script principal...
    python scripts/main_script.py
)

pause
