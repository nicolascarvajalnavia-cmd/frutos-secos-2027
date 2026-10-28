# Contenido del informe. Niveles de evidencia de cada dato:
#   "o" = fuente original (abierta y leída)
#   "e" = fuente original, leída en un extracto público
#   "t" = citado por un tercero (medio o asociación que cita el estudio)
#   "p" = pronóstico, observación de feria o selección de productos (sin cifra de ventas)
# Geografía de cada tarjeta (según dónde se midió el dato): col, latam, global, eeuu

CORTE = "28 de octubre de 2026"

S = {  # fuentes reutilizadas
    "innova27": ("Innova, Top 10 Trends 2027 (vía Food Ingredients First)", "https://www.foodingredientsfirst.com/news/innova-top-ten-trends-2027-nutrient-density-protein.html", "oct 2026"),
    "innovaC27": ("Innova, Consumer Trends 2027", "https://www.innovamarketinsights.com/press-releases/innova-market-insights-will-host-its-annual-consumer-trends-webinar-on-october-15/", "oct 2026"),
    "wp_col": ("Worldpanel by Numerator, El efecto salud – LATAM 2026", "https://es.worldpanelbynumerator.com/insights/bienestar-salud-consumo-colombia", "sep 2026"),
    "ific_upf": ("IFIC Food & Health Survey 2026", "https://ific.org/media/for-the-first-time-in-21-years-convenience-outranks-health/", "jul 2026"),
    "ific_prot": ("IFIC Food & Health Survey 2026 (salud y proteína)", "https://ific.org/media/trying-harder-yet-feeling-worse-americans-self-reported-health-status-hits-a-record-low/", "oct 2026"),
    "ific_pdf": ("IFIC 2026, informe de nutrición (PDF)", "https://ific.org/wp-content/uploads/2026-IFIC-Food-Health-Survey-Nutrition.pdf", "2026"),
    "euro_prot": ("Euromonitor, proteína y GLP-1", "https://www.euromonitor.com/newsroom/press-releases/july-2026/wellness-trends-and-glp-1s-fuel-protein-market", "jul 2026"),
    "niq_snack": ("NIQ, The accountability era of snacking", "https://nielseniq.com/global/en/insights/analysis/2026/the-accountability-era-of-snacking/", "jul 2026"),
    "niq25": ("NIQ, Global Health & Wellness 2025", "https://nielseniq.com/global/en/news-center/2025/niq-report-reveals-2025-global-health-wellness-trends/", "may 2025"),
    "gallup_glp": ("Gallup, uso de GLP-1", "https://news.gallup.com/poll/712157/glp-usage-reaches-new-high.aspx", "jul 2026"),
    "cornell": ("Cornell / Numerator, Journal of Marketing Research", "https://news.cornell.edu/stories/2025/12/ozempic-changing-foods-americans-buy", "dic 2025"),
    "circana": ("Circana, 2026 Global Snack Unwrap", "https://www.circana.com/post/snacking-enters-a-new-era-of-function-fuel-and-fun-as-global-sales-surge-past-record-levels-circa", "jul 2026"),
    "circana_glp": ("Circana vía FreshFruitPortal", "https://www.freshfruitportal.com/news/2026/01/26/glp-1-grocery-circana/", "ene 2026"),
    "mdlz26": ("Mondelēz, State of Snacking 2026", "https://www.mondelezinternational.com/news/the-state-of-snacking-in-2026-6-insights-shaping-how-the-world-eats/", "jun 2026"),
    "mdlz25": ("Mondelēz, Savor each bite (encuesta 2024)", "https://www.mondelezinternational.com/news/savor-each-bite-mindful-snacking-and-prioritizing-portions/index.html", "jun 2025"),
    "mintel27": ("Mintel, 2027 Food & Drink Predictions", "https://www.mintel.com/press-centre/2027-food-and-drink-predictions/", "oct 2026"),
    "fmcg27": ("FMCG Gurus, Top Ten Trends 2027 (PDF)", "https://fmcggurus.com/wp-content/themes/fmcg/static/img/FMCG-Gurus-Top-Ten-Trends-2027.pdf", "2026"),
    "wf26": ("Whole Foods Market, tendencias 2026 (Business Wire)", "https://www.businesswire.com/news/home/20251008117621/en", "oct 2025"),
    "mdlz_sos": ("Mondelēz, State of Snacking (7.ª edición)", "https://www.mondelezinternational.com/stateofsnacking/index.html", "2026"),
    "wf27": ("Whole Foods Market, tendencias 2027", "https://press.aboutamazon.com/2026/10/whole-foods-market-reveals-its-top-food-and-beverage-trend-predictions-for-2027", "oct 2026"),
    "inc_macao": ("INC, Congreso de Macao 2026", "https://inc.nutfruit.org/1300-global-leaders-convene-at-inc-congress-in-macao-to-advance-future-of-nuts-and-dried-fruit/", "may 2026"),
    "inc_ar": ("INC, Annual Report 2025 (PDF, pág. 32)", "https://inc.nutfruit.org/wp-content/uploads/2026/04/2025-ANNUAL-REPORT.pdf", "abr 2026"),
    "pist_crop": ("Morning Ag Clips / California Farm Bureau", "https://www.morningagclips.com/growers-harvest-short-pistachio-crop-as-costs-mount/", "oct 2026"),
    "nutlink": ("Nutlink, precios del pistacho", "https://nutlink.org/en/war-in-iran-and-the-rise-of-dubai-chocolate-drive-pistachio-prices-higher/", "abr 2026"),
    "upra": ("UPRA, Boletín de precios (PDF)", "https://upra.gov.co/sites/default/files/2026-01/01_BolPpmS1_20251218.pdf", "dic 2025"),
    "lr_mp": ("La República, marcas propias en Colombia", "https://www.larepublica.co/empresas/el-hard-discount-reina-en-marcas-propias-4241004", "oct 2025"),
    "pym": ("Revista P&M, crema de nueces de Manitoba", "https://www.revistapym.com.co/articulos/comunicacion/96670/manitoba-amplia-su-portafolio-con-el-lanzamiento-de-su-nueva-crema-de-nueces-a-base-de-almendra-y-maranon", "abr 2026"),
    "forbes_mani": ("Forbes Colombia, Manitoba", "https://forbes.co/2026/06/17/negocios/el-emprendimiento-de-colegio-que-se-transformo-en-empresa-la-historia-de-manitoba/", "jun 2026"),
    "dane": ("DANE, boletín IPC septiembre 2026 (PDF)", "https://www.dane.gov.co/files/operaciones/IPC/sep2026/bol-IPC-sep2026.pdf", "oct 2026"),
    "kantar_hog": ("Kantar vía Portafolio", "https://www.portafolio.co/economia/regiones/asi-estan-cambiando-las-compras-de-los-colombianos-mas-canales-mas-salud-y-menos-tiempo-para-cocinar-495878", "jun 2026"),
    "worldpanel_ecom": ("Worldpanel vía Portafolio", "https://www.portafolio.co/negocios/comercio/hogares-compran-menos-pero-gastan-mas-asi-se-movera-el-consumo-en-490214", "mar 2026"),
    "kantar_latam": ("Worldpanel (Kantar), El efecto salud 2025", "https://www.kantar.com/latin-america/inspiracion/consumidor/2025/decodificando-las-tendencias-del-consumo-en-america-latina", "2025"),
    "infobae_gusto": ("Worldpanel vía Infobae", "https://www.infobae.com/colombia/2026/07/16/productos-de-bienestar-y-autocuidado-impulsan-el-consumo-de-los-hogares-en-colombia-durante-2026/", "jul 2026"),
    "sfa": ("Specialty Food Association", "https://www.specialtyfood.com/news-media/news-features/association-press-releases/pink-packaging-pistachio-and-more-trends-noted-by-drexel-food-lab-students-at-the-specialty-food-a/", "ago 2025"),
    "bakery_nuts": ("BakeryandSnacks, tendencias de frutos secos 2026", "https://www.bakeryandsnacks.com/Article/2026/05/27/nutella-lindt-haagen-dazs-lead-2026s-biggest-nut-trends/", "may 2026"),
    "kerry": ("Kerry, Taste Charts 2026", "https://www.kerry.com/insights/kerrydigest/2026/taste-charts-2026", "ene 2026"),
    "innova_street": ("Innova, Beyond the Snack", "https://www.innovamarketinsights.com/trends/beyond-the-snack-expanding-function-flavor-and-format/", "oct 2026"),
    "fn_pb": ("FoodNavigator, mantequilla de maní (datos SPINS)", "https://www.foodnavigator.com/Article/2026/06/03/peanut-butter-market-growth-driven-by-protein-snacking-trend/", "jun 2026"),
    "snb26": ("Snack Food & Wholesale Bakery (datos Circana)", "https://www.snackandbakery.com/articles/116073-state-of-the-industry-2026-nuts-and-snack-mixes-gain-ground", "2026"),
    "fp_hull": ("Food Processing, IFT FIRST 2026", "https://www.foodprocessing.com/ingredients/article/55401043/novel-ingredients-from-the-ift-food-expo", "ago 2026"),
    "infobae_maranon": ("Infobae (cita informe del ICA)", "https://www.infobae.com/colombia/2026/10/05/que-es-el-maranon-y-por-que-podria-ser-mas-rentable-que-el-arroz-en-colombia-esto-vale-una-tonelada-de-la-fruta/", "oct 2026"),
    "fn_fiber": ("FoodNavigator (informe de That's It)", "https://www.foodnavigator.com/Article/2026/01/21/why-fiber-is-poised-to-rival-protein-in-snacking/", "ene 2026"),
    "gallup_alc": ("Gallup, consumo de alcohol", "https://news.gallup.com/poll/713534/americans-drinking-remains-record-low.aspx", "ago 2026"),
    "pwc": ("PwC, Voice of the Consumer 2026", "https://www.pwc.com/co/es/publicaciones/consumer-insights-survey.html", "jul 2026"),
    "elcol_snacks": ("El Colombiano (datos Euromonitor y NielsenIQ)", "https://www.elcolombiano.com/negocios/snacks-colombia-15-billones-crecimiento-lacteos-portatiles-EG34765991", "mar 2026"),
    "invima_810": ("Invima, Resolución 2492 de 2022 (normograma)", "https://normograma.invima.gov.co/normograma/compilacion/docs/resolucion_minsaludps_2492_2022.htm", "vigente"),
    "dian_icui": ("DIAN, impuestos saludables", "https://www.dian.gov.co/aduanas/Paginas/Impuestos-Saludables.aspx", "vigente"),
    "dian_5500": ("DIAN, Concepto 5500 de 2024", "https://normograma.dian.gov.co/dian/compilacion/docs/oficio_dian_5500_2024.htm", "2024"),
    "minsalud_pr": ("MinSalud, proyecto de resolución de etiquetado (PDF)", "https://www.minsalud.gov.co/Normatividad_Nuevo/PR%20Etiquetado%20Frontal.pdf", "abr 2026"),
    "infoalim": ("Infoalimentario, proyecto MinSalud", "https://infoalimentario.com/es/novedades-regulatorias/ministry-of-health-proposes-modifying-resolution-810-and-its-front-of-package-fo", "may 2026"),
    "carnotecnia": ("Carnotecnia, sello de ultraprocesado", "https://carnotecnia.com/sello-ultraprocesado/", "sep 2026"),
    "andi": ("La República, la ANDI y el proyecto", "https://www.larepublica.co/empresas/andi-alerta-de-riesgos-por-nuevo-proyecto-de-resolucion-de-etiquetado-de-minsalud-4378997", "abr 2026"),
    "mintel_latam": ("Mintel, Predicciones 2027 LatAm (evento)", "https://www.mintel.com/insights/events/2027-global-food-and-drink-predictions-latam-spanish/", "dic 2026"),
    "usda_tn": ("USDA FAS, Tree Nuts: World Markets and Trade", "https://apps.fas.usda.gov/psdonline/circulars/TreeNuts.pdf", "2026"),
    "gfi": ("GFI con datos SPINS", "https://gfi.org/marketresearch/", "2025"),
    "fn_alpha": ("FoodNavigator (datos NIQ)", "https://www.foodnavigator.com/Article/2026/08/18/what-gen-alpha-wants-from-snacks-according-to-niq/", "ago 2026"),
    "gws": ("Global Wellness Summit, tendencias 2026", "https://www.globalwellnesssummit.com/press/press-releases/global-wellness-summit-releases-10-wellness-trends-for-2026/", "ene 2026"),
    "lilly": ("Eli Lilly, aprobación de Foundayo (orforglipron)", "https://investor.lilly.com/news-releases/news-release-details/fda-approves-lillys-foundayotm-orforglipron-only-glp-1-pill", "abr 2026"),
    "reuters_br": ("Reuters, semaglutida genérica en Brasil", "https://www.reuters.com/legal/litigation/brazil-approves-first-generic-semaglutide-pen-after-ozempic-patent-expiry-2026-05-26/", "may 2026"),
}


