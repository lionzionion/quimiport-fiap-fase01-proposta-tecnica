#!/usr/bin/env python3
"""Verifica estrutura e links Markdown do pacote técnico, sem dependências externas."""
from pathlib import Path
from urllib.parse import unquote
import re, sys

root = Path(__file__).resolve().parents[1]
required = ["README.md", "docs/01-contexto-e-domínio.md",
  "docs/02-ddd.md", "docs/03-casos-de-uso.md",
  "docs/04-regras-de-negocio.md", "docs/05-arquitetura.md",
  "docs/06-diagramas.md", "docs/07-plano-de-qualidade.md",
  "docs/08-javascript-typescript.md", "docs/09-decisoes-e-roadmap.md",
  *[f"docs/{i:02d}-" for i in range(10,16)],
  "diagramas/dominio.mmd", "diagramas/status.mmd",
  "apresentacao/ROTEIRO_FALA_8_MINUTOS.md"]
errors=[]
for item in required:
    if item.endswith("-"):
        matches=list((root/"docs").glob(Path(item).name+"*.md"))
        if len(matches)!=1: errors.append(f"Ausente ou duplicado: {item}")
    elif not (root/item).is_file(): errors.append(f"Arquivo ausente: {item}")
pattern=re.compile(r'!?\[[^]]*\]\(([^)]+)\)')
for md in root.rglob("*.md"):
    text=re.sub(r'(?ms)^\s*```.*?^\s*```','',md.read_text(encoding="utf-8"))
    for m in pattern.finditer(text):
        href=m.group(1).split(' "')[0].strip().strip("<>")
        if href.startswith(("https://","http://","mailto:","#","data:")): continue
        target=unquote(href.split("#")[0])
        if target and not (md.parent/target).resolve().is_file():
            errors.append(f"Link quebrado: {md.relative_to(root)} -> {href}")
for file_name,token in [("dominio","classDiagram"),("status","stateDiagram-v2")]:
    f=root/"diagramas"/f"{file_name}.mmd"
    if f.exists() and token not in f.read_text(encoding="utf-8"):
        errors.append(f"Tipo de diagrama inválido: {file_name}")
cases=(root/"docs"/"03-casos-de-uso.md").read_text(encoding="utf-8")
found=re.findall(r"^## UC(\d{2}) —",cases,re.M)
if found!=[f"{i:02d}" for i in range(1,12)]: errors.append(f"UC01–UC11 ausentes: {found}")
if errors:
    print("\n".join("ERRO: "+e for e in errors)); sys.exit(1)
print("OK — estrutura, documentos, casos de uso, diagramas e links internos validados.")
print("A validação técnica não substitui revisão do autor, avaliação FIAP ou vídeo.")
