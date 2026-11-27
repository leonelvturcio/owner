# Proyecto: ingresos nocturnos con Claude Code (Alemania, 1–2 h/día)

## La idea en una frase

**Localización "lista para mergear" de juegos y apps indie al español (y después al alemán).**
Tú entras al repositorio del cliente con Claude Code, traduces los archivos de idioma
(`en.json`, `.po`, `.csv`, `strings.xml`, `.resx`, Godot/Unity), pasas un control de calidad
automático y entregas un **Pull Request listo**, no un documento de Word.

## Por qué esta idea y no otra

| Criterio | Por qué encaja |
|---|---|
| **No es genérica** | No es "hago webs" ni "hago automatizaciones". Es un nicho concreto con un dolor concreto: el 2.º idioma más hablado en Steam/móvil es el español y la mayoría de indies lo dejan para "algún día". |
| **Claude Code es la ventaja real** | Una agencia de traducción entrega un Excel y el dev tiene que integrarlo. Tú trabajas *dentro del repo*: respetas placeholders, formatos, longitudes de UI y entregas un PR que compila. Eso es lo que Claude Code hace mejor que un chat. |
| **Tu ventaja injusta** | Español nativo + vives en Alemania (contexto alemán para la fase 2) + horario nocturno europeo = solapas con devs de EE. UU. por la tarde. |
| **1–2 h por la noche** | Trabajo asíncrono. Nada de llamadas ni horarios. Un juego indie pequeño tiene 300–3.000 textos: 1–3 noches de trabajo. |
| **Dinero en 30 días** | Es un servicio con comprador directo (devs que ya tienen el producto). No necesitas audiencia para la primera venta. |
| **Escalable** | Servicio → paquetes cerrados → actualizaciones recurrentes → kit/glosarios vendibles → más idiomas con revisores freelance. |
| **Fiscalmente simple en Alemania** | Traductor es *Freiberuf* (§18 EStG): normalmente sin Gewerbeanmeldung. Ver [`alemania-legal-fiscal.md`](alemania-legal-fiscal.md). |

### Ideas que descarté (y por qué)
- **Webs / automatizaciones para negocios locales**: genérico, mucha competencia, requiere reuniones en horario laboral.
- **Ebooks/KDP, print-on-demand**: saturado; casi nunca da dinero en 30 días.
- **Micro-SaaS**: posible a 6–12 meses, pero rara vez cobra en 30 días.
- **Guías para hispanos en Alemania**: buena idea *secundaria* (mes 3+), pero necesita audiencia antes de vender.

## Oferta inicial (precios de lanzamiento)

| Paquete | Qué incluye | Precio |
|---|---|---|
| **Piloto** | Hasta 300 textos ES, PR + informe QA | **49 €** (solo los 2–3 primeros clientes, a cambio de testimonio) |
| **Indie** | Hasta 1.500 palabras, ES neutro, 1 ronda de cambios, PR | **149 €** |
| **Estándar** | Hasta 5.000 palabras, glosario del juego, capturas revisadas | **0,06 €/palabra** (≈ 300 € por 5.000) |
| **Mantenimiento** | Cada update/parche traducido en < 72 h | **39 €/mes** o por palabra nueva |

> Referencia: agencias cobran 0,10–0,20 €/palabra y entregan hojas de cálculo. Tú eres más barato, más rápido y entregas integrado.

## Proyección realista a 30 días

| Semana | Objetivo | Ingreso esperado (realista) | Optimista |
|---|---|---|---|
| 1 | Montar sistema + portafolio (2 demos open source) | 0 € | 0 € |
| 2 | 40 contactos, 1–2 pilotos | 49–98 € | 150 € |
| 3 | Entregar pilotos, testimonios, 1 cliente Indie | 150–300 € | 450 € |
| 4 | 1–2 clientes de pago + 1 mantenimiento | 200–450 € | 800 € |
| **Total mes 1** | | **≈ 400–850 €** | **≈ 1.400 €** |

Escenario pesimista honesto: 0–100 € el primer mes si la tasa de respuesta es baja. El plan incluye
puntos de control (días 14 y 21) para cambiar de canal si pasa eso.

### Escalado meses 2–3
1. **Mes 2**: subir precio a 0,08 €/palabra, 3–5 clientes de mantenimiento recurrentes (objetivo 500–1.200 €/mes).
2. **Mes 2**: añadir **alemán** (DE es el 3.er mercado de Steam). Si no eres nativo en alemán, subcontratas revisión nativa y cobras margen.
3. **Mes 3**: vender el **kit** (script QA + glosarios de género: RPG, roguelike, cozy) en itch.io/Gumroad a 15–29 € — ingreso pasivo.
4. **Mes 3+**: ofrecer otros idiomas con revisores freelance; tú pones el pipeline de Claude Code y el control de calidad.

## Archivos del proyecto

- [`calendario-30-dias.md`](calendario-30-dias.md) — plan noche por noche con métricas.
- [`alemania-legal-fiscal.md`](alemania-legal-fiscal.md) — empleador, Finanzamt, Kleinunternehmer, facturas.
- [`plantillas-outreach.md`](plantillas-outreach.md) — mensajes de contacto, perfil y prompts de Claude Code.
- [`herramientas/l10n_qa.py`](herramientas/l10n_qa.py) — script de QA (placeholders, claves, longitudes). Pruébalo:
  ```bash
  python3 herramientas/l10n_qa.py herramientas/ejemplo/en.json herramientas/ejemplo/es.json
  ```
- [`seguimiento.csv`](seguimiento.csv) — CRM mínimo para tus contactos.

## Costes

| Concepto | Coste |
|---|---|
| Claude Pro (o Max si te quedas corto) | ~20 €/mes (Max ~100 €/mes) |
| Dominio/email profesional (opcional) | ~1–5 €/mes |
| Stripe / PayPal / Wise | comisión por cobro |
| **Total** | **≈ 20–25 €/mes** |
