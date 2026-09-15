# OyeLoMex Cultural Library Roadmap — Strategy

**Status:** Built; ready for critic review. **Date:** 2026-09-15 EDT. This is an implementation proposal derived from the research and MASTER_PLAN; factual claims are cited in the research source URLs. Any unverified status is labeled **uncertainty**.

## Operating principles
- Build the smallest beautiful, audio-first library; public-domain-first (MASTER_PLAN).
- Separate a work from every edition, translation, transcription, and recording. No item becomes publishable from a catalog link alone.
- Present Mexico as plural: periods, regions, women, Indigenous and Afro-Mexican voices, diaspora, and dissenting traditions. Coverage targets below are **proposals**, not claims of completeness.
- AI may draft metadata; a human verifies every factual statement.

## Plan by horizon
### 0–3 months (P0: prove the safe loop)
1. Audit the nine existing fichas and normalize author/work IDs.
2. Build the rights ledger and evidence fields before ingesting media.
3. Clear a small pilot of 5–8 concrete public-domain candidates, proposed: *El Zarco* selections, Sor Juana selections, and *El Periquillo Sarniento*; confirm each edition, territory, and source first (**uncertainty**).
4. Produce 2–3 original, credited readings only after clearance; preserve transcript, pronunciation notes, checksum, and consent.
5. Ship author/work page templates, audio player (resume position), search facets, and one Camino: “Conoce México” (prototype).

### 3–6 months (P1: broaden and test)
1. Add chronological, regional, genre, and language coverage; proposed minimum: one Nahua sample with linguistic/community review and one women-authored work beyond Sor Juana.
2. Prototype *Caminos*: Conoce México, Aprende a Pensar México, México para Jóvenes, México y Estados Unidos. These are proposed editorial products.
3. Run a licensed pilot for one rights-active work (candidate Azuela, Castellanos, or Reyes; selection is **uncertain** until rights contacts respond).
4. Add transcript search, “¿Por qué escuchar esto?”, related works, and accessibility QA.
5. Commission a coverage review against the matrix below.

### 6–12 months (P2: licensed, multilingual, sustainable)
1. Negotiate publisher/author/estate/institution licenses for contemporary and rights-active authors.
2. Add Indigenous-language/bilingual audio only with informed consent, competent speakers, translation attribution, and community review.
3. Expand professional narration, compensation, and production standards; never infer permission from an online player.
4. Add diaspora and education partnerships, analytics, recommendations, and offline access only where licenses permit. These partnerships and sequencing are **proposals**.

## P0/P1/P2 work queue
| Priority | Work | Done when |
|---|---|---|
| P0 | Rights ledger + evidence review | Every candidate has work/edition/translation/transcription/recording statuses, territory, URL, reviewer, expiry |
| P0 | Catalog normalization | Stable IDs, authority IDs where available, deduplicated authors/works |
| P0 | 5–8 cleared pilot works | Clearance packet, source provenance, QA transcript, credited audio |
| P0 | Author/work/audio templates | Mobile page, playback resume, transcript, related items, accessibility checks |
| P0 | Search facets | Author, title, period, region, genre, theme, language, audio/rights status |
| P1 | Caminos + coverage dashboard | Each path has rationale, sequence, source links, and rights-safe items |
| P1 | Indigenous-language review process | Named advisor/community process, pronunciation/translation/consent evidence |
| P1 | First license pilot | Signed grant, territory/term/media/credit/compensation recorded |
| P2 | Living-author/estate catalog | Rights agreements before full text/audio; takedown and renewal process |
| P2 | Institutional/education/diaspora partnerships | Written scope, accessibility and data/rights responsibilities |

## Metadata schema (proposal)
Use stable `author_id`, `work_id`, `edition_id`, `translation_id`, `recording_id`, and `path_id`.

**Author:** `name`, `variants`, `birth_date`, `death_date`, `regions`, `languages`, `traditions`, `authority_ids`, `bio`, `portrait_rights`, `sources[]`, `reviewer`, `reviewed_at`.

