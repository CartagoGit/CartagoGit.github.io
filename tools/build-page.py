#!/usr/bin/env python3
"""Generate the static portfolio page.

The page is generated rather than hand-edited so the two languages cannot
drift apart, every technology chip carries its real brand mark, and every
destination link carries the icon of what it is.
"""
import pathlib

SITE = pathlib.Path(__file__).resolve().parent.parent
BRAND = SITE / "assets" / "brand"

# Each entry: (es, en)
T = {
    # ---- hero ----
    "eyebrow_hero": ("Frontend engineer · Angular + SCSS", "Frontend engineer · Angular + SCSS"),
    "hero_role": (
        "Interfaces para sistemas que no se pueden romper",
        "Interfaces for systems that must not break",
    ),
    "hero_lead": (
        "ERP, logística, inventario, personal: las mismas pantallas ocho horas al día, con "
        "permisos que cambian según el rol y reglas que tienen que sobrevivir al trimestre. "
        "<strong>Angular con SCSS</strong>, Ionic cuando hace falta Android, Material para el "
        "sistema de diseño.",
        "ERP, logistics, inventory, workforce: the same screens eight hours a day, with "
        "permissions that shift by role and rules that have to survive the quarter. "
        "<strong>Angular with SCSS</strong>, Ionic when Android is needed, Material for the "
        "design system.",
    ),
    "hero_secondary": (
        "Alrededor, la parte que casi nadie documenta: mentoría, decisiones de arquitectura, "
        "CI, contenedores y las herramientas que me faltaban. Lo que hay en GitHub es el trabajo "
        "de las horas que no son de cliente.",
        "Around it, the part almost nobody documents: mentoring, architecture decisions, CI, "
        "containers, and the tools I was missing. What is on GitHub is the work of the hours that "
        "are not client work.",
    ),
    "cta_work": ("Ver el trabajo", "See the work"),
    "cta_what": ("Qué hago", "What I do"),
    "at_a_glance": ("En una línea", "In one line"),
    "facts": [
        ("Base", "Base", "Angular · SCSS · Ionic · Material"),
        ("Detrás", "Behind", "NestJS · Bun · SQLite"),
        ("Entrega", "Delivery", "Docker · GitLab CI · Actions"),
        ("Rol", "Role", "Mentor · Decisiones técnicas"),
        ("En GitHub", "On GitHub", "25 repos · 3 paquetes"),
    ],

    # ---- work ----
    "eyebrow_work": ("Qué hago", "What I do"),
    "h_work": (
        "Seis cosas que hago, y por qué.",
        "Six things I do, and why.",
    ),
    "pillars": [
        (
            "01 · Front-end operativo",
            "01 · Operational front-end",
            "Las pantallas que se usan ocho horas al día",
            "The screens people use eight hours a day",
            "Comercial, financiero, inventario, logística, personal. Estados que dependen del "
            "rol, informes que no cuadran si el estado se desincroniza, y permisos que hay que "
            "cambiar sin tocar el resto.",
            "Commercial, financial, inventory, logistics, workforce. States that depend on the "
            "role, reports that stop adding up when a state desynchronises, and permissions that "
            "change without touching everything else.",
        ),
        (
            "02 · Web y Android",
            "02 · Web and Android",
            "El mismo código, en el navegador y en el bolsillo",
            "The same code, in the browser and in the pocket",
            "Angular e Ionic, empaquetado con Capacitor. La decisión importante no es la "
            "tecnología: es diseñar para uso repetido, donde cada clic de más se paga treinta "
            "veces al día.",
            "Angular and Ionic, packaged with Capacitor. The important decision is not the "
            "stack: it is designing for repeated use, where every extra click is paid for thirty "
            "times a day.",
        ),
        (
            "03 · Decisiones y mentoría",
            "03 · Decisions and mentoring",
            "Lo que hay que decidir antes de escribir código",
            "What has to be decided before any code is written",
            "Qué se queda en el front y qué baja a un servicio. Qué lleva una puerta de calidad "
            "y qué lleva una decisión escrita. Y el código del equipo cuando la feature aprieta "
            "y ya no da tiempo a hacerlo bien.",
            "What stays in the front-end and what moves to a service. What gets a quality gate "
            "and what gets a written decision. And the team's code when the feature is tight and "
            "there is no time to do it properly.",
        ),
        (
            "04 · CI y contenedores",
            "04 · CI and containers",
            "El mismo entorno en el portátil y en el runner",
            "The same environment on the laptop and on the runner",
            "GitLab CI para el producto, GitHub Actions para lo propio. Imágenes de Node/Bun, "
            "Angular, Ionic y NestJS con las versiones fijadas, porque un «latest» que cambia "
            "un martes es un incidente el miércoles.",
            "GitLab CI for the product, GitHub Actions for my own work. Images for Node/Bun, "
            "Angular, Ionic and NestJS with pinned versions, because a 'latest' that moves on a "
            "Tuesday is an incident on Wednesday.",
        ),
        (
            "05 · Herramientas propias",
            "05 · Own tooling",
            "Construidas porque me faltaban",
            "Built because I was missing them",
            "Un runtime MCP, un análisis estático de APIs, una librería de serialización, un "
            "gestor de secretos. Ninguno salió de una hoja de ruta: salieron todos de un "
            "problema mío de un martes por la tarde.",
            "An MCP runtime, a static analysis engine for APIs, a serialization library, a secret "
            "manager. None of them came off a roadmap: all of them came from one of my problems "
            "on a Tuesday afternoon.",
        ),
        (
            "06 · Lo que hay detrás",
            "06 · What sits behind",
            "Backend suficiente para no delegarlo",
            "Enough backend to not delegate it away",
            "NestJS y Bun para lo que necesita servidor. SQLite cuando el dato es local y "
            "PostgreSQL cuando no. Lo justo para poder tocar el circuito entero sin tener que "
            "pedir permiso a otro equipo.",
            "NestJS and Bun for whatever needs a server. SQLite when the data is local and "
            "PostgreSQL when it is not. Just enough to touch the whole circuit without asking "
            "another team for permission.",
        ),
    ],

    # ---- evidence ----
    "eyebrow_evidence": ("Evidencia", "Evidence"),
    "h_evidence": (
        "Lo que se puede medir, medido.",
        "What can be measured, measured.",
    ),
    "evidence": [
        ("Commits", "Commits", "17.484", "17,484", "en el runtime MCP"),
        ("Líneas de fuente", "Source lines", "628.712", "628,712", "sin contar los tests"),
        ("Líneas de test", "Test lines", "460.854", "460,854", "el 42% del repositorio"),
        ("Paquetes", "Packages", "84", "84", "en un solo monorepo"),
        ("Workflows de CI", "CI workflows", "18", "18", "en el runtime"),
        ("Frameworks", "Frameworks", "25", "25", "detectados desde el código"),
    ],

    # ---- projects ----
    "eyebrow_projects": ("Proyectos", "Projects"),
    "h_projects": (
        "Lo que está en GitHub, y en qué estado.",
        "What is on GitHub, and in which state.",
    ),
    "all_repos": ("Todos", "All"),
    "projects": [
        (
            "assets/delendai.svg", "Runtime MCP", "MCP runtime",
            "DelendAI",
            "Núcleo agnóstico para montar servidores MCP y el cargador de plugins que los "
            "alimenta. Superficie perezosa, errores públicos, datos privados y un ciclo de "
            "propuesta a release alrededor.",
            "An agnostic core for building MCP servers and the plugin loader that feeds them. A "
            "lazy surface, public errors, private data, and a proposal-to-release cycle around "
            "it.",
            [("repo", "https://github.com/CartagoGit/DelendAI"),
             ("releases", "https://github.com/CartagoGit/DelendAI/releases")],
        ),
        (
            "assets/tanit.svg", "Análisis estático", "Static analysis",
            "API Source Tanit",
            "Detecta el framework leyendo el código, recupera los cuerpos de las peticiones de "
            "los esquemas de validación y exporta a Postman, Bruno, Insomnia, HAR, OpenAPI o "
            "cURL. Sin levantar el servidor.",
            "Detects the framework by reading the code, recovers request bodies from validation "
            "schemas, and exports to Postman, Bruno, Insomnia, HAR, OpenAPI or cURL. Without "
            "starting the server.",
            [("repo", "https://github.com/CartagoGit/api-source-tanit"),
             ("releases", "https://github.com/CartagoGit/api-source-tanit/releases")],
        ),
        (
            "assets/quickmodel.png", "Librería", "Library",
            "QuickModel",
            "Transformación automática de tipos y adaptadores de validación sobre una base "
            "SOLID. Los tests pesan más que el código fuente, y es a propósito.",
            "Automatic type transformation and validation adapters over a SOLID base. The tests "
            "weigh more than the source, on purpose.",
            [("repo", "https://github.com/CartagoGit/quickmodel"),
             ("docs", "https://cartagogit.github.io/quickmodel/")],
        ),
        (
            "assets/keyer.svg", "Paquete publicado", "Published package",
            "Keyer",
            "Cifra claves y ficheros de entorno desde la terminal. Publicado en npm y usado para "
            "que ninguna credencial real acabe en un repositorio o en una imagen.",
            "Encrypts keys and environment files from the terminal. Published on npm and used so "
            "that no real credential ends up in a repository or an image.",
            [("repo", "https://github.com/CartagoGit/Keyer"),
             ("package", "https://www.npmjs.com/package/@cartago-git/keyer")],
        ),
        (
            "assets/print-cv.svg", "Aplicación", "Application",
            "Print CV",
            "El currículum como datos validados, en dos idiomas, con un modo de impresión "
            "diseñado alrededor del papel real. Es la aplicación que vive en cartagogit.github.io.",
            "A CV modelled as validated data, in two languages, with a print mode designed around "
            "real paper. This is the application that lives at cartagogit.github.io.",
            [("repo", "https://github.com/CartagoGit/print-cv"),
             ("live", "https://cartagogit.github.io/print-cv/")],
        ),
        (
            "assets/cartago.svg", "Sitio", "Site",
            "Portfolio",
            "Este sitio: Angular zoneless, render en servidor, bilingüe y con el tema del sistema. "
            "El generador de la página está en el propio repositorio.",
            "This site: zoneless Angular, server-rendered, bilingual and following the system "
            "theme. The page generator lives in the repository itself.",
            [("repo", "https://github.com/CartagoGit/portfolio"),
             ("live", "https://cartagogit.github.io")],
        ),
        (
            "assets/docker.svg", "Infraestructura", "Infrastructure",
            "Imágenes de desarrollo",
            "Node/Bun, Angular, Ionic, NestJS y Zsh, con las versiones fijadas. El mismo "
            "entorno en el portátil y en el runner, que es de donde salen casi todos los "
            "problemas de «en mi máquina funciona».",
            "Node/Bun, Angular, Ionic, NestJS and Zsh, with pinned versions. The same environment "
            "on the laptop and on the runner, which is where most 'works on my machine' problems "
            "come from.",
            [("repo", "https://github.com/CartagoGit/DockerNodeBun"),
             ("live", "https://hub.docker.com/u/cartagodocker")],
        ),
        (
            "assets/brand/steam-keys.svg", "Escritorio", "Desktop",
            "Gestor local de claves",
            "Una aplicación de escritorio, Tauri y SQLite, donde las claves no salen del equipo. "
            "El mismo criterio local-first que el resto de mis herramientas.",
            "A desktop application, Tauri and SQLite, where the keys never leave the machine. The "
            "same local-first rule as the rest of my tooling.",
            [("repo", "https://github.com/CartagoGit/steam-keys")],
        ),
        (
            "assets/tanit.svg", "Mods y contenido", "Mods and content",
            "Fabricación de mods",
            "Herramientas y contenido para modificar juegos: formatos binarios, localización y "
            "automatización. Un terreno abierto, con proyectos que van y vienen.",
            "Tools and content for modding games: binary formats, localisation and automation. An "
            "open field, with projects that come and go.",
            [("repo", "https://github.com/CartagoGit/aoe2-mods"),
             ("repo", "https://github.com/CartagoGit/pcfutbol6-mod")],
        ),
    ],

    # ---- stack ----
    "eyebrow_stack": ("Con qué trabajo", "What I work with"),
    "h_stack": (
        "El stack, por capas y no por logotipo.",
        "The stack, by layer and not by logo.",
    ),
    "stack_note": (
        "La capa de arriba es la que uso cada día. Las de abajo están porque en algún momento "
        "hizo falta.",
        "The top layer is what I use every day. The ones below are there because at some point "
        "they were needed.",
    ),

    # ---- contact ----
    "eyebrow_contact": ("Contacto", "Contact"),
    "h_contact": ("Mario Cabrero Volarich", "Mario Cabrero Volarich"),
    "contact_text": (
        "El código abierto, el contexto técnico y los datos de contacto están en GitHub y "
        "LinkedIn.",
        "The open-source work, the technical context and the contact details are on GitHub and "
        "LinkedIn.",
    ),
    "footer_meta": (
        "Front-end · Decisiones · Entrega",
        "Front-end · Decisions · Delivery",
    ),

    # ---- nav (order matches the sections) ----
    "nav": [
        ("Qué hago", "What I do"),
        ("Evidencia", "Evidence"),
        ("Proyectos", "Projects"),
        ("Con qué", "Tools"),
        ("Contacto", "Contact"),
    ],
}

