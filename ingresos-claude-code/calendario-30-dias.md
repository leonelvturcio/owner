# Calendario de 30 noches (1–2 h cada una)

Inicio propuesto: **lunes 30 nov 2026** → fin **martes 29 dic 2026**.
Horario sugerido: 21:00–22:30 (coincide con la tarde en EE. UU., cuando los devs contestan).

Regla de oro de cada noche: **primero lo que genera dinero (contactar/entregar), después lo demás.**

> Navidad cae en la semana 4. Es buen momento: muchos indies preparan lanzamientos de enero y
> demos para el Steam Next Fest de febrero, y necesitan idiomas *ya*. Los días 24–26 son ligeros.

---

## Semana 1 — Montar la máquina (0 € esperados)

| Día | Fecha | Tarea (≈1,5 h) | Entregable / métrica |
|---|---|---|---|
| 1 | Lu 30 nov | Leer [`alemania-legal-fiscal.md`](alemania-legal-fiscal.md). Revisar tu contrato laboral (cláusula *Nebentätigkeit*) y redactar el aviso a tu empleador. Crear cuenta en Wise/PayPal/Stripe. | Aviso enviado o listo · cuenta de cobro |
| 2 | Ma 1 dic | Con Claude Code: probar `herramientas/l10n_qa.py`, ampliarlo a `.po` y `.csv` (pídeselo a Claude Code). | Script con 3 formatos |
| 3 | Mi 2 dic | Buscar en GitHub 5 juegos/apps open source **sin español** (`topic:game` + carpeta `locales`/`i18n`). Elegir 2 pequeños. | Lista de 5 repos |
| 4 | Ju 3 dic | **Demo 1**: fork + traducción completa con Claude Code + QA + abrir PR público al proyecto. | PR público #1 |
| 5 | Vi 4 dic | **Demo 2**: igual con otro formato (Godot `.csv` o Android `strings.xml`). | PR público #2 |
| 6 | Sá 5 dic | Página de portafolio mínima (README de GitHub o perfil de itch.io) con: oferta, precios, enlaces a los 2 PR, antes/después de una captura. | Enlace de portafolio |
| 7 | Do 6 dic | Construir la lista de prospectos: 60 juegos en itch.io/Steam "Coming soon"/r/gamedev/r/IndieDev sin español. Rellenar [`seguimiento.csv`](seguimiento.csv). | 60 filas en el CSV |

**Control semana 1:** 2 PR públicos + 60 prospectos. Si no llegas, no pases a la semana 2 sin terminar las demos: son tu prueba social.

---

## Semana 2 — Salir a vender (objetivo: 1–2 pilotos)

| Día | Fecha | Tarea | Métrica |
|---|---|---|---|
| 8 | Lu 7 dic | Personalizar plantilla A ([`plantillas-outreach.md`](plantillas-outreach.md)) con Claude Code para 10 prospectos (menciona algo concreto de su juego). Enviar. | 10 mensajes |
| 9 | Ma 8 dic | 10 mensajes más (email, Discord del juego, X/Bluesky). | 20 acumulados |
| 10 | Mi 9 dic | Publicar en r/gamedev / r/IndieDev el **caso de estudio** de la demo 1 (qué errores típicos encontraste: placeholders, textos largos…). Valor, no anuncio. | 1 post |
| 11 | Ju 10 dic | 10 mensajes + responder a todo. Para cada "sí": enviar presupuesto en < 12 h. | 30 acumulados |
| 12 | Vi 11 dic | Comentar ofreciendo ayuda en hilos "looking for translators" (r/gameDevClassifieds, foros de itch.io, Discords de Godot/GameMaker). | 5 respuestas útiles |
| 13 | Sá 12 dic | 10 mensajes + seguimiento (plantilla B) a quienes no contestaron hace 4+ días. | 40 acumulados |
| 14 | Do 13 dic | **Revisión**: tasa de respuesta. Plantilla de factura lista (ver archivo legal). | Decisión (abajo) |

