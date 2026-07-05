#!/usr/bin/env python3
"""Build kindling-gate.html from the template by inlining the
artwork in assets/web/ as base64 data URIs."""
import base64, os, pathlib

ROOT = pathlib.Path(__file__).parent
IMAGES = ["mountain", "tavern", "dragon", "camp", "summit", "gate", "gateopen"]

html = (ROOT / "kindling-gate.template.html").read_text()
for name in IMAGES:
    data = (ROOT / "assets" / "web" / f"{name}.webp").read_bytes()
    uri = "data:image/webp;base64," + base64.b64encode(data).decode()
    token = f"__IMG_{name.upper()}__"
    assert token in html, f"missing token {token}"
    html = html.replace(token, uri)

out = ROOT / "kindling-gate.html"
out.write_text(html)
print(f"built {out.name}: {out.stat().st_size // 1024} KB")