def d(texto, fuente, nivel):
    return {"t": texto, "s": fuente, "n": nivel}


RESUMEN = [
    ("Cada bocado tiene que rendir más",
     "El consumidor no quiere comer menos: quiere que lo que come valga la pena. Proteína y fibra de verdad, pocos ingredientes y porción clara. El fruto seco ya trae todo eso; falta contarlo bien."),
    ("El placer no se negocia",
     "Sabor y textura siguen mandando. Dulce-picante, sabores locales, crocante con cremoso. El bienestar que no sabe rico no se recompra."),
    ("En Colombia mandan el precio y la etiqueta",
     "Los frutos secos subieron más del doble que los alimentos en general y el descuento duro crece. Además, un proyecto de MinSalud podría crear un sello de “ultraprocesado” y otro verde de “alimento saludable”."),
]

ACCIONES = [
    "Lanzar una mezcla diaria de 25-30 g, sin sellos, con proteína y fibra en el frente del empaque.",
    "Probar un crocante con sabor local (limón y ají, panela picante) en edición limitada.",
    "Revisar ya las fórmulas frente al posible sello de ultraprocesado, y dejar el pistacho para un piloto pequeño hasta que baje su costo con la cosecha 2027.",
]

CONSUMIDOR = [
    {
        "id": "c-glp1", "titulo": "La era GLP-1: comer menos, pero mejor",
        "idea": "Los medicamentos tipo Ozempic cambian cuánto y qué se compra, y ponen la saciedad y la energía estable en el centro de la conversación, incluso para quien no los usa.",
        "geo": ["eeuu", "col"], "conf": "Alta en EE.UU. · media en Colombia",
        "datos": [
            d("En EE.UU., los adultos que usan hoy un GLP-1 para bajar de peso pasaron del 3% (2024) al 8% (2025) y al 11% (2026).", "gallup_glp", "e"),
            d("Los hogares que empiezan un GLP-1 recortan 5,3% el gasto de supermercado y 10,1% el de snacks salados en seis meses.", "cornell", "e"),
            d("Colombia: el 25% de los hogares conoce los GLP-1, frente al 20% en 2025. Es conocimiento, no uso.", "wp_col", "o"),
        ],
        "mini": {"titulo": "Adultos de EE.UU. que usan GLP-1 para bajar de peso", "unidad": "%", "datos": [("2024", 3), ("2025", 8), ("2026", 11)], "fuente": "gallup_glp", "max": 14},
        "accion": "Pierde el snack salado genérico y de bolsa grande. Gana la porción pequeña y densa en nutrientes: “poco volumen, mucha nutrición”. En Colombia, vigilar y tener el formato listo, sin hacer de esto el eje del negocio y sin promesas médicas.",
        "rel": ["s-metabolico", "s-porcion"],
    },
    {
        "id": "c-proteina", "titulo": "Proteína con criterio; la fibra es la que sigue",
        "idea": "La proteína ya es lo mínimo esperado y empieza a generar dudas cuando viene en polvo y en exceso. La fibra sube rápido, de la mano de la salud intestinal.",
        "geo": ["eeuu", "global"], "conf": "Alta",
        "datos": [
            d("El 70% de los estadounidenses intenta comer proteína. La dieta “alta en proteína” pasó del 4% (2018) al 27% (2026).", "ific_prot", "o"),
            d("Alerta: entre quienes buscan proteína, solo el 53% la obtiene de frutos secos y semillas (68% en 2016).", "ific_pdf", "e"),
            d("Más de un tercio cree que la industria exagera con la proteína.", "niq_snack", "o"),
            d("Euromonitor: “la fibra es la próxima proteína”.", "euro_prot", "o"),
        ],
        "accion": "El fruto seco es proteína y fibra “de verdad”, sin aislados. Hay que recuperar su lugar como fuente de proteína en la cabeza del consumidor y mostrar los gramos de proteína y fibra por porción.",
        "rel": ["s-densidad"],
    },
    {
        "id": "c-upf", "titulo": "Rechazo a los ultraprocesados",
        "idea": "La pregunta ya no es solo cuánta azúcar tiene un producto. Ahora también es cuántos ingredientes tiene y qué tan procesado está. Las apps que escanean etiquetas aceleran el cambio.",
        "geo": ["eeuu", "global"], "conf": "Alta",
        "datos": [
            d("En EE.UU., quienes conocen el término “ultraprocesado” pasaron del 32% (2024) al 52% (2026).", "ific_upf", "o"),
            d("El 41% de los adultos que quieren mejorar su dieta está comiendo menos ultraprocesados (encuesta global, n=21.156).", "euro_prot", "o"),
            d("El 25% usa apps que escanean ingredientes, y el 87% de ellos devuelve el producto a la góndola si sale mal calificado.", "niq_snack", "o"),
        ],
        "mini": {"titulo": "Conocen el término “ultraprocesado” (EE.UU.)", "unidad": "%", "datos": [("2024", 32), ("2025", 44), ("2026", 52)], "fuente": "ific_upf", "max": 100},
        "accion": "Es la mayor ventaja de la categoría. Tostado en seco, de 1 a 3 ingredientes, sin maltodextrina ni saborizantes. En Colombia puede volverse obligatorio en la práctica (ver la sección Colombia).",
        "rel": ["s-minimo", "col-reg"],
    },
    {
        "id": "c-azucar", "titulo": "Menos azúcar y más lectura de etiqueta",
        "idea": "En Colombia el cuidado de la salud ya es mayoría, aunque cada quien lo lleva a su ritmo. El azúcar es lo primero que se mira.",
        "geo": ["col", "global"], "conf": "Alta",
        "datos": [
            d("Colombia: el 76% de los consumidores tiene prácticas de cuidado de la salud (29% muy activos y 47% moderados).", "wp_col", "o"),
            d("Colombia: el 43% se declara “reductor de azúcar”, el 69% de los hogares revisa el azúcar en la etiqueta y el volumen de azúcar comprado bajó 2%.", "wp_col", "o"),
            d("En el mundo, el 59% lee toda o casi toda la información nutricional del empaque.", "innova27", "o"),
        ],
        "accion": "Sin azúcar añadida como norma. En las mezclas, cuidado con la fruta confitada y las coberturas, que son las que suben el azúcar. Ofrecer una entrada fácil para quien empieza y más información para quien ya se cuida.",
        "rel": ["s-minimo", "s-textura"],
    },
    {
        "id": "c-comidas", "titulo": "El snack reemplaza comidas",
        "idea": "El esquema de tres comidas se fragmenta. Hay hogares más pequeños y menos tiempo para cocinar, y el snack se vuelve una mini-comida.",
        "geo": ["eeuu", "col"], "conf": "Alta",
        "datos": [
            d("El 41% de quienes comen snacks en EE.UU. ya reemplazó una comida por snacks.", "mdlz26", "o"),
            d("El 55% de los compradores de EE.UU. come 3 o más snacks al día, 9 puntos más que en 2021.", "circana", "o"),
            d("Colombia: los hogares de una persona son el 20%, y el tiempo para preparar comida bajó a 23 minutos por ocasión.", "kantar_hog", "t"),
        ],
        "accion": "Mezclas pensadas como mini-comida (fruto seco, fruta, semilla y algo de grano), complementos para yogur o avena, y empaques para una persona. Poner la ocasión en el empaque: media mañana, oficina, después del ejercicio.",
        "rel": ["s-porcion"],
    },
    {
        "id": "c-valor", "titulo": "Que valga la pena: el precio manda",
        "idea": "El consumidor sigue presionado por el precio. Compara más y compra menos por impulso, pero paga cuando el beneficio es claro. El mercado se divide entre lo barato y lo premium.",
        "geo": ["col", "eeuu"], "conf": "Alta",
        "datos": [
            d("Por primera vez en 21 años, la conveniencia (61%) supera a la salud (56%) como factor de compra de comida en EE.UU. El sabor (88%) y el precio (78%) siguen arriba.", "ific_upf", "o"),
            d("El 46% compra snacks con menos frecuencia por la inflación, y el 38% reduce las compras por impulso.", "niq_snack", "o"),
            d("Colombia: “frutos secos y nueces” subió 12,46% en el IPC de enero a noviembre de 2025, frente a 5,18% de los alimentos.", "upra", "o"),
            d("Colombia: inflación anual de 6,29% en septiembre de 2026.", "dane", "e"),
        ],
        "accion": "Comunicar el precio por porción, tener formatos pequeños de entrada para la tienda de barrio y el descuento duro, usar mezclas con base de maní y reservar marañón, pistacho y macadamia para el gusto premium.",
        "rel": ["s-valor", "mercado"],
    },
    {
        "id": "c-gustos", "titulo": "Estrés, consuelo y pequeños gustos",
        "idea": "Ante la incertidumbre, la gente busca pausas agradables y gustos pequeños sin culpa. El bienestar también es disfrutar.",
        "geo": ["latam", "col", "global"], "conf": "Media-alta",
        "datos": [
            d("Para el 65%, los pequeños gustos son más importantes que antes.", "innovaC27", "e"),
            d("América Latina: el 37% come o bebe por impulso cuando no se siente bien física o mentalmente.", "kantar_latam", "o"),
            d("Colombia: los momentos de gusto crecieron 9% y los de autocuidado 15%.", "infobae_gusto", "t"),
            d("Dos de cada tres consideran necesarios los snacks para compartir con amigos o familia.", "mdlz_sos", "o"),
        ],
        "accion": "“Gusto mejor”: cacao oscuro con almendra, sabores locales, presentaciones para compartir y regalar. Mensajes de disfrute sin culpa, nunca como remedio contra el estrés.",
        "rel": ["s-sabores", "s-textura"],
    },
    {
        "id": "c-longevidad", "titulo": "Envejecer bien",
        "idea": "El interés pasa de “verse joven” a vivir más años con salud: músculo, corazón, cerebro y autonomía. Y ya no es solo cosa de mayores.",
        "geo": ["eeuu", "global"], "conf": "Media-alta",
        "datos": [
            d("Por primera vez, envejecer de forma saludable es el beneficio más buscado en los alimentos en EE.UU. (53% entre los baby boomers).", "ific_prot", "o"),
            d("El 57% prioriza envejecer bien más que hace cinco años.", "niq25", "o"),
            d("Los lanzamientos con declaración de “envejecer bien” crecieron 55% en un año.", "innova27", "o"),
        ],
        "accion": "Hay respaldo nutricional para hablar de corazón y dieta mediterránea (la nuez es un ícono), pero en Colombia las declaraciones de salud están restringidas. Hablar de alimentación cotidiana y pensar en empaques fáciles de abrir y en texturas como las cremas.",
        "rel": ["s-cremas"],
    },
    {
        "id": "c-confianza", "titulo": "Confianza que se demuestra",
        "idea": "Con tanta desinformación, la confianza se gana con pruebas: origen, análisis y datos claros, sin superlativos vagos.",
        "geo": ["global"], "conf": "Media-alta",
        "datos": [
            d("El 62% es más escéptico ante las declaraciones de salud de las empresas de alimentos, y el 82% pide etiquetas más claras (19 países).", "niq25", "o"),
            d("El 55% confía más en marcas que muestran evidencia científica, pero al 52% le abruma la información científica en el empaque.", "fmcg27", "o"),
            d("El 39% confiaría más si viera resultados de pruebas de calidad o inocuidad.", "innovaC27", "e"),
        ],
        "accion": "Un código QR con el origen del lote y los análisis de calidad (por ejemplo, de aflatoxinas). Composición, alérgenos y porción claros en el frente, sin recargar el empaque.",
        "rel": ["s-origen"],
    },
    {
        "id": "c-sistemas", "titulo": "Bienestar personalizado: apps, IA y rutinas",
        "idea": "La gente combina alimentos, suplementos, apps y relojes para lograr un objetivo (dormir mejor, tener energía estable). Y cada vez le pregunta más a la IA qué comer.",
        "geo": ["global", "eeuu", "col"], "conf": "Media",
        "datos": [
            d("Reino Unido: entre quienes usan alimentos funcionales para cuidar su salud, el 66% también toma suplementos, el 54% usa un monitor de ejercicio y el 37% una app de nutrición.", "mintel27", "o"),
            d("El 23% de los estadounidenses le preguntaría a una IA si un alimento es ultraprocesado.", "ific_upf", "o"),
            d("Colombia: los hogares que compran en línea pasaron del 40% al 57%.", "worldpanel_ecom", "t"),
        ],
        "accion": "Ser legible para personas y para máquinas: fichas de producto completas y consistentes en el comercio electrónico, e ingredientes simples que salgan bien calificados en las apps. No hace falta una app propia.",
        "rel": ["s-minimo"],
    },
]

