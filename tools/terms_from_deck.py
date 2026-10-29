"""Build a review page's terms include from a deck's "Definitions from this lecture" slides.
usage: python3 tools/terms_from_deck.py ../2026w1-slides/slides/l11.qmd _terms/page-l11.md"""
import re, sys
deck, out = sys.argv[1], sys.argv[2]
s = open(deck).read()
parts = []
for m in re.finditer(r'(?ms)^## Definitions from this (?:lecture|part)[^\n]*\n(.*?)(?=^#{1,2} )', s):
    body = re.sub(r'::: notes.*?\n:::', '', m.group(1), flags=re.S)
    if 'this part' in m.group(0).split('\n', 1)[0] and not re.search(r'(?m)^\*\*.+\*\*\s*$', body):
        # a part's slide with no group label takes the title of the block divider above it
        div = re.findall(r'(?m)^# (Block \d+: .+?) \{#', s[:m.start()])
        if div:
            parts.append(f"### {re.sub(r'^Block \d+: ', '', div[-1])[:1].upper()}{re.sub(r'^Block \d+: ', '', div[-1])[1:]}\n")
    for line in body.split('\n'):
        h = re.match(r'^\*\*(.+?)\*\*\s*$', line.strip())
        b = re.match(r"^- \*\*(.+?)\*\*((?:\s*\([^)]*\))?):\s*(.*)$", line.strip())
        if h:
            parts.append(f"### {h.group(1).replace('🔍 ', '')}\n")
        elif b:
            term, extra, d = b.groups()
            d = d.rstrip('.')
            parts.append(f"**{term}**{extra}. {d[0].upper()}{d[1:]}.\n")
open(out, 'w').write('\n'.join(parts))
print(out, sum(p.startswith('**') for p in parts), 'terms')
