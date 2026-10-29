#!/usr/bin/env python3
"""Genera index.html a partir de datos.py. Uso: python3 build.py"""
from html import escape as e
from pathlib import Path

import datos as D

GEO = {"col": "Colombia", "latam": "Latinoamérica", "global": "Global", "eeuu": "EE.UU."}
NIVEL = {
    "o": ("Fuente original", "Leído en la publicación del autor del estudio."),
    "e": ("Fuente original (extracto)", "Leído en un extracto público de la publicación del autor."),
    "t": ("Citado por un tercero", "Un medio o asociación cita el estudio; no se vio la base original."),
    "p": ("Pronóstico u observación", "Previsión, selección de productos u observación de feria; no mide ventas."),
}
USADAS = set()


def fuente(clave):
    USADAS.add(clave)
    nombre, url, fecha = D.S[clave]
    return f'<a href="{e(url)}" target="_blank" rel="noopener">{e(nombre)}</a>, {e(fecha)}'


def fmt(x, dec=0):
    s = f"{x:,.{dec}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return s


TITULOS = {c["id"]: c["titulo"] for c in D.CONSUMIDOR + D.SNACKS + D.IDEAS}
TITULOS.update({"mercado": "El mercado en cifras", "col-reg": "Regulación en Colombia"})


def rel_links(ids):
    if not ids:
        return ""
    links = " · ".join(f'<a href="#{i}" class="rel">{e(TITULOS[i])}</a>' for i in ids)
    return f'<p class="rels"><span>Relacionado:</span> {links}</p>'


# ---------- gráficos SVG ----------

def mini_bars(m):
    w, h, pad_b, pad_t = 260, 120, 22, 18
    n = len(m["datos"])
    bw, gap = 46, 2
    slot = (w - 20) / n
    out = [f'<svg viewBox="0 0 {w} {h}" class="mini" role="img" aria-label="{e(m["titulo"])}">']
    base = h - pad_b
    out.append(f'<line x1="10" x2="{w-10}" y1="{base}" y2="{base}" class="axis"/>')
    for i, (lab, v) in enumerate(m["datos"]):
        x = 10 + slot * i + (slot - bw) / 2
        bh = (base - pad_t) * v / m["max"]
        y = base - bh
        tip = f'{lab}: {fmt(v)}{m["unidad"]}'
        out.append(f'<path d="{bar_path(x, y, bw, bh)}" class="mark" data-tip="{e(tip)}"/>')
        out.append(f'<text x="{x+bw/2}" y="{y-5}" class="val" text-anchor="middle">{fmt(v)}{m["unidad"]}</text>')
        out.append(f'<text x="{x+bw/2}" y="{h-6}" class="lab" text-anchor="middle">{e(lab)}</text>')
    out.append("</svg>")
    return (f'<figure class="minifig"><figcaption class="mt">{e(m["titulo"])}</figcaption>{"".join(out)}'
            f'<figcaption class="src">Fuente: {fuente(m["fuente"])}</figcaption></figure>')


def bar_path(x, y, w, h, r=4):
    """Barra vertical con extremo de datos redondeado (arriba) y base recta."""
    r = min(r, w / 2, h)
    return (f"M{x:.1f},{y+h:.1f} V{y+r:.1f} Q{x:.1f},{y:.1f} {x+r:.1f},{y:.1f} "
            f"H{x+w-r:.1f} Q{x+w:.1f},{y:.1f} {x+w:.1f},{y+r:.1f} V{y+h:.1f} Z")


def hbar_path(x0, y, length, h, r=4):
    """Barra horizontal anclada en x0; extremo redondeado en la punta (length puede ser negativo)."""
    r = min(r, abs(length), h / 2)
    if length >= 0:
        x1 = x0 + length
        return (f"M{x0:.1f},{y:.1f} H{x1-r:.1f} Q{x1:.1f},{y:.1f} {x1:.1f},{y+r:.1f} V{y+h-r:.1f} "
                f"Q{x1:.1f},{y+h:.1f} {x1-r:.1f},{y+h:.1f} H{x0:.1f} Z")
    x1 = x0 + length
    return (f"M{x0:.1f},{y:.1f} H{x1+r:.1f} Q{x1:.1f},{y:.1f} {x1:.1f},{y+r:.1f} V{y+h-r:.1f} "
            f"Q{x1:.1f},{y+h:.1f} {x1+r:.1f},{y+h:.1f} H{x0:.1f} Z")