SNACKS = [
    {
        "id": "s-densidad", "titulo": "Densidad nutricional: proteína y fibra al frente",
        "idea": "Es la tendencia número 1 de Innova para 2027. Los frutos secos traen proteína, fibra y grasas buenas sin añadir nada.",
        "geo": ["global", "eeuu"], "conf": "Alta",
        "datos": [
            d("Los lanzamientos que declaran proteína y fibra a la vez crecieron 15% en un año.", "innova27", "o"),
            d("El 64% de los consumidores de EE.UU. busca más fibra.", "fn_fiber", "t"),
            d("Whole Foods incluyó “Focus on Fiber” en sus tendencias 2026.", "wf26", "p"),
        ],
        "accion": "Gramos de proteína y de fibra por porción en el frente del empaque, y cuánto aporta del requerimiento diario. Subir la fibra con semillas (chía, linaza, ajonjolí) o fruta deshidratada, no con fibra aislada.",
        "rel": ["c-proteina", "idea-mezcla"],
    },
    {
        "id": "s-metabolico", "titulo": "Saciedad y “ventaja metabólica”",
        "idea": "Innova la pone número 4 en 2027. Crecen los productos que prometen energía estable, saciedad y bajo índice glucémico, empujados por los GLP-1.",
        "geo": ["global", "eeuu"], "conf": "Alta global · media en Colombia",
        "datos": [
            d("Lanzamientos “aptos para GLP-1”: +190%. Con saciedad o control del apetito: +34%. Con bajo índice glucémico: +30%.", "innova27", "o"),
            d("Los usuarios de GLP-1 se mueven hacia proteína, frutos secos y granos, y se alejan de lo dulce y lo frito.", "circana", "o"),
            d("Los hogares con GLP-1 ya hacen el 23% de las unidades de alimentos vendidas en EE.UU.; Circana proyecta 35% para 2030.", "circana_glp", "o"),
            d("Matiz: el 56% de los usuarios de GLP-1 en EE.UU. dice que se da más gustos desde que empezó.", "innova27", "o"),
        ],
        "accion": "Porciones de 100 a 150 kcal con proteína, fibra y grasa buena. El argumento es la saciedad y “mucha nutrición en poco volumen”, nunca adelgazar.",
        "rel": ["c-glp1"],
    },
    {
        "id": "s-porcion", "titulo": "Porción controlada y mini-comida",
        "idea": "El empaque ayuda a decidir cuánto comer y cuánto gastar. El formato pequeño sirve al bienestar y al bolsillo a la vez.",
        "geo": ["global", "latam"], "conf": "Alta",
        "datos": [
            d("El 69% busca snacks con porción controlada (encuesta internacional de 2024).", "mdlz25", "o"),
            d("Brasil: el 43% come un snack entre el almuerzo y la comida todos los días.", "mdlz26", "o"),
        ],
        "accion": "Multipacks de porciones individuales y bolsa resellable con guía de porción. Medir recompra, costo del empaque y margen antes de escalar.",
        "rel": ["c-comidas", "c-glp1", "idea-mezcla"],
    },
    {
        "id": "s-minimo", "titulo": "Pocos ingredientes y “sin sellos”",
        "idea": "Una lista corta de ingredientes se lee como señal de calidad, y el fruto seco natural parte con ventaja. En Colombia, no llevar sellos de advertencia ya es un argumento de venta.",
        "geo": ["eeuu", "col"], "conf": "Alta",
        "datos": [
            d("Whole Foods pone el “minimalismo de ingredientes” entre sus 8 tendencias 2027, con ejemplos de mantequilla de pistacho y barras de nueces y semillas.", "wf27", "p"),
            d("Manitoba lanzó en 2026 una crema de almendra y marañón que vende como “libre de sellos”.", "pym", "o"),
        ],
        "accion": "Tostar en seco o con aceite de oliva o alto oleico, y evitar coberturas con exceso de azúcar o sodio. Explicar en la etiqueta por qué la crema natural separa aceite.",
        "rel": ["c-upf", "c-azucar", "col-reg"],
    },
    {
        "id": "s-pistacho", "titulo": "Pistacho: el fruto seco de moda (piloto, no apuesta total)",
        "idea": "El chocolate Dubai lo volvió el sabor estrella de confitería, cremas y panadería, y en 2026 pasó a las grandes marcas. Pero su costo está en máximos.",
        "geo": ["global", "eeuu"], "conf": "Alta (sabor) · media (moda Dubai)",
        "datos": [
            d("“El pistacho es el nuevo fruto seco de moda, desplazando a la almendra”, según observación de feria de la Specialty Food Association.", "sfa", "p"),
            d("En 2026 lanzaron productos de pistacho Lindt, Häagen-Dazs y Costco, entre otros.", "bakery_nuts", "o"),
            d("Precio de US$4,57 por libra en marzo de 2026, el más alto en 8 años.", "nutlink", "o"),
            d("Cosecha de EE.UU.: 1.570 M lb en 2025 (récord), cerca de 655 M lb en 2026 y 1.760 a 1.900 M lb proyectadas para 2027.", "pist_crop", "o"),
        ],
        "accion": "Edición limitada de crema o bocado con pistacho, declarando su proporción real. Mezclas con marañón para bajar el costo. Escalar cuando entre la cosecha de EE.UU. 2027 (septiembre-octubre).",
        "rel": ["mercado", "idea-crema"],
    },
    {
        "id": "s-sabores", "titulo": "Dulce-picante y sabores con acento local",
        "idea": "Miel picante, chile y limón, chamoy: los sabores intensos llegan a los frutos secos. En Colombia, lo mejor es partir de sabores conocidos.",
        "geo": ["global", "latam"], "conf": "Media-alta",
        "datos": [
            d("Lanzamientos dulce-picante: +31%. Ácido-picante: +27%.", "innova27", "o"),
            d("El 55% se interesa por sabores de comida callejera en productos empacados.", "innova_street", "o"),
            d("Kerry ubica lima con chile entre las señales nuevas de snacks en Latinoamérica.", "kerry", "p"),
        ],
        "accion": "Maní o marañón con limón y ají, panela con picante, mango biche con sal y limón. Ediciones limitadas para medir la rotación con poco riesgo.",
        "rel": ["c-gustos", "idea-crocante"],
    },
    {
        "id": "s-textura", "titulo": "La textura es parte del placer",
        "idea": "Crocante con cremoso, clusters y fruta liofilizada: el consumidor quiere gusto y beneficio sin tener que elegir.",
        "geo": ["global"], "conf": "Media-alta",
        "datos": [
            d("El 56% busca combinaciones de texturas interesantes, y los formatos liofilizados crecieron 46%.", "innova27", "o"),
            d("El 67% de los alemanes prefiere snacks que mezclan texturas.", "mdlz26", "o"),
        ],
        "accion": "Clusters de frutos secos con chocolate oscuro y poco azúcar, y fruta liofilizada colombiana (uchuva, mango, fresa) en las mezclas.",
        "rel": ["c-gustos", "idea-crocante"],
    },
    {
        "id": "s-cremas", "titulo": "Cremas y untables, más allá del maní",
        "idea": "La crema de maní se mueve hacia la proteína y aparecen mezclas de almendra, marañón y pistacho, con más usos en el día.",
        "geo": ["eeuu", "col"], "conf": "Media-alta",
        "datos": [
            d("En EE.UU., las ventas de mantequillas de frutos secos bajaron 1%. Jif lanzó una versión de 3 ingredientes con 8 g de proteína.", "fn_pb", "t"),
            d("Colombia: según Nielsen, la crema de almendra crece 30% y la de marañón cerca de 980% (seguramente desde una base muy pequeña).", "pym", "t"),
            d("Manitoba creció 23% en 2025.", "pym", "o"),
        ],
        "accion": "Cremas de mezcla (maní con marañón, almendra con cacao), en formatos individuales o squeeze, con tres usos en la etiqueta: desayuno, fruta y salsa.",
        "rel": ["c-longevidad", "idea-crema"],
    },
    {
        "id": "s-valor", "titulo": "Mezclas inteligentes y marca propia",
        "idea": "La presión del precio y el descuento duro empujan la marca propia. Las mezclas permiten ofrecer variedad y un toque premium a menor costo.",
        "geo": ["eeuu", "col", "global"], "conf": "Alta",
        "datos": [
            d("En EE.UU., las ventas de mezclas y snacks nutritivos crecieron 3,3%, frente a 0,9% de los frutos secos solos.", "snb26", "t"),
            d("La marca propia tiene el 16,6% de las unidades de snacks en EE.UU. y el 46,6% en Europa.", "circana", "o"),
            d("Colombia: más del 80% de lo que vende D1 es marca propia, y en Ara el 41%.", "lr_mp", "o"),
        ],
        "accion": "Base de maní con piezas premium. Decidir si se compite con marca, si se maquila para marca propia o ambas cosas, con líneas separadas.",
        "rel": ["c-valor", "idea-mezcla"],
    },
    {
        "id": "s-origen", "titulo": "Origen y cero desperdicio, con pruebas",
        "idea": "De dónde viene lo que comemos importa cada vez más, y el aprovechamiento de subproductos gana espacio. Colombia tiene historias de origen que contar.",
        "geo": ["eeuu", "col", "global"], "conf": "Media",
        "datos": [
            d("Whole Foods pone el origen (“Terroir's New Territory”) como su tendencia número 1 de 2027, junto a “Zero Waste 2.0”.", "wf27", "p"),
            d("El Almond Board presentó polvo de cáscara de almendra: una porción de granola con él aportó 11 g de fibra.", "fp_hull", "o"),
            d("Colombia: Vichada tiene entre 8.200 y 8.500 hectáreas de marañón, más del 90% de la oferta nacional.", "infobae_maranon", "o"),
        ],
        "accion": "Contar el origen por lote (por ejemplo, marañón del Vichada) solo con trazabilidad real. Aprovechar trozos y partidos para cremas y toppings.",
        "rel": ["c-confianza"],
    },
]

