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
        "Construyo el front-end de sistemas que se usan todo el día",
        "I build the front-end of systems people use all day",
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
        "Además: mentoría del equipo, decisiones de arquitectura, CI y contenedores, y las "
        "herramientas de desarrollo que construyo para mi propio trabajo. Lo publicado en "
        "GitHub es trabajo independiente.",
        "Also: team mentoring, architecture decisions, CI and containers, and the developer "
        "tooling I build for my own work. What is published on GitHub is independent work.",
    ),
    "cta_work": ("Ver el trabajo", "See the work"),
    "cta_what": ("Qué hago", "What I do"),
    "at_a_glance": ("En una línea", "In one line"),
    "facts": [
        ("Base", "Base", "Angular · SCSS · Ionic · Material", "Angular · SCSS · Ionic · Material"),
        ("Detrás", "Behind", "NestJS · Bun · SQLite", "NestJS · Bun · SQLite"),
        ("Entrega", "Delivery", "Docker · GitLab CI · Actions", "Docker · GitLab CI · Actions"),
        ("Rol", "Role", "Mentor · Decisiones técnicas", "Mentor · Technical decisions"),
        ("En GitHub", "On GitHub", "89 repositorios · 26 activos", "89 repositories · 26 active"),
    ],

    # ---- work ----
    "eyebrow_work": ("Qué hago", "What I do"),
    "h_work": (
        "Qué desarrollo, y cómo lo entrego.",
        "What I develop, and how I ship it.",
    ),
    "pillars": [
        (
            "01 · Aplicaciones de gestión",
            "01 · Business applications",
            "ERP, almacén y personal, en Angular",
            "ERP, warehouse and workforce, in Angular",
            "Desarrollo front-end de aplicaciones operativas: permisos que cambian según el rol, "
            "formularios que tienen que sobrevivir a un uso distinto cada turno y listados que "
            "aguantan años sin volverse lentos. Con SCSS propio y Material para el sistema de "
            "diseño.",
            "Front-end development of operational applications: permissions that shift by role, "
            "forms that have to survive a different way of working every shift, and listings "
            "that stay quick after years. With my own SCSS and Material for the design system.",
        ),
        (
            "02 · Móvil, tablet y quiosco",
            "02 · Mobile, tablet and kiosk",
            "La misma aplicación en tres formatos",
            "The same application in three shapes",
            "Ionic y Capacitor para llevar la aplicación a Android sin duplicar el código, "
            "Quasar para los paneles de gestión, y PWA para lo que tiene que funcionar sin "
            "instalación. Incluye terminales de almacén con lector de código de barras.",
            "Ionic and Capacitor to take the application to Android without duplicating the "
            "code, Quasar for the management panels, and PWA for what has to work without "
            "being installed. Includes warehouse handhelds with a barcode reader.",
        ),
        (
            "03 · Arquitectura y mentoría",
            "03 · Architecture and mentoring",
            "Decidir antes de escribir, y que el equipo pueda seguir",
            "Decide before writing, and let the team carry on",
            "Elijo el límite entre el front y el servicio, qué lleva una puerta de calidad y qué "
            "lleva una decisión escrita. Reviso el código del equipo y mentorizo a quien se "
            "incorpora.",
            "I choose the boundary between the front-end and the service, and what gets a "
            "quality gate and what gets a written decision. I review the team's code and "
            "mentor whoever joins.",
        ),
        (
            "04 · CI y contenedores",
            "04 · CI and containers",
            "El mismo entorno en el portátil y en el runner",
            "The same environment on the laptop and on the runner",
            "GitLab CI para el producto, GitHub Actions para lo propio. Imágenes de Node/Bun, "
            "Angular, Ionic y NestJS con las versiones fijadas, para que el entorno del "
            "portátil y el del runner sean el mismo.",
            "GitLab CI for the product, GitHub Actions for my own work. Images for Node/Bun, "
            "Angular, Ionic and NestJS with pinned versions, so the environment on the laptop "
            "and on the runner is the same one.",
        ),
        (
            "05 · Herramientas propias",
            "05 · Own tooling",
            "Construidas porque me faltaban",
            "Built because I was missing them",
            "Un servidor MCP con 62 capacidades, un análisis estático de APIs, una librería de "
            "serialización, un gestor de secretos y un gestor de claves. Cada uno nació de una "
            "necesidad concreta de mi propio trabajo.",
            "An MCP server with 62 capabilities, a static analysis engine for APIs, a "
            "serialization library, a secret manager and a key manager. Each one started from "
            "a concrete need in my own work.",
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
        "La actividad, en cifras.",
        "The activity, in numbers.",
    ),
    "evidence": [
        ("Repositorios", "Repositories", "89", "89", "68 públicos y 21 privados", "68 public and 21 private"),
        ("Repos activos", "Active repositories", "26", "26", "publicados y mantenidos ahora", "published and maintained now"),
        ("Commits", "Commits", "22.638", "22,638", "en los repositorios públicos activos", "across the active public repositories"),
        ("Años en GitHub", "Years on GitHub", "5", "5", "publicando desde octubre de 2021", "publishing since October 2021"),
        ("Capacidades", "Capabilities", "62", "62", "plugins aisladas en DelendAI", "isolated plugins in DelendAI"),
        ("Puertas de CI", "CI gates", "18", "18", "cada una con su aserción", "each one with its own assertion"),
    ],

    # ---- projects ----
    "eyebrow_projects": ("Proyectos", "Projects"),
    "h_projects": (
        "Proyectos independientes, con código abierto.",
        "Independent projects, with open code.",
    ),
    "all_repos": ("Todos", "All"),
    "projects": [
        (
            "assets/delendai.svg", "Plataforma", "Platform",
            "DelendAI",
            "Un servidor MCP al que apuntas a un proyecto y le da exactamente las capacidades "
            "que ese proyecto necesita: 62 plugins aisladas, una CLI, nueve presets y un ciclo "
            "de propuesta → implementación → revisión → release detrás de 18 puertas de CI. No "
            "sabe nada de tu stack, y se desarrolla con agentes usando el propio servidor.",
            "An MCP server you point at a project, and it hands that project exactly the "
            "capabilities it needs: 62 isolated plugins, a CLI, nine presets and a proposal → "
            "implement → review → release cycle behind 18 CI gates. It knows nothing about your "
            "stack, and it is developed by agents using the server it builds.",
            [("repo", "https://github.com/CartagoGit/DelendAI", "DelendAI"),
             ("releases", "https://github.com/CartagoGit/DelendAI/releases", "Releases")],
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
            [("repo", "https://github.com/CartagoGit/api-source-tanit", "Tanit"),
             ("releases", "https://github.com/CartagoGit/api-source-tanit/releases", "Releases")],
        ),
        (
            "assets/quickmodel.png", "Librería", "Library",
            "QuickModel",
            "Transformación automática de tipos y adaptadores de validación sobre una base "
            "SOLID, con un servidor MCP encima. Los tests pesan más que el código fuente, y es "
            "a propósito.",
            "Automatic type transformation and validation adapters over a SOLID base, with an "
            "MCP server on top. The tests weigh more than the source, on purpose.",
            [("repo", "https://github.com/CartagoGit/quickmodel", "QuickModel"),
             ("docs", "https://cartagogit.github.io/quickmodel/", "Docs")],
        ),
        (
            "assets/keyer.svg", "Paquete publicado", "Published package",
            "Keyer",
            "Cifra claves y ficheros de entorno desde la terminal. Publicado en npm y usado para "
            "que ninguna credencial real acabe en un repositorio o en una imagen.",
            "Encrypts keys and environment files from the terminal. Published on npm and used so "
            "that no real credential ends up in a repository or an image.",
            [("repo", "https://github.com/CartagoGit/Keyer", "Keyer"),
             ("package", "https://www.npmjs.com/package/@cartago-git/keyer")],
        ),
        (
            "assets/print-cv.svg", "Aplicación", "Application",
            "Print CV",
            "El currículum como datos validados, en dos idiomas, con un modo de impresión "
            "diseñado alrededor del papel real. Es la aplicación que vive en cartagogit.github.io.",
            "A CV modelled as validated data, in two languages, with a print mode designed around "
            "real paper. This is the application that lives at cartagogit.github.io.",
            [("repo", "https://github.com/CartagoGit/print-cv", "Print CV"),
             ("live", "https://cartagogit.github.io/print-cv/", "Live")],
        ),
        (
            "assets/cartago.svg", "Sitio", "Site",
            "Portfolio",
            "El sitio que estas leyendo: una pagina estatica generada desde un script, en dos "
            "idiomas y con el tema del sistema. El repositorio detras es una aplicacion Angular "
            "con render en servidor.",
            "The site you are reading: a static page generated from a script, in two languages and "
            "following the system theme. The repository behind it is an Angular application with "
            "server-side rendering.",
            [("repo", "https://github.com/CartagoGit/portfolio", "Cartago"),
             ("live", "https://cartagogit.github.io", "Live")],
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
            [("repo", "https://github.com/CartagoGit/DockerNodeBun", "DockerNodeBun"),
             ("live", "https://hub.docker.com/u/cartagodocker", "Docker Hub")],
        ),
        (
            "assets/brand/steam-keys.svg", "Escritorio", "Desktop",
            "Gestor local de claves",
            "Una aplicación de escritorio, Tauri 2 y SQLite, donde las claves de Steam y de "
            "otras tiendas no salen del equipo. Sin cuentas, sin nube y sin telemetría.",
            "A desktop application, Tauri 2 and SQLite, where Steam keys and keys from other "
            "stores never leave the machine. No accounts, no cloud, no telemetry.",
            [("repo", "https://github.com/CartagoGit/steam-keys", "Steam Keys")],
        ),
        (
            "assets/brand/mods.svg", "Mods y contenido", "Mods and content",
            "Fabricación de mods",
            "Herramientas y contenido para modificar juegos: formatos binarios, localización y "
            "automatización de contenido. Un terreno abierto, con proyectos que van y vienen.",
            "Tools and content for modding games: binary formats, localisation and content "
            "automation. An open field, with projects that come and go.",
            [("repo", "https://github.com/CartagoGit/aoe2-mods", "Aoe2 mods"),
             ("repo", "https://github.com/CartagoGit/pcfutbol6-mod", "PC Fútbol 6")],
        ),
    ],

    # ---- professional work ----
    "eyebrow_pro": ("Trabajo profesional", "Professional work"),
    "h_pro": (
        "Lo que he construido para clientes, descrito por su función.",
        "What I have built for clients, described by function.",
    ),
    "pro_note": (
        "El código de estos sistemas es de la empresa y los clientes tienen su nombre, así que "
        "no hay enlaces. Sí hay cifras: los commits de cada repositorio llevan mi firma.",
        "The code behind these systems belongs to the company and the clients have their name, "
        "so there are no links. There are numbers though: the commits in each repository carry "
        "my signature.",
    ),
    "pro": [
        (
            "assets/pro/logistics.svg",
            "Logística", "Logistics",
            "El terminal del operario, en Android",
            "The operator's handheld, on Android",
            "Software para los PDAs de almacén: entradas, salidas, inventario, traspasos, "
            "reubicación, recepciones y transporte externo. Lo remodelé casi por completo y "
            "seguí añadiendo funcionalidad durante años, sobre Angular y Material.",
            "Software for the warehouse handhelds: inbound, outbound, inventory, transfers, "
            "relocation, reception and outsourced transport. I remodelled it almost entirely and "
            "kept adding features for years, on Angular and Material.",
            [("angular", "Angular"), ("typescript", "TypeScript"), ("capacitor", "Capacitor")],
        ),
        (
            "assets/pro/attendance.svg",
            "Personal", "Workforce",
            "Web y móvil sobre la misma base de código",
            "Web and mobile over one codebase",
            "Monorepo con una aplicación web y otra móvil/tablet que comparten servicios, "
            "estilos y recursos. Geolocalización y notificaciones push para registrar la "
            "presencia del personal.",
            "A monorepo with a web application and a mobile/tablet one sharing services, styles "
            "and resources. Geolocation and push notifications to record staff presence.",
            [("angular", "Angular"), ("ionic", "Ionic"), ("capacitor", "Capacitor")],
        ),
        (
            "assets/pro/signature.svg",
            "Entregas", "Deliveries",
            "La firma del cliente, en el móvil",
            "The customer's signature, on the phone",
            "Aplicación web progresiva en Angular para recoger la firma de recepción de material "
            "en la entrega, a pantalla completa en móvil o tablet, con la tienda y la entrega "
            "pendiente elegidas a mano.",
            "An Angular progressive web app to capture the material receipt signature on "
            "delivery, full screen on a phone or tablet, with the store and the pending delivery "
            "picked by hand.",
            [("angular", "Angular"), ("typescript", "TypeScript")],
        ),
        (
            "assets/pro/screens.svg",
            "Almacén", "Warehouse",
            "Lo que los operarios ven en las TVs",
            "What the operators see on the TVs",
            "Las pantallas de Mesa, Ruta y Bultos-Ruta del sistema de gestión, replicadas en las "
            " TVs del almacén para que el operario vea el estado sin volver al terminal.",
            "The Table, Route and Parcels screens of the management system, replicated on the "
            "warehouse TVs so the operator sees the state without going back to the handheld.",
            [("angular", "Angular"), ("typescript", "TypeScript")],
        ),
        (
            "assets/pro/candidates.svg",
            "Gestión", "Management",
            "Un panel en Vue y Quasar",
            "A panel in Vue and Quasar",
            "Gestión de proyectos y de candidatos con sus formularios, sus filtros y sus "
            "informes, y una capa de seguridad con roles y contraseñas.",
            "Project and candidate management with its forms, its filters and its reports, and a "
            "security layer with roles and passwords.",
            [("vue", "Vue"), ("sass", "Sass"), ("typescript", "TypeScript")],
        ),
        (
            "assets/pro/erp.svg",
            "ERP", "ERP",
            "La parte frontal de un ERP de servicios",
            "The front-end of a services ERP",
            "Listados, formularios y flujos de trabajo de un ERP de servicios, con su "
            "integración en el backend y sus reglas de negocio en la interfaz.",
            "Listings, forms and workflows of a services ERP, with its backend integration and "
            "its business rules in the interface.",
            [("angular", "Angular"), ("typescript", "TypeScript")],
        ),
        (
            "assets/pro/minigames.svg",
            "Quioscos", "Kiosks",
            "Un motor, siete juegos, tres formatos",
            "One engine, seven games, three shapes",
            "Monorepo Nx con Angular, Capacitor y Phaser: un motor, un catálogo de juegos y un "
            "shell que los monta en quiosco, web o móvil. Siete juegos y cinco idiomas. "
            "Desarrollé el front-end completo y el servicio que lo acompaña, y parte del diseño "
            "visual.",
            "An Nx monorepo with Angular, Capacitor and Phaser: an engine, a game catalogue and "
            "a shell that mounts them on a kiosk, the web or a phone. Seven games and five "
            "languages. I developed the whole front-end and the service behind it, and part of "
            "the visual design.",
            [("angular", "Angular"), ("nestjs", "NestJS"), ("typescript", "TypeScript")],
        ),
    ],

    # ---- stack ----
    "eyebrow_stack": ("Con qué trabajo", "What I work with"),
    "h_stack": (
        "Las tecnologías, agrupadas por uso.",
        "The technologies, grouped by use.",
    ),
    "stack_note": (
        "La primera capa es la que uso a diario; las demás, según lo que pide cada proyecto.",
        "The first layer is what I use daily; the rest, depending on what each project needs.",
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
        ("Trabajo", "Work"),
        ("Evidencia", "Evidence"),
        ("Proyectos", "Projects"),
        ("Con qué", "Tools"),
        ("Contacto", "Contact"),
    ],
}

