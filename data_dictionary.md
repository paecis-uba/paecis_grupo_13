# Diccionario de Datos

Este documento proporciona una descripción de las variables presentes en el dataset de comentarios de YouTube.

| **Variable**           | **Tipo de Dato** | **Descripción**                                            |
|------------------------|------------------|------------------------------------------------------------|
| `comment_id`           | String           | Identificador único del comentario.                        |
| `comment`              | String           | Texto completo del comentario realizado por el usuario.    |
| `user_id`              | String           | Identificador único del usuario que dejó el comentario.    |
| `user_name`            | String           | Nombre de usuario que comentó.                             |
| `comment_time`         | String           | Hora en la que se dejó el comentario.                      |
| `comment_likes`        | Integer          | Cantidad de "me gusta" que recibió el comentario.          |
| `total_reply_count`    | Integer          | Número total de respuestas que tiene el comentario.        |
| `is_top_level_comment` | Boolean          | Indica si el comentario es un comentario de nivel superior (sin respuestas). |
| `video_title`          | String           | Título del video al que pertenece el comentario.           |
| `channel_title`        | String           | Nombre del canal de YouTube que publicó el video.          |
| `video_published_at`   | String           | Fecha y hora en que el video fue publicado.                |
| `video_views`          | Integer          | Número total de vistas del video.                          |
| `video_likes`          | Integer          | Número total de "me gusta" que recibió el video.           |
| `relacion_evento`      | String           | Relación del comentario con un evento específico.          |
| `evento`               | String           | Nombre del evento asociado al comentario.                  |
| `tipo_evento`          | String           | Tipo de evento al que se refiere el comentario.            |
| `condiciones_cuenta`   | String           | Condiciones asociadas a la cuenta de youtube (favorable o no con Milei). |
| `duration_timedelta`   | String           | Duración del video en formato `timedelta` (diferencia de tiempo). |
| `duration_seconds`     | Float            | Duración del video en segundos.                            |
| `translated_text`      | String           | Texto del comentario traducido (usado para en sentiment analisis).                |
| `polarity`             | Float            | Polaridad del comentario: valor numérico que indica si es positivo, negativo o neutral. de 1 a -1 |
| `Sentimiento`          | String           | Sentimiento clasificado del comentario (positivo, negativo, neutral). |
| `contiene_insulto`     | String           | Indica si el comentario contiene insultos.                 |

## Notas:
- Las variables con tipo `String` contienen texto libre.
- Las variables con tipo `Integer` son números enteros.
- Las variables con tipo `Float` contienen valores numéricos con decimales.
- La variable `is_top_level_comment` es un valor booleano (`True`/`False`).