# Gráficos de mercado (cada uno de una sola fuente)
PRODUCCION = [("15/16", 3.78), ("16/17", 4.21), ("17/18", 4.18), ("18/19", 4.44), ("19/20", 4.67),
              ("20/21", 5.49), ("21/22", 5.36), ("22/23", 5.36), ("23/24", 5.68), ("24/25", 6.02), ("25/26*", 5.93)]
CAMBIO_2627 = [("Nuez de Brasil", 81), ("Piñón", 63), ("Avellana", 39), ("Almendra", 3), ("Nuez de nogal", 0.15),
               ("Marañón", -3), ("Maní", -6), ("Pistacho", -36)]
PISTACHO = [("2025", 1570, None), ("2026", 655, None), ("2027 (proyección)", 1760, 1900)]
PARTICIPACION = [("Almendra", 27), ("Pistacho", 20), ("Marañón", 19), ("Nuez de nogal", 19), ("Avellana", 10), ("Otros", 5)]

COLOMBIA_TILES = [
    ("76%", "de los consumidores tiene prácticas de cuidado de la salud", "wp_col"),
    ("43%", "se declara “reductor de azúcar”", "wp_col"),
    ("25%", "de los hogares conoce los GLP-1 (20% en 2025)", "wp_col"),
    ("+12,5%", "subieron los frutos secos en el IPC 2025, frente a +5,2% de los alimentos", "upra"),
    ("COP 8,4 bill.", "valía el mercado de snacks en 2023; crece más de 5% al año", "elcol_snacks"),
    ("Más del 80%", "de las ventas de D1 son marca propia", "lr_mp"),
]

