"""Extract every fenced block of the guide page; dry-run each gherkin block; rebuild the Level 1 example from the page and run it."""
import re, subprocess, sys, textwrap, shutil
from pathlib import Path
page = Path(sys.argv[1]).read_text(); out = Path(sys.argv[2]); shutil.rmtree(out, ignore_errors=True)
blocks = [(m.group(2), textwrap.dedent(m.group(3))) for m in re.finditer(r"^( *)```(\w*)\n(.*?)^\1```", page, flags=re.S | re.M)]
def run(d, *args):
    r = subprocess.run(["uvx", "behave", *args], cwd=d, capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr
g = [b for lang, b in blocks if lang == "gherkin"]
for i, b in enumerate(g):
    d = out / f"g{i}"; (d / "features/steps").mkdir(parents=True)
    text = b if "Feature:" in b else "Feature: wrapper\n\n" + b
    (d / "features/x.feature").write_text(text)
    code, o = run(d, "--dry-run", "--no-snippets")
    tail = [l for l in o.splitlines() if "scenarios passed" in l or "steps passed" in l or "Error" in l]
    nsteps = len(re.findall(r"^\s*(Given|When|Then|And|But) ", b, flags=re.M))
    print(f"g{i} exit={code} written_steps={nsteps} first={b.strip().splitlines()[0][:40]!r} {tail}")
py = [b for lang, b in blocks if lang == "python"]
d = out / "level1"; (d / "features/steps").mkdir(parents=True)
(d / "prices.py").write_text(py[0]); (d / "features/environment.py").write_text(py[1]); (d / "features/steps/price_steps.py").write_text(py[2])
l1 = [b for b in g if "sends 6 price updates" in b][0]; (d / "features/latest_price.feature").write_text(l1)
code, o = run(d); print("LEVEL1 exit", code); print(o)
(d / "prices.py").write_text(py[0].replace('if update["id"] in seen:', "if False:")); code, o = run(d); print("BROKEN exit", code); print("\n".join(o.splitlines()[-12:]))
(d / "prices.py").write_text(py[0]); print(run(d, "--steps-catalog")[1])
live = [b for b in g if "@live" in b][0]; (d / "features/live.feature").write_text(live); (d / "behave.ini").write_text("[behave]\ndefault_tags = not @live\n")
print("LIVE default", "\n".join(run(d)[1].splitlines()[-4:]))
