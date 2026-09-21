#!/usr/bin/env python3
"""Genera index.html: un unico file autonomo con pdf-lib, pdf.js e i moduli WASM incorporati.

Uso:  python3 build.py [cartella_node_modules]
Richiede pdf-lib@1.17.x e pdfjs-dist@5.x installati (npm i pdf-lib pdfjs-dist).
"""
import base64, json, re, sys
from pathlib import Path

ROOT = Path(__file__).parent
NM = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "node_modules"

pdflib = (NM / "pdf-lib/dist/pdf-lib.min.js").read_text(encoding="utf-8")
pdfjs = (NM / "pdfjs-dist/legacy/build/pdf.min.mjs").read_text(encoding="utf-8")
worker = (NM / "pdfjs-dist/legacy/build/pdf.worker.min.mjs").read_text(encoding="utf-8")
wasm = {n: base64.b64encode((NM / "pdfjs-dist/wasm" / n).read_bytes()).decode()
        for n in ("openjpeg.wasm", "jbig2.wasm")}
versions = {k: json.loads((NM / k / "package.json").read_text())["version"] for k in ("pdf-lib", "pdfjs-dist")}

# pdf.js è un modulo ES: trasformo l'export finale in un oggetto globale.
m = re.search(r"export\s*\{([^}]*)\};?\s*$", pdfjs)
assert m, "export finale di pdf.js non trovato"
items = []
for part in m.group(1).split(","):
    part = part.strip()
    a, _, b = part.partition(" as ")
    items.append(f"{b}:{a}" if b else part)
pdfjs = pdfjs[: m.start()] + "globalThis.pdfjsLib={" + ",".join(items) + "};"

# Nel worker: fetch sostituito. Restituisce solo i WASM incorporati, nessuna richiesta di rete.
prefix = (
    "(()=>{const W=" + json.dumps(wasm) + ";"
    "self.fetch=async u=>{u=String(u);for(const k in W)if(u.endsWith('/'+k)){"
    "const b=atob(W[k]),a=new Uint8Array(b.length);for(let i=0;i<b.length;i++)a[i]=b.charCodeAt(i);"
    "return new Response(a,{headers:{'Content-Type':'application/wasm'}})}"
    "throw new TypeError('Rete disabilitata in PDF Tool: '+u)};"
    "self.XMLHttpRequest=undefined;})();\n"
)
worker = prefix + worker

for name, code in (("pdf-lib", pdflib), ("pdf.js", pdfjs), ("worker", worker)):
    low = code.lower()
    assert "</script" not in low and "<!--" not in low and "<script" not in low, f"{name}: sequenza non sicura"

libs = (
    f"<!-- pdf-lib {versions['pdf-lib']} (MIT) — https://github.com/Hopding/pdf-lib -->\n"
    f"<script>{pdflib}</script>\n"
    f"<!-- pdf.js {versions['pdfjs-dist']} (Apache-2.0) — https://github.com/mozilla/pdf.js -->\n"
    f"<script type=\"module\">{pdfjs}</script>\n"
    f"<script type=\"text/plain\" id=\"pdfjs-worker\">{worker}</script>\n"
)
tpl = (ROOT / "src/app.html").read_text(encoding="utf-8")
assert "<!--@@LIBS@@-->" in tpl
out = tpl.replace("<!--@@LIBS@@-->", libs)
(ROOT / "index.html").write_text(out, encoding="utf-8")
print(f"index.html: {len(out.encode())/1024/1024:.2f} MB  (pdf-lib {versions['pdf-lib']}, pdf.js {versions['pdfjs-dist']})")