REGULACION = [
    ("Hoy: sellos de advertencia", "Resolución 810 de 2021 y 2492 de 2022. Cinco sellos negros (“exceso en” sodio, azúcares, grasas saturadas o trans, y “contiene edulcorantes”). Solo aplican si el nutriente fue añadido. Un fruto seco natural o tostado en seco no lleva sello; uno salado probablemente lleve el de sodio (umbral de 300 mg por 100 g en sólidos).", "invima_810"),
    ("Hoy: impuesto saludable (ICUI) del 20%", "Ley 2277 de 2022: 10% en 2023, 15% en 2024 y 20% desde 2025. Según la DIAN, aplica a productos ultraprocesados (más de 5 ingredientes o aditivos) con azúcar, sal o grasa añadidas por encima de los umbrales. Un fruto seco solo con sal probablemente no está gravado; uno recubierto y saborizado podría estarlo. Confirmarlo con un tributarista.", "dian_5500"),
    ("En camino: sello de “ultraprocesado” y sello verde", "Proyecto de MinSalud publicado el 21 de abril de 2026: un sello de “ultraprocesado” para productos con ingredientes como maltodextrina o con aditivos “cosméticos” (colorantes, saborizantes, potenciadores), y un sello verde voluntario de “alimento saludable” para alimentos sin procesar o mínimamente procesados. La consulta cerró el 6 de mayo de 2026. A octubre seguía sin expedirse y la ANDI se opone.", "minsalud_pr"),
]