**Punto de control día 14:**
- ≥ 1 piloto aceptado → sigue el plan.
- 0 respuestas positivas con 40 mensajes → cambia el mensaje (oferta: *"traduzco gratis tu página de Steam/itch, si te gusta seguimos"*) y prueba otro canal (devs de apps móviles/Shopify themes/plugins de WordPress, que también tienen `.po`).

---

## Semana 3 — Entregar, cobrar, conseguir prueba social (objetivo: 150–300 €)

| Día | Fecha | Tarea | Métrica |
|---|---|---|---|
| 15 | Lu 14 dic | Piloto 1: clonar repo, extraer textos, crear **glosario** del juego (nombres propios, tono, tú/usted) con Claude Code. | Glosario |
| 16 | Ma 15 dic | Piloto 1: traducción + QA + PR. Enviar con informe ("encontré 3 textos sin traducir en el original"…). | Entrega 1 |
| 17 | Mi 16 dic | Cobrar piloto 1. Pedir testimonio + "¿conoces a otro dev?". 10 mensajes nuevos. | 1.º € 🎉 |
| 18 | Ju 17 dic | Piloto 2 (o 10 mensajes más si no hay). | Entrega 2 |
| 19 | Vi 18 dic | Ofrecer a los pilotos el paquete **Mantenimiento** (39 €/mes). | 1 propuesta recurrente |
| 20 | Sá 19 dic | Añadir testimonios al portafolio. Subir precio público (fin de pilotos a 49 €). | Portafolio v2 |
| 21 | Do 20 dic | **Revisión**: ¿cuántas horas te llevó cada piloto? Documentar el proceso en un `CLAUDE.md` reutilizable (prompts, pasos, checklist). | Proceso documentado |

**Punto de control día 21:** si cada entrega te lleva > 4 h, simplifica (formatos que aceptas, tamaño máximo). Si < 2 h, el precio es bajo: súbelo.

---

## Semana 4 — Primeros clientes de pago y recurrencia (objetivo: 200–450 €)

| Día | Fecha | Tarea | Métrica |
|---|---|---|---|
| 22 | Lu 21 dic | 15 mensajes con ángulo "**Next Fest de febrero**: llega con tu demo en español". | 15 mensajes |
| 23 | Ma 22 dic | Trabajo de cliente Indie/Estándar. | Avance |
| 24 | Mi 23 dic | Trabajo de cliente + factura. | Entrega |
| 25 | Ju 24 dic | 🎄 Ligero (30 min): responder mensajes. | — |
| 26 | Vi 25 dic | 🎄 Libre. | — |
| 27 | Sá 26 dic | Ligero: preparar el **kit vendible** (script QA + glosario plantilla). | Borrador kit |
| 28 | Do 27 dic | Escribir el caso de estudio del cliente (con permiso) y publicarlo. | 1 post |
| 29 | Lu 28 dic | Planificar mes 2: alemán (¿revisor nativo?), precio nuevo, 5 recurrentes objetivo. | Plan mes 2 |
| 30 | Ma 29 dic | **Cierre**: sumar ingresos, horas, € por hora, tasa de respuesta. Apuntar ingresos para la *Steuererklärung*. | Informe del mes |

---

## Métricas que importan (apúntalas en `seguimiento.csv`)

- Mensajes enviados → respuestas → pilotos → clientes de pago (embudo).
- Horas por 1.000 palabras (objetivo: < 1 h con Claude Code + QA).
- € por hora real (objetivo mes 1: > 25 €/h; mes 3: > 50 €/h).

Referencia de embudo típico en outreach personalizado: 5–15 % responde, 1/3 de esos acepta piloto.
Con 60–80 mensajes ⇒ 3–8 respuestas ⇒ 1–3 clientes. Por eso el volumen de contactos no es opcional.
