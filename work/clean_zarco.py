#!/usr/bin/env python3
"""Clean El Zarco raw PDF text and emit ordered paragraphs for TTS."""
import re

RAW = "zarco_raw.txt"
OUT_TXT = "zarco_clean.txt"
PILOT_CHARS = 26000   # ~ first part of the novel for the pilot (≈ 20-25 min)

def drop_noise(t):
    t = t.strip()
    if not t:
        return True
    if re.fullmatch(r"\d{1,4}", t):                       # page numbers
        return True
    if "http://" in t or "bibliotecadigital" in t:        # footer/URL
        return True
    if re.match(r"^0[aá]", t):                            # '0á' artifact
        return True
    return False

def main():
    raw_lines = open(RAW, encoding="utf-8").read().split("\n")

    # Start content at the opening section heading "Yautepec"
    start = 0
    for i, ln in enumerate(raw_lines):
        if ln.strip() == "Yautepec":
            start = i
            break
    body = raw_lines[start:]

    # Merge runs of non-empty lines into paragraphs; keep blank-line breaks.
    paragraphs = []
    buf = []
    for ln in body:
        s = ln.replace("\u00ad", "").strip()   # strip soft hyphens
        if drop_noise(s):
            if buf:
                paragraphs.append(" ".join(buf))
                buf = []
            continue
        buf.append(" ".join(s.split()))
    if buf:
        paragraphs.append(" ".join(buf))

    # Take paragraphs until we hit the pilot char budget
    pilot = []
    used = 0
    for p in paragraphs:
        if used + len(p) > PILOT_CHARS and pilot:
            break
        pilot.append(p)
        used += len(p)

    out = "\n\n".join(pilot)
    open(OUT_TXT, "w", encoding="utf-8").write(out)
    print(f"clean paragraphs used: {len(pilot)}, pilot chars total: {len(out)}")

    print("\n--- HEAD ---")
    print(pilot[0][:320])
    print("\n--- TAIL ---")
    print(pilot[-1][:320])

if __name__ == "__main__":
    main()