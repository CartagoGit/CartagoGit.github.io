#!/usr/bin/env python3
"""Generate the static portfolio page.

The page is generated rather than hand-edited so the two languages cannot
drift apart and so every technology chip carries its real brand mark.
"""
import pathlib

SITE = pathlib.Path(__file__).resolve().parent.parent
BRAND = SITE / "assets" / "brand"

# Each entry: (es, en)
T = {
    "eyebrow_hero": ("Frontend engineer · Sevilla, España", "Frontend engineer · Seville, Spain"),
    "hero_lead": (
        'Construyo <strong>front-ends operativos</strong>: aplicaciones de negocio que se usan '
        'todo el día, con los estados, permisos y reglas de negocio que tienen que seguir '
        'funcionando el trimestre que viene. Mi base es <strong>Angular con SCSS</strong>, Ionic '
        'para móvil y Material para el sistema de diseño.',
        'I build <strong>operational front-ends</strong> — business applications people use all '
        'day, with the states, permissions and long-lived rules that have to keep working next '
        'quarter. My base is <strong>Angular with SCSS</strong>, Ionic for mobile and Material '
        'for the design system.',
    ),
    "hero_secondary": (
        "Alrededor de esa base, mentorizo al equipo, tomo las decisiones de arquitectura, pongo "
        "las puertas de calidad y dockerizo lo que entregamos. En mi tiempo libre construyo "
        "herramientas de desarrollo, que es donde todavía puedo profundizar en lo que me importa.",
        "Around that base I mentor the team, take the architecture decisions, set the quality "
        "gates and containerise what we ship. In my own time I build developer tooling, which is "
        "where I can still go deep on the parts I care about.",
    ),
    "cta_work": ("Ver el trabajo", "See the work"),
    "cta_what": ("Qué hago", "What I do"),
    "at_a_glance": ("De un vistazo", "At a glance"),
    "facts": [
        ("Base", "Base", "Angular · SCSS · Ionic · Material"),
        ("También", "Also", "NestJS · Bun · Node · SQLite"),
        ("Entrega", "Delivery", "Docker · GitLab CI · GitHub Actions"),
        ("Rol", "Role", "Mentor · Decisiones · Front-end"),
        ("Propio", "Independent", "Runtime MCP · Tooling · Librerías"),
    ],
    "eyebrow_work": ("Qué hago", "What I do"),
    "h_work": (
        "Front-ends operativos, y todo lo necesario para entregarlos.",
        "Operational front-ends, and everything it takes to ship them.",
    ),
    "pillars": [
        (
            "Entrega de front-end operativo",
            "Operational front-end delivery",
            "Aplicaciones de negocio para procesos comerciales, financieros, de inventario, "
            "logística y de personal. Estados complejos, permisos, informes y reglas de producto "
            "que tienen que sobrevivir a la siguiente release: no pantallas de demo.",
            "Business applications for commercial, financial, inventory, logistics and workforce "
            "processes. Complex states, permissions, reporting and product rules that have to "
            "survive the next release — not demo screens.",
        ),
        (
            "Web y Android",
            "Web and Android",
            "Aplicaciones Angular e Ionic, empaquetadas para Android con Capacitor. Interfaces "
            "diseñadas para un uso repetido y con mucho contexto, no para interacciones sueltas.",
            "Angular and Ionic applications, packaged for Android with Capacitor. Interfaces "
            "designed for repeated, high-context use rather than one-off interactions.",
        ),
        (
            "Mentoría y decisiones técnicas",
            "Mentoring & technical decisions",
            "Mentorizo al equipo y resuelvo los trade-offs: qué se queda en el front, qué pasa a "
            "un servicio, qué lleva una puerta de calidad y qué lleva una decisión escrita.",
            "I mentor the team and settle the trade-offs: what stays in the front-end, what moves "
            "to a service, what gets a gate and what gets a written decision.",
        ),
        (
            "Bases de entrega",
            "Delivery foundations",
            "Entornos de desarrollo dockerizados, pipelines de GitLab CI y GitHub Actions, "
            "imágenes de contenedor y cobertura de tests donde de verdad se rompe algo.",
            "Dockerised development environments, GitLab CI and GitHub Actions pipelines, "
            "container images, and focused test coverage on the parts that actually break.",
        ),
        (
            "Herramientas de desarrollo",
            "Developer tooling",
            "Un runtime MCP, una librería de serialización de modelos y un motor de análisis "
            "estático: construidos porque las herramientas que quería todavía no existían.",
            "An MCP runtime, a model serialization library and a static analysis engine — built "
            "because the tools I wanted did not exist yet.",
        ),
        (
            "Backend y runtime",
            "Backend & runtime",
            "NestJS, Bun y Node para los servicios que hay detrás de las interfaces; SQLite y "
            "PostgreSQL para los datos. Suficiente para ownsar el camino entero.",
            "NestJS, Bun and Node for the services behind the interfaces; SQLite and PostgreSQL "
            "for the data. Enough to own the whole path.",
        ),
    ],
    "eyebrow_evidence": ("Evidencia", "Evidence"),
    "h_evidence": (
        "Medido sobre los repositorios públicos, no estimado.",
        "Measured on the public repositories, not estimated.",
    ),
    "evidence": [
        ("Commits", "Commits", "17.484", "17,484", "MCP runtime core"),
        ("Líneas de código", "Source lines", "628.712", "628,712", "Runtime core, sin tests"),
        ("Líneas de test", "Test lines", "460.854", "460,854", "2.709 ficheros de test"),
        ("Frameworks", "Frameworks", "25", "25", "Detectados desde el código"),
        ("Pulls de Docker", "Docker pulls", "4.833", "4,833", "Cinco imágenes publicadas"),
        ("Workflows de CI", "CI workflows", "18", "18", "Puertas de calidad del runtime core"),
    ],
    "eyebrow_projects": ("Proyectos", "Projects"),
    "h_projects": (
        "Trabajo independiente, hecho en mi tiempo libre.",
        "Independent work, built in my own time.",
    ),
    "all_repos": ("Todos los repositorios", "All repositories"),
    "eyebrow_stack": ("Stack principal", "Core stack"),
    "h_stack": (
        "Las herramientas que uso, con el front-end primero.",
        "The tools I reach for, with the front-end first.",
    ),
    "eyebrow_contact": ("Contacto", "Contact"),
    "h_contact": ("Mario Cabrero Volarich", "Mario Cabrero Volarich"),
    "contact_text": (
        "El trabajo open source, el contexto técnico y los datos de contacto están disponibles "
        "en GitHub y LinkedIn.",
        "Open-source work, technical context and contact details are available through GitHub and "
        "LinkedIn.",
    ),
    "footer_meta": ("Front-end · Arquitectura · Entrega", "Front-end · Architecture · Delivery"),
    "nav": [
        ("Qué hago", "What I do"),
        ("Evidencia", "Evidence"),
        ("Proyectos", "Projects"),
        ("Stack", "Stack"),
        ("Contacto", "Contact"),
    ],
}

