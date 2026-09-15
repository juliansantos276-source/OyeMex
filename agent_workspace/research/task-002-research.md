# Investigación task-002 — *El Zarco*, capítulo III

**Fecha de consulta:** 2026-09-14/15 EDT  
**Rol:** Researcher  
**Estado:** investigación completa; `task-002.json` se deja sin modificar en `queued/currentRole: researcher` para que el orquestador haga la transición formal a Builder.

## Fuente primaria verificada
- **URL exacta de lectura:** https://es.wikisource.org/wiki/El_Zarco/Cap%C3%ADtulo_III
- **Respuesta observada:** HTTP 200, `text/html`, título *El Zarco/Capítulo III* (consulta mediante `web_fetch`, 2026-09-15 00:15 UTC aprox.).
- **Evidencia textual:** la página comienza exactamente: “En el patio interior de una casita pobre pero de graciosa apariencia, que estaba situada a las orillas de la población y en los bordes del río, con su respectiva huerta de naranjos, limoneros y platanares, se hallaba tomando el fresco una familia compuesta de una señora de edad y de dos jóvenes muy hermosas, aunque de diversa fisonomía.” Continúa con la descripción de Manuela y Pilar y el diálogo de Doña Antonia sobre los “plateados”, Yautepec y los peligros de la región. Esto confirma que la URL corresponde al capítulo, no a un índice vacío.
- `https://es.wikisource.org/wiki/El_Zarco/III` **no es fuente válida**: responde con página 200 pero indica “En este momento no hay texto en esta página”. No usarla.

## Límites/extracción
El capítulo debe extraerse **únicamente del contenido textual de la página `El_Zarco/Capítulo_III`**, desde el primer párrafo que comienza “En el patio interior…” hasta el último párrafo del capítulo en esa misma página, excluyendo la navegación, encabezados, notas de Wikisource y enlaces de navegación a capítulos vecinos. La captura de lectura devolvió 14.2 KB de texto legible y fue truncada por el límite de consulta; por ello Builder debe descargar/extraer la página completa (HTML o exportación de texto/Wikitext) y guardar una copia de trabajo temporal fuera de los archivos permitidos, o usar un extractor HTML reproducible. No inventar un cierre a partir del fragmento visible. Verificar al final que el texto termina antes del enlace al capítulo IV y conservar acentos, diálogos y puntuación.

La solicitud directa a la API MediaWiki desde el entorno respondió 403; eso no invalida la página pública HTML (HTTP 200), pero sí hace recomendable que Builder use la página HTML/exportación disponible y documente el comando/método exacto. La URL `?printable=yes` puede servir para una extracción más limpia, siempre que se vuelva a comprobar el mismo comienzo y el límite final.

## Derechos y publicación
Ignacio Manuel Altamirano falleció en 1893; la obra original es presumiblemente de dominio público, pero Wikisource es una fuente de lectura y no una garantía automática de que toda edición, transcripción, prólogo, anotación o formato moderno tenga idénticos derechos. Para narración basada en el texto original, mantener atribución a Ignacio Manuel Altamirano y enlazar la página fuente. No redistribuir una edición moderna escaneada/anotada sin revisar su licencia. El MP3 es una nueva grabación OyeLoMex, no el audio de Wikisource; la procedencia/licencia declarada para audios existentes (`Biblioteca Digital ILCE · grabación OyeLoMex`) no fue independientemente demostrada en esta fase.

## Contexto local del proyecto
- `index.html` contiene dos fichas existentes: *El Zarco · Parte I* y *El Zarco · Parte II*, ambas con `textUrl` Wikisource a capítulos I/II, y ambas con `audioSrc` local.
- Convención prevista para el nuevo archivo: `audio/elzarco_cap3.mp3`; no existe todavía.
- Audios existentes sin modificar: `audio/elzarco_cap1.mp3` y `audio/elzarco_cap2.mp3`, ambos MP3 mono, 24 kHz, 64 kbps, aprox. 9.5 MB.
- Commits recientes muestran que se añadieron enlaces de lectura y se publicó el catálogo base; el código ya renderiza enlaces de texto condicionalmente y el reproductor toma la duración real del elemento Audio. Builder debe confirmar que no se afirma una duración fija falsa.

## Recomendación de producción
1. Builder obtiene el HTML/texto completo de la URL verificada y delimita capítulo III por su encabezado/contenido, no por una aproximación de caracteres.
2. Narrar en español mexicano, respetando ortografía y diálogos; revisar manualmente nombres propios (Manuela, Pilar, Doña Antonia, Nicolás, Yautepec, Xochimancas, plateados).
3. Generar `audio/elzarco_cap3.mp3` mediante el pipeline de voz ya usado para capítulos I/II; no alterar esos archivos.
4. Añadir ficha “El Zarco · Parte III” con `audioSrc: "audio/elzarco_cap3.mp3"`, `textUrl` exactamente igual a la URL de arriba y duración basada en metadatos/HTMLMediaElement tras generación, no una estimación declarada.
5. Registrar en Build/Critic: URL, método de extracción, evidencia de duración (`ffprobe` o `audio.duration`), archivos cambiados y pruebas locales. No publicar sin aprobación y sin PASS del Critic.

## Fuentes locales consultadas
- `agent_workspace/tasks/task-002.json` (alcance y criterios de aceptación).
- `agent_workspace/research/task-001-research.md` (convención de catálogo y advertencias de derechos).
- `index.html` (catálogo, enlaces de texto, reproductor).
- `audio/elzarco_cap1.mp3`, `audio/elzarco_cap2.mp3` (contexto técnico; no modificados).
