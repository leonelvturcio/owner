# Plantillas de contacto y prompts de Claude Code

## Plantilla A — primer contacto (inglés, corto, personalizado)

> **Subject:** Spanish version of {GAME} — ready as a PR
>
> Hi {NAME},
>
> I played/watched {GAME} — {DETALLE CONCRETO: mecánica, arte, algo del devlog}.
> I noticed it's not available in Spanish yet (Spanish is one of the largest language
> groups on Steam and mobile).
>
> I'm a native Spanish speaker and I localize indie games **directly in the repo**: I deliver a
> pull request with the translated files, placeholders and UI lengths checked, so you don't have to
> copy-paste from spreadsheets. Example: {LINK PR DEMO}
>
> I'm taking 3 pilot projects at €49 (up to 300 strings) in exchange for honest feedback.
> Would that be useful for {GAME}?
>
> {TU NOMBRE}

**Reglas:** máximo 120 palabras · 1 detalle real del juego · 1 enlace · 1 pregunta. Nunca envíos masivos idénticos.

## Plantilla B — seguimiento (4–5 días después)

> Hi {NAME}, quick follow-up on the Spanish version for {GAME}. Happy to translate your
> Steam/itch page description for free first so you can judge the quality. No pressure either way!

## Plantilla C — presupuesto

> Thanks! Here's the plan for {GAME}:
> - Scope: {N} strings / ~{W} words, files: {FORMATOS}
> - Delivery: pull request in {X} days, plus a QA report
> - Includes: glossary for names/terms, 1 round of revisions
> - Price: €{P} (no VAT, small business under §19 UStG) — paid via {Wise/PayPal/Stripe} after delivery
>   (pilots) / 50 % upfront (projects > €150)
>
> Could you give me read access to the repo (or send the language files)?

## Dónde encontrar prospectos

- **itch.io**: juegos en desarrollo con devlogs activos; filtra los que no listan "Spanish".
- **Steam "Coming Soon"** y participantes del próximo **Steam Next Fest** (demos).
- **Reddit**: r/gamedev, r/IndieDev, r/godot, r/gameDevClassifieds (hilos "[For Hire]").
- **GitHub**: repos con carpeta `locales/`, `i18n/`, `translations/` sin `es` → apps open source y juegos.
- **Discords** de motores (Godot, GameMaker, Bevy) — canal de colaboración / anuncios.

---

## Prompts para Claude Code (dentro del repo del cliente)

**1. Reconocimiento**
```
Explora este repositorio y dime: qué sistema de i18n usa, dónde están los archivos de idioma,
cuántas claves/palabras hay en el idioma base, y qué formatos de placeholder aparecen.
No cambies nada todavía.
```

**2. Glosario**
```
Extrae nombres propios, términos de juego (objetos, habilidades, lugares) y el tono general.
Crea glossary.es.md con: término original, traducción propuesta, nota. Marca las dudas.
```

**3. Traducción**
```
Crea el archivo de idioma español equivalente a {ARCHIVO_BASE} siguiendo glossary.es.md.
Español neutro, tuteo, sin cambiar claves ni placeholders ({...}, %s, etiquetas [color]).
Si un texto de UI es corto (botones), mantén la traducción igual de corta.
Registra el idioma en la configuración del proyecto si hace falta.
```

**4. QA y PR**
```
Ejecuta python3 l10n_qa.py {base} {es}. Corrige todos los errores y revisa los avisos.
Luego crea una rama "add-spanish-localization", haz commit y prepara la descripción del PR
con: archivos cambiados, decisiones del glosario y puntos que el dev debe verificar en pantalla.
```

## CLAUDE.md reutilizable (crea uno en tu carpeta de trabajo)
Guarda allí tus reglas de estilo (tuteo, comillas «» o "", signos ¿¡, formato de números 1.000,5),
lista de checks y la tarifa. Así cada proyecto nuevo arranca igual y cada vez tardas menos.
