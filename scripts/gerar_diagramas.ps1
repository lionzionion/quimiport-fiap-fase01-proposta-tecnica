# Requer Graphviz instalado: https://graphviz.org/download/
$ErrorActionPreference = 'Stop'
$raiz = Split-Path -Parent $PSScriptRoot
Set-Location $raiz
if (-not (Get-Command dot -ErrorAction SilentlyContinue)) {
  throw 'Comando dot nao encontrado. Instale o Graphviz e reabra o PowerShell.'
}
dot -V
foreach ($nome in @('dominio','status')) {
  dot -Tsvg "diagramas/$nome.dot" -o "diagramas/$nome.svg"
  if ($LASTEXITCODE -ne 0) { throw "Erro no diagrama $nome" }
}
Write-Host 'Diagramas SVG regenerados com sucesso.'