STACK_GROUPS = [
    ("Front-end — mi base", "Front-end — my base", "Operaciones con estado predecible", "Operational applications with predictable state", [
        ("angular", "Angular"), ("ionic", "Ionic"), ("angular", "Material"),
        ("sass", "Sass"), ("typescript", "TypeScript"), ("rxjs", "RxJS"),
        ("capacitor", "Capacitor"), ("tailwindcss", "Tailwind"),
        ("vue", "Vue"), ("react", "React"),
    ]),
    ("Servicios, datos y runtime", "Services, data & runtime", "Suficiente backend para ownsar el camino", "Enough backend to own the whole path", [
        ("nestjs", "NestJS"), ("bun", "Bun"), ("nodejs", "Node.js"),
        ("postgresql", "PostgreSQL"), ("sqlite", "SQLite"),
        ("mongodb", "MongoDB"), ("zod", "Zod"), ("openapi", "OpenAPI"),
    ]),
    ("Tooling e infraestructura de IA", "Tooling & AI infrastructure", "Lo que construyo cuando la herramienta no existe", "What I build when the tool does not exist", [
        ("model-context-protocol", "MCP"), ("tauri", "Tauri"), ("rust", "Rust"),
        ("godot", "Godot"), ("python", "Python"), ("storybook", "Storybook"),
        ("prime-ng", "PrimeNG"),
    ]),
    ("Calidad y entrega", "Quality & delivery", "Releases fiables, no solo builds locales", "Reliable releases, not just local builds", [
        ("vitest", "Vitest"), ("playwright", "Playwright"), ("eslint", "ESLint"),
        ("prettier", "Prettier"), ("docker", "Docker"), ("gitlab", "GitLab CI"),
        ("github-actions", "GitHub Actions"), ("linux", "Linux"),
    ]),
    ("Cómo trabajo con la IA", "How I work with AI", "Los agentes proponen, las puertas deciden", "Agents propose, machine-checked gates decide", [
        ("claude", "Claude"), ("openai", "Codex"), ("minimax", "MiniMax"),
        ("grok", "Grok"),
    ]),
]

SOCIAL = [
    ("github", "GitHub", "https://github.com/CartagoGit", "GitHub profile"),
    ("linkedin", "LinkedIn", "https://www.linkedin.com/in/mario-cabrero-volarich", "LinkedIn profile"),
    ("npm", "npm", "https://www.npmjs.com/~cartago-git", "npm packages"),
    ("docker", "Docker Hub", "https://hub.docker.com/u/cartagodocker", "Docker Hub images"),
]