**Work:** `title`, `variants`, `author_id`, `first_publication_date`, `period`, `regions[]`, `genres[]`, `themes[]`, `traditions[]`, `original_language`, `language_variant`, `extent`, `summary`, `why_listen`, `content_notes`, `age_guidance`, `sources[]`.

**Expression/edition:** `edition_id`, `work_id`, `publisher`, `edition_date`, `editor`, `source_url`, `source_institution`, `source_record_id`, `text_version`, `transcription_status`, `access_checked_at`.

**Translation (when applicable):** `translation_id`, `edition_id`, `source_language`, `target_language`, `translator`, `language_consultant`, `translation_date`, `translation_source`, `translation_status`, `rights_evidence_url`, `notes`. A translation is never treated as interchangeable with the underlying work.

**Rights (separate statuses):** `underlying_work_status`, `edition_status`, `translation_status`, `transcription_status`, `recording_status`; each supports `status` (cleared/restricted/unknown), `territories[]`, `evidence_url`, `contact`, `license`, `term`, `review_due`, `notes`.

**Recording:** `recording_id`, `work_or_expression_id`, `audio_status`, `performer`, `producer`, `recording_date`, `duration`, `file_checksum`, `audio_url`, `transcript_url`, `pronunciation_notes`, `consent_notes`, `credits`, `license`.

**Curation/audit:** `path_ids[]`, `confidence`, `factual_claim_sources[]`, `reviewer`, `last_reviewed`, `change_log`, `takedown_state`.

## Rights-clearance workflow
1. Identify the exact work, expression, edition/translation, territory, intended media, and term.
2. Verify author death/publication facts against institutional sources; **do not assume public domain** from age or a web copy.
3. Record separate statuses for underlying work, edition, translation, transcription, image, and recording.
4. Capture URL, institution, access date, license text/contract, contact, territory, term, attribution, and restrictions.
5. For Indigenous/oral material: identify language/variant, speaker/community authority, consent, compensation, cultural restrictions, translation and pronunciation review.
6. Legal/editorial reviewer signs a clearance packet; unresolved items remain `unknown` and unpublished.
7. Produce only from the cleared source; checksum files and retain provenance.
8. Publish credits, license/limits, transcript status, and takedown contact; review before expiry and honor takedowns.

## Author/work page architecture
**Author page:** identity/authority block; concise sourced bio; place and period; “why this person matters”; start-here work; works/audio; related authors, regions, traditions; sources and rights-safe portrait.

**Work page:** title/author/date; period/region/genre/language; short sourced description; prominent player + resume; duration; transcript when cleared; “¿Por qué escuchar esto?”; content notes; rights/access notice; related works and Caminos; citation/source and report issue control. Proposed UI, not an existing implementation.

## Search/filter taxonomy
- **Entities:** author, title, collection, Camino.
- **Facets:** period (Mesoamérica, Colonia, Independencia/19C, Revolución, 20C, contemporary), region (controlled Mexican regions plus border/diaspora), genre (novel, story, poetry, essay, chronicle, oral discourse, history, theatre—latter additions proposed), language/variant, themes (identity, family, migration, death, love, community, colonialism, class, Indigenous life), tradition, age/difficulty, audio/transcript availability, rights state.
- Search ranking proposal: exact title/author > facet match > curated relevance; never rank restricted media as playable.

## Caminos (proposals)
1. **Conoce México:** Indigenous/Mesoamerican contexts → New Spain → nation formation → Revolution → modern Mexico → today.
2. **Aprende a Pensar México:** essays, philosophy, cultural criticism, intellectual history.
3. **México para Jóvenes (12–18):** age-appropriate, contextualized selections; age guidance requires editorial review.
4. **México y Estados Unidos:** migration, border, identity, Mexican-American life; label diaspora distinctly.
Each path needs an editor, rationale, sequence, source list, rights-safe playable set, and coverage review.