CALENDARIO = [
    ("29 oct 2026", "USDA publica su informe semestral de frutos secos (oferta y precios).", "usda_tn"),
    ("Nov 2026", "Euromonitor suele publicar a inicios de noviembre sus tendencias globales del consumidor del año siguiente.", None),
    ("2 dic 2026", "Mintel presenta en español sus predicciones 2027 para Latinoamérica.", "mintel_latam"),
    ("2027", "Posible expedición de la nueva resolución de etiquetado de MinSalud (sin fecha confirmada).", "infoalim"),
    ("15 ago 2027", "Fecha que fija el borrador para retirar productos que no cumplan, si la resolución se expide así.", "carnotecnia"),
    ("Sep-oct 2027", "Cosecha alta de pistacho en EE.UU.: podría aliviar su precio para el segundo semestre.", "pist_crop"),
]

IDEAS = [
    {
        "id": "idea-mezcla", "cuando": "Primero", "titulo": "Mezcla diaria “mini-comida”",
        "que": "Base de maní con almendra, semillas y fruta deshidratada sin azúcar añadida, en porciones de 25 a 30 g y sin sellos. Gramos de proteína y fibra en el frente del empaque.",
        "por": "Densidad nutricional, porción, valor y el snack que reemplaza comidas.",
        "medir": "Agrado, precio aceptado, recompra y margen.",
        "rel": ["s-densidad", "s-porcion", "s-valor", "c-comidas"],
    },
    {
        "id": "idea-crocante", "cuando": "Primero", "titulo": "Crocante con sabor local",
        "que": "Maní o marañón con limón y ají, o panela con picante, en bolsa individual y resellable. Edición limitada.",
        "por": "Dulce-picante, textura y pequeños gustos.",
        "medir": "Intensidad preferida, ocasión, rotación y costo del empaque.",
        "rel": ["s-sabores", "s-textura", "c-gustos"],
    },
    {
        "id": "idea-sellos", "cuando": "Ya (preventivo)", "titulo": "Auditoría de fórmulas y ficha de confianza",
        "que": "Revisar cada referencia frente a los sellos actuales y al posible sello de ultraprocesado. Ver cuáles podrían optar al sello verde. Añadir un QR con el origen y los análisis del lote.",
        "por": "Rechazo a los ultraprocesados, regulación colombiana y confianza.",
        "medir": "Qué porcentaje del portafolio queda sin sellos y el costo de reformular.",
        "rel": ["col-reg", "c-upf", "c-confianza"],
    },
    {
        "id": "idea-crema", "cuando": "Después", "titulo": "Crema de 2-3 ingredientes y piloto de pistacho",
        "que": "Crema de maní con marañón en squeeze o porción individual, con usos en la etiqueta. Una edición pequeña con pistacho, para escalar cuando baje su costo con la cosecha 2027.",
        "por": "Cremas, pistacho, ingredientes mínimos.",
        "medir": "Uso real en casa, estabilidad de la textura y disposición a pagar.",
        "rel": ["s-cremas", "s-pistacho"],
    },
]

