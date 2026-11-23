# Prompts para Claude Code

Úsalos en orden dentro de tu repo `web-plantilla`. Sustituye lo que va entre `[corchetes]`.

## 1. Plantilla base (día 2, una sola vez)

```
Crea una plantilla de web para pequeños negocios locales en Alemania.
- HTML + CSS sin frameworks, una carpeta por cliente en /clientes/<nombre>.
- Mobile-first, carga en < 1 s, buena puntuación en Lighthouse.
- Secciones configurables desde un archivo datos.json: hero, servicios/menú,
  horarios, reseñas, galería, mapa (enlace a Google Maps, sin iframe para no
  necesitar banner de cookies), contacto.
- Páginas /impressum.html y /datenschutz.html generadas desde datos.json
  (nombre, dirección, teléfono, email, Inhaber, USt-ID si existe).
- Sin cookies ni Google Fonts externas (fuentes alojadas localmente) para
  simplificar el cumplimiento de la DSGVO.
- Un script build.js que genere /dist/<cliente> a partir de datos.json.
- README con cómo crear un cliente nuevo en 5 pasos.
```

## 2. Demo personalizada (≈ 20 min por negocio)

```
Crea un cliente nuevo en /clientes/[nombre-negocio] con esta información pública:
Nombre: [..] · Tipo: [peluquería/restaurante/..] · Ciudad: [..]
Dirección: [..] · Teléfono: [..] · Horarios: [..]
Servicios/precios: [pegar texto de su web/Instagram/Google]
3 reseñas de Google: [pegar]
Tono: [cercano/elegante], idioma: [alemán | alemán + español].
Elige una paleta acorde al tipo de negocio. Marca el pie como "Entwurf/Demo".
Genera el build y dime el comando para publicarlo en una URL de prueba.
```

## 3. Web final del cliente

```
Convierte la demo de /clientes/[nombre] en la versión final:
- Sustituye textos y fotos por los que están en /clientes/[nombre]/material.
- Completa Impressum y Datenschutz con los datos reales.
- Añade formulario de contacto (Formspree/Netlify Forms) y menciónalo en la Datenschutz.
- Optimiza imágenes (WebP, máx. 200 KB).
- Quita la marca "Demo". Revisa en 375 px y 1440 px.
- Lista de comprobación final antes de entregar.
```

## 4. Automatización (extra 150–300 €)

```
Para el cliente [nombre], añade [reservas online / menú QR / formulario que
envía un email al dueño y una confirmación al cliente]. Usa solo servicios
con plan gratuito y servidores en la UE cuando sea posible. Documenta en
/clientes/[nombre]/MANTENIMIENTO.md cómo cambiarlo.
```

## 5. Escalar: generador en un comando (día 27)

```
Crea un comando `node nuevo-cliente.js` que pregunte en la terminal los datos
del negocio (o lea un CSV de mi pipeline), genere datos.json, haga el build y
deje la demo lista para publicar. Objetivo: demo en < 10 minutos.
```
