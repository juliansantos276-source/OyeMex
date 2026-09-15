# Investigación task-004 — Rights Ledger MVP

**Fecha:** 2026-09-15 (EDT) · **Rol:** Researcher

## Cobertura
El ledger contiene las nueve fichas actuales del catálogo y las veinte obras/candidatos propuestos en task-003 (30 entradas tras añadir El Zarco · Parte III en la fase Builder). Cada entrada incluye metadatos bibliográficos, idioma/variante, territorios MX/US, traducción cuando aplica, y capas separadas para obra subyacente, edición, traducción, transcripción y grabación.

## Fuentes
Se conservaron las fuentes concretas verificadas en task-001 para *El Zarco* (capítulos I y II) y *Redondillas* de Wikisource. Para los demás registros se usa el catálogo de descubrimiento de Biblioteca Virtual Miguel de Cervantes; también informaron la investigación los catálogos Letras Mexicanas/UNAM, BNM, UNESCO, DILA, Library of Congress y WIPO, enumerados en task-003. Ninguna fuente de catálogo se trata como licencia automática.

## Incertidumbres y política segura
Los estados de todas las capas son `unknown` porque no se verificó una licencia/contrato específico por expresión, edición, traducción, transcripción o audio. Los campos no comprobados usan `unknown`, `null` o listas explícitas, y las notas indican que ello bloquea publicación. No se inventaron URLs de obras concretas ni contactos. Las fechas/idiomas/géneros de candidatos requieren verificación bibliográfica.

López Velarde y Alfonso Reyes tienen `legalReviewRequired: true` y notas explícitas de incertidumbre jurisdiccional/terminación; no deben distribuirse sin revisión legal territorial. Las expresiones indígenas, tradicionales o bilingües registran traductor y consultor lingüístico como desconocidos cuando corresponde; consentimiento, atribución y revisión comunitaria siguen pendientes.

## Validación
`python3 -m json.tool oyelomex/agent_workspace/state/rights-ledger.json` pasó. No se modificaron archivos de producción, ni se publicó, comprometió o envió nada.
