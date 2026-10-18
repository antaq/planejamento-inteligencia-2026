#!/usr/bin/env python3
"""Gera os slides do Dia de Fiscal 2026 — Planejamento e inteligência das fiscalizações.

Versão compacta (15 slides de conteúdo, fora capa, apresentador, divisórias e
encerramento) de duas fontes:
  - Trilha Técnica, aula 8 (TrilhaTecnico/materiais/aula-8-planejamento-inteligencia):
    planejamento (PPF, responsiva, 3 níveis, sistemas) e inteligência (SISBIN,
    RedeMAIS, SINESP/INFOSEG, Conportos e CEPAI/SP).
  - PAF 2027 ao Diretor-Geral (Planejamento2026/apresentacao_paf_diretoria):
    IPR 2.0, composição do PAF, temáticas e operacionais.

Mesmo esqueleto do deck do PAF (cabeçalho com kicker, zoom de texto --tz, divisórias
de bloco). Para regerar: python3 build_slides.py
"""

from pathlib import Path

DST = Path(__file__).resolve().parent
TOTAL = 21
RODAPE = "Dia de Fiscal 2026 · Planejamento e inteligência das fiscalizações · SFC / GPF — ANTAQ"

BASE_CSS = """
body { margin:0; padding:0; overflow:hidden; font-family:'Open Sans',sans-serif; }
.slide { width:100vw; height:100vh; position:relative; display:flex; flex-direction:column; overflow:hidden; background:#ffffff; }
.font-montserrat { font-family:'Montserrat',sans-serif; }
.text-brand { color:#003366; } .bg-brand { background-color:#003366; }
.text-accent { color:#0066CC; } .bg-accent { background-color:#0066CC; }
.header-bar { height:10px; background:#003366; width:100%; }
.secondary-bar { height:4px; background:#0066CC; width:100%; }
.stat-card { background:linear-gradient(135deg,#003366,#004d99); border-radius:16px; padding:20px 18px; text-align:center; color:white; position:relative; overflow:hidden; }
.stat-num { font-family:'Montserrat',sans-serif; font-weight:900; font-size:calc(48px * var(--tz)); line-height:1; }
.stat-lbl { font-size:calc(17px * var(--tz)); line-height:1.3; color:#BFD3E8; margin-top:6px; }
.card { display:flex; align-items:flex-start; gap:16px; padding:14px 20px; background:#F8FAFC; border-radius:14px; border-left:5px solid #0066CC; }
.card-green { background:linear-gradient(135deg,#F0FDF4,#DCFCE7); border-left-color:#22C55E; }
.card-amber { background:linear-gradient(135deg,#FFFBEB,#FEF3C7); border-left-color:#F59E0B; }
.card-red   { background:linear-gradient(135deg,#FEF2F2,#FEE2E2); border-left-color:#EF4444; }
.card-gold  { background:linear-gradient(135deg,#FFFBEB,#FEF3C7); border-left-color:#FFD700; }
.ico { width:50px; height:50px; border-radius:12px; flex-shrink:0; display:flex; align-items:center; justify-content:center; background:#DBEAFE; }
.ico i { color:#0066CC; font-size:calc(22px * var(--tz)); }
.ct { font-family:'Montserrat',sans-serif; font-weight:700; color:#003366; font-size:calc(22px * var(--tz)); line-height:1.25; margin:0; }
.cd { color:#475569; font-size:calc(18px * var(--tz)); line-height:1.45; margin:3px 0 0; }
.cd b, .cd strong { color:#003366; }
.slide > .flex-1 > .flex.flex-col,
.slide > .flex-1 > .grid > .flex.flex-col { justify-content:center; }
.pill { display:inline-block; padding:3px 12px; border-radius:999px; font-family:'Montserrat',sans-serif; font-weight:700; font-size:calc(15px * var(--tz)); letter-spacing:0.04em; }
.pill-a { background:#DCFCE7; color:#166534; } .pill-b { background:#DBEAFE; color:#1E40AF; }
.pill-c { background:#FEE2E2; color:#991B1B; } .pill-gold { background:#FEF3C7; color:#92400E; }
.formula { background:#0F172A; color:#E2E8F0; border-radius:14px; padding:16px 24px; font-family:'Courier New',monospace; font-size:calc(19px * var(--tz)); }
.destaque { background:linear-gradient(135deg,#003366,#0066CC); color:#fff; border-radius:16px; padding:18px 26px; }
.destaque p { margin:0; }
.legenda { color:#64748B; font-size:calc(15px * var(--tz)); line-height:1.5; }
.num-b { font-family:'Montserrat',sans-serif; font-weight:900; color:#0066CC; font-size:calc(34px * var(--tz)); line-height:1; min-width:56px; text-align:center; }
.sec { font-family:'Montserrat',sans-serif; font-weight:700; font-size:calc(15px * var(--tz)); letter-spacing:.12em; text-transform:uppercase; color:#64748B; margin:0 0 10px; }
.hdr .text-5xl { font-size:46px; line-height:1; } .hdr .text-lg { font-size:19px; line-height:1.5; } .ftr .text-sm { font-size:14px; line-height:1.4; }
.gap-3 { row-gap:22px; } .gap-4 { row-gap:24px; } .gap-5 { row-gap:26px; } .gap-6 { row-gap:28px; }
"""

HEAD = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>{title}</title>
<link rel="icon" type="image/png" href="favicon.png">
<link rel="icon" type="image/x-icon" href="favicon.ico">
<link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;700;900&family=Open+Sans:wght@400;600&display=swap" rel="stylesheet"/>
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet"/>
<style>{css}</style>
</head>
<body>
<div class="slide">
  <div class="header-bar"></div>
  <div class="secondary-bar"></div>

  <div class="px-16 pt-6 pb-2 hdr">
    <div class="flex items-center gap-3">
      <div style="width:5px;height:44px;" class="bg-accent"></div>
      <div>
        <p class="font-montserrat font-bold text-gray-400 text-lg uppercase tracking-widest">{kicker}</p>
        <p class="text-5xl font-montserrat font-bold text-brand uppercase tracking-tight">{titulo}</p>
      </div>
      <div class="ml-auto flex items-center gap-3">
        <span class="font-montserrat font-bold text-accent uppercase tracking-widest" style="font-size:15px;"><i class="fas {tagico}"></i>&nbsp; {tag}</span>
        <img src="assets/logo-antaq-azul.png" alt="ANTAQ" style="height:32px;">
        <p class="font-montserrat font-bold text-gray-400 tracking-wider" style="font-size:12px; line-height:1.35;">SFC<br/>GPF</p>
      </div>
    </div>
  </div>

