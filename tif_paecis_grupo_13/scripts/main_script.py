 # Script para configurar entorno virtual
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Definir rutas de entrada y salida
data_dir = os.path.join('..', 'data', 'processed')
input_file = os.path.join(data_dir, 'dfscore_final.csv')

# Validar que el archivo de entrada exista
if not os.path.exists(input_file):
    print(f"Error: El archivo de entrada {input_file} no existe.")
    sys.exit(1)

# Cargar el archivo CSV
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print(f"Datos cargados exitosamente desde {file_path}.")
        return data
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        sys.exit(1)

data = load_data(input_file)

# Exploración y visualización de datos
def visualize_data(data):
    try:
        sns.set(style="whitegrid")

        # Conteo de polaridades
        plt.figure(figsize=(10, 6))
        sns.countplot(x='polarity', data=data, palette='viridis')
        plt.title("Distribución de polaridades de sentimiento")
        plt.xlabel("Polaridad")
        plt.ylabel("Frecuencia")
        plt.show()

        # Nube de palabras (si existe una columna relevante)
        if 'cleaned_text' in data.columns:
            from wordcloud import WordCloud

            text = " ".join(data['cleaned_text'].dropna())
            wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

            plt.figure(figsize=(10, 6))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis("off")
            plt.title("Nube de palabras de los comentarios")
            plt.show()

    except Exception as e:
        print(f"Error durante la visualización de datos: {e}")
        sys.exit(1)

visualize_data(data)

# Análisis adicional (modificar según necesidades específicas)
def sentiment_analysis_summary(data):
    try:
        summary = data.groupby('polarity').size()
        print("\nResumen del análisis de sentimiento:")
        print(summary)
    except Exception as e:
        print(f"Error durante el resumen de análisis de sentimiento: {e}")
        sys.exit(1)

sentiment_analysis_summary(data)