SENALES = [
    ("Leguminosas como rivales", "Whole Foods pone el “boom del fríjol” (lupini, edamame, garbanzo) en 2027. Compiten con los frutos secos en el pasillo de snacks con proteína.", "wf27"),
    ("GLP-1 más baratos", "La primera píldora GLP-1 se aprobó en EE.UU. en abril de 2026 y Brasil ya tiene semaglutida genérica. Si llegan genéricos a Colombia, la adopción podría acelerarse en 2027-2028.", "reuters_br"),
    ("Menos alcohol", "En EE.UU. solo el 54% de los adultos bebe, el mínimo histórico. La picada social sigue, pero con bebidas sin alcohol.", "gallup_alc"),
    ("Sueño y descanso", "El 40% tiene mejorar el sueño entre sus principales objetivos. El vínculo con frutos secos (magnesio) está por validar; nada de promesas.", "pwc"),
    ("Salud femenina y menopausia", "El Global Wellness Summit la puso como tendencia número 1 de 2026. Los datos son sobre todo de suplementos, no de alimentos.", "gws"),
    ("Niños que leen etiquetas", "Los padres en EE.UU. dicen que sus hijos de la generación Alpha ya preguntan por ingredientes y piden snacks con proteína: una oportunidad para loncheras.", "fn_alpha"),
    ("Leche de almendra a la baja", "Las bebidas vegetales caen en EE.UU. y la almendra pierde terreno; solo crecen nichos como el pistacho, desde bases pequeñas.", "gfi"),
]