{body}

  <div class="px-16 pb-4 flex justify-between items-center border-t border-gray-100 pt-3 mx-8 ftr">
    <p class="text-gray-400 text-sm">{rodape}</p>
    <p class="text-gray-300 text-sm font-mono">{n} / {total}</p>
  </div>
</div>
<script src="zoom.js"></script>
<script src="anim.js"></script>
<script>document.addEventListener("keydown",function(e){{if(["ArrowRight","ArrowLeft","PageDown","PageUp","Home","End"," ","f","F"].indexOf(e.key)!==-1){{e.preventDefault();window.parent.postMessage({{type:"slide-nav",key:e.key}},"*");}}}});</script>
</body>
</html>
"""

MODULOS = {
    1: ("Planejamento", "fa-clipboard-list"),
    2: ("PAF", "fa-calendar-check"),
    3: ("Inteligência", "fa-satellite-dish"),
    4: ("Visita técnica", "fa-route"),
}

SLIDES = []


BASES = {4:1.7,5:1.7,6:1.6,7:1.45,8:2.1,10:1.5,11:1.35,12:1.65,13:1.55,14:1.7,16:1.55,17:1.7,18:1.55,19:2.0,20:1.7}


def slide(n, mod, title, kicker, titulo, body, extra_css="", base=1.0):
    SLIDES.append(dict(n=n, mod=mod, title=title, kicker=kicker, titulo=titulo,
                       body=body, extra_css=extra_css, base=BASES.get(n, base)))


def card(icon, titulo, texto, cls=""):
    return (f'<div class="card {cls}"><div class="ico"><i class="fas {icon}"></i></div>'
            f'<div><p class="ct">{titulo}</p><p class="cd">{texto}</p></div></div>')


def stat(num, rotulo, extra=""):
    return (f'<div class="stat-card" {extra}><p class="stat-num">{num}</p>'
            f'<p class="stat-lbl">{rotulo}</p></div>')


def wrap(inner, cols="grid-cols-12"):
    return f'  <div class="flex-1 px-16 pb-4 grid {cols} gap-8 items-center min-h-0">\n{inner}\n  </div>'


def col(span, inner, extra=""):
    return f'    <div class="col-span-{span} flex flex-col gap-4 {extra}">\n{inner}\n    </div>'


# ---------------------------------------------------------------------------
# MÓDULO 1 — Planejamento da fiscalização (slides 4..8)
# ---------------------------------------------------------------------------
org = """
      <div class="destaque text-center">
        <p class="font-montserrat font-black" style="font-size:calc(34px * var(--tz));">SFC</p>
        <p style="font-size:calc(17px * var(--tz)); color:#DBEAFE;">Superintendência de Fiscalização e Coordenação das Unidades Regionais</p>
      </div>
      <div class="grid grid-cols-3 gap-4">
        <div class="card" style="border-left-color:#FFD700; background:#FFFBEB; flex-direction:column; gap:4px;">
          <p class="ct" style="color:#92400E;">GPF</p>
          <p class="cd">Planejamento e Inteligência da Fiscalização</p>
          <span class="pill pill-gold" style="margin-top:6px;">quem apresenta</span></div>
        <div class="card" style="flex-direction:column; gap:4px;"><p class="ct">GCOR</p>
          <p class="cd">Coordenação das Unidades Regionais</p></div>
        <div class="card" style="flex-direction:column; gap:4px;"><p class="ct">GRAT</p>
          <p class="cd">Recursos e Apoio Técnico</p></div>
      </div>
      <div class="card card-green">
        <div class="ico" style="background:#BBF7D0;"><i class="fas fa-ship" style="color:#15803D;"></i></div>
        <div><p class="ct">Gerências e Unidades Regionais</p>
        <p class="cd">Braço operacional da ANTAQ em todo o território: executam as inspeções e as ações de campo, como as que você vai acompanhar.</p></div>
      </div>"""
comp = "\n".join(
    f'      <div class="card"><p class="num-b">{i}</p><div><p class="ct">{t}</p><p class="cd">{d}</p></div></div>'
    for i, (t, d) in enumerate([
        ("Apoiar a fiscalização", "com recursos humanos, financeiros, tecnológicos e logísticos."),
        ("Diagnosticar os regulados", "para subsidiar as ações de inteligência."),
        ("Propor planos e diretrizes", "de fiscalização: o PPF e o PAF."),
        ("Propor ações conjuntas", "com órgãos de inteligência."),
        ("Supervisionar os sistemas", "da fiscalização e mantê-los atualizados."),
    ], 1))
slide(4, 1, "Quem planeja a fiscalização", "SFC · GPF", "Quem planeja a fiscalização",
      wrap(col(6, org) + "\n" + col(6, '      <p class="sec">Cinco competências da GPF</p>\n' + comp)))

lvl = lambda n, t, d, cor, ic: (
    f'<div class="card" style="border-left-color:{cor};"><div class="ico"><i class="fas {ic}"></i></div>'
    f'<div><p class="ct">Nível {n} · {t}</p><p class="cd">{d}</p></div></div>')
slide(5, 1, "Fiscalização responsiva e em 3 níveis", "PPF 2025–2028 · Perspectivas de atuação",
      "Responsiva e em 3 níveis",
      wrap(
          col(6, """
      <p class="sec">Fiscalização responsiva · a intensidade acompanha o risco</p>
      <div class="grid grid-cols-2 gap-4" style="align-items:stretch;">
        <div class="card card-amber" style="flex-direction:column;"><p class="ct">Risco da atividade</p>
          <p class="cd"><b>probabilidade × impacto</b> de dano ao mercado, à segurança e ao interesse público.</p></div>
        <div class="card card-amber" style="flex-direction:column;"><p class="ct">Comportamento do agente</p>
          <p class="cd"><b>histórico × postura</b>: conformidade passada e disposição de cooperar.</p></div>
      </div>
      <div class="destaque">
        <p class="font-montserrat font-bold" style="font-size:calc(22px * var(--tz));">Risco × comportamento = intensidade da fiscalização</p>
        <p style="font-size:calc(18px * var(--tz)); color:#DBEAFE; margin-top:6px !important;">Do incentivo à conformidade, para quem coopera, às medidas mais rigorosas, para quem reincide.</p>
      </div>
      <p class="legenda">Fiscalizar todos do mesmo jeito desperdiça esforço: a Agência concentra recursos onde o risco é maior.</p>""")
          + "\n" + col(6, """
      <p class="sec">Fiscalização em 3 níveis · do mais barato ao mais caro</p>
      """ + lvl(1, "Monitoramento", "Sistemas automatizados apontam possíveis infrações em tempo real.", "#94A3B8", "fa-satellite-dish") + """
      """ + lvl(2, "Ação à distância", "Análise documental e evidências audiovisuais, sem deslocar a equipe.", "#3B82F6", "fa-file-circle-check") + """
      """ + lvl(3, "Ação presencial", "Inspeção direcionada às áreas de maior risco e complexidade.", "#003366", "fa-helmet-safety") + """
      <p class="legenda"><i class="fas fa-arrow-right text-accent"></i>&nbsp; Custo e esforço crescem do nível 1 ao 3. A visita técnica mostra o nível 3.</p>""")))

faixas = [("A1", 272, "monitoramento", "a"), ("A2", 159, "monitoramento", "a"), ("B1", 906, "documental", "b"),
          ("B2", 502, "à distância", "b"), ("C1", 286, "programada", "c"), ("C2", 194, "sem aviso", "c"),
          ("C3", 77, "intensiva", "c"), ("C4", 30, "intervenção", "c")]
fx = "\n".join(
    f'        <div class="text-center"><span class="pill pill-{g}">{f}</span>'
    f'<p class="font-montserrat font-black text-brand" style="font-size:calc(20px * var(--tz)); margin:6px 0 0;">{q:,}</p>'
    f'<p class="legenda" style="margin:0; font-size:calc(9.5px * var(--tz));">{s}</p></div>'.replace(",", ".")
    for f, q, s, g in faixas)
slide(6, 1, "Classificação de risco: o IPR", "Fiscalização responsiva · Modelo de risco", "Classificação de risco: o IPR",
      wrap(
          col(5, """
      <div class="destaque"><p class="font-montserrat font-bold" style="font-size:calc(24px * var(--tz));">Índice de Perfil de Risco (IPR)</p>
        <p style="font-size:calc(18px * var(--tz)); color:#DBEAFE; margin-top:6px !important;">Cada outorga recebe uma <b style="color:#FFD700;">nota de 0 a 100</b> e uma <b style="color:#FFD700;">faixa de A1 a C4</b>.</p></div>
      """ + card("fa-file-signature", "A unidade é a outorga, não a empresa", "Uma empresa com quatro linhas de travessia tem quatro IPRs: cada uma tem o seu risco.") + """
      """ + card("fa-scale-balanced", "A nota mistura duas coisas", "<b>O que a empresa já fez</b> (autuações, reincidência, denúncias) e <b>o que ela é</b> (atividade, porte, acesso, maturidade).") + """
      """ + card("fa-user-check", "O índice prioriza; a chefia decide", "Toda inclusão ou exclusão fora da regra fica registrada, com autor e fundamento.")) + "\n"
          + col(7, f"""
      <p class="sec">2.426 outorgas ativas no ciclo 2027, por faixa de risco</p>
      <div class="bar-row"><div class="bar-trk flex" style="height:64px; border-radius:14px; overflow:hidden; font-family:Montserrat; font-weight:900; color:#fff; font-size:calc(22px * var(--tz));">
        <div style="width:17.8%; background:#22C55E;" class="seg flex items-center justify-center">A</div>
        <div style="width:58%; background:#3B82F6;" class="seg flex items-center justify-center">B</div>
        <div style="width:24.2%; background:#EF4444;" class="seg flex items-center justify-center">C</div>
      </div></div>
      <div class="grid grid-cols-3 gap-4">
        <div class="card card-green" style="flex-direction:column;"><p class="ct">Grupo A · 431</p><p class="cd">menor risco: monitoramento e sorteio auditável</p></div>
        <div class="card" style="flex-direction:column;"><p class="ct">Grupo B · 1.408</p><p class="cd">risco intermediário: ação remota</p></div>
        <div class="card card-red" style="flex-direction:column;"><p class="ct">Grupo C · 587</p><p class="cd">maior risco: ação presencial, até intervenção</p></div>
      </div>
      <p class="sec" style="margin-top:6px;">Solução fiscal de cada faixa</p>
      <div class="grid grid-cols-8 gap-2">
{fx}
      </div>
      <p class="legenda">Fonte: minuta da NT de Metodologia do PAF 2027 (rodada de validação de 29/09/2026), Quadro 2.</p>""")))

slide(7, 1, "Priorizar o que verificar", "Fiscalização em 3 níveis · Eixos de risco", "Priorizar o que verificar",
      wrap(
          col(5, """
      <p class="sec">Três eixos priorizam as obrigações</p>
      """ + card("fa-repeat", "1 · Probabilidade de ocorrência", "Com que frequência os regulados descumprem a obrigação?") + """
      """ + card("fa-burst", "2 · Impacto no mercado", "Qual o dano possível aos usuários, ao meio ambiente e à concorrência?") + """
      """ + card("fa-coins", "3 · Custo fiscalizatório", "Quanto esforço exige verificar: monitorável, remoto ou presencial?") + """
      <p class="legenda">Quanto mais frequente e danosa a falha, e mais barata a checagem, maior a prioridade.</p>""")
          + "\n" + col(7, """
      <p class="sec">Exemplo ilustrativo · uma ação presencial (alto custo)</p>
      <div class="card" style="flex-direction:column; gap:8px;">
        <p class="ct">Resolução ANTAQ nº X, art. X · são infrações:</p>
        <p class="cd" style="margin:0;">I prestar informação fora do prazo · II não enviar documentação · III bloquear indevidamente o acesso ao serviço · IV descumprir determinação da Agência · V não manter registros atualizados · VI não informar alteração operacional</p>
      </div>
      <p class="sec" style="margin-top:4px;">O que a equipe verifica em campo, nesta ordem</p>
      <div class="grid grid-cols-2 gap-3">
        <div class="card card-red"><p class="num-b" style="color:#B91C1C;">1º</p><div><p class="ct">Inciso III</p><p class="cd">alta probabilidade, alto impacto</p></div></div>
        <div class="card card-amber"><p class="num-b" style="color:#B45309;">2º</p><div><p class="ct">Inciso V</p><p class="cd">alta probabilidade, impacto relevante</p></div></div>
        <div class="card"><p class="num-b">3º</p><div><p class="ct">Inciso VI</p><p class="cd">probabilidade média, impacto relevante</p></div></div>
        <div class="card"><p class="num-b">4º</p><div><p class="ct">Inciso II</p><p class="cd">probabilidade média, impacto moderado</p></div></div>
      </div>
      <div class="destaque"><p style="font-size:calc(19px * var(--tz));"><b>Nem toda infração prevista na norma é verificada presencialmente.</b> Os incisos I e IV ficam de fora desta ação, por baixa priorização.</p></div>""")))

sist = [
    ("fa-database", "SFIS", "Sistema de Fiscalização, de 2009. Cadastra os processos, controla penalidades e TAC e gera o boleto das multas."),
    ("fa-mobile-screen", "SFIS Mobile", "Aplicativo Android que substitui prancheta, caneta, máquina fotográfica e impressões em campo."),
    ("fa-plug", "SFIS Pro", "Extensão que liga o SFIS ao SEI: traz o processo sancionador e gera documentos nativos."),
    ("fa-chart-column", "PIF", "Painel Interno da Fiscalização, BI desde 2015, aberto a todos os servidores pela Intranet SFC."),
    ("fa-globe", "Painel de Dados Públicos", "Infrações transitadas em julgado e base para download, no Portal da ANTAQ (Central de Conteúdo, Painéis)."),
    ("fa-toolbox", "Ecossistema SFC", "CEF, AeroSFC, A Gente SFC, OuvidoriaSFC e ReportSFC apoiam o dia a dia da fiscalização."),
]
slide(8, 1, "Sistemas e painéis da fiscalização", "Ferramentas do fiscal", "Sistemas e painéis",
      '  <div class="flex-1 px-16 pb-4 grid grid-cols-3 gap-6 items-center min-h-0" style="align-content:center;">\n'
      + "\n".join("    " + card(i, t, d) for i, t, d in sist) + "\n  </div>")

# ---------------------------------------------------------------------------
# MÓDULO 2 — PAF (slides 10..14)
# ---------------------------------------------------------------------------
cats = [
    ("fa-gauge-high", "Grupo de risco", "Núcleo central. O IPR define quem fiscalizar e com que intensidade.", ""),
    ("fa-route", "Operacionais", "Rotina em regiões distantes, com deslocamento, pernoite e logística própria.", ""),
    ("fa-file-contract", "Rito próprio", "Novas outorgas, embarcações em construção, investimentos portuários e concessões.", ""),
    ("fa-layer-group", "Temáticas", "Ações coordenadas sobre um tema, abrangendo vários regulados de uma vez.", ""),
]
slide(10, 2, "Plano Anual de Fiscalização", "PAF · O que é", "Plano Anual de Fiscalização",
      wrap(
          col(7, """
      <div class="destaque"><p style="font-size:calc(21px * var(--tz));"><b style="color:#FFD700;">PPF</b> é o plano de quatro anos (2025–2028). <b style="color:#FFD700;">PAF</b> é o plano do ano: detalha quais ações vão a campo, e onde.</p></div>
      <p class="sec">Quatro categorias de fiscalização no PAF</p>
      <div class="grid grid-cols-2 gap-4" style="align-items:stretch;">
      """ + "\n".join(card(i, t, d) for i, t, d, _ in cats) + """
      </div>""")
          + "\n" + col(5, """
      <p class="sec">Como se mede a execução</p>
      <div class="stat-card" style="padding:26px 24px;">
        <p style="font-family:Montserrat; font-weight:700; font-size:calc(21px * var(--tz)); color:#BFD3E8; margin:0 0 10px;">Indicador EPAF</p>
        <p class="font-montserrat font-black" style="font-size:calc(26px * var(--tz)); line-height:1.3;">processos instaurados<br/><span style="color:#FFD700;">÷ processos previstos × 100</span></p>
        <p class="stat-lbl" style="font-size:calc(20px * var(--tz));">Meta: <b style="color:#FFD700;">≥ 90%</b>, com acompanhamento mensal</p>
      </div>
      """ + card("fa-people-arrows", "Quem faz o quê", "<b>GPF</b> planeja, em parceria com a <b>GCOR</b> e a <b>GRAT</b>.<br/><b>SFC</b> traz as diretrizes.<br/><b>Diretoria</b> aprova.<br/><b>Unidades regionais</b> executam.") + """
      """ + card("fa-file-lines", "Versão em construção", "O PAF 2027 segue para a Diretoria Colegiada até 31/10. Os próximos slides mostram a proposta.", "card-gold"))))

cal = [("29/09", "Validação do IPR e da equalização"), ("30/09", "Data de referência do ciclo 2027"),
       ("Outubro", "Extração oficial, sorteio e escolha das 3 temáticas"), ("Até 31/10", "Proposta à Diretoria Colegiada")]
calh = "\n".join(
    f'        <div class="card" style="padding:10px 16px;"><p class="font-montserrat font-black text-accent" style="font-size:calc(20px * var(--tz)); min-width:96px; margin:0;">{d}</p>'
    f'<p class="cd" style="margin:0;">{t}</p></div>' for d, t in cal)
slide(11, 2, "PAF 2027 em duas frentes", "PAF 2027 · Visão geral", "PAF 2027 em duas frentes",
      wrap(
          col(6, """
      <span class="pill pill-c" style="align-self:flex-start;">Frente 1 · grupo de risco</span>
      <p class="font-montserrat font-bold text-brand" style="font-size:calc(28px * var(--tz)); margin:0;">Quem fiscalizar, e com que intensidade?</p>
      <div class="grid grid-cols-3 gap-4">
        """ + stat("2.466", "outorgas avaliadas") + stat("≈669", "entram no PAF 2027") + stat("83%", "da capacidade (45,9 mil h)") + """
      </div>
      <p class="cd">A nota de risco (IPR 2.0) define a ação: <b>presencial</b> no Grupo C, <b>remota</b> no B, <b>sorteio</b> no A.</p>
      <span class="pill pill-b" style="align-self:flex-start; margin-top:8px;">Frente 2 · temáticas</span>
      <p class="font-montserrat font-bold text-brand" style="font-size:calc(28px * var(--tz)); margin:0;">Que problema do setor examinar a fundo?</p>
      <div class="grid grid-cols-3 gap-4">
        """ + stat("99", "contribuições da Agenda Regulatória") + stat("7", "temáticas em 2027") + stat("4 + 3", "mantidas e a escolher") + """
      </div>""")
          + "\n" + col(6, f"""
      <p class="sec">Calendário até a Diretoria Colegiada</p>
{calh}
      <div class="destaque"><p style="font-size:calc(19px * var(--tz));">As duas frentes formam <b>um só plano</b>, medido contra a força de trabalho de cada unidade.</p></div>
      <p class="legenda">Fontes: minuta da NT de Metodologia do PAF 2027 e Nota Técnica nº 27/2026/GPF/SFC (SEI 3024667).</p>""")))

ind = [("ICF", "peso 3", "Cobertura fiscalizatória", "Há quanto tempo ninguém olha. Nunca visitada leva a nota máxima."),
       ("IVO", "peso 2", "Volume operacional", "O porte da operação, comparado com pares da mesma categoria."),
       ("ICD", "peso 1", "Custo-distância", "Esforço para chegar ao local, medido pela via real, não pela linha reta."),
       ("IMA", "peso 1", "Maturidade empresarial", "Idade do CNPJ e porte. Priorização, não punição."),
       ("Piso", "atividade", "Risco da atividade", "Atividade perigosa tem nota mínima: nunca cai em A1.")]
indh = "\n".join(
    f'      <div class="card" style="padding:10px 18px;"><div style="min-width:86px; text-align:center;"><p class="font-montserrat font-black text-accent" style="font-size:calc(26px * var(--tz)); margin:0; line-height:1;">{s}</p>'
    f'<p class="legenda" style="margin:2px 0 0; font-size:calc(13px * var(--tz));">{p}</p></div><div><p class="ct" style="font-size:calc(20px * var(--tz));">{t}</p><p class="cd" style="margin:0;">{d}</p></div></div>'
    for s, p, t, d in ind)
slide(12, 2, "IPR 2.0: o que a nota enxerga", "IPR 2.0 · NT 11, 12, 19 e 20/2026", "IPR 2.0: o que mudou",
      wrap(
          col(5, """
      <p class="sec">O defeito que motivou a revisão</p>
      <p class="cd" style="font-size:calc(21px * var(--tz));">Os indicadores antigos dependiam de fiscalização anterior. Quem <b>nunca foi fiscalizado</b> marcava zero em tudo e caía em A1: quanto menos a Agência olhava, mais segura a outorga parecia.</p>
      <div class="grid grid-cols-2 gap-4">
        """ + stat("595", "outorgas nunca fiscalizadas") + stat("38%", "do universo sem visita há mais de 5 anos ou nunca") + """
      </div>
      <div class="formula">IPR = MAIOR( nota ponderada, piso da atividade )</div>""")
          + "\n" + col(7, '      <p class="sec">Os cinco componentes da nota</p>\n' + indh)))

slide(13, 2, "O que entra no PAF 2027", "PAF 2027 · Composição", "O que entra no PAF 2027",
      wrap(
          col(7, """
      <p class="sec">A regra é por grupo, não um número fixo</p>
      <div class="card card-red"><p class="num-b" style="color:#B91C1C; font-size:calc(44px * var(--tz)); min-width:150px;">587</p>
        <div><p class="ct">Grupo C entra inteiro</p><p class="cd">Fiscalizar as outorgas de maior risco é obrigação do modelo: o Grupo C é o <b>piso</b> do plano.</p></div></div>
      <div class="card"><p class="num-b" style="font-size:calc(44px * var(--tz)); min-width:150px;">52</p>
        <div><p class="ct">Grupo B entra na medida do que cabe</p><p class="cd">As primeiras do ranking, até o limite da força de trabalho, em ordem estrita.</p></div></div>
      <div class="card card-green"><p class="num-b" style="color:#15803D; font-size:calc(44px * var(--tz)); min-width:150px;">≈30</p>
        <div><p class="ct">Grupo A entra por sorteio</p><p class="cd">Uma fração das 431 de menor risco, para que ninguém fique fora do radar.</p></div></div>""")
          + "\n" + col(5, """
      <div class="destaque text-center"><p class="font-montserrat font-black" style="font-size:calc(52px * var(--tz)); line-height:1;">≈669</p>
        <p style="font-size:calc(19px * var(--tz)); color:#DBEAFE;">outorgas e <b style="color:#FFD700;">45.880 horas</b>: 83% das 55.560 horas disponíveis. Antes era um recorte informal de 200.</p></div>
      """ + card("fa-dice", "Sorteio que qualquer um pode refazer", "A lista de elegíveis é publicada antes de a semente ser conhecida. Mesma lista e mesma semente dão as mesmas sorteadas.") + """
      """ + card("fa-id-card", "Todo CNPJ conferido na Receita", "Baixados ou suspensos saem da lista, ou ficam por decisão fundamentada. Nenhum bloqueio sem tratamento."))))

slide(14, 2, "Temáticas e operacionais", "PAF 2027 · Temáticas e operacionais", "Temáticas e operacionais",
      wrap(
          col(6, """
      <span class="pill pill-b" style="align-self:flex-start;">Temáticas · o tema, não a outorga</span>
      """ + card("fa-inbox", "1 · Ouvir", "99 contribuições da revisão da Agenda Regulatória 2025–2028 (90 do público externo, 8 de unidades internas, 1 do Poder Concedente).") + """
      """ + card("fa-sitemap", "2 · Agrupar e confrontar", "25 subgrupos, comparados com a Agenda Regulatória, a Agenda de Estudos e as temáticas de 2026, para não duplicar esforço.") + """
      """ + card("fa-list-check", "3 · Decidir", "Sete temáticas: quatro mantidas com escopo ajustado, como o diagnóstico das Autoridades Portuárias, e três a escolher.") + """""")
          + "\n" + col(6, """
      <span class="pill pill-gold" style="align-self:flex-start;">Operacionais · o problema, não o agente</span>
      <div class="card" style="flex-direction:column; gap:8px;"><p class="sec" style="margin:0;">Planejar, nesta ordem</p>
        <p class="cd" style="font-size:calc(20px * var(--tz));"><b>1 Problema</b> · <b>2 Evidência</b> · <b>3 Instrumento</b> · <b>4 Abordagem diferenciada</b></p>
        <p class="cd">O que prejudica o usuário, o que medir em campo, o que as ferramentas de hoje resolvem e quem precisa apoiar.</p></div>
      <div class="card card-green" style="flex-direction:column; gap:8px;"><p class="sec" style="margin:0;">Medir, no ciclo seguinte</p>
        <p class="cd">Resolvemos o problema? Houve melhoria? Precisamos de nova abordagem? A fiscalização sozinha consegue resolver?</p></div>
      <div class="destaque"><p style="font-size:calc(19px * var(--tz));"><b>A ordem importa.</b> O objetivo é que o campo gere evidência para aperfeiçoar a norma, e não apenas relatórios.</p></div>""")))

# ---------------------------------------------------------------------------
# MÓDULO 3 — Inteligência (slides 16..19)
# ---------------------------------------------------------------------------
niveis = [("1", "Órgão central", "ABIN coordena o Sistema", False), ("2", "Permanentes", "Núcleo estável: ANAC, ANTT, Polícia Federal…", False),
          ("3", "Dedicados", "Inteligência setorial: MPOR…", False), ("4", "Associados", "ANTAQ, AGU, CGU, ANVISA…", True),
          ("5", "Federados", "Estados e o Distrito Federal", False)]
nv = "\n".join(
    f'      <div class="card" style="padding:10px 18px; {"border-left-color:#FFD700; background:#FFFBEB;" if g else ""}"><p class="num-b" style="{"color:#B45309;" if g else ""}">{n}</p>'
    f'<div><p class="ct" style="font-size:calc(20px * var(--tz));">{t}</p><p class="cd" style="margin:0;">{d}</p></div></div>'
    for n, t, d, g in niveis)
slide(16, 3, "SISBIN e a participação da ANTAQ", "Inteligência · SISBIN", "SISBIN e a ANTAQ",
      wrap(
          col(5, """
      <p class="sec">Sistema Brasileiro de Inteligência</p>
      <p class="cd" style="font-size:calc(20px * var(--tz));">Integra órgãos públicos na produção e difusão de conhecimento de inteligência, para assessorar decisões de Estado.</p>
      <div class="card" style="flex-direction:column; gap:6px;">
        <p class="cd"><b>1999</b> · Lei nº 9.883, cria o SISBIN e a Abin</p>
        <p class="cd"><b>2002</b> · Decreto nº 4.376, regulamenta</p>
        <p class="cd"><b>2023</b> · Decreto nº 11.693, o <b>Novo SISBIN</b></p>
      </div>
      """ + card("fa-handshake", "A ANTAQ participa desde 2018", "Pela GPF, com participação oficializada pela Portaria GAB/DG/ABIN nº 926/2023.", "card-gold"))
          + "\n" + col(7, '      <p class="sec">Níveis de integração do Novo SISBIN</p>\n' + nv + """
      <p class="cd"><i class="fas fa-anchor text-accent"></i>&nbsp; O setor aquaviário concentra fluxos sensíveis de pessoas, cargas e infraestrutura. A ANTAQ <b>coleta, integra e compartilha</b> esses dados, como no Painel Situação dos Portos.</p>""")))

slide(17, 3, "RedeMAIS: satélite na fiscalização", "Inteligência · Programa Brasil MAIS", "RedeMAIS: satélite e alertas",
      wrap(
          col(6, """
      <div style="border-radius:16px; overflow:hidden; border:1px solid #E2E8F0; box-shadow:0 8px 24px rgba(0,0,0,.12);">
        <img src="assets/santos-comparativo.webp" alt="Comparativo de imagens de satélite do Porto de Santos" style="width:100%; height:auto; display:block; max-height:640px; object-fit:cover;"></div>
      <p class="legenda text-center">Imagens do Porto de Santos em duas datas: o que mudou entre elas.</p>""")
          + "\n" + col(6, """
      <p class="cd" style="font-size:calc(20px * var(--tz));">Acesso a uma plataforma de <b>imagens de satélite de todo o Brasil</b>, com imagens diárias e alertas de alteração. Vigência de 60 meses, sem repasse de recursos.</p>
      """ + card("fa-ship", "Alerta de embarcações", "Relatório diário de embarcações, dragas ou balsas dentro de um perímetro delimitado, como áreas de restrição em portos.") + """
      """ + card("fa-building", "Alerta de construções", "Relatório diário de novas obras, como edificações em arrendamentos com restrição.") + """
      """ + card("fa-bolt", "Fiscalização remota e tempestiva", "A Agência identifica intervenções não autorizadas logo após a detecção, sem depender de visita.", "card-green"))))

slide(18, 3, "SINESP / INFOSEG", "Inteligência · Segurança pública", "SINESP / INFOSEG",
      wrap(
          col(6, """
      <p class="cd" style="font-size:calc(20px * var(--tz));">Plataforma nacional do Ministério da Justiça que reúne <b>informações de segurança pública</b> de órgãos federais e estaduais. Uma única consulta alcança várias bases.</p>
      """ + card("fa-bolt", "Operacional", "Apoia o campo e a verificação de dados durante a fiscalização.") + """
      """ + card("fa-magnifying-glass-chart", "Investigativo", "Cruza informações para aprofundar análises e apurações.") + """
      """ + card("fa-chess", "Estratégico", "Dá visão agregada para planejar e priorizar.") + """
      <p class="legenda"><i class="fas fa-lock text-accent"></i>&nbsp; Acesso restrito por perfil e função, vinculado à atividade de fiscalização.</p>""")
          + "\n" + col(6, """
      <div style="border-radius:16px; overflow:hidden; border:1px solid #E2E8F0; box-shadow:0 8px 24px rgba(0,0,0,.12);">
        <img src="assets/infoseg-tela.png" alt="Tela de pesquisa do Infoseg" style="width:100%; height:auto; display:block;"></div>
      <div class="grid grid-cols-3 gap-3">
        <div class="card" style="flex-direction:column; padding:10px 14px;"><p class="ct" style="font-size:calc(18px * var(--tz));">Planejamento</p><p class="cd" style="font-size:calc(15px * var(--tz));">ações conjuntas com outros órgãos</p></div>
        <div class="card" style="flex-direction:column; padding:10px 14px;"><p class="ct" style="font-size:calc(18px * var(--tz));">Intimações</p><p class="cd" style="font-size:calc(15px * var(--tz));">mais precisão ao localizar envolvidos</p></div>
        <div class="card" style="flex-direction:column; padding:10px 14px;"><p class="ct" style="font-size:calc(18px * var(--tz));">Segurança</p><p class="cd" style="font-size:calc(15px * var(--tz));">protege agentes em abordagens</p></div>
      </div>""")))

slide(19, 3, "Conportos e CEPAI/SP", "Inteligência · Segurança portuária", "Segurança portuária em rede",
      '  <div class="flex-1 px-16 pb-4 grid grid-cols-3 gap-6 min-h-0" style="align-items:stretch; align-content:center; padding-top:60px; padding-bottom:60px;">\n'
      + card("fa-shield-halved", "Conportos", "Comissão Nacional de Segurança Pública nos Portos, Terminais e Vias Navegáveis. Reúne Marinha, Polícia Federal, ANTAQ e outros para coordenar a segurança portuária.", "")
      + card("fa-list-check", "O que a Conportos faz", "Grupo de Trabalho do Código ISPS, Declaração de Cumprimento para terminais e o Curso Nacional de Auditoria em Instalação Portuária.", "")
      + card("fa-people-group", "CEPAI/SP", "Comissão Estadual de Prevenção de Acidentes e Incidentes: fórum técnico em Santos e São Sebastião, que integra agentes portuários e órgãos reguladores.", "")
      + "\n  </div>")

# ---------------------------------------------------------------------------
# Fecho — Do plano ao campo (slide 20)
# ---------------------------------------------------------------------------
slide(20, 4, "Do plano ao campo", "Dia de Fiscal · Visita técnica", "Do plano ao campo",
      wrap(
          col(7, """
      <p class="sec">Perguntas para fazer ao fiscal durante a visita</p>
      """ + card("fa-bullseye", "Por que esta instalação?", "Qual faixa de risco, qual categoria do PAF e qual fator a trouxe para a lista.") + """
      """ + card("fa-stairs", "Qual nível de ação é este?", "O que se verifica em campo, e o que já foi resolvido à distância ou por monitoramento.") + """
      """ + card("fa-mobile-screen", "Como se registra?", "Como o SFIS Mobile e os demais sistemas entram no trabalho de campo.") + """
      """ + card("fa-satellite", "O que a inteligência acrescentou?", "Imagens, alertas e bases consultadas antes de chegar ao local."))
          + "\n" + col(5, """
      <div class="destaque"><p class="font-montserrat font-bold" style="font-size:calc(24px * var(--tz));">Seu papel na visita</p>
        <p style="font-size:calc(19px * var(--tz)); color:#DBEAFE; margin-top:8px !important;">Você acompanha e observa. <b style="color:#FFD700;">Não compõe a equipe de fiscalização</b> e não elabora atos como notificações, autos de infração ou interdições.</p></div>
      """ + card("fa-helmet-safety", "Segurança primeiro", "Se for preciso, a SFC cede o EPI adicional para acompanhar a fiscalização.") + """
      """ + card("fa-comments", "Troca de experiências", "Ao final, os grupos compartilham o que viveram, e a Gerência Regional apresenta seu trabalho.", "card-gold"))))


# ---------------------------------------------------------------------------
# Divisórias de bloco — espelham o deck do PAF (KIT, seção 7.1)
# ---------------------------------------------------------------------------
DIVISOR = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>{title}</title>
<link rel="icon" type="image/png" href="favicon.png">
<link rel="icon" type="image/x-icon" href="favicon.ico">
<link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&family=Open+Sans:wght@400;600&display=swap" rel="stylesheet"/>
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet"/>
<style>
body {{ margin:0; padding:0; overflow:hidden; font-family:'Open Sans',sans-serif; }}
.slide {{ width:100vw; height:100vh; position:relative; display:flex; flex-direction:column; overflow:hidden;
  background:linear-gradient(135deg, #002244 0%, #003366 50%, #004488 100%); color:white; }}
.font-montserrat {{ font-family:'Montserrat',sans-serif; }}
.accent-left-gold {{ position:absolute; left:0; top:0; width:12px; height:100%; background:#FFD700; z-index:20; }}
.accent-left-blue {{ position:absolute; left:12px; top:0; width:4px; height:100%; background:#0066CC; z-index:20; }}
.shape-circle {{ position:absolute; border-radius:50%; z-index:0; }}
.shape-1 {{ width:620px; height:620px; top:-180px; right:-160px; border:60px solid rgba(255,255,255,0.03); }}
.shape-2 {{ width:420px; height:420px; bottom:-140px; right:18%; border:40px solid rgba(255,255,255,0.03); }}
.bg-pattern {{ background-image:radial-gradient(rgba(255,255,255,0.05) 1px, transparent 1px); background-size:22px 22px; }}
.module-num {{ font-family:'Montserrat',sans-serif; font-weight:900; line-height:0.9; font-size:188px;
  letter-spacing:-4px; color:#FFD700; text-shadow:0 8px 24px rgba(0,0,0,0.35); }}
.seal {{ display:inline-flex; align-items:center; gap:16px;
  background:linear-gradient(90deg, rgba(255,215,0,0.16) 0%, rgba(255,215,0,0.04) 100%);
  border:2px solid rgba(255,215,0,0.55); border-radius:999px; padding:16px 34px; }}
.chip {{ display:flex; align-items:center; gap:18px; background:rgba(255,255,255,0.07);
  border:1px solid rgba(255,255,255,0.14); border-radius:16px; padding:22px 22px; }}
.chip-icon {{ width:64px; height:64px; border-radius:14px; flex-shrink:0; display:flex; align-items:center;
  justify-content:center; font-size:28px; background:rgba(0,102,204,0.30); color:#7CC0FF; }}
.chip-text {{ font-family:'Montserrat',sans-serif; font-weight:600; color:#FFFFFF; font-size:22px; line-height:1.25; margin:0; }}
</style>
</head>
<body>
<div class="slide">
  <div class="accent-left-gold"></div>
  <div class="accent-left-blue"></div>
  <div class="shape-circle shape-1"></div>
  <div class="shape-circle shape-2"></div>
  <div class="absolute inset-0 bg-pattern"></div>
  <img src="assets/logo-antaq-branca.png" alt="" class="absolute"
       style="top:42%; left:66%; width:48vw; max-width:720px; transform:translate(-50%,-50%); opacity:0.05; z-index:0; pointer-events:none;"/>
  <div class="absolute text-white z-0" style="bottom:-60px; right:-40px; font-size:500px; line-height:0; opacity:0.05; transform:translate(8%,8%);">
    <i class="fas {icone}"></i>
  </div>

  <div class="absolute z-10 flex items-center gap-4" style="top:56px; left:96px;">
    <img src="assets/logo-antaq-branca.png" alt="Logo ANTAQ" style="height:52px; width:auto;"/>
    <div style="border-left:1px solid rgba(255,255,255,0.20); padding-left:18px;">
      <p class="font-montserrat font-bold uppercase" style="font-size:18px; letter-spacing:.18em; color:#BFDBFE;">Dia de Fiscal 2026</p>
      <p class="font-montserrat font-semibold uppercase" style="font-size:17px; letter-spacing:.12em; color:#93C5FD; opacity:.85;">Planejamento e inteligência das fiscalizações</p>
    </div>
  </div>

  <div class="relative z-10 flex-1 flex flex-col justify-center" style="padding-left:96px; padding-right:80px; padding-top:96px; padding-bottom:24px;">
    <div class="flex items-center gap-4" style="margin-bottom:26px;">
      <div style="width:72px; height:4px; background-color:#FFD700;"></div>
      <p class="font-montserrat font-semibold uppercase" style="font-size:22px; letter-spacing:.3em; color:#BFDBFE;">Módulo</p>
    </div>
    <div class="flex items-end" style="gap:40px; margin-bottom:46px;">
      <span class="module-num">{num}</span>
      <div style="border-left:5px solid rgba(255,215,0,0.55); padding-left:36px; padding-bottom:10px;">
        <h1 class="font-montserrat font-black text-white" style="font-size:80px; line-height:1.06; letter-spacing:-1.5px;">{titulo}</h1>
        <p class="font-montserrat" style="font-size:30px; font-weight:400; line-height:1.4; color:#DBEAFE; max-width:1300px; margin-top:16px;">{resumo}</p>
      </div>
    </div>
    <div class="grid grid-cols-{ncol}" style="gap:20px; max-width:1640px;">
{chips}
    </div>
    <div style="margin-top:44px;">
      <span class="seal"><i class="fas fa-file-lines" style="color:#FFD700; font-size:28px;"></i>
        <span class="font-montserrat" style="font-size:26px; font-weight:700; color:#fff;">{base_doc}</span></span>
    </div>
  </div>

  <div class="relative z-10 flex justify-between items-end" style="padding:0 96px 32px;">
    <p class="font-montserrat" style="font-size:18px; color:#BFDBFE; opacity:.75;">{rodape}</p>
    <p class="font-mono" style="font-size:18px; color:#BFDBFE; opacity:.75;">{n} / {total}</p>
  </div>
</div>
<script>document.addEventListener("keydown",function(e){{if(["ArrowRight","ArrowLeft","PageDown","PageUp","Home","End"," ","f","F"].indexOf(e.key)!==-1){{e.preventDefault();window.parent.postMessage({{type:"slide-nav",key:e.key}},"*");}}}});</script>
</body>
</html>
"""