PROJECTS = [
    ("assets/delendai.svg", "Runtime MCP", "MCP runtime core", "DelendAI",
     "Un núcleo agnóstico para construir servidores MCP y el cargador de plugins que los alimenta: "
     "capacidades nombradas resueltas en tiempo de ejecución, superficie perezosa, errores "
     "públicos y datos privados — envuelto en un pipeline completo de propuesta a release.",
     "A project-agnostic core for building MCP servers, and the plugin loader that feeds them: "
     "named capabilities resolved at runtime, a lazy surface, public errors, private data — "
     "wrapped in a full proposal-to-release pipeline.",
     [("Repositorio", "Repository", "https://github.com/CartagoGit/DelendAI"),
      ("Releases", "Releases", "https://github.com/CartagoGit/DelendAI/releases")]),
    ("assets/tanit.svg", "Análisis estático", "Static analysis", "API Source Tanit",
     "Detecta el framework desde el propio código, recupera los cuerpos de las peticiones de los "
     "esquemas de validación y exporta a Postman, Bruno, Insomnia, HAR, OpenAPI o cURL. CLI, "
     "builds de escritorio y contenedores.",
     "Detects the framework from the code itself, recovers request bodies from validation "
     "schemas, and exports to Postman, Bruno, Insomnia, HAR, OpenAPI or cURL. CLI, desktop "
     "builds and containers.",
     [("Repositorio", "Repository", "https://github.com/CartagoGit/api-source-tanit"),
      ("Releases", "Releases", "https://github.com/CartagoGit/api-source-tanit/releases")]),
    ("assets/quickmodel.png", "Librería TypeScript", "TypeScript library", "QuickModel",
     "Transformación automática de tipos, adaptadores de validación, tests de seguridad y "
     "benchmarks, publicado como librería con un servidor MCP encima. El suite de tests es más "
     "grande que el código fuente a propósito.",
     "Automatic type transformation, validation adapters, security tests and benchmarks, "
     "published as a library with an MCP server on top. The test suite is larger than the source "
     "on purpose.",
     [("Repositorio", "Repository", "https://github.com/CartagoGit/quickmodel"),
      ("Documentación", "Documentation", "https://cartagogit.github.io/quickmodel/")]),
    ("assets/keyer.svg", "Paquete publicado", "Published package", "Keyer",
     "Cifra claves, API keys y ficheros <code>.env</code> desde la línea de comandos. Publicado "
     "en npm y usado para que las credenciales reales no acaben en los repositorios ni en las "
     "imágenes.",
     "Encrypts keys, API keys and <code>.env</code> files from the command line. Published on npm "
     "and used to keep real credentials out of the repositories and the images.",
     [("Repositorio", "Repository", "https://github.com/CartagoGit/Keyer"),
      ("Paquete npm", "npm package", "https://www.npmjs.com/package/@cartago-git/keyer")]),
    ("assets/print-cv.svg", "CV para imprimir", "Print-ready CV", "Print CV",
     "Vue 3 y TypeScript, con el currículum modelado como datos validados, internacionalizado en "
     "inglés y español, y un modo de impresión diseñado alrededor del papel real.",
     "Vue 3 and TypeScript, with the curriculum modelled as validated data, internationalised in "
     "English and Spanish, and a print mode designed around real paper.",
     [("Repositorio", "Repository", "https://github.com/CartagoGit/print-cv"),
      ("App en vivo", "Live app", "https://cartagogit.github.io/print-cv/")]),
    ("assets/cartago.svg", "Ingeniería de producto", "Product engineering", "Angular 22 zoneless SSR",
     "La aplicación Angular que hay detrás de este perfil: sin zone.js, con render en servidor, "
     "con tests unitarios y de integración y con un servidor MCP integrado en el build.",
     "The Angular application behind this profile: zoneless, server-rendered, with unit and "
     "integration tests, and an MCP server wired into the build.",
     [("Repositorio", "Repository", "https://github.com/CartagoGit/portfolio")]),
    ("assets/docker.svg", "Contenedores", "Containers", "Imágenes de desarrollo",
     "Entornos Docker para Angular, Ionic, NestJS, Node/Bun y Zsh, publicados con matrices de "
     "versiones fijadas.",
     "Docker environments for Angular, Ionic, NestJS, Node/Bun and Zsh workflows, published with "
     "pinned version matrices.",
     [("Docker Hub", "Docker Hub", "https://hub.docker.com/u/cartagodocker")]),
    ("assets/tanit.svg", "Contenido de juegos", "Game content", "Fábrica de campañas históricas",
     "Contenido de campañas validado por esquema para Age of Empires II, escrito en inglés y "
     "localizado para España con un pipeline de TypeScript y Python.",
     "Schema-validated campaign content for Age of Empires II, authored in English and localised "
     "for Spain through a TypeScript and Python pipeline.",
     [("Repositorio", "Repository", "https://github.com/CartagoGit/aoe2-mods")]),
]