STACK_GROUPS = [
    ("Front-end — a diario", "Front-end — daily", "Angular, SCSS, Ionic y el diseño", "Angular, SCSS, Ionic and the design", [
        ("angular", "Angular"), ("sass", "Sass"), ("ionic", "Ionic"),
        ("typescript", "TypeScript"), ("rxjs", "RxJS"), ("angular", "Material"),
        ("capacitor", "Capacitor"), ("tailwindcss", "Tailwind"),
        ("vue", "Vue"), ("react", "React"),
    ]),
    ("Cuando hace falta servidor", "When a server is needed", "Servicios, datos y contratos", "Services, data and contracts", [
        ("nestjs", "NestJS"), ("bun", "Bun"), ("nodejs", "Node.js"),
        ("postgresql", "PostgreSQL"), ("sqlite", "SQLite"),
        ("mongodb", "MongoDB"), ("zod", "Zod"), ("openapi", "OpenAPI"),
    ]),
    ("Herramientas que construyo", "Tools I build", "Lo que sale de un problema mío", "What comes out of one of my problems", [
        ("model-context-protocol", "MCP"), ("tauri", "Tauri"), ("rust", "Rust"),
        ("godot", "Godot"), ("python", "Python"), ("storybook", "Storybook"),
        ("prime-ng", "PrimeNG"),
    ]),
    ("Calidad y entrega", "Quality and delivery", "Lo que impide que rompa", "What stops it from breaking", [
        ("vitest", "Vitest"), ("playwright", "Playwright"), ("eslint", "ESLint"),
        ("prettier", "Prettier"), ("docker", "Docker"), ("gitlab", "GitLab CI"),
        ("github-actions", "GitHub Actions"), ("linux", "Linux"),
    ]),
    ("Con la IA", "With AI", "Quien propone y quien decide", "Who proposes and who decides", [
        ("claude", "Claude"), ("openai", "Codex"), ("minimax", "MiniMax"),
        ("grok", "Grok"),
    ]),
]

