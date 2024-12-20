import os
import pandas as pd
import numpy as np
from fpdf import FPDF
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import nltk
from nltk.corpus import stopwords
from scipy.stats import ttest_ind, mannwhitneyu

# Asegurarse de que las stopwords estén disponibles
nltk.download("stopwords")
stopwords_set = set(stopwords.words('spanish', 'english'))
stopwords_set.update(["@usuario", 'usuario', 'emoji','hashtag', 'http', 'https', 'url', 'q ', 'si', 'che', 'pq', 'd', 'p', 'x', 'jajaja', 'href','youtube', 'watch', 'quot'])

# Clase para generar el PDF
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, '', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')
    
    def chapter_body(self, body):
        # Añadir el texto del cuerpo del capítulo
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_image(self, image_path):
        # Añadir una imagen al documento
        self.image(image_path, x=10, w=180)


# Cargar datos
# Obtener el directorio actual del script principal
base_dir = os.path.dirname(os.path.abspath(__file__))

# Construir el path relativo para los archivos
file_path = os.path.join(base_dir, '../data/processed/dfscore_final.csv')

df_inicial = pd.read_csv(file_path)
df_inicial['comment_time'] = pd.to_datetime(df_inicial['comment_time'])
df_inicial['video_published_at'] = pd.to_datetime(df_inicial['video_published_at'])

# Cálculo de métricas generales
distinct_counts = pd.DataFrame({
    'Comentarios Únicos': [df_inicial['comment_id'].nunique()],
    'Usuarios Únicos': [df_inicial['user_id'].nunique()],
    'Videos': [df_inicial['video_title'].nunique()],
    'Eventos Relacionados': [df_inicial['evento'].nunique()],
    'Canales': [df_inicial['channel_title'].nunique()]
})

likes_totales = df_inicial['comment_likes'].sum()
usuarios_unicos = df_inicial['user_id'].nunique()
comentarios_totales = len(df_inicial)

# Contar comentarios por tipo de insulto
comentarios_insulto = df_inicial['contiene_insulto'].value_counts()

# Contar comentarios clasificados como positivos y negativos (sin considerar neutros)
comentarios_clasificados = df_inicial[df_inicial['Sentimiento'].isin(['Negativo', 'Positivo'])]['Sentimiento'].value_counts()

# Eventos positivos, negativos y neutros
eventos_tipo = df_inicial['tipo_evento'].value_counts().to_dict()

# Total de vistas por tipo de evento
vistas_por_tipo = df_inicial.groupby('tipo_evento')['video_views'].sum().to_dict()

# Contar la cantidad de comentarios por tipo de canal (A favor, En contra, Neutral)
comentarios_por_tipo = df_inicial['condiciones_cuenta'].value_counts()

# Evento con más comentarios
evento_top = df_inicial['evento'].value_counts().idxmax()
comentarios_evento_top = df_inicial['evento'].value_counts().max()

# Usuarios más activos
comments_by_user = df_inicial.groupby(['user_name', 'user_id']).size().reset_index(name='conteo_comentarios')
comments_by_user_ordered = comments_by_user.sort_values(by='conteo_comentarios', ascending=False)

# Cálculo de outliers en comentarios
percentil_999 = np.percentile(comments_by_user['conteo_comentarios'], 99.9)
outliers = comments_by_user[comments_by_user['conteo_comentarios'] > percentil_999]
total_comentarios = comments_by_user['conteo_comentarios'].sum()
total_outliers_comentarios = outliers['conteo_comentarios'].sum()
porcentaje_outliers = (total_outliers_comentarios / total_comentarios) * 100


#direcciones de imagenes
wordcloud_path = os.path.join(base_dir, '../data/processed/wordcloud.png')
output_pdf_path = os.path.join(base_dir, '../data/processed/informe_resumido.pdf')
temporal_analysis_path = os.path.join(base_dir, '../data/processed/temporal_analysis.png')


