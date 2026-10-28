# Ajwa Dates Wholesale — site one-page EN / FR / ES

Site vitrine d'une seule page, en trois langues, chacune à sa propre adresse :

| Langue | Adresse | Mot-clé SEO principal |
|---|---|---|
| Anglais (**par défaut**) | `https://ajwadateswholesale.vercel.app/` | « ajwa dates wholesale » |
| Français | `https://ajwadateswholesale.vercel.app/fr/` | « dattes ajwa en gros » |
| Espagnol | `https://ajwadateswholesale.vercel.app/es/` | « dátiles ajwa al por mayor » |

> Le site est en ligne sur `ajwadateswholesale.vercel.app` (Vercel). L'ancienne adresse `/en/` redirige vers `/`.
> S'il change, modifiez `SITE` dans `tools/build.py`, `robots.txt`, puis relancez la génération.

Objectif : faire contacter le vendeur sur **WhatsApp** (`https://wa.me/212664738219`).

- 100 % statique : HTML + CSS + un petit JavaScript (menu mobile). **Aucun framework, aucune installation.**
- Chaque langue est une **vraie page HTML complète** : titre, description, Open Graph / Twitter, `canonical`,
  `hreflang` (en, fr, es, `x-default` → page anglaise), FAQ JSON-LD, textes alternatifs, message WhatsApp
  pré-rempli dans la bonne langue. Google lit chaque version sans JavaScript.
- Sélecteur **EN / FR / ES** (en-tête et pied de page) = simples liens. Pas de redirection automatique.
- Bouton WhatsApp flottant + 16 liens WhatsApp par page, tous marqués `data-cta="whatsapp"` et `data-cta-location="…"`.
- Données structurées : `Organization` + `WebSite` (nom, adresse, WhatsApp uniquement), `FAQPage` par langue.
- `robots.txt`, `sitemap.xml` (3 adresses + `hreflang`), favicon, image de partage 1200×630.
- **Aucun outil de suivi installé** (ni GA4, ni GTM, ni pixel) : emplacements GTM prévus, vides.

---

## 1. Voir le site sur votre ordinateur

**Le plus simple :** double-cliquez sur `index.html`. Tous les chemins sont relatifs, le design, les images
et le sélecteur de langue fonctionnent (testé).

**Comme en ligne (recommandé avant publication)** — dans un terminal, depuis le dossier du projet :

```bash
npx serve .
# ou, sans Node : python3 -m http.server 8000
```
Puis ouvrez l'adresse affichée (ex. http://localhost:3000/ — anglais), `/fr/` et `/es/`.

---

## 2. Structure du projet

```
index.html                 ← page anglaise (générée)
fr/index.html              ← page française (générée)
es/index.html              ← page espagnole (générée)
css/style.css              ← le design (or, brun profond, ambre)
js/main.js                 ← menu mobile, ombre de l'en-tête, liens de langue en double-clic
images/                    ← photos WebP optimisées + og-image.jpg + apple-touch-icon.png
favicon.svg                ← icône du site
robots.txt, sitemap.xml    ← pour Google (sitemap généré)
vercel.json                ← adresses propres, /en → / (redirection 308), cache
tools/translations.json    ← TOUS les textes, en EN / FR / ES
tools/index.template.html  ← le modèle HTML commun aux 3 pages
tools/build.py             ← génère les 3 pages + sitemap.xml
```

Sections : en-tête fixe · hero · bandeau de confiance · l'Ajwa de Madinah (`#about-ajwa`) ·
saison de récolte avec calendrier (`#harvest`) · produits & conditionnements · pourquoi nous ·
qualité & certifications (`#certifications`) · ce que recherchent les acheteurs · marchés (`#markets`) ·
FAQ · appel à l'action final · pied de page (About Ajwa | Harvest Season | Certifications | Markets).

---

## 3. Modifier un texte ou une traduction

1. Ouvrez `tools/translations.json` : chaque texte existe en `fr`, `en` et `es` (mêmes clés).
2. Modifiez le texte voulu (gardez les guillemets et virgules).
3. Régénérez les pages :
   ```bash
   python3 tools/build.py
   ```
   Cela réécrit `index.html`, `fr/index.html`, `es/index.html` et `sitemap.xml`.
   **Ne modifiez pas directement ces fichiers HTML** : ils seraient écrasés à la prochaine génération.

Autres réglages dans `tools/build.py` :
- `WA_NUMBER` : numéro WhatsApp (format international sans `+`).
- `HARVEST` : statut de chaque mois du calendrier (`stock`, `early`, `peak`, `main`, `new`).
- `SITE` : adresse du site ; `LASTMOD` : date du sitemap.

---

## 4. Ajouter Google Tag Manager (plus tard)