# The icon that says what each destination is.
LINK_ICONS = {
    "repo": ("github", "Repositorio", "Repository"),
    "releases": ("releases", "Releases", "Releases"),
    "docs": ("docs", "Documentación", "Documentation"),
    "live": ("live", "En vivo", "Live"),
    "package": ("package", "npm", "npm package"),
}

SOCIAL = [
    ("github", "GitHub", "https://github.com/CartagoGit", "GitHub profile"),
    ("linkedin", "LinkedIn", "https://www.linkedin.com/in/mario-cabrero-volarich", "LinkedIn profile"),
    ("npm", "npm", "https://www.npmjs.com/~cartago-git", "npm packages"),
    ("docker", "Docker Hub", "https://hub.docker.com/u/cartagodocker", "Docker Hub images"),
]


def i18n(es, en):
    """Both languages of one string, side by side, so the switch can swap them."""
    return f'<span data-lang="es">{es}</span><span data-lang="en">{en}</span>'


def chip(slug, name):
    if not (BRAND / f"{slug}.svg").exists():
        return f"<span>{name}</span>"
    return (
        f'<span class="chip"><img src="assets/brand/{slug}.svg?v=2" alt="" '
        f'width="16" height="16" loading="lazy">{name}</span>'
    )


def link(kind, href):
    slug, es, en = LINK_ICONS[kind]
    return (
        f'<a class="link-pill" href="{href}" target="_blank" rel="noreferrer" '
        f'title="{es} / {en}">'
        f'<img src="assets/brand/{slug}.svg?v=2" alt="" width="15" height="15" loading="lazy">'
        f'<span>{i18n(es, en)}</span>'
        f"</a>"
    )


