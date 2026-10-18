# Dia de Fiscal 2026 — Planejamento e inteligência das fiscalizações

Deck de 21 slides (15 de conteúdo, mais capa, apresentador, três divisórias de módulo e encerramento) para o módulo teórico do
curso **Dia de Fiscal 2026**, em 19/10/2026, das 17h às 18h, voltado aos servidores que entraram em exercício a partir de 2026
(Projeto Básico, SEI nº 2808684, processo 50300.002963/2026-89).

Versão compacta de duas fontes, no mesmo template do deck `apresentacao_paf_diretoria`:
- Trilha Técnica, aula 8 (`TrilhaTecnico/materiais/aula-8-planejamento-inteligencia`): planejamento e inteligência.
- PAF 2027 ao Diretor-Geral (`Planejamento2026/apresentacao_paf_diretoria`): IPR 2.0, composição do PAF, temáticas e operacionais.

Estrutura: 01 capa · 02 apresentador · 03 divisória · 04–08 Módulo 1, Planejamento · 09 divisória · 10–14 Módulo 2, PAF ·
15 divisória · 16–19 Módulo 3, Inteligência · 20 do plano ao campo · 21 encerramento.

- `slide-01`, `slide-02` e `slide-21`: escritos à mão, não passam por `build_slides.py`.
- `slide-03..20`: gerados por `python3 build_slides.py`. O dicionário `BASES` fixa a escala de texto de cada slide, medida no Chrome.
- Os números do PAF 2027 vêm da minuta da NT de Metodologia (rodada de 29/09/2026) e são proposta, ainda sem aprovação da Diretoria Colegiada.
  Dados por unidade regional e custos de deslocamento ficaram de fora de propósito.

Para ver: `python3 -m http.server 8766` nesta pasta e abrir `http://localhost:8766/`.