# Generación de nube de palabras
comentarios_texto = ' '.join(df_inicial['comment'].astype(str))
wordcloud = WordCloud(stopwords=stopwords_set, background_color="white").generate(comentarios_texto)
plt.figure(figsize=(12, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig(wordcloud_path)
plt.close()

# Análisis temporal por semana
df_inicial['week'] = df_inicial['comment_time'].dt.to_period('W')
temporal_data_week = df_inicial.groupby('week').agg(
    mean_polarity=('polarity', 'mean'),
    count_positive=('polarity', lambda x: (x > 0).sum()),
    count_negative=('polarity', lambda x: (x < 0).sum())
).reset_index()
temporal_data_week['week'] = temporal_data_week['week'].dt.to_timestamp()

# Eventos
eventos = df_inicial.groupby(['evento', 'tipo_evento']).agg({'video_published_at': 'min'}).reset_index()
eventos = eventos.rename(columns={'video_published_at': 'fecha'})
eventos['fecha'] = eventos['fecha'].dt.strftime('%Y-%m-%d')
eventos_list = eventos.to_dict(orient='records')

# Función para asignar colores
def asignar_color(tipo_evento):
    if tipo_evento == 'Favorable':
        return 'green'
    elif tipo_evento == 'Desfavorable':
        return 'red'
    else:
        return 'black'

# Crear gráfico temporal
fig, ax = plt.subplots(figsize=(14, 7))
color_positive = 'tab:green'
color_negative = 'tab:red'
ax.set_xlabel('Semana', fontsize=12)
ax.set_ylabel('Cantidad de Comentarios', fontsize=12)

sns.lineplot(data=temporal_data_week, x='week', y='count_positive', marker='o', label='Positivos', color=color_positive, ax=ax)
sns.lineplot(data=temporal_data_week, x='week', y='count_negative', marker='o', label='Negativos', color=color_negative, ax=ax)

for evento in eventos_list:
    fecha_evento_week = pd.to_datetime(evento['fecha'])
    color_evento_week = asignar_color(evento['tipo_evento'])
    ax.axvline(fecha_evento_week, color=color_evento_week, linestyle='--', label=f'{evento["evento"]} ({evento["tipo_evento"]})')
    ax.annotate(evento['evento'], xy=(fecha_evento_week, 0.2), xytext=(fecha_evento_week, 0.5),
                fontsize=12, color=color_evento_week, ha='left', rotation=90)

plt.legend()
plt.tight_layout()
#plt.savefig('/data/processed/temporal_analysis.png')
plt.savefig(temporal_analysis_path)
plt.close()

# Generación del PDF
#output_pdf_path = '/data/processed/informe_resumido.pdf'
if os.path.exists(output_pdf_path):
    os.remove(output_pdf_path)

pdf = PDF()
pdf.add_page()
#pdf.set_font('Arial', '', 12)

# Título general (más grande)
pdf.set_font("Arial", 'B', 20)  # 'B' es para negrita, 20 es el tamaño
pdf.cell(200, 10, "Informe Resumido Autogenerado", ln=True, align='C')  # Centrado

# Espacio después del título principal
pdf.ln(10)  # Salto de línea


# # Sección inicial descriptiva
# pdf.multi_cell(0, 10, """
# Informe Resumido Autogenerado""")

# Tabla de métricas generales
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, "Métricas Generales", 0, 1, 'C')
pdf.set_font('Arial', '', 12)

columnas = ["Métrica", "Valor"]
valores = [
    ["Comentarios Únicos", distinct_counts['Comentarios Únicos'][0]],
    ["Usuarios Únicos", distinct_counts['Usuarios Únicos'][0]],
    ["Videos", distinct_counts['Videos'][0]],
    ["Eventos Relacionados", distinct_counts['Eventos Relacionados'][0]],
    ["Canales", distinct_counts['Canales'][0]],
    ["Likes de los Comentarios", likes_totales],
    ["Comentarios Totales", comentarios_totales],
    ["Comentarios Eventos Favorables", eventos_tipo.get("Favorable", 0)],
    ["Comentarios Eventos Desfavorables", eventos_tipo.get("Desfavorable", 0)],
    ["Comentarios Eventos Neutros", eventos_tipo.get("Neutral", 0)],
    ["Comentarios Canales A Favor", comentarios_por_tipo.get("A favor", 0)],
    ["Comentarios Canales En Contra", comentarios_por_tipo.get("En contra", 0)],
    ["Comentarios Canales Neutros", comentarios_por_tipo.get("Neutral", 0)],
    ["Vistas Eventos Favorables", vistas_por_tipo.get("Favorable", 0)],
    ["Vistas Eventos Desfavorables", vistas_por_tipo.get("Desfavorable", 0)],
    ["Evento con más comentarios", evento_top],
    ["Cantidad Comentarios del evento top", comentarios_evento_top],
    ["Comentarios con Insulto", comentarios_insulto.get("Insulta", 0)],
    ["Comentarios sin Insulto", comentarios_insulto.get("No insulta", 0)],
    ["Comentarios Clasificados como Negativo", comentarios_clasificados.get("Negativo", 0)],
    ["Comentarios Clasificados como Positivo", comentarios_clasificados.get("Positivo", 0)],
    ["Total Comentarios Clasificados", comentarios_clasificados.get("Negativo", 0) + comentarios_clasificados.get("Positivo", 0)]

]

for columna, valor in valores:
    pdf.cell(95, 10, f"{columna}", 1)
    pdf.cell(95, 10, f"{valor}", 1, ln=1)

# Insertar nube de palabras
pdf.add_page()
pdf.cell(0, 10, "Representación de los comentarios como una Nube de Palabras", 0, 1, 'C')
pdf.image(wordcloud_path, x=10, y=30, w=190)
os.remove(wordcloud_path)

# Obtener la posición vertical actual
pos_actual_y = pdf.get_y()

# Establecer un desplazamiento de, por ejemplo, 10 líneas hacia abajo
desplazamiento = 120  # Puedes ajustar este valor según el espacio que necesites

# Mover el cursor hacia abajo desde la posición actual
pdf.set_y(pos_actual_y + desplazamiento)

#pdf.add_page()

# Guardamos como un listado de datos las variables categoricas
columnas_categoricas = [
    'channel_title', 'evento', 'tipo_evento', 'condiciones_cuenta', 
    'contiene_insulto'
]

# Convertimos columnas de fechas
df_inicial['comment_time'] = pd.to_datetime(df_inicial['comment_time'])
df_inicial['video_published_at'] = pd.to_datetime(df_inicial['video_published_at'])

# Eliminamos comentarios neutros (polarity == 0)
df_inicial = df_inicial[df_inicial['polarity'] != 0]

# Obtenemos el rango de fechas
inicio = df_inicial['comment_time'].min()
final = df_inicial['comment_time'].max()
pdf.chapter_body(f"Análisis de los comentarios desde {inicio} hasta {final}")

# Creamos columna temporal agrupada (mensual)
df_inicial['month'] = df_inicial['comment_time'].dt.to_period('M')

# Calculamos promedio de polarity por mes
temporal_trend = df_inicial.groupby('month')['polarity'].mean()

# Calculamos volúmenes por período
temporal_data = df_inicial.groupby('month').agg(
    mean_polarity=('polarity', 'mean'),
    count_positive=('polarity', lambda x: (x > 0).sum()),
    count_negative=('polarity', lambda x: (x < 0).sum())
).reset_index()

# Convertimos a formato datetime para graficar
temporal_data['month'] = temporal_data['month'].dt.to_timestamp()

# Crear gráfico de comentarios positivos y negativos
fig, ax = plt.subplots(figsize=(14, 7))
color_positive = 'tab:green'
color_negative = 'tab:red'
ax.set_xlabel('Fecha', fontsize=12)
ax.set_ylabel('Cantidad de Comentarios', fontsize=12)
sns.lineplot(data=temporal_data, x='month', y='count_positive', marker='o', label='Positivos', color=color_positive, ax=ax)
sns.lineplot(data=temporal_data, x='month', y='count_negative', marker='o', label='Negativos', color=color_negative, ax=ax)
ax.tick_params(axis='y')
fig.suptitle('Volumen de Comentarios Positivos y Negativos', fontsize=16)
fig.tight_layout()
ax.legend(loc='upper right', bbox_to_anchor=(0.99, 1), title="Volumen de Comentarios")

# Guardar el gráfico como imagen
image_path = 'temp_image_1.png'
plt.savefig(image_path)
plt.close()

# Añadir imagen al PDF
pdf.add_image(image_path)

# Crear gráfico de la polaridad promedio
fig, ax1 = plt.subplots(figsize=(14, 7))
color = 'tab:blue'
ax1.set_xlabel('Fecha', fontsize=12)
ax1.set_ylabel('Promedio de Polarity', color=color, fontsize=12)
sns.lineplot(data=temporal_data, x='month', y='mean_polarity', marker='o', label='Promedio de Polarity', color=color, ax=ax1)
ax1.tick_params(axis='y', labelcolor=color)
ax1.grid(visible=True, linestyle="--", alpha=0.7)

# Crear segundo eje compartido para cantidad de comentarios positivos y negativos
ax2 = ax1.twinx()
color_positive = 'tab:green'
color_negative = 'tab:red'
ax2.set_ylabel('Cantidad de Comentarios', fontsize=12)
sns.lineplot(data=temporal_data, x='month', y='count_positive', marker='o', label='Positivos', color=color_positive, ax=ax2)
sns.lineplot(data=temporal_data, x='month', y='count_negative', marker='o', label='Negativos', color=color_negative, ax=ax2)
ax2.tick_params(axis='y')

# Título y leyenda
fig.suptitle('Evolución del Sentimiento y Volumen de Comentarios', fontsize=16)
fig.tight_layout()
ax1.legend(loc='upper left', bbox_to_anchor=(0.01, 1), title="Promedio de Polarity")
ax2.legend(loc='upper right', bbox_to_anchor=(0.99, 1), title="Volumen de Comentarios")

# Guardar el gráfico como imagen
image_path = 'temp_image_2.png'
plt.savefig(image_path)
plt.close()

# Añadir imagen al PDF
pdf.add_image(image_path)

# Insertar gráfico temporal
#pdf.add_page()
# Obtener la posición vertical actual
pos_actual_y = pdf.get_y()

# Establecer un desplazamiento de, por ejemplo, 10 líneas hacia abajo
desplazamiento = 120  # Puedes ajustar este valor según el espacio que necesites

# Mover el cursor hacia abajo desde la posición actual
pdf.set_y(pos_actual_y + desplazamiento)

#pdf.cell(0, 10, "Análisis Temporal: Comentarios por Semana", 0, 1, 'C')
fig.suptitle('Evolución del Sentimiento y Volumen de Comentarios por semana', fontsize=16)
pdf.image(temporal_analysis_path, x=10, y=140, w=190)
os.remove(temporal_analysis_path)

pdf.add_page()  # Nueva página antes de los comentarios
pdf.cell(0, 10, "Análisis Estadístico: Análisis de significación estadística entre el inicio y el final del periodo", 0, 1, 'C')

# Comparación estadística (t-test y Mann-Whitney)
midpoint = inicio + (final - inicio) / 2
inicio_periodo = df_inicial[df_inicial['comment_time'] < midpoint]['polarity']
final_periodo = df_inicial[df_inicial['comment_time'] >= midpoint]['polarity']

# Descripción de los datos
descripcion_inicio = inicio_periodo.describe()
descripcion_final = final_periodo.describe()

# Añadir análisis estadístico al PDF
pdf.chapter_body(f"Inicio del período:\n{descripcion_inicio}\n")
pdf.chapter_body(f"\nFinal del período:\n{descripcion_final}\n")

# T-test
t_stat, p_value = ttest_ind(inicio_periodo, final_periodo, equal_var=False)
pdf.chapter_body(f"T-test: t={t_stat}, p={p_value}\n")

# Mann-Whitney U
u_stat, p_value = mannwhitneyu(inicio_periodo, final_periodo)
pdf.chapter_body(f"Mann-Whitney U: u={u_stat}, p={p_value}\n")

# Obtener la posición vertical actual
pos_actual_y = pdf.get_y()

# Establecer un desplazamiento de, por ejemplo, 10 líneas hacia abajo
desplazamiento = 3  # Puedes ajustar este valor según el espacio que necesites

# Mover el cursor hacia abajo desde la posición actual
pdf.set_y(pos_actual_y + desplazamiento)

# Insertar comentarios adicionales
comentario_adicional = """
Interpretación de los resultados.

0. Inicio del periodo:
Media (mean): 0.1146 -> Esto indica que, en promedio, los comentarios del inicio tienen un sentimiento levemente positivo.
Mediana (50%): 0.115 -> Similar a la media, muestra que la distribución está centrada en valores ligeramente positivos.
Desviación estándar (std): 0.4158 -> La variabilidad en los sentimientos es moderada; algunos comentarios son extremadamente positivos (máximo: 1) y otros extremadamente negativos (mínimo: -1).

1. Final del periodo:
Media (mean): 0.1398 -> El promedio de sentimiento es algo más positivo al final.
Mediana (50%): 0.1364 -> Esto refuerza la ligera inclinación hacia lo positivo.
Desviación estándar (std): 0.4243 -> La variabilidad es similar al inicio.

Conclusión descriptiva:
Hay un leve aumento en el promedio de los sentimientos hacia el final del periodo (de 0.1146 a 0.1398), pero también una ligera dispersión mayor. El cambio parece pequeño a nivel descriptivo.

2. Resultados estadísticos
T-test (prueba t para medias):
t = -6.703: Este valor negativo refleja que la media del grupo inicial es menor que la del grupo final.
p = 2.06e-11: Este p-value es mucho menor que 0.05, lo que indica que el cambio en las medias es estadísticamente significativo.
"""
pdf.multi_cell(0, 10, comentario_adicional)

# Guardar el PDF
pdf.output(output_pdf_path)

# Limpiar imágenes temporales
os.remove('temp_image_1.png')
os.remove('temp_image_2.png')

print(f"Informe generado en: {output_pdf_path}")