def divisor(n, num, titulo, resumo, icone, chips, base_doc):
    html_chips = "\n".join(
        f'      <div class="chip"><div class="chip-icon"><i class="fas {ic}"></i></div><p class="chip-text">{tx}</p></div>'
        for ic, tx in chips)
    (DST / f"slide-{n:02d}.html").write_text(DIVISOR.format(
        title=f"Módulo {int(num)} — {titulo}", num=num, titulo=titulo, resumo=resumo, icone=icone,
        chips=html_chips, ncol=len(chips), base_doc=base_doc, rodape=RODAPE, n=n, total=TOTAL), encoding="utf-8")
    print(f"slide-{n:02d}.html (divisória)")


divisor(3, "01", "Planejamento da fiscalização",
        "Como a ANTAQ decide onde, quando e com que intensidade fiscalizar.", "fa-clipboard-list",
        [("fa-sitemap", "Quem planeja"), ("fa-stairs", "Responsiva e em 3 níveis"), ("fa-gauge-high", "Risco e IPR"),
         ("fa-list-ol", "Priorizar o que verificar"), ("fa-laptop-code", "Sistemas e painéis")],
        "Plano de Fiscalização (PPF) 2025–2028")
divisor(9, "02", "O PAF: plano anual",
        "O que vai a campo no ano, e por quê: a proposta do PAF 2027, em construção.", "fa-calendar-check",
        [("fa-calendar-days", "O que é o PAF"), ("fa-eye", "IPR 2.0"), ("fa-list-check", "O que entra em 2027"),
         ("fa-layer-group", "Temáticas e operacionais")],
        "Minuta da NT de Metodologia do PAF 2027 · NT nº 27/2026/GPF/SFC")
divisor(15, "03", "Inteligência da fiscalização",
        "Parcerias e fontes que ampliam a detecção, a análise e a atuação do fiscal.", "fa-satellite-dish",
        [("fa-brain", "SISBIN"), ("fa-satellite", "RedeMAIS"), ("fa-database", "SINESP / INFOSEG"),
         ("fa-anchor", "Conportos e CEPAI/SP")],
        "Decreto nº 11.693/2023 · Portaria GAB/DG/ABIN nº 926/2023")


def render(s):
    css = f':root {{ --tz-base: {s["base"]:.4g}; }}\n' + BASE_CSS + s["extra_css"]
    tag, ico = MODULOS[s["mod"]]
    return HEAD.format(title=f'{s["title"]} — Dia de Fiscal 2026', css=css, kicker=s["kicker"], titulo=s["titulo"],
                       tag=tag, tagico=ico, body=s["body"], rodape=RODAPE, n=s["n"], total=TOTAL)


for s in sorted(SLIDES, key=lambda s: s["n"]):
    (DST / f"slide-{s['n']:02d}.html").write_text(render(s), encoding="utf-8")
    print(f"slide-{s['n']:02d}.html")