def tabla(cabeceras, filas):
    th = "".join(f"<th>{e(c)}</th>" for c in cabeceras)
    tr = "".join("<tr>" + "".join(f"<td>{e(str(c))}</td>" for c in f) + "</tr>" for f in filas)
    return f'<details class="tabla"><summary>Ver tabla</summary><table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></details>'


def figura(titulo, sub, svg, fuente_html, tabla_html, nota=""):
    nota = f'<p class="nota">{nota}</p>' if nota else ""
    return (f'<figure class="chart"><h4>{e(titulo)}</h4><p class="sub">{e(sub)}</p>{svg}{nota}'
            f'<figcaption class="src">Fuente: {fuente_html}</figcaption>{tabla_html}</figure>')


def chart_produccion():
    w, h = 640, 300
    l, r, t, b = 44, 70, 20, 34
    pts = D.PRODUCCION
    n = len(pts)
    ymax = 7
    x = lambda i: l + (w - l - r) * i / (n - 1)
    y = lambda v: t + (h - t - b) * (1 - v / ymax)
    o = [f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="Producción mundial de frutos secos de árbol por temporada">']
    for g in range(0, ymax + 1):
        o.append(f'<line x1="{l}" x2="{w-r}" y1="{y(g):.1f}" y2="{y(g):.1f}" class="{"axis" if g == 0 else "grid"}"/>')
        o.append(f'<text x="{l-8}" y="{y(g)+4:.1f}" class="lab" text-anchor="end">{g}</text>')
    for i, (lab, v) in enumerate(pts):
        if i % 2 == 0 or i == n - 1:
            o.append(f'<text x="{x(i):.1f}" y="{h-10}" class="lab" text-anchor="middle">{e(lab)}</text>')
    path = " ".join(f'{"M" if i == 0 else "L"}{x(i):.1f},{y(v):.1f}' for i, (_, v) in enumerate(pts))
    o.append(f'<path d="{path}" class="line"/>')
    o.append(f'<line class="guide" x1="0" x2="0" y1="{t}" y2="{h-b}"/>')
    for i, (lab, v) in enumerate(pts):
        o.append(f'<circle cx="{x(i):.1f}" cy="{y(v):.1f}" r="4" class="dot" data-i="{i}"/>')
    # etiquetas directas: inicio, máximo y final
    o.append(f'<text x="{x(0)+4:.1f}" y="{y(pts[0][1])+22:.1f}" class="val" text-anchor="start">3,78 Mt</text>')
    o.append(f'<text x="{x(9):.1f}" y="{y(pts[9][1])-12:.1f}" class="val" text-anchor="middle">6,02 Mt récord</text>')
    o.append(f'<text x="{x(n-1)+8:.1f}" y="{y(pts[-1][1])+18:.1f}" class="val" text-anchor="start">5,93</text>')
    step = (w - l - r) / (n - 1)
    for i, (lab, v) in enumerate(pts):
        tip = f'Temporada 20{lab.replace("*", "")}: {fmt(v, 2)} millones de t' + (" (estimado)" if "*" in lab else "")
        o.append(f'<rect class="hit" tabindex="0" aria-label="{e(tip)}" x="{x(i)-step/2:.1f}" y="{t}" width="{step:.1f}" height="{h-t-b}" '
                 f'data-tip="{e(tip)}" data-gx="{x(i):.1f}" data-i="{i}"/>')
    o.append("</svg>")
    filas = [(f"20{lab}", fmt(v, 2)) for lab, v in pts]
    return figura("La producción mundial creció 57% en diez años",
                  "Frutos secos de árbol, millones de toneladas (sin maní). Peso sin cáscara, excepto pistacho con cáscara. *2025/26 estimado.",
                  "".join(o), fuente("inc_ar"),
                  tabla(["Temporada", "Millones de t"], filas))


def chart_pistacho():
    w, h = 640, 280
    l, r, t, b = 50, 20, 30, 36
    ymax = 2000
    y = lambda v: t + (h - t - b) * (1 - v / ymax)
    n = len(D.PISTACHO)
    slot = (w - l - r) / n
    bw = 90
    o = [f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="Cosecha de pistacho de Estados Unidos">',
         '<defs><pattern id="hatch" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
         '<rect width="7" height="7" class="hatchbg"/><line x1="0" y1="0" x2="0" y2="7" class="hatchln"/></pattern></defs>']
    for g in range(0, ymax + 1, 500):
        o.append(f'<line x1="{l}" x2="{w-r}" y1="{y(g):.1f}" y2="{y(g):.1f}" class="{"axis" if g == 0 else "grid"}"/>')
        o.append(f'<text x="{l-8}" y="{y(g)+4:.1f}" class="lab" text-anchor="end">{fmt(g)}</text>')
    base = y(0)
    for i, (lab, v, vmax) in enumerate(D.PISTACHO):
        x = l + slot * i + (slot - bw) / 2
        if vmax:
            top = vmax
            o.append(f'<path d="{bar_path(x, y(vmax), bw, base - y(vmax))}" fill="url(#hatch)" class="proj"/>')
            texto = f"{fmt(v)}–{fmt(vmax)}"
            tip = f"{lab}: entre {fmt(v)} y {fmt(vmax)} millones de libras"
        else:
            top = v
            o.append(f'<path d="{bar_path(x, y(v), bw, base - y(v))}" class="mark"/>')
            texto = fmt(v)
            tip = f"{lab}: {fmt(v)} millones de libras"
        o.append(f'<text x="{x+bw/2:.1f}" y="{y(top)-8:.1f}" class="val" text-anchor="middle">{texto}</text>')
        o.append(f'<text x="{x+bw/2:.1f}" y="{h-12}" class="lab" text-anchor="middle">{e(lab)}</text>')
        o.append(f'<rect class="hit" tabindex="0" aria-label="{e(tip)}" x="{l+slot*i:.1f}" y="{t}" width="{slot:.1f}" height="{base-t:.1f}" data-tip="{e(tip)}"/>')
    o.append("</svg>")
    filas = [(lab, fmt(v) if not vm else f"{fmt(v)}–{fmt(vm)}") for lab, v, vm in D.PISTACHO]
    return figura("Pistacho de EE.UU.: cosecha corta estimada en 2026 y recuperación potencial en 2027",
                  "Millones de libras. 2026 es una estimación del sector; la barra rayada es un escenario condicionado al clima.",
                  "".join(o), fuente("pist_crop"), tabla(["Año", "Millones de lb"], filas),
                  nota="Nutlink reportó cerca de US$4,57 por libra en marzo de 2026, máximo de ocho años; no es una cotización de compra para Colombia (" + fuente("nutlink") + ").")


def chart_cambio():
    w = 640
    rows = D.CAMBIO_2627
    rh, gap = 26, 8
    t, b = 10, 28
    h = t + b + len(rows) * (rh + gap)
    lab_w = 130
    lo, hi = -40, 90
    x = lambda v: lab_w + (w - lab_w - 56) * (v - lo) / (hi - lo)
    o = [f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="Cambio previsto de producción 2026/27 por fruto seco">']
    for g in (-40, -20, 0, 20, 40, 60, 80):
        o.append(f'<line x1="{x(g):.1f}" x2="{x(g):.1f}" y1="{t}" y2="{h-b}" class="{"axis" if g == 0 else "grid"}"/>')
        o.append(f'<text x="{x(g):.1f}" y="{h-8}" class="lab" text-anchor="middle">{g:+d}%</text>'.replace("+0%", "0%"))
    for i, (nombre, v) in enumerate(rows):
        yy = t + i * (rh + gap)
        cls = "mark" if v >= 0 else "neg"
        o.append(f'<text x="{lab_w-10}" y="{yy+rh/2+5:.1f}" class="lab strong" text-anchor="end">{e(nombre)}</text>')
        o.append(f'<path d="{hbar_path(x(0), yy, x(v)-x(0), rh)}" class="{cls}"/>')
        val = f"{'+' if v >= 0 else '−'}{fmt(abs(v), 2 if abs(v) < 1 else 0)}%"
        if v >= 0:
            o.append(f'<text x="{x(v)+6:.1f}" y="{yy+rh/2+5:.1f}" class="val" text-anchor="start">{val}</text>')
        else:
            o.append(f'<text x="{x(0)+6:.1f}" y="{yy+rh/2+5:.1f}" class="val" text-anchor="start">{val}</text>')
        o.append(f'<rect class="hit" tabindex="0" aria-label="{e(nombre)}: {val}" x="{lab_w}" y="{yy-gap/2}" width="{w-lab_w}" height="{rh+gap}" data-tip="{e(nombre)}: {val} frente a 2025/26"/>')
    o.append("</svg>")
    leyenda = '<p class="legend"><span class="sw mark-bg"></span>Sube <span class="sw neg-bg"></span>Baja</p>'
    filas = [(n, f"{'+' if v >= 0 else '−'}{fmt(abs(v), 2 if abs(v) < 1 else 0)}%") for n, v in rows]
    return figura("Qué se viene en oferta para 2026/27",
                  "Previsión temprana del INC (mayo de 2026) frente a 2025/26; puede cambiar con la cosecha. Total de frutos de árbol: estable en unos 6 Mt.",
                  leyenda + "".join(o), fuente("inc_macao"), tabla(["Fruto", "Cambio previsto"], filas),
                  nota="Lectura: una menor oferta puede presionar precios (pistacho) y una mayor oferta puede aliviarlos (avellana, nuez de Brasil), pero estos porcentajes no permiten anticipar el costo de compra en Colombia.")


def chart_participacion():
    w = 640
    rows = D.PARTICIPACION
    rh, gap, t, b = 24, 8, 6, 6
    h = t + b + len(rows) * (rh + gap)
    lab_w = 130
    x = lambda v: (w - lab_w - 60) * v / 30
    o = [f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="Participación por fruto seco en la producción mundial">']
    o.append(f'<line x1="{lab_w}" x2="{lab_w}" y1="{t}" y2="{h-b}" class="axis"/>')
    for i, (nombre, v) in enumerate(rows):
        yy = t + i * (rh + gap)
        o.append(f'<text x="{lab_w-10}" y="{yy+rh/2+5:.1f}" class="lab strong" text-anchor="end">{e(nombre)}</text>')
        o.append(f'<path d="{hbar_path(lab_w, yy, x(v), rh)}" class="mark"/>')
        o.append(f'<text x="{lab_w+x(v)+6:.1f}" y="{yy+rh/2+5:.1f}" class="val">{v}%</text>')
        o.append(f'<rect class="hit" tabindex="0" aria-label="{e(nombre)}: {v}%" x="{lab_w}" y="{yy-gap/2}" width="{w-lab_w}" height="{rh+gap}" data-tip="{e(nombre)}: {v}% de la producción 2024/25"/>')
    o.append("</svg>")
    return figura("Almendra, pistacho, marañón y nuez dominan",
                  "Participación en la producción mundial de frutos de árbol, temporada 2024/25. Convención del INC: peso sin cáscara, excepto pistacho con cáscara. No representa ventas.",
                  "".join(o), fuente("inc_ar"), tabla(["Fruto", "%"], rows),
                  nota="“Otros” incluye pecana (2%), macadamia (1%), piñón (1%) y nuez de Brasil (menos de 1%). El maní, que es una leguminosa, se mide aparte: unos 51,8 millones de t con cáscara en 2024/25.")


# ---------- bloques HTML ----------

def tarjeta(c):
    geo = c["geo"]
    tags = "".join(f'<span class="tag geo">{GEO[g]}</span>' for g in geo)
    datos_html = []
    for x in c["datos"]:
        nv, ayuda = NIVEL[x["n"]]
        datos_html.append(f'<li><p>{e(x["t"])}</p><p class="cite">{fuente(x["s"])} '
                          f'<span class="lvl lvl-{x["n"]}" title="{e(ayuda)}">{nv}</span></p></li>')
    mini = mini_bars(c["mini"]) if c.get("mini") else ""
    return f'''<details class="card" id="{c["id"]}" data-geo="{" ".join(geo)}">
<summary><span class="chev" aria-hidden="true"></span><h3>{e(c["titulo"])}</h3><p class="idea">{e(c["idea"])}</p>
<p class="tags">{tags}<span class="tag conf">Confianza: {e(c["conf"])}</span></p></summary>
<div class="body">{mini}
<h4>La evidencia</h4><ul class="ev">{"".join(datos_html)}</ul>
<div class="accion"><h4>Qué significa para un negocio de frutos secos</h4><p>{e(c["accion"])}</p></div>
{rel_links(c.get("rel"))}
<button type="button" class="copy" data-id="{c["id"]}">Copiar enlace a esta tendencia</button>
</div></details>'''


def filtro(seccion):
    return f'''<div class="filtro js-only" role="group" aria-label="Filtrar por dónde se midió el dato" data-sec="{seccion}">
<span class="flabel">Dónde se midió:</span>
<button type="button" class="chip on" data-f="all" aria-pressed="true">Todas</button>
<button type="button" class="chip" data-f="col" aria-pressed="false">Colombia</button>
<button type="button" class="chip" data-f="latam" aria-pressed="false">Latinoamérica</button>
<button type="button" class="chip" data-f="eeuu global" aria-pressed="false">EE.UU. y global</button>
<span class="count" aria-live="polite"></span>
<button type="button" class="toggle-all" data-open="1">Abrir todas</button><button type="button" class="toggle-all" data-open="0">Cerrar todas</button>
</div>'''


def build():
    resumen = "".join(
        f'<div class="idea-card"><span class="num">{i+1}</span><h3>{e(t)}</h3><p>{e(p)}</p>'
        f'<p class="src"><b>Síntesis propia basada en:</b> '
        + "; ".join(f"{fuente(k)} ({e(alc)})" for k, alc in fs) + ".</p>"
        + rel_links(rel) + "</div>"
        for i, (t, p, fs, rel) in enumerate(D.RESUMEN))
    acciones = "".join(f"<li>{e(a)}</li>" for a in D.ACCIONES)
    consumidor = "".join(tarjeta(c) for c in D.CONSUMIDOR)
    snacks = "".join(tarjeta(c) for c in D.SNACKS)
    charts = chart_produccion() + chart_participacion() + chart_cambio() + chart_pistacho()
    tiles = "".join(f'<div class="tile"><p class="big">{e(v)}</p><p>{e(t)}</p><p class="cite">{fuente(s)}</p></div>'
                    for v, t, s in D.COLOMBIA_TILES)
    reg = "".join(f'<div class="reg"><h3>{e(t)}</h3><p>{e(p)}</p><p class="cite">{fuente(s)}</p></div>'
                  for t, p, s in D.REGULACION)
    reg_extra = (f'<p class="cite">Más: {fuente("dian_icui")} · {fuente("infoalim")} · {fuente("andi")} · '
                 f'{fuente("carnotecnia")} · {fuente("invima_810")}</p>')
    ideas = "".join(f'''<details class="card idea" id="{i["id"]}" open><summary><span class="chev" aria-hidden="true"></span>
<p class="when">{e(i["cuando"])}</p><h3>{e(i["titulo"])}</h3><p class="idea">{e(i["que"])}</p></summary>
<div class="body"><p><strong>Por qué:</strong> {e(i["por"])}</p><p><strong>Qué medir:</strong> {e(i["medir"])}</p>
{rel_links(i["rel"])}</div></details>''' for i in D.IDEAS)
    cal = "".join(f'<li><p class="fecha">{e(f)}</p><p>{e(t)}' + (f' <span class="cite">({fuente(s)})</span>' if s else "") + "</p></li>"
                  for f, t, s in D.CALENDARIO)
    senales = "".join(f'<li><strong>{e(t)}.</strong> {e(p)} <span class="cite">({fuente(s)})</span></li>' for t, p, s in D.SENALES)
    coinc = "".join(f"<li>{e(x)}</li>" for x in D.CONSENSO["coinciden"])
    difs = "".join(f'<tr><th scope="row">{e(a)}</th><td>{e(b)}</td><td>{e(c)}</td></tr>' for a, b, c in D.CONSENSO["difieren"])
    brechas = "".join(f"<li>{e(x)}</li>" for x in D.BRECHAS)
    niveles = "".join(f'<li><span class="lvl lvl-{k}">{n}</span> {e(a)}</li>' for k, (n, a) in NIVEL.items())

    # la lista de fuentes se arma al final, cuando ya se registraron todas las citadas
    fuentes = sorted({(D.S[k][0], D.S[k][1]) for k in USADAS} | set(D.OTRAS_FUENTES), key=lambda x: x[0].lower())
    lista_fuentes = "".join(f'<li><a href="{e(u)}" target="_blank" rel="noopener">{e(n)}</a></li>' for n, u in fuentes)
    n_tend = len(D.CONSUMIDOR) + len(D.SNACKS)

    tpl = Path(__file__).with_name("plantilla.html").read_text(encoding="utf-8")
    html = (tpl.replace("{{CORTE}}", e(D.CORTE)).replace("{{RESUMEN}}", resumen).replace("{{ACCIONES}}", acciones)
            .replace("{{FILTRO_C}}", filtro("consumidor")).replace("{{FILTRO_S}}", filtro("snacks"))
            .replace("{{CONSUMIDOR}}", consumidor).replace("{{SNACKS}}", snacks).replace("{{CHARTS}}", charts)
            .replace("{{TILES}}", tiles).replace("{{REG}}", reg + reg_extra).replace("{{IDEAS}}", ideas)
            .replace("{{CAL}}", cal).replace("{{SENALES}}", senales).replace("{{COINC}}", coinc).replace("{{DIFS}}", difs)
            .replace("{{BRECHAS}}", brechas).replace("{{NIVELES}}", niveles).replace("{{FUENTES}}", lista_fuentes)
            .replace("{{N_FUENTES}}", str(len(fuentes))).replace("{{N_TEND}}", str(n_tend)))
    assert "{{" not in html, "quedó un marcador sin reemplazar"
    Path(__file__).with_name("index.html").write_text(html, encoding="utf-8")
    print(f"index.html: {len(html)//1024} KB, {n_tend} tendencias, {len(fuentes)} fuentes")


if __name__ == "__main__":
    build()
