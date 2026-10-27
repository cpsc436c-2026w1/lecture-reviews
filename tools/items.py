#!/usr/bin/env python3
"""Per-item short links ilm.wiki/436c/r<n>-<kk>, one per quiz block on a review page.

items.tsv is the registry. A link name is a permanent id, not a position: it is assigned once, in page order when a
page is first registered, and never renumbered or reused. A block added later takes the next free number wherever it
sits on the page; a block that is removed keeps its row with status 'retired' and its link points at the page.

    python3 tools/items.py check     anchors exist on the pages, every quiz block has a row, deck short links match
    python3 tools/items.py golinks   the ops/golink.sh add lines for every live and retired row
"""
import csv, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent.parent
DECKS = pathlib.Path('/Users/imusabirov/mds/436c/2026w1-slides/slides')
BASE = 'https://cpsc436c-2026w1.github.io/lecture-reviews'
rows = list(csv.DictReader(open(HERE / 'items.tsv'), delimiter='\t'))


def blocks(qmd):
    """Anchor of the heading above each quizdown block, in page order."""
    out, h = [], None
    for line in qmd.read_text().splitlines():
        m = re.match(r'^#{2,3} .*\{#([\w-]+)\}', line)
        if m:
            h = m.group(1)
        if line.startswith('```quizdown') and h not in out:
            out.append(h)
    return out


def check():
    bad = 0
    for page in sorted({r['page'] for r in rows}):
        qmd = HERE / page.replace('.html', '.qmd')
        mine = [r for r in rows if r['page'] == page]
        if not qmd.exists():
            if any(r['status'] != 'planned' for r in mine):
                print(f'✗ {page}: no source, but rows are not planned'); bad += 1
            continue
        have = blocks(qmd)
        reg = {r['anchor'] for r in mine if r['status'] != 'retired'}
        for a in sorted(reg - set(have)):
            print(f'✗ {page}: registry anchor #{a} is not a quiz block on the page'); bad += 1
        for a in have:
            if a not in reg:
                print(f'✗ {page}: quiz block #{a} has no row (give it the next free number)'); bad += 1
    by_slide = {s: r['link'] for r in rows for s in r['deck_slide'].split(',') if s}
    for qmd in sorted(DECKS.glob('l1[1-9]*.qmd')):
        sid = None
        for line in qmd.read_text().splitlines():
            m = re.match(r'^## .*\{#([\w-]+)', line)
            if m:
                sid = m.group(1)
            m = re.search(r'class="short-link">ilm\.wiki/436c/([\w-]+)<', line)
            # a bare page link (r12) is the older form on delivered decks and is fine; a wrong item number is not
            if m and sid in by_slide and m.group(1) not in (by_slide[sid], by_slide[sid].split('-')[0]):
                print(f'✗ {qmd.name} {sid}: short link {m.group(1)}, registry says {by_slide[sid]}'); bad += 1
    nums = [r['link'] for r in rows]
    if len(nums) != len(set(nums)):
        print('✗ a link name is used twice'); bad += 1
    print('items: OK' if not bad else f'items: {bad} problem(s)')
    return bad


def golinks():
    for r in rows:
        if r['status'] == 'live':
            print(f"bash ops/golink.sh add 436c/{r['link']} {BASE}/{r['page']}#{r['anchor']}")
        elif r['status'] == 'retired':
            print(f"bash ops/golink.sh add 436c/{r['link']} {BASE}/{r['page']}")


if __name__ == '__main__':
    {'check': lambda: sys.exit(1 if check() else 0), 'golinks': golinks}[sys.argv[1] if len(sys.argv) > 1 else 'check']()
