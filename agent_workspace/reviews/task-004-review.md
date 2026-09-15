# Review task-004 — Rights-Ledger MVP

**Critic verdict: PASS** (with two non-blocking observations)
**Date:** 2026-09-15 (EDT) · **Role:** Critic

## Independent verification

1. **Catalog coverage — PASS.** Ledger contains the 9 current catalog works (el-zarco-parte-i/ii/iii, los-de-abajo, navidad-en-las-montanas, la-suave-patria, poesia-selecta-sor-juana, cartucho, el-plano-oblicuo) plus 21 entries matching the task-003 shortlist candidates (Sor Juana ×3, Nezahualcóyotl, Popol Vuh, Huehuetlatolli, Códice Florentino, Periquillo, Prieto, Azuela, Campobello, Nahui Olin, Castellanos, Poniatowska, Sabines, Vasconcelos, Ramos, Zea, Paz, Rulfo, indigenous poetry selección, Anzaldúa). Every task-003 shortlist row is represented.
2. **Count and uniqueness — PASS.** Exactly 30 entries; 30 unique workIds; 30 unique (workId, title) pairs; no duplicates.
3. **Five rights layers — PASS.** Every entry has exactly {underlyingWork, edition, translation, transcription, recording}; every layer has status ∈ {cleared, restricted, unknown} (all currently `unknown`), non-empty territories (MX/US), evidenceUrl (string|null), and reviewDue present. No missing or extra layers.
4. **Safe unknowns / no license misrepresentation — PASS.** All statuses are `unknown`; license fields are null or "unknown" everywhere (entry and layer level); no source URL (Wikisource, Cervantes Virtual discovery catalog) is asserted as a license. Notes consistently state unknown blocks publication.
5. **Translation records — PASS.** Entries with translated/bilingual expression (poemas-nezahualcoyotl, popol-vuh, huehuetlatolli, codice-florentino-selecciones, arte-poesia-indigena) carry translation objects with translator, languageConsultant, sourceLanguage, targetLanguage, translationStatus — all set to null/"unknown" pending verification, which is the correct safe default.
6. **Jurisdiction flags — PASS.** `la-suave-patria` (López Velarde, d. 1921) and `el-plano-oblicuo` (Reyes, d. 1959) are the only two entries with `legalReviewRequired: true`, both with notes citing jurisdiction/term uncertainty and requiring legal review before publication or recording. (All rights layers still unknown, so no other entry can publish anyway.)
7. **JSON + Schema validation — PASS.** Independently re-validated: `jsonschema.validate(doc, schema)` with Draft 2020-12 → 0 errors; ledger parses as valid JSON.
8. **No production files changed — PASS.** `git status` shows changes only under `agent_workspace/` (plus pre-existing untracked `plans/`). No production file (index.html, sw.js, netlify/*, audio/*, assets/*, android/*) modified or newer than prior task artifacts. No commit or push performed.
9. **Scope and task state — PASS.** All touched files are within `scope.allowedFiles` of task-004.json. History shows queued → researched (29 entries, Zarco III gap flagged) → built (Zarco III added, 30 entries) — consistent with artifacts.

## Non-blocking observations
- **Visión de Anáhuac** (Reyes) and **Pedro Páramo** (Rulfo) appear in the task-003 shortlist only as slash-listed alternates ("Visión de Anáhuac, El plano oblicuo"; "El Llano en llamas / Pedro Páramo"); the ledger registers one primary work per author-row. If either alternate is later selected, a new entry must be added before any rights work begins.
- `research/task-004-research.md` still says "29 entradas"; the actual ledger now has 30 after the Builder added El Zarco Parte III (build doc correctly reports 30). Cosmetic only.
- `el-zarco-parte-iii` has null sourceUrl/sourceInstitution — correctly so, since only an audio asset exists, but it must be filled if a text source is ever attached.

## Conclusion
The ledger is a faithful, publication-safe MVP: 30 entries, five unknown (blocking) layers each, no invented licenses, correct legal-review flags, valid against its schema, and no production changes. Critic issues **PASS**. Per the ledger's own rule, every layer remains non-publishable until evidence upgrades status from `unknown`.