def i18n(es, en):
    """Both languages of one string, side by side, so the switch can swap them."""
    return (
        f'<span data-lang="es">{es}</span>'
        f'<span data-lang="en">{en}</span>'
    )


def chip(slug, name):
    if not (BRAND / f"{slug}.svg").exists():
        return f"<span>{name}</span>"
    return (
        f'<span class="chip"><img src="assets/brand/{slug}.svg" alt="" '
        f'width="16" height="16" loading="lazy">{name}</span>'
    )


def build():
    facts = "\n".join(
        f'              <div><dt>{i18n(es, en)}</dt><dd>{value}</dd></div>'
        for es, en, value in T["facts"]
    )

    pillars = "\n".join(
        f'            <article class="pillar reveal">\n'
        f'              <span class="pillar__index">{i:02d}</span>\n'
        f"              <h3>{i18n(es_title, en_title)}</h3>\n"
        f"              <p>{i18n(es, en)}</p>\n"
        f"            </article>"
        for i, (es_title, en_title, es, en) in enumerate(T["pillars"], 1)
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
        + "".join(
            f'<a href="{href}">{i18n(es_l, en_l)}</a>' for es_l, en_l, href in links
        )
        + "</div>\n"
        f"            </article>"
        for i, (icon, es_type, en_type, title, es, en, links) in enumerate(PROJECTS)
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
        f'                <img src="assets/brand/{slug}.svg" alt="" width="18" height="18" loading="lazy">\n'
        f"                <span>{label}</span>\n"
        f"              </a>\n"
        f"            </li>"
        for slug, label, href, _aria in SOCIAL
    )

    header_links = "\n".join(
        f'          <a class="icon-link" href="{href}" target="_blank" rel="noreferrer" aria-label="{aria}">\n'
        f'            <img src="assets/brand/{slug}.svg" alt="" width="17" height="17">\n'
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
    <title>Mario Cabrero Volarich — Frontend engineer · Angular, Ionic &amp; SCSS</title>
    <meta name="description" content="Mario Cabrero Volarich is a frontend engineer building operational applications with Angular, Ionic and SCSS, and the developer tooling and infrastructure to ship them.">
    <meta name="author" content="Mario Cabrero Volarich">
    <meta name="theme-color" content="#070d1c">
    <meta property="og:title" content="Mario Cabrero Volarich — Frontend engineer">
    <meta property="og:description" content="Operational front-ends with Angular, Ionic and SCSS — plus the tooling, the gates and the containers to ship them.">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://cartagogit.github.io/">
    <meta property="og:image" content="https://cartagogit.github.io/assets/banner-03-neon.png">
    <link rel="icon" type="image/svg+xml" href="assets/cartago.svg">
    <link rel="apple-touch-icon" href="assets/cartago.svg">
    <link rel="stylesheet" href="styles.css">
    <script>
      // Applied before the first paint so the page never flashes the wrong theme.
      // Dark is the default: the palette was designed for it. The light theme is
      // opt-in and remembered once the visitor picks it.
      (function () {{
        try {{
          var theme = localStorage.getItem("cartago-theme") || "dark";
          document.documentElement.dataset.theme = theme;
          var lang = localStorage.getItem("cartago-lang") || "es";
          document.documentElement.lang = lang;
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
            <h1>Mario Cabrero<br><span class="hero__accent">Volarich</span></h1>
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

      <section class="section" id="work" aria-labelledby="work-title">
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
          document.title = lang === "es"
            ? "Mario Cabrero Volarich — Frontend engineer · Angular, Ionic & SCSS"
            : "Mario Cabrero Volarich — Frontend Engineer · Angular, Ionic & SCSS";
        }});
      }});

      function syncToggles() {{
        document.querySelectorAll("[data-set-theme]").forEach((button) => {{
          button.setAttribute("aria-pressed", String(button.dataset.setTheme === root.dataset.theme));
        }});
        document.querySelectorAll("[data-set-lang]").forEach((button) => {{
          button.setAttribute("aria-pressed", String(button.dataset.setLang === root.lang));
        }});
        // The browser chrome on mobile follows the theme.
        const meta = document.querySelector('meta[name="theme-color"]');
        if (meta) meta.content = root.dataset.theme === "light" ? "#f2f5fb" : "#070d1c";
      }}
      syncToggles();

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
print("reveal elements:", page.count('class="pillar reveal"') + page.count('project reveal"') + page.count('stack-group reveal"'))
print("lang spans:", page.count('data-lang="es"'))