def build():
    facts = "\n".join(
        f'              <div><dt>{i18n(es, en)}</dt><dd>{value}</dd></div>'
        for es, en, value in T["facts"]
    )

    pillars = "\n".join(
        f'            <article class="pillar reveal">\n'
        f'              <p class="pillar__kicker">{i18n(es_k, en_k)}</p>\n'
        f"              <h3>{i18n(es_t, en_t)}</h3>\n"
        f"              <p>{i18n(es, en)}</p>\n"
        f"            </article>"
        for es_k, en_k, es_t, en_t, es, en in T["pillars"]
    )

    evidence = "\n".join(
        f'            <div class="evidence-grid__item reveal">'
        f"<dt>{i18n(es_k, en_k)}</dt><dd>{i18n(es_v, en_v)}</dd><p>{note}</p></div>"
        for es_k, en_k, es_v, en_v, note in T["evidence"]
    )

    projects = "\n".join(
        f'            <article class="project{" project--feature" if i == 0 else ""} reveal">\n'
        f'              <img class="project__icon{" project__icon--photo" if icon.endswith(".png") else ""}" '
        f'src="{icon}" alt="" width="56" height="56">\n'
        f'              <div class="project__body">\n'
        f'                <p class="project__type">{i18n(es_type, en_type)}</p>\n'
        f"                <h3 class=\"project__title\">{title}</h3>\n"
        f'                <p class="project__text">{i18n(es, en)}</p>\n'
        f"              </div>\n"
        f'              <div class="project__links">'
        + "".join(link(kind, href) for kind, href in links)
        + "</div>\n"
        f"            </article>"
        for i, (icon, es_type, en_type, title, es, en, links) in enumerate(T["projects"])
    )

    stack = "\n".join(
        f'            <article class="stack-group reveal">\n'
        f'              <p class="stack-group__label">{i18n(es_l, en_l)}</p>\n'
        f"              <h3>{i18n(es_t, en_t)}</h3>\n"
        '              <div class="chip-list">'
        + "".join(chip(slug, name) for slug, name in items)
        + "</div>\n"
        f"            </article>"
        for es_l, en_l, es_t, en_t, items in STACK_GROUPS
    )

    social = "\n".join(
        f'            <li>\n'
        f'              <a href="{href}" target="_blank" rel="noreferrer">\n'
        f'                <img src="assets/brand/{slug}.svg?v=2" alt="" width="18" height="18" loading="lazy">\n'
        f"                <span>{label}</span>\n"
        f"              </a>\n"
        f"            </li>"
        for slug, label, href, _aria in SOCIAL
    )

    header_links = "\n".join(
        f'          <a class="icon-link" href="{href}" target="_blank" rel="noreferrer" aria-label="{aria}">\n'
        f'            <img src="assets/brand/{slug}.svg?v=2" alt="" width="17" height="17">\n'
        f"          </a>"
        for slug, _label, href, aria in SOCIAL
    )

    nav = "\n".join(
        f'          <a href="#{target}">{i18n(es, en)}</a>'
        for (es, en), target in zip(T["nav"], ["work", "evidence", "projects", "stack", "contact"])
    )

    return f"""<!doctype html>
<html lang="es" data-theme="dark">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Mario Cabrero Volarich — Frontend engineer · Angular + SCSS</title>
    <meta name="description" content="Mario Cabrero Volarich is a frontend engineer: Angular, SCSS and Ionic for operational applications, plus the tooling, CI and infrastructure to ship them.">
    <meta name="author" content="Mario Cabrero Volarich">
    <meta name="theme-color" content="#070d1c">
    <meta property="og:title" content="Mario Cabrero Volarich — Frontend engineer">
    <meta property="og:description" content="Angular, SCSS and Ionic for operational applications, plus the tooling, CI and infrastructure to ship them.">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://cartagogit.github.io/">
    <meta property="og:image" content="https://cartagogit.github.io/assets/cartago-banner.png">
    <link rel="icon" type="image/svg+xml" href="assets/cartago.svg">
    <link rel="apple-touch-icon" href="assets/cartago.svg">
    <link rel="stylesheet" href="styles.css">
    <script>
      // Applied before the first paint so the page never flashes the wrong
      // theme or language. The visitor's own system settings decide, unless
      // they have already chosen here.
      (function () {{
        try {{
          var storedTheme = localStorage.getItem("cartago-theme");
          var prefersLight = matchMedia("(prefers-color-scheme: light)").matches;
          document.documentElement.dataset.theme = storedTheme || (prefersLight ? "light" : "dark");

          var storedLang = localStorage.getItem("cartago-lang");
          var browserLang = (navigator.language || "en").toLowerCase();
          document.documentElement.lang = storedLang || (browserLang.indexOf("es") === 0 ? "es" : "en");
        }} catch (error) {{}}
      }})();
    </script>
  </head>
  <body>
    <a class="skip-link" href="#main">Skip to content</a>

    <header class="site-header">
      <div class="shell site-header__inner">
        <a class="brand" href="#top" aria-label="Mario Cabrero Volarich — home">
          <img src="assets/cartago.svg" alt="" width="36" height="36" class="brand__mark">
          <span class="brand__name">Cartago</span>
        </a>

        <nav class="site-nav" aria-label="Primary navigation">
{nav}
        </nav>

        <div class="header-tools">
          <div class="toggle" role="group" aria-label="Idioma / Language">
            <button type="button" data-set-lang="es" aria-pressed="true">ES</button>
            <button type="button" data-set-lang="en" aria-pressed="false">EN</button>
          </div>
          <div class="toggle" role="group" aria-label="Tema / Theme">
            <button type="button" data-set-theme="dark" aria-pressed="true">&#9789;</button>
            <button type="button" data-set-theme="light" aria-pressed="false">&#9788;</button>
          </div>
{header_links}
        </div>
      </div>
    </header>

    <main id="main">
      <section class="hero" id="top">
        <div class="shell hero__inner">
          <div class="hero__copy reveal">
            <p class="eyebrow">{i18n(*T["eyebrow_hero"])}</p>

            <h1 class="hero__name">
              <span class="hero__mark">
                <img src="assets/cartago.svg" alt="" width="104" height="104">
              </span>
              <span class="hero__words">
                <span class="hero__first">Mario</span>
                <span class="hero__last">Cabrero Volarich</span>
              </span>
            </h1>

            <p class="hero__rule"><span></span></p>

            <p class="hero__role">{i18n(*T["hero_role"])}</p>
            <p class="hero__lead">{i18n(*T["hero_lead"])}</p>
            <p class="hero__secondary">{i18n(*T["hero_secondary"])}</p>

            <div class="hero__actions">
              <a class="button button--primary" href="#projects">{i18n(*T["cta_work"])}</a>
              <a class="button button--ghost" href="#work">{i18n(*T["cta_what"])}</a>
            </div>
          </div>

          <aside class="hero__panel reveal" aria-label="At a glance">
            <p class="hero__panel-title">{i18n(*T["at_a_glance"])}</p>
            <dl class="facts">
{facts}
            </dl>
          </aside>
        </div>
      </section>

      <section class="section section--work" id="work" aria-labelledby="work-title">
        <div class="shell">
          <div class="section__heading reveal">
            <p class="eyebrow">{i18n(*T["eyebrow_work"])}</p>
            <h2 id="work-title">{i18n(*T["h_work"])}</h2>
          </div>

          <div class="pillar-grid">
{pillars}
          </div>
        </div>
      </section>

      <section class="section section--evidence" id="evidence" aria-labelledby="evidence-title">
        <div class="shell">
          <div class="section__heading reveal">
            <p class="eyebrow">{i18n(*T["eyebrow_evidence"])}</p>
            <h2 id="evidence-title">{i18n(*T["h_evidence"])}</h2>
          </div>
          <dl class="evidence-grid">
{evidence}
          </dl>
        </div>
      </section>

      <section class="section section--projects" id="projects" aria-labelledby="projects-title">
        <div class="shell">
          <div class="section__heading section__heading--row reveal">
            <div>
              <p class="eyebrow">{i18n(*T["eyebrow_projects"])}</p>
              <h2 id="projects-title">{i18n(*T["h_projects"])}</h2>
            </div>
            <a class="text-link" href="https://github.com/CartagoGit?tab=repositories">{i18n(*T["all_repos"])} →</a>
          </div>

          <div class="project-grid">
{projects}
          </div>
        </div>
      </section>

      <section class="section section--stack" id="stack" aria-labelledby="stack-title">
        <div class="shell">
          <div class="section__heading reveal">
            <p class="eyebrow">{i18n(*T["eyebrow_stack"])}</p>
            <h2 id="stack-title">{i18n(*T["h_stack"])}</h2>
            <p class="section__note">{i18n(*T["stack_note"])}</p>
          </div>
          <div class="stack-grid">
{stack}
          </div>
        </div>
      </section>

      <section class="section" id="contact" aria-labelledby="contact-title">
        <div class="shell">
          <div class="contact-card reveal">
            <div class="contact-card__copy">
              <p class="eyebrow">{i18n(*T["eyebrow_contact"])}</p>
              <h2 id="contact-title">{i18n(*T["h_contact"])}</h2>
              <p>{i18n(*T["contact_text"])}</p>
            </div>
            <ul class="social-links">
{social}
            </ul>
          </div>
        </div>
      </section>
    </main>

    <footer class="site-footer">
      <div class="shell site-footer__inner">
        <span>© Mario Cabrero Volarich</span>
        <span class="site-footer__meta">{i18n(*T["footer_meta"])}</span>
      </div>
    </footer>

    <script>
      // ---- theme and language -------------------------------------------------
      const root = document.documentElement;

      document.querySelectorAll("[data-set-theme]").forEach((button) => {{
        button.addEventListener("click", () => {{
          const theme = button.dataset.setTheme;
          root.dataset.theme = theme;
          try {{ localStorage.setItem("cartago-theme", theme); }} catch (error) {{}}
          syncToggles();
        }});
      }});

      document.querySelectorAll("[data-set-lang]").forEach((button) => {{
        button.addEventListener("click", () => {{
          const lang = button.dataset.setLang;
          root.lang = lang;
          try {{ localStorage.setItem("cartago-lang", lang); }} catch (error) {{}}
          syncToggles();
        }});
      }});

      function syncToggles() {{
        document.querySelectorAll("[data-set-theme]").forEach((button) => {{
          button.setAttribute("aria-pressed", String(button.dataset.setTheme === root.dataset.theme));
        }});
        document.querySelectorAll("[data-set-lang]").forEach((button) => {{
          button.setAttribute("aria-pressed", String(button.dataset.setLang === root.lang));
        }});
        const meta = document.querySelector('meta[name="theme-color"]');
        if (meta) meta.content = root.dataset.theme === "light" ? "#eef1f8" : "#060b18";
      }}
      syncToggles();

      // A visitor who changes the system theme after loading gets it applied.
      matchMedia("(prefers-color-scheme: light)").addEventListener("change", (event) => {{
        let stored = null;
        try {{ stored = localStorage.getItem("cartago-theme"); }} catch (error) {{}}
        if (stored) return;
        root.dataset.theme = event.matches ? "light" : "dark";
        syncToggles();
      }});

      // ---- scroll reveal ------------------------------------------------------
      const revealables = document.querySelectorAll(".reveal");
      if ("IntersectionObserver" in window) {{
        const observer = new IntersectionObserver((entries) => {{
          entries.forEach((entry) => {{
            if (!entry.isIntersecting) return;
            entry.target.classList.add("is-visible");
            observer.unobserve(entry.target);
          }});
        }}, {{ rootMargin: "0px 0px -8% 0px", threshold: 0.08 }});
        revealables.forEach((element, index) => {{
          element.style.transitionDelay = `${{ (index % 6) * 55 }}ms`;
          observer.observe(element);
        }});
      }} else {{
        revealables.forEach((element) => element.classList.add("is-visible"));
      }}

      // ---- the nav follows the section you are reading -------------------------
      const sections = [...document.querySelectorAll("main section[id]")];
      const navLinks = [...document.querySelectorAll(".site-nav a")];

      function markActiveSection() {{
        let current = sections[0] ? sections[0].id : "";
        sections.forEach((section) => {{
          if (section.getBoundingClientRect().top <= 140) current = section.id;
        }});
        navLinks.forEach((link) => {{
          link.classList.toggle("is-active", link.getAttribute("href") === `#${{current}}`);
        }});
      }}

      let ticking = false;
      window.addEventListener("scroll", () => {{
        if (ticking) return;
        ticking = true;
        requestAnimationFrame(() => {{
          markActiveSection();
          ticking = false;
        }});
      }}, {{ passive: true }});
      markActiveSection();
    </script>
  </body>
</html>
"""


page = build()
(SITE / "index.html").write_text(page, encoding="utf-8")
print("written", len(page), "bytes")
print("lang spans:", page.count('data-lang="es"'))
print("link pills:", page.count('class="link-pill"'))
