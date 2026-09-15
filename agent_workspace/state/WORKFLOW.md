# Flujo del equipo

`queued → researching → researched → building → built → reviewing → passed/failed → approved → published`

- Researcher: `queued → researching → researched`
- Builder: `researched → building → built`
- Critic: `built → reviewing → passed/failed`
- Orchestrator: `passed → approved → published`

Un FAIL vuelve a `building` con una lista de correcciones. La publicación es una acción separada y requiere aprobación del Orchestrator.