CONSENSO = {
    "coinciden": [
        "La idea central: comer rico, con ingredientes que se entienden y a un precio que permita repetir la compra.",
        "Densidad nutricional (proteína y fibra juntas), etiqueta corta, porción y valor son lo más sólido para 2027.",
        "El placer (sabor y textura) es parte del bienestar, no lo contrario.",
        "No usar proyecciones de consultoras del tipo “el mercado valdrá US$X en 2034” ni cifras gigantes del “mercado del bienestar” como prueba de demanda.",
        "Separar siempre el dato medido, el pronóstico de terceros y nuestra lectura, y decir dónde se midió cada cifra.",
    ],
    "difieren": [
        ("GLP-1", "Claude lo veía como un motor fuerte; Codex, como una señal a vigilar en Colombia.", "Es un motor global bien documentado. En Colombia solo hay datos de conocimiento (25% de los hogares), no de uso: vigilarlo y tener el formato listo, sin hacerlo el eje."),
        ("Pistacho", "Claude lo ponía como tendencia fuerte; Codex pedía “una prueba, no una apuesta”.", "El sabor sigue en 2027, pero su costo está en máximos de 8 años. Piloto pequeño ahora y escalar con la cosecha de EE.UU. de 2027."),
        ("Colombia", "La investigación de Codex no cubría la regulación ni los costos; la de Claude sí.", "Se incluyen como el factor local más decisivo: sellos, impuesto, proyecto de sello de ultraprocesado y precios."),
        ("Formato", "Codex propuso una sola página con tarjetas desplegables, filtro por geografía y pocas gráficas.", "Se adoptó tal cual. Claude añadió gráficas de mercado de una sola fuente cada una, el calendario y las ideas enlazadas a las tendencias."),
    ],
}

BRECHAS = [
    "No hay datos públicos recientes del consumo de frutos secos en Colombia (frecuencia, motivaciones, participación por tipo). Euromonitor, NielsenIQ y Mintel LatAm están detrás de muro de pago.",
    "No hay datos de uso real de GLP-1 en Colombia, solo de conocimiento.",
    "Las cifras de EE.UU. y de encuestas globales no se trasladan tal cual a Colombia.",
    "Las lecturas sobre sellos e impuestos son orientativas: confirmarlas con un asesor regulatorio y uno tributario, y con análisis de laboratorio de cada producto.",
    "Los crecimientos de lanzamientos (Innova) miden productos nuevos, no ventas.",
]

OTRAS_FUENTES = [
    ("USDA FAS, Tree Nuts: World Markets and Trade", "https://apps.fas.usda.gov/psdonline/circulars/TreeNuts.pdf"),
    ("INC, Global Statistical Review 2025", "https://inc.nutfruit.org/inc-nuts-and-dried-fruit-global-statistical-review-2025-edition-available-now/"),
    ("Innova, Top 10 Food Trends 2027", "https://www.innovamarketinsights.com/trends/top-10-food-trends-2027/"),
    ("Innova, Health & Nutrition Trends 2027", "https://www.innovamarketinsights.com/trends/top-global-health-nutrition-trends-2027-global-market-overview/"),
    ("Mintel, Global Predictions 2027", "https://www.mintel.com/insights/consumer-research/global-consumer-trends/"),
    ("Euromonitor, tendencias del consumidor 2026", "https://www.euromonitor.com/newsroom/press-releases/november-2025/euromonitor-international-unveils-global-consumer-trends-for-2026"),
    ("McKinsey, Future of Wellness", "https://www.mckinsey.com/industries/consumer-packaged-goods/our-insights/future-of-wellness-trends"),
    ("McKinsey, State of the Consumer 2026", "https://www.mckinsey.com/industries/consumer-packaged-goods/our-insights/state-of-consumer"),
    ("NIQ, Snackonomics 4.0 (PDF)", "https://nielseniq.com/wp-content/uploads/sites/4/2026/05/NIQ-Snackonomics-4.0-Part-I-May-2026.pdf"),
    ("ADM, Snacking Report 2026 (PDF)", "https://www.adm.com/globalassets/news/adm-stories/2026/adm_snacking-report_2026.pdf"),
    ("Almond Board, Sensory Satisfaction 2026 (PDF)", "https://www.almonds.org/sites/default/files/2026-02/Almond-Trends-mini%20Inforgraphics-Sensory.pdf"),
    ("Importaco, tendencias con frutos secos 2026", "https://importaconutsinternational.com/en/report-on-trends-and-product-development-with-nuts-2026/"),
    ("RPAC, mercado de la almendra", "https://www.rpacalmonds.com/marketnews/202609"),
    ("Ecofin, marañón en Côte d'Ivoire", "https://www.ecofinagency.com/news-agriculture/0902-52685-ivory-coast-cuts-cashew-prices-6-amid-u-s-market-uncertainty"),
    ("Produce Report, informe del INC", "https://www.producereport.com/article/inc-tree-nut-report-china-strengthens-its-position-global-production-trade"),
    ("Global Wellness Institute, Wellness Economy Monitor", "https://globalwellnessinstitute.org/press-room/press-releases/the-global-wellness-economy-hits-a-record-6-8-trillion-and-is-forecast-to-reach-9-8-trillion-by-2029/"),
    ("KFF, uso de IA para información de salud", "https://www.kff.org/public-opinion/kff-tracking-poll-on-health-information-and-trust-use-of-ai-for-health-information-and-advice/"),
    ("Lilly, Foundayo (orforglipron)", "https://investor.lilly.com/news-releases/news-release-details/fda-approves-lillys-foundayotm-orforglipron-only-glp-1-pill"),
    ("Worldpanel, el consumidor colombiano", "https://es.worldpanelbynumerator.com/insights/el-consumidor-colombiano-redefine-el-mercado-de-consumo-masivo"),
    ("Invima, alerta por productos fraudulentos para bajar de peso", "https://www.invima.gov.co/blog/sala-de-prensa-13/el-invima-alerta-por-aumento-de-productos-fraudulentos-para-bajar-de-peso-comercializados-en-redes-sociales-513"),
    ("DIAN, impuestos saludables", "https://www.dian.gov.co/aduanas/Paginas/Impuestos-Saludables.aspx"),
    ("La República, la ANDI y el proyecto de etiquetado", "https://www.larepublica.co/empresas/andi-alerta-de-riesgos-por-nuevo-proyecto-de-resolucion-de-etiquetado-de-minsalud-4378997"),
]
