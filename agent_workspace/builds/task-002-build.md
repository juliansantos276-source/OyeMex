# Build task-002

## Extracción y fuente
- URL exacta: https://es.wikisource.org/wiki/El_Zarco/Cap%C3%ADtulo_III (HTTP 200).
- Comando: `curl -L -A 'Mozilla/5.0' -o /tmp/c3.html 'https://es.wikisource.org/wiki/El_Zarco/Cap%C3%ADtulo_III'`.
- Método: script Python con `html.parser`/regex sobre el HTML público; seleccioné `<p>` desde el primer `<p>` cuyo texto empieza `En el patio interior...` hasta el cierre del contenido, antes de la navegación. Se conservaron exclusivamente los 52 párrafos del cuerpo; salida temporal `/tmp/c3.txt`, 18,626 caracteres. El último párrafo termina `...en ese tiempo en Yautepec.`

## Audio
- Chunks: 8, todos <=3200 caracteres (máximo 3,148).
- Comando por chunk: `edge-tts --voice es-MX-JorgeNeural --rate=-4% --text "$(cat chunk)" --write-media chunk.mp3`.
- Concatenación con ffmpeg de imageio_ffmpeg: `FF=$(python3 -c 'import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())'); $FF -f concat -safe 0 -i /tmp/list.txt -c copy /tmp/c3.mp3`.
- Metadatos: ffmpeg `-metadata title='El Zarco · Parte III' -metadata artist='Ignacio Manuel Altamirano' -metadata album='OyeLoMex'`, recodificado a 64 kb/s.
- Evidencia: ffmpeg reportó `Duration: 00:20:44.40`, MP3 mono 24 kHz, 64 kb/s. Catálogo usa `20m 44s`.

## Archivos cambiados
- `audio/elzarco_cap3.mp3` (nuevo).
- `index.html` (nueva ficha El Zarco · Parte III; audioSrc y URL verificada exactos).
- `agent_workspace/builds/task-002-build.md`.
- `agent_workspace/tasks/task-002.json`.

## Pruebas
- `node --check /tmp/oyelomex-task-002.js` (script extraído de la etiqueta script): PASS.
- `git diff --check`: PASS.
- Servidor local `python3 -m http.server` bajo `oyelomex`: página `/index.html` HTTP 200 y `/audio/elzarco_cap3.mp3` HTTP 200.
- No se modificaron `audio/elzarco_cap1.mp3` ni `audio/elzarco_cap2.mp3`; no commit, push ni deploy.