STACK_GROUPS = [
    ("Front-end — a diario", "Front-end — daily", "Angular, SCSS, Ionic y el diseño", "Angular, SCSS, Ionic and the design", [
        ("angular", "Angular"), ("sass", "Sass"), ("ionic", "Ionic"),
        ("typescript", "TypeScript"), ("rxjs", "RxJS"), ("material", "Material"),
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
        f'<span class="chip"><img src="assets/brand/{slug}.svg?v=3" alt="" '
        f'width="16" height="16">{name}</span>'
    )


def link(kind, href, label=None):
    slug, es, en = LINK_ICONS[kind]
    if label is None:
        text = i18n(es, en)
        title = f"{es} / {en}"
    else:
        text = label
        title = label
    return (
        f'<a class="link-pill" href="{href}" target="_blank" rel="noreferrer" '
        f'title="{title}">'
        f'<img src="assets/brand/{slug}.svg?v=3" alt="" width="15" height="15">'
        f"<span>{text}</span>"
        f"</a>"
    )


def build():
    facts = "\n".join(
        f'              <div><dt>{i18n(es, en)}</dt><dd>{i18n(v_es, v_en)}</dd></div>'
        for es, en, v_es, v_en in T["facts"]
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
        f"<dt>{i18n(es_k, en_k)}</dt><dd>{i18n(es_v, en_v)}</dd><p>{i18n(note_es, note_en)}</p></div>"
        for es_k, en_k, es_v, en_v, note_es, note_en in T["evidence"]
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
        + "".join(link(*entry) for entry in links)
        + "</div>\n"
        f"            </article>"
        for i, (icon, es_type, en_type, title, es, en, links) in enumerate(T["projects"])
    )

    pro = "\n".join(
        f'            <article class="project reveal">\n'
        f'              <img class="project__icon" src="{icon}" alt="" width="56" height="56">\n'
        f'              <div class="project__body">\n'
        f'                <p class="project__type">{i18n(es_kicker, en_kicker)}</p>\n'
        f'                <h3 class="project__title">{i18n(es_title, en_title)}</h3>\n'
        f'                <p class="project__text">{i18n(es, en)}</p>\n'
        f'                <div class="chip-list">'
        + "".join(chip(slug, name) for slug, name in stack_items)
        + "</div>\n"
        f"              </div>\n"
        f"            </article>"
        for icon, es_kicker, en_kicker, es_title, en_title, es, en, stack_items in T["pro"]
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
        f'                <img src="assets/brand/{slug}.svg?v=3" alt="" width="18" height="18">\n'
        f"                <span>{label}</span>\n"
        f"              </a>\n"
        f"            </li>"
        for slug, label, href, _aria in SOCIAL
    )

    header_links = "\n".join(
        f'          <a class="icon-link" href="{href}" target="_blank" rel="noreferrer" aria-label="{aria}">\n'
        f'            <img src="assets/brand/{slug}.svg?v=3" alt="" width="17" height="17">\n'
        f"          </a>"
        for slug, _label, href, aria in SOCIAL
    )

    nav = "\n".join(
        f'          <a href="#{target}">{i18n(es, en)}</a>'
        for (es, en), target in zip(
            T["nav"], ["work", "pro", "evidence", "projects", "stack", "contact"]
        )
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
    <a class="skip-link" href="#main">{i18n("Saltar al contenido", "Skip to content")}</a>

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

          <aside class="hero__aside reveal">
            <img class="hero__banner" src="assets/cartago-banner.png" alt="" width="1672" height="941" aria-hidden="true">
            <div class="hero__panel">
              <p class="hero__panel-title">{i18n(*T["at_a_glance"])}</p>
              <dl class="facts">
{facts}
              </dl>
            </div>
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

      <section class="section section--pro" id="pro" aria-labelledby="pro-title">
        <div class="shell">
          <div class="section__heading reveal">
            <p class="eyebrow">{i18n(*T["eyebrow_pro"])}</p>
            <h2 id="pro-title">{i18n(*T["h_pro"])}</h2>
            <p class="section__note">{i18n(*T["pro_note"])}</p>
          </div>
          <div class="project-grid">
{pro}
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