## Audio production queue
- **P0:** 2–3 short cleared selections; one narrator/consistent room standard; transcript and pronunciation QA; master + web derivative + checksum.
- **P1:** 4–8 additional cleared works/selections; test multiple voices and accessibility; one reviewed Nahua-language sample (proposal, not guaranteed).
- **P2:** licensed living authors, bilingual Indigenous-language productions, professional narration, community compensation. Candidate titles are not commitments.
- Every recording packet: performer agreement, producer, script version, language consultant, consent, credits, license/territory/term, loudness/format QA, transcript, takedown path.

## Representation / coverage scorecard (proposal)
Review monthly; score each 0 absent, 1 present but thin, 2 represented with rights-safe depth, 3 strong with contextual plurality.
- Periods: Mesoamerican, colonial, 19C, Revolution, 20C, contemporary.
- Regions: center/CDMX, north/frontier, west, south/southeast, Gulf/coasts, diaspora.
- Gender: women, men, gender-diverse voices (where verified and respectfully self-described).
- Indigenous languages/communities and Afro-Mexican histories.
- Genres/forms: poetry, fiction, essay, chronicle, oral tradition, theatre, science/history.
- Traditions and viewpoints: Indigenous, colonial/Catholic, liberal/national, revolutionary, feminist, philosophical, dissenting.
- Rights depth: cleared text, edition, translation, transcription, recording—not just a catalog link.
Gate proposal: no Camino launch until no dimension is 0 without an explicit editorial rationale; publish a coverage note and gaps.

## Acceptance gates
1. **Evidence:** each factual claim has an institutional/source URL, or is labeled proposal/uncertainty.
2. **Rights:** all five rights layers have a status; playable material is cleared for territory/media/term.
3. **Representation:** scorecard reviewed; Indigenous/language claims receive qualified review; gaps are visible.
4. **Product:** mobile playback/resume, search facets, transcript/accessibility, stable IDs, source display, error/takedown route.
5. **Audio:** consent/contract, credits, checksum, transcript, technical QA.
6. **Editorial:** no propaganda framing; contextual notes distinguish colonial viewpoint, attribution uncertainty, and translation from original.
7. **Human sign-off:** Julian (or delegated rights/editorial authority) approves launch; unresolved uncertainty blocks publication.

## Autonomy boundaries
**Can be autonomous:** draft schema and metadata; deduplicate; suggest tags/paths; collect source URLs; create internal checklists; run file/checksum/accessibility QA; generate draft summaries clearly marked for review; report scorecard gaps.

**Requires Julian or explicitly authorized human:** legal rights conclusions, contacting/contracting rights holders, consent/compensation, publication approval, representing Indigenous/community authority, factual disputes, sensitive framing, spending, and any production/deployment change.

## Proposed first three implementation tasks
1. **Rights-ledger MVP:** create schema/storage and enter every current candidate with separate rights statuses, evidence URL, territory, reviewer, and `unknown` defaults; acceptance = no candidate missing a rights layer.
2. **Pilot catalog + page contract:** normalize 5–8 P0 records and implement author/work JSON fixtures/templates plus audio state model; acceptance = one end-to-end cleared work passes mobile, transcript, provenance, and takedown gates. Add a translation record whenever the selected expression is translated or bilingual.
3. **Afro-Mexican coverage plan:** identify candidate authors, works, archives, and an expert/community consultation route for the P1 coverage review; do not treat the scorecard dimension as complete until this plan exists.
4. **Discovery + Camino audit:** implement controlled facets and “Conoce México” draft; run representation scorecard and document gaps before publishing; acceptance = every path item has rationale, source, rights state, and human review owner.
5. **Jurisdiction-sensitive rights rows:** make López Velarde and Reyes explicit ledger cases with per-territory uncertainty, exact death/publication dates, and legal review before any playable release.

## Source and uncertainty note
Primary source URLs and rights notes are in `agent_workspace/research/task-003-research.md`, including Cervantes, Letras Mexicanas, UNAM, BNM, Wikisource, UNESCO, DILA, Library of Congress, and WIPO. They are discovery/context sources, not blanket permissions. All sequencing, thresholds, score values, candidate choices, and product designs in this document are proposals unless explicitly marked otherwise.
