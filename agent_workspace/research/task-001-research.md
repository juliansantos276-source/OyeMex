# Investigación task-001 — catálogo legible y fuentes verificadas

Fecha de consulta: 2026-09-14/15 (EDT). Investigador: Researcher.

## Resumen ejecutivo
El catálogo existente contiene nueve fichas. Sólo tres incluyen `textUrl`: dos capítulos de *El Zarco* y las *Redondillas* de Sor Juana; las seis restantes no ofrecen enlace de lectura. La interfaz ya abre `textUrl` en pestaña nueva con `target="_blank"` y `rel="noopener"`, y no muestra controles de audio cuando `audioSrc` es nulo. Se verificó que las tres URL actuales responden HTTP 200 y contienen texto legible. Recomiendo conservarlas como fuentes primarias de lectura, separar explícitamente hechos bibliográficos de copy editorial y ampliar el catálogo únicamente con URLs comprobadas individualmente. No debe inferirse que una página de acceso libre equivale automáticamente a una licencia para redistribuir su edición.

## Fuentes y hechos verificados
### Fuentes actualmente usadas
1. Wikisource, *El Zarco/Capítulo I*: https://es.wikisource.org/wiki/El_Zarco/Cap%C3%ADtulo_I (consulta HTTP 200; título “El Zarco/Capítulo I”; comienza “Yautepec es una población…”; texto HTML visible).
2. Wikisource, *El Zarco/Capítulo II*: https://es.wikisource.org/wiki/El_Zarco/Cap%C3%ADtulo_II (HTTP 200; título correcto; comienza situando la escena “un día de agosto de 1861”; texto visible).
3. Wikisource, *Redondillas*: https://es.wikisource.org/wiki/Redondillas (HTTP 200; contiene el poema y el comienzo “Hombres necios que acusáis…”).
4. Biblioteca Virtual de las Letras Mexicanas, catálogo: https://www.letrasmexicanas.mx/catalogo_titulo/ (HTTP 200; el sitio se describe como catálogo de obras; la página consultada muestra 7.120 resultados y formatos HTML/“Leer obra”). Es un buen índice para investigación posterior, no una URL concreta a añadir sin revisar obra, autor y derechos.
5. Biblioteca Virtual Miguel de Cervantes, materia literatura mexicana: https://www.cervantesvirtual.com/obras/materia/literatura-mexicana-526/?p=1 (resultado público de catálogo; requiere seleccionar y verificar cada registro).
6. UNAM Material de Lectura: https://materialdelectura.unam.mx/ e índices https://materialdelectura.unam.mx/indices (portal institucional con textos/selecciones; las ediciones contemporáneas pueden tener derechos vigentes).

### Estado observado en `index.html`
- Fichas: *El Zarco · Parte I* (Ignacio Manuel Altamirano, 1900), *El Zarco · Parte II* (Altamirano, 1900), *Los de abajo* (Mariano Azuela, 1915), *Navidad en las montañas* (Altamirano, 1871), *La Suave Patria* (Ramón López Velarde, 1921), *Poesía selecta de Sor Juana* (Sor Juana Inés de la Cruz, 1692), *Cartucho* (Nellie Campobello, 1931), *El plano oblicuo* (Alfonso Reyes, 1920), *El diablo desinteresado* (Amado Nervo, 1916).
- Los años/autoría son los metadatos declarados por el proyecto y deben etiquetarse como “año de primera publicación/edición” sólo tras confirmar la convención editorial exacta.
- “MÉXICO PROFUNDO” aparece en fichas pero no como botón de categoría; es una inconsistencia de taxonomía a resolver.
- `source` de los audios dice “Biblioteca Digital ILCE · grabación OyeLoMex”; no se investigó aquí evidencia pública suficiente para validar la procedencia/licencia del audio.

## Hechos vs. supuestos
**Verificados:** las tres URLs de Wikisource son accesibles y contienen el texto correspondiente; el código sólo genera el botón “Leer texto completo” si existe `textUrl`; el audio sólo se ofrece cuando existe `audioSrc`.

**Supuestos/no verificados:** que 1900 sea el año correcto de la edición concreta de *El Zarco*; que cada ficha tenga una fuente pública concreta; que los textos/ediciones de Wikisource puedan copiarse o redistribuirse bajo una licencia determinada; que “Biblioteca Digital ILCE” sea la fuente del archivo MP3 actual; que las frases `excerpt`, `whyListen` y `desc` sean citas documentales (deben tratarse como copy editorial salvo fuente).

## Dominio público y derechos
Las fechas de fallecimiento pueden hacer probable el dominio público de varias obras, pero no bastan para autorizar la copia de una edición moderna, traducción, prólogo, anotación, transcripción o grabación. Wikisource es una fuente de lectura pública, no por sí sola una garantía universal de licencia; revisar la página de obra y su historial/licencia antes de reutilizar contenido. Sor Juana y Altamirano son autores históricos con obras presumiblemente en dominio público; Campobello, López Velarde, Reyes, Nervo, Azuela y otros requieren revisión jurisdiccional y de la edición específica. Mantener enlaces externos en vez de descargar/republicar el texto reduce riesgo.

## Metadatos propuestos para nuevas fichas
Usar campos separados: `title`, `author`, `year` (con etiqueta “año de primera publicación” o “año de edición consultada”), `period/category` (taxonomía controlada), `desc`/`whyListen` (ficha editorial), `textUrl` (fuente primaria concreta), `textSourceName`, `textAccessCheckedAt`, `rightsNote`, `audioSrc` sólo si existe audio autorizado, y opcional `audioStatus`. No añadir `textUrl` por dominio o buscador: debe ser una URL de obra/capítulos que cargue y corresponda al título.

## Riesgos y preguntas pendientes
- Confirmar bibliografía y años con catálogos institucionales (UNAM, Cervantes Virtual, Biblioteca Nacional) antes de afirmar “año”.
- Obtener evidencia de licencia/procedencia de MP3; no presentar audio como “de dominio público” sin documentación.
- Revisar si las URLs de Wikisource siguen estables y si cubren texto completo o sólo capítulo.
- Decidir si se incorporan enlaces a Cervantes/UNAM para *Los de abajo*, *Navidad…*, *La Suave Patria*, *Cartucho*, *El plano oblicuo* y *El diablo desinteresado*; cada uno necesita registro exacto y derechos.
- Corregir o documentar la categoría “MÉXICO PROFUNDO” para que sea filtrable, o cambiarla por una categoría existente.

## Recomendación para Builder/Critic
1. No inventar fuentes ni completar enlaces por aproximación.
2. Mantener los tres enlaces verificados, con nombre de fuente y fecha de comprobación en datos internos o documentación.
3. Añadir obras sólo después de prueba HTTP y revisión visual del texto; usar pestaña nueva y `noopener`.
4. Etiquetar hechos bibliográficos frente a descripción editorial en la ficha.
5. Ejecutar validación sintáctica local de HTML/JS y registrar salida; el Critic debe emitir PASS antes de publicar.

## Pruebas de investigación reproducibles
- `web_fetch` de las tres URLs de Wikisource: HTTP 200 y texto correspondiente.
- `web_fetch` de catálogo Letras Mexicanas: HTTP 200, catálogo con 7.120 resultados.
- Inspección local: `grep -n "textUrl\|modalContent\|openWorkModal" index.html` confirmó enlaces sólo en las tres fichas y render condicional del enlace.