Deux commentaires « GOOGLE TAG MANAGER — emplacement réservé, vide » sont prévus dans `tools/index.template.html` :
dans le `<head>` (script GTM) et juste après `<body>` (`<noscript>`). Collez-y le code GTM puis relancez
`python3 tools/build.py`. Pour suivre les clics WhatsApp, créez dans GTM un déclencheur « Clic – Tous les éléments »
sur `a[data-cta="whatsapp"]` et utilisez l'attribut `data-cta-location` (header, hero, harvest, product-bulk, final, floating…)
pour savoir quel bouton a été cliqué.

---

## 5. À compléter / à vérifier avant publication

- **Numéro WhatsApp** `+212 664 738 219` (confirmé par Jose, octobre 2026). Pour le changer : `WA_NUMBER` dans `tools/build.py` et le numéro affiché dans `tools/index.template.html`, puis `python3 tools/build.py`.
- **Certifications** : aucune n'est citée (commentaire `TODO` dans le modèle). N'ajoutez que des certifications réelles et vérifiables.
- **Avis clients** : remplacés par « ce que recherchent les acheteurs ». Ajoutez de vrais témoignages seulement s'ils existent (`TODO`).
- Aucun prix, minimum de commande, volume, année ou nom d'entreprise n'a été inventé.
- **Calendrier de récolte** : formulation prudente (« généralement fin juillet à septembre, pic en août,
  nouvelle récolte conditionnée vers octobre, disponible toute l'année grâce au froid »), d'après :
  - International Dates Council — https://intdc.org/en/about-dates/ajwa/ (récolte juillet–septembre)
  - Saudipedia — https://saudipedia.com/en/article/4124/ (stade tamr atteint vers août)

---

## 6. Crédits photos

Toutes les photos viennent de **Pexels** (licence Pexels : usage commercial gratuit, attribution non obligatoire mais faite ici).

| Fichier | Photo | Auteur | Remarque |
|---|---|---|---|
| `dattes-ajwa-en-gros-*.webp`, `og-image.jpg` | https://www.pexels.com/photo/8952691/ | Kübra Doğu | Décrite comme des dattes Ajwa |
| `palmiers-madinah-*.webp` | https://www.pexels.com/photo/39215549/ | Samet Kaplan | Palmiers dattiers à Médine |
| `recolte-dattes-ajwa-*.webp` | https://www.pexels.com/photo/17877979/ | Radwan Menzer | ⚠️ **Pas Madinah, pas de l'Ajwa** (Biskra, Algérie) — photo d'ambiance récolte, à remplacer par une photo réelle |
| `dattes-ajwa-premium-*.webp` | https://www.pexels.com/photo/6200512/ | Ali El Khatib | ⚠️ **Pas clairement de l'Ajwa** (ressemble à de la Medjool) — à remplacer par une photo réelle |

Le mieux reste de remplacer ces photos par vos propres photos de produits (mêmes noms de fichiers, format WebP).

## Suivi Google Ads + GA4 (Consent Mode v2, mode basique)

- Bloc `<head>` : `tools/head-block.html` (inséré par `tools/build.py` dans les 3 pages d'accueil et les 3 pages de confidentialité). Il met les 4 signaux à `denied`, puis `url_passthrough` et `ads_data_redaction`. **Aucun gtag.js n'est chargé avant « Accepter »**, donc aucune requête Google et aucun ping sans cookie.
- `js/analytics.js` : bandeau EN/FR/ES (nomme Google Analytics et Google Ads), choix stocké 6 mois dans `localStorage` `ajw_cookie_consent_v2`.
  - Accepter : les 4 signaux passent à `granted`, puis un seul gtag.js (`id=AW-18529460502`) est injecté.
  - Refuser : les 4 signaux restent à `denied` et les cookies `_ga*`/`_gcl*` sont supprimés. Si la personne retire son accord après avoir accepté, la page se recharge.
  - Clic WhatsApp (`a[data-cta="whatsapp"]`), seulement après Accepter : `whatsapp_click` (GA4, `link_location` = `data-cta-location`), puis la conversion Ads `AW-18529460502/_PkpCOiWlq0dEJbCxINF` (50 GBP, beacon). Ce libellé ne sert que pour ce site.
- GA4 : l'ID n'existe pas encore. Remplacer `<AJWA_GA4_ID>` par le vrai `G-…` dans `GA4_ID` (tools/build.py), puis relancer `python3 tools/build.py`. Tant que c'est le texte de remplacement, aucun événement GA4 n'est envoyé ; les conversions Ads fonctionnent déjà.
- Pages de confidentialité (`noindex`, hors sitemap) : `/privacy/`, `/fr/confidentialite/`, `/es/privacidad/`. Leur texte est dans `tools/privacy_content.py`. Lien « Gérer les cookies » dans le pied de page.
