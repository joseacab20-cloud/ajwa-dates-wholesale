# Privacy policy text (EN / FR / ES / PT), used by tools/build.py for /privacy/, /fr/confidentialite/, /es/privacidad/, /pt/privacidade/.
# Modelled on the rosewaterbulk policy. No legal controller name. Region-specific consent: banner and
# Consent Mode "denied" only in the EEA, the UK and Switzerland. {PHONE} and {KEY} are filled in by build.py.
UPDATED = {"en": "Last updated: October 28, 2026", "fr": "Dernière mise à jour : 28 octobre 2026",
           "es": "Última actualización: 28 de octubre de 2026",
           "pt": "Última atualização: 28 de outubro de 2026"}

META = {
    "en": {"title": "Privacy policy | Ajwa Dates Wholesale",
           "description": "How the Ajwa Dates Wholesale website uses Google Analytics and Google Ads cookies, to measure visits and WhatsApp contacts, the consent asked in the EEA, the UK and Switzerland, and how to opt out.",
           "h1": "Privacy policy", "back": "Back to home page", "manage": "Manage my cookie choices"},
    "fr": {"title": "Politique de confidentialité | Dattes Ajwa en Gros",
           "description": "Comment le site Dattes Ajwa en Gros utilise les cookies Google Analytics et Google Ads, pour mesurer les visites et les contacts WhatsApp, le consentement demandé dans l'EEE, au Royaume-Uni et en Suisse, et comment vous y opposer.",
           "h1": "Politique de confidentialité", "back": "Retour à l'accueil", "manage": "Gérer mes choix de cookies"},
    "es": {"title": "Política de privacidad | Dátiles Ajwa al por Mayor",
           "description": "Cómo el sitio Dátiles Ajwa al por Mayor usa cookies de Google Analytics y Google Ads, para medir las visitas y los contactos por WhatsApp, el consentimiento que se pide en el EEE, el Reino Unido y Suiza, y cómo oponerse.",
           "h1": "Política de privacidad", "back": "Volver a la página de inicio", "manage": "Gestionar mis opciones de cookies"},
    "pt": {"title": "Política de privacidade | Tâmaras Ajwa por Grosso",
           "description": "Como o site Tâmaras Ajwa por Grosso usa cookies do Google Analytics e do Google Ads para medir as visitas e os contactos por WhatsApp, o consentimento pedido no EEE, no Reino Unido e na Suíça, e como se opor.",
           "h1": "Política de privacidade", "back": "Voltar à página inicial", "manage": "Gerir as minhas opções de cookies"},
}

BODY = {
"en": """
<p>This page explains what data is collected when you visit the Ajwa Dates Wholesale website ({SITE}/), why, how long it is kept and how to exercise your rights.</p>

<h2>1. Who is responsible for your data?</h2>
<p>The data controller is the publisher of the Ajwa Dates Wholesale website. For any question about your data, contact us on WhatsApp at <a href="{WA}" target="_blank" rel="noopener" data-cta="whatsapp" data-cta-location="privacy">{PHONE}</a>.</p>

<h2>2. What data is collected?</h2>
<p>This site has no forms, no customer accounts and no online payments. The only data collected on the site comes from <strong>Google Analytics&nbsp;4</strong> audience measurement and <strong>Google Ads</strong> advertising measurement, used to measure visits and WhatsApp contacts. Visitors in the European Economic Area, the United Kingdom and Switzerland are asked for their consent first:</p>
<ul>
  <li>the pages you view, the date and length of your visit, and the page you came from (search engine, social network, direct link);</li>
  <li>technical information: device type, operating system, browser, language, screen resolution;</li>
  <li>an approximate location (country, region, city), derived from your IP address. According to Google, Google Analytics&nbsp;4 does not log or store IP addresses;</li>
  <li>clicks on the WhatsApp buttons (where the button is on the page and the link address);</li>
  <li>a random identifier stored in a cookie, which tells visits and visitors apart without knowing who you are;</li>
  <li>if you reach the site by clicking one of our Google ads, the identifier of that ad click ("gclid"), which shows whether the visit from the ad led to a click on a WhatsApp button (a "conversion").</li>
</ul>
<p>This data is used for visit statistics, to understand how the site is used and improve it, and to measure the performance of our ads (how many visits from an ad lead to a WhatsApp enquiry). In the European Economic Area, the United Kingdom and Switzerland, the legal basis is your consent; elsewhere, it is our legitimate interest in measuring and improving the site and our ads, which you can object to at any time (see section&nbsp;4).</p>
<p>Google Ads may also use your visits to this site to show you our ads on other sites (remarketing and personalised advertising). Our Google Analytics property is linked to our Google Ads account for these purposes. You can turn this off at any time (see section&nbsp;4).</p>

<h2>3. Cookies and local storage</h2>
<p>The Google tag (Google Analytics and Google Ads) is loaded on every page. If you are in the European Economic Area, the United Kingdom or Switzerland, a banner asks for your consent and, until you click "Accept" (or if you click "Decline"), Google's Consent Mode is set to "denied": no Google Analytics or Google Ads cookie is set, no WhatsApp click is counted as an ad conversion, and Google only receives cookieless, aggregate signals (for example that a page was viewed) without an identifier that would recognise you. If you arrive from an ad, the ad click identifier may stay in the address (URL) of the pages you then view, without being stored in a cookie. To tell whether to show the banner, the site checks your country from your IP address (through our host, Vercel); this country is not stored.</p>
<div class="table-wrap"><table>
  <thead><tr><th>Name</th><th>Purpose</th><th>Duration</th></tr></thead>
  <tbody>
    <tr><td><code>_ga</code></td><td>Google Analytics cookie: tells visitors apart (random identifier). In the EEA, the UK and Switzerland: only after "Accept".</td><td>13&nbsp;months maximum</td></tr>
    <tr><td><code>_ga_&lt;id&gt;</code></td><td>Google Analytics cookie: keeps the session state. In the EEA, the UK and Switzerland: only after "Accept".</td><td>13&nbsp;months maximum</td></tr>
    <tr><td><code>_gcl_au</code></td><td>Google Ads cookie: measures conversions (WhatsApp clicks) that come from our ads. In the EEA, the UK and Switzerland: only after "Accept".</td><td>90&nbsp;days</td></tr>
    <tr><td><code>_gcl_aw</code></td><td>Google Ads cookie: keeps the identifier of a click on one of our ads (gclid), if you arrived from an ad. In the EEA, the UK and Switzerland: only after "Accept".</td><td>90&nbsp;days</td></tr>
    <tr><td><code>{KEY}</code></td><td>Your browser's local storage (not a cookie): remembers your "Accept" or "Decline" choice (EEA, UK and Switzerland) so you are not asked on every page.</td><td>6&nbsp;months</td></tr>
  </tbody>
</table></div>

<h2>4. Your consent and how to opt out</h2>
<p>In the European Economic Area, the United Kingdom and Switzerland, a banner asks you on your first visit to accept or decline audience measurement (Google Analytics) and advertising cookies (Google Ads). Declining is as easy as accepting and does not stop you from using the site. Your choice is kept for 6&nbsp;months, after which the banner appears again. You can change your mind at any time: <button type="button" class="link-btn" data-consent-open>{MANAGE}</button> (also available through the "Manage cookies" link at the bottom of every page). If you decline or withdraw your consent, the Google Analytics cookies (<code>_ga</code>…) and Google Ads cookies (<code>_gcl</code>…) are deleted.</p>
<p>Wherever you are, you can also opt out:</p>
<ul>
  <li>in your browser settings, by blocking or deleting cookies for this site (or third-party cookies);</li>
  <li>in your Google account, by turning off personalised ads in <a href="https://myadcenter.google.com/" target="_blank" rel="noopener">My Ad Center (Google ad settings)</a>;</li>
  <li>for Google Analytics, by installing the <a href="https://tools.google.com/dlpage/gaoptout" target="_blank" rel="noopener">Google Analytics opt-out browser add-on</a>.</li>
</ul>

<h2>5. How long data is kept</h2>
<ul>
  <li>Google Analytics statistics: 14&nbsp;months maximum, then deleted automatically.</li>
  <li>Google Analytics cookies: 13&nbsp;months maximum.</li>
  <li>Google Ads cookies: 90&nbsp;days.</li>
  <li>Your consent choice (EEA, UK and Switzerland): 6&nbsp;months.</li>
  <li>Messages you send us on WhatsApp: as long as needed to answer your request and follow up on your order.</li>
</ul>

<h2>6. Who receives this data?</h2>
<ul>
  <li><strong>Google</strong> (Google Analytics), as a service provider for audience measurement, and <strong>Google</strong> (Google Ads), for measuring the performance of our ads and, where allowed (in the EEA, the UK and Switzerland, with your consent), remarketing and personalised advertising. For Google Ads, Google also uses this data under its own rules: <a href="https://policies.google.com/technologies/partner-sites" target="_blank" rel="noopener">how Google uses data from sites that use its services</a>. Data may be transferred to the United States; Google LLC is certified under the EU–US Data Privacy Framework.</li>
  <li><strong>Vercel</strong>, the site's host, which processes technical logs (including IP addresses) needed to run and secure the site.</li>
  <li><strong>WhatsApp</strong>: when you click a WhatsApp button, you leave the site; the messages you send are handled by WhatsApp under its own privacy policy.</li>
</ul>
<p>We never sell your personal data.</p>

<h2>7. Your rights</h2>
<p>Depending on where you live (for example in the European Union, the United Kingdom or certain US states), you may have the right to access, correct, delete or receive a copy of your data, to object to or restrict its use, and to withdraw your consent at any time. To exercise these rights, message us on WhatsApp ({PHONE}). Because Google Analytics and Google Ads data is pseudonymous, we cannot always link it to a specific person; the simplest option is then to decline or withdraw your consent, or use the opt-out options in section&nbsp;4, and delete your cookies.</p>
<p>If you believe your rights have not been respected, you can file a complaint with your local data protection authority.</p>

<h2>8. Changes</h2>
<p>This policy may be updated, for example if new tools are added to the site. The date of the last update is shown at the top of this page.</p>
""",
"fr": """
<p>Cette page explique quelles données sont collectées lorsque vous visitez le site Dattes Ajwa en Gros ({SITE}/fr/), pourquoi, combien de temps elles sont conservées et comment exercer vos droits.</p>

<h2>1. Qui est responsable de vos données ?</h2>
<p>Le responsable du traitement est l'éditeur du site Dattes Ajwa en Gros. Pour toute question sur vos données, contactez-nous sur WhatsApp au <a href="{WA}" target="_blank" rel="noopener" data-cta="whatsapp" data-cta-location="privacy">{PHONE}</a>.</p>

<h2>2. Quelles données sont collectées ?</h2>
<p>Ce site n'a ni formulaire, ni compte client, ni paiement en ligne. Les seules données collectées sur le site proviennent de la mesure d'audience <strong>Google Analytics&nbsp;4</strong> et de la mesure publicitaire <strong>Google Ads</strong>, utilisées pour mesurer les visites et les contacts WhatsApp. Les visiteurs de l'Espace économique européen, du Royaume-Uni et de la Suisse sont d'abord invités à donner leur consentement :</p>
<ul>
  <li>les pages consultées, la date et la durée de la visite, et la page d'où vous venez (moteur de recherche, réseau social, lien direct) ;</li>
  <li>des informations techniques : type d'appareil, système d'exploitation, navigateur, langue, résolution d'écran ;</li>
  <li>une localisation approximative (pays, région, ville), déduite de votre adresse IP. Selon Google, Google Analytics&nbsp;4 n'enregistre ni ne conserve les adresses IP ;</li>
  <li>les clics sur les boutons WhatsApp (emplacement du bouton dans la page et adresse du lien) ;</li>
  <li>un identifiant aléatoire stocké dans un cookie, qui distingue les visites et les visiteurs sans savoir qui vous êtes ;</li>
  <li>si vous arrivez en cliquant sur l'une de nos annonces Google, l'identifiant de ce clic (« gclid »), qui indique si la visite issue de l'annonce a mené à un clic sur un bouton WhatsApp (une « conversion »).</li>
</ul>
<p>Ces données servent aux statistiques de visite, à comprendre l'utilisation du site pour l'améliorer, et à mesurer la performance de nos annonces (combien de visites issues d'une annonce mènent à une demande sur WhatsApp). Dans l'Espace économique européen, au Royaume-Uni et en Suisse, la base légale est votre consentement ; ailleurs, c'est notre intérêt légitime à mesurer et améliorer le site et nos annonces, auquel vous pouvez vous opposer à tout moment (voir la section&nbsp;4).</p>
<p>Google Ads peut aussi utiliser vos visites sur ce site pour vous montrer nos annonces sur d'autres sites (remarketing et publicité personnalisée). Notre propriété Google Analytics est associée à notre compte Google Ads à ces fins. Vous pouvez désactiver cela à tout moment (voir la section&nbsp;4).</p>

<h2>3. Cookies et stockage local</h2>
<p>La balise Google (Google Analytics et Google Ads) est chargée sur chaque page. Si vous êtes dans l'Espace économique européen, au Royaume-Uni ou en Suisse, un bandeau vous demande votre consentement et, tant que vous n'avez pas cliqué sur « Accepter » (ou si vous cliquez sur « Refuser »), le mode Consentement de Google est réglé sur « refusé » : aucun cookie Google Analytics ou Google Ads n'est déposé, aucun clic WhatsApp n'est compté comme conversion publicitaire, et Google ne reçoit que des signaux agrégés sans cookie (par exemple qu'une page a été vue), sans identifiant permettant de vous reconnaître. Si vous arrivez depuis une annonce, l'identifiant du clic peut rester dans l'adresse (URL) des pages que vous consultez ensuite, sans être enregistré dans un cookie. Pour savoir s'il faut afficher le bandeau, le site détermine votre pays à partir de votre adresse IP (via notre hébergeur, Vercel) ; ce pays n'est pas conservé.</p>
<div class="table-wrap"><table>
  <thead><tr><th>Nom</th><th>Finalité</th><th>Durée</th></tr></thead>
  <tbody>
    <tr><td><code>_ga</code></td><td>Cookie Google Analytics : distingue les visiteurs (identifiant aléatoire). Dans l'EEE, au Royaume-Uni et en Suisse : uniquement après « Accepter ».</td><td>13&nbsp;mois maximum</td></tr>
    <tr><td><code>_ga_&lt;id&gt;</code></td><td>Cookie Google Analytics : conserve l'état de la session. Dans l'EEE, au Royaume-Uni et en Suisse : uniquement après « Accepter ».</td><td>13&nbsp;mois maximum</td></tr>
    <tr><td><code>_gcl_au</code></td><td>Cookie Google Ads : mesure les conversions (clics WhatsApp) issues de nos annonces. Dans l'EEE, au Royaume-Uni et en Suisse : uniquement après « Accepter ».</td><td>90&nbsp;jours</td></tr>
    <tr><td><code>_gcl_aw</code></td><td>Cookie Google Ads : conserve l'identifiant d'un clic sur l'une de nos annonces (gclid), si vous venez d'une annonce. Dans l'EEE, au Royaume-Uni et en Suisse : uniquement après « Accepter ».</td><td>90&nbsp;jours</td></tr>
    <tr><td><code>{KEY}</code></td><td>Stockage local de votre navigateur (pas un cookie) : mémorise votre choix « Accepter » ou « Refuser » (EEE, Royaume-Uni et Suisse) pour ne pas vous le redemander à chaque page.</td><td>6&nbsp;mois</td></tr>
  </tbody>
</table></div>

<h2>4. Votre consentement et comment vous opposer au suivi</h2>
<p>Dans l'Espace économique européen, au Royaume-Uni et en Suisse, un bandeau vous demande lors de votre première visite d'accepter ou de refuser la mesure d'audience (Google Analytics) et les cookies publicitaires (Google Ads). Refuser est aussi simple qu'accepter et ne vous empêche pas d'utiliser le site. Votre choix est conservé 6&nbsp;mois, après quoi le bandeau réapparaît. Vous pouvez changer d'avis à tout moment : <button type="button" class="link-btn" data-consent-open>{MANAGE}</button> (aussi accessible par le lien « Gérer les cookies » en bas de chaque page). Si vous refusez ou retirez votre consentement, les cookies Google Analytics (<code>_ga</code>…) et Google Ads (<code>_gcl</code>…) sont supprimés.</p>
<p>Où que vous soyez, vous pouvez aussi vous opposer au suivi :</p>
<ul>
  <li>dans les réglages de votre navigateur, en bloquant ou supprimant les cookies de ce site (ou les cookies tiers) ;</li>
  <li>dans votre compte Google, en désactivant les annonces personnalisées dans <a href="https://myadcenter.google.com/?hl=fr" target="_blank" rel="noopener">Mon centre publicitaire (paramètres des annonces Google)</a> ;</li>
  <li>pour Google Analytics, en installant le <a href="https://tools.google.com/dlpage/gaoptout?hl=fr" target="_blank" rel="noopener">module complémentaire de navigateur pour la désactivation de Google Analytics</a>.</li>
</ul>

<h2>5. Durée de conservation</h2>
<ul>
  <li>Statistiques Google Analytics : 14&nbsp;mois maximum, puis suppression automatique.</li>
  <li>Cookies Google Analytics : 13&nbsp;mois maximum.</li>
  <li>Cookies Google Ads : 90&nbsp;jours.</li>
  <li>Votre choix de consentement (EEE, Royaume-Uni et Suisse) : 6&nbsp;mois.</li>
  <li>Messages que vous nous envoyez sur WhatsApp : le temps nécessaire pour répondre à votre demande et suivre votre commande.</li>
</ul>

<h2>6. Qui reçoit ces données ?</h2>
<ul>
  <li><strong>Google</strong> (Google Analytics), en tant que prestataire de mesure d'audience, et <strong>Google</strong> (Google Ads), pour mesurer la performance de nos annonces et, lorsque c'est permis (dans l'EEE, au Royaume-Uni et en Suisse, avec votre consentement), pour le remarketing et la publicité personnalisée. Pour Google Ads, Google utilise aussi ces données selon ses propres règles : <a href="https://policies.google.com/technologies/partner-sites?hl=fr" target="_blank" rel="noopener">comment Google utilise les données des sites qui utilisent ses services</a>. Les données peuvent être transférées aux États-Unis ; Google LLC est certifiée au titre du Data Privacy Framework UE–États-Unis.</li>
  <li><strong>Vercel</strong>, l'hébergeur du site, qui traite les journaux techniques (dont les adresses IP) nécessaires au fonctionnement et à la sécurité du site.</li>
  <li><strong>WhatsApp</strong> : en cliquant sur un bouton WhatsApp, vous quittez le site ; les messages que vous envoyez sont traités par WhatsApp selon sa propre politique de confidentialité.</li>
</ul>
<p>Nous ne vendons jamais vos données personnelles.</p>

<h2>7. Vos droits</h2>
<p>Selon votre lieu de résidence (par exemple l'Union européenne, le Royaume-Uni ou certains États américains), vous pouvez avoir le droit d'accéder à vos données, de les rectifier, de les effacer ou d'en recevoir une copie, de vous opposer à leur utilisation ou de la limiter, et de retirer votre consentement à tout moment. Pour exercer ces droits, écrivez-nous sur WhatsApp ({PHONE}). Les données Google Analytics et Google Ads étant pseudonymes, nous ne pouvons pas toujours les relier à une personne précise ; le plus simple est alors de refuser ou retirer votre consentement, ou d'utiliser les options de la section&nbsp;4, et de supprimer vos cookies.</p>
<p>Si vous estimez que vos droits ne sont pas respectés, vous pouvez déposer une réclamation auprès de l'autorité de protection des données de votre pays (en France, la CNIL).</p>

<h2>8. Modifications</h2>
<p>Cette politique peut être mise à jour, par exemple si de nouveaux outils sont ajoutés au site. La date de la dernière mise à jour figure en haut de cette page.</p>
""",
"es": """
<p>Esta página explica qué datos se recogen cuando visita el sitio Dátiles Ajwa al por Mayor ({SITE}/es/), para qué, cuánto tiempo se conservan y cómo ejercer sus derechos.</p>

<h2>1. ¿Quién es responsable de sus datos?</h2>
<p>El responsable del tratamiento es el editor del sitio Dátiles Ajwa al por Mayor. Para cualquier pregunta sobre sus datos, escríbanos por WhatsApp al <a href="{WA}" target="_blank" rel="noopener" data-cta="whatsapp" data-cta-location="privacy">{PHONE}</a>.</p>

<h2>2. ¿Qué datos se recogen?</h2>
<p>Este sitio no tiene formularios, ni cuentas de cliente, ni pagos en línea. Los únicos datos recogidos en el sitio proceden de la medición de audiencia de <strong>Google Analytics&nbsp;4</strong> y de la medición publicitaria de <strong>Google Ads</strong>, que sirven para medir las visitas y los contactos por WhatsApp. A los visitantes del Espacio Económico Europeo, el Reino Unido y Suiza se les pide antes su consentimiento:</p>
<ul>
  <li>las páginas que visita, la fecha y duración de la visita, y la página de procedencia (buscador, red social, enlace directo);</li>
  <li>información técnica: tipo de dispositivo, sistema operativo, navegador, idioma, resolución de pantalla;</li>
  <li>una ubicación aproximada (país, región, ciudad), deducida de su dirección IP. Según Google, Google Analytics&nbsp;4 no registra ni almacena direcciones IP;</li>
  <li>los clics en los botones de WhatsApp (ubicación del botón en la página y dirección del enlace);</li>
  <li>un identificador aleatorio guardado en una cookie, que distingue visitas y visitantes sin saber quién es usted;</li>
  <li>si llega al sitio haciendo clic en uno de nuestros anuncios de Google, el identificador de ese clic («gclid»), que indica si la visita desde el anuncio terminó en un clic en un botón de WhatsApp (una «conversión»).</li>
</ul>
<p>Estos datos sirven para las estadísticas de visitas, para entender cómo se usa el sitio y mejorarlo, y para medir el rendimiento de nuestros anuncios (cuántas visitas desde un anuncio terminan en una consulta por WhatsApp). En el Espacio Económico Europeo, el Reino Unido y Suiza, la base legal es su consentimiento; en otros lugares, es nuestro interés legítimo en medir y mejorar el sitio y nuestros anuncios, al que puede oponerse en cualquier momento (vea la sección&nbsp;4).</p>
<p>Google Ads también puede usar sus visitas a este sitio para mostrarle nuestros anuncios en otros sitios (remarketing y publicidad personalizada). Nuestra propiedad de Google Analytics está vinculada a nuestra cuenta de Google Ads con estos fines. Puede desactivarlo en cualquier momento (vea la sección&nbsp;4).</p>

<h2>3. Cookies y almacenamiento local</h2>
<p>La etiqueta de Google (Google Analytics y Google Ads) se carga en todas las páginas. Si está en el Espacio Económico Europeo, el Reino Unido o Suiza, un aviso le pide su consentimiento y, mientras no haga clic en «Aceptar» (o si hace clic en «Rechazar»), el modo de consentimiento de Google queda en «denegado»: no se instala ninguna cookie de Google Analytics o Google Ads, ningún clic en WhatsApp se cuenta como conversión publicitaria y Google solo recibe señales agregadas sin cookies (por ejemplo, que se vio una página), sin un identificador que permita reconocerle. Si llega desde un anuncio, el identificador del clic puede quedar en la dirección (URL) de las páginas que visite después, sin guardarse en una cookie. Para saber si debe mostrar el aviso, el sitio determina su país a partir de su dirección IP (a través de nuestro proveedor de alojamiento, Vercel); ese país no se guarda.</p>
<div class="table-wrap"><table>
  <thead><tr><th>Nombre</th><th>Finalidad</th><th>Duración</th></tr></thead>
  <tbody>
    <tr><td><code>_ga</code></td><td>Cookie de Google Analytics: distingue a los visitantes (identificador aleatorio). En el EEE, el Reino Unido y Suiza: solo tras «Aceptar».</td><td>13&nbsp;meses como máximo</td></tr>
    <tr><td><code>_ga_&lt;id&gt;</code></td><td>Cookie de Google Analytics: mantiene el estado de la sesión. En el EEE, el Reino Unido y Suiza: solo tras «Aceptar».</td><td>13&nbsp;meses como máximo</td></tr>
    <tr><td><code>_gcl_au</code></td><td>Cookie de Google Ads: mide las conversiones (clics en WhatsApp) que proceden de nuestros anuncios. En el EEE, el Reino Unido y Suiza: solo tras «Aceptar».</td><td>90&nbsp;días</td></tr>
    <tr><td><code>_gcl_aw</code></td><td>Cookie de Google Ads: guarda el identificador de un clic en uno de nuestros anuncios (gclid), si llegó desde un anuncio. En el EEE, el Reino Unido y Suiza: solo tras «Aceptar».</td><td>90&nbsp;días</td></tr>
    <tr><td><code>{KEY}</code></td><td>Almacenamiento local del navegador (no es una cookie): recuerda su elección «Aceptar» o «Rechazar» (EEE, Reino Unido y Suiza) para no preguntarle en cada página.</td><td>6&nbsp;meses</td></tr>
  </tbody>
</table></div>

<h2>4. Su consentimiento y cómo oponerse</h2>
<p>En el Espacio Económico Europeo, el Reino Unido y Suiza, en su primera visita un aviso le pide aceptar o rechazar la medición de audiencia (Google Analytics) y las cookies publicitarias (Google Ads). Rechazar es tan fácil como aceptar y no le impide usar el sitio. Su elección se conserva 6&nbsp;meses; después, el aviso vuelve a aparecer. Puede cambiar de opinión en cualquier momento: <button type="button" class="link-btn" data-consent-open>{MANAGE}</button> (también desde el enlace «Gestionar cookies» al pie de cada página). Si rechaza o retira su consentimiento, se eliminan las cookies de Google Analytics (<code>_ga</code>…) y de Google Ads (<code>_gcl</code>…).</p>
<p>Esté donde esté, también puede oponerse:</p>
<ul>
  <li>en los ajustes de su navegador, bloqueando o borrando las cookies de este sitio (o las cookies de terceros);</li>
  <li>en su cuenta de Google, desactivando los anuncios personalizados en <a href="https://myadcenter.google.com/?hl=es" target="_blank" rel="noopener">Mi Centro de anuncios (configuración de anuncios de Google)</a>;</li>
  <li>para Google Analytics, instalando el <a href="https://tools.google.com/dlpage/gaoptout?hl=es" target="_blank" rel="noopener">complemento de inhabilitación para navegadores de Google Analytics</a>.</li>
</ul>

<h2>5. Plazos de conservación</h2>
<ul>
  <li>Estadísticas de Google Analytics: 14&nbsp;meses como máximo; después se eliminan automáticamente.</li>
  <li>Cookies de Google Analytics: 13&nbsp;meses como máximo.</li>
  <li>Cookies de Google Ads: 90&nbsp;días.</li>
  <li>Su elección de consentimiento (EEE, Reino Unido y Suiza): 6&nbsp;meses.</li>
  <li>Mensajes que nos envía por WhatsApp: el tiempo necesario para responder a su solicitud y dar seguimiento a su pedido.</li>
</ul>

<h2>6. ¿Quién recibe estos datos?</h2>
<ul>
  <li><strong>Google</strong> (Google Analytics), como proveedor de medición de audiencia, y <strong>Google</strong> (Google Ads), para medir el rendimiento de nuestros anuncios y, cuando está permitido (en el EEE, el Reino Unido y Suiza, con su consentimiento), para remarketing y publicidad personalizada. Para Google Ads, Google también usa estos datos según sus propias normas: <a href="https://policies.google.com/technologies/partner-sites?hl=es" target="_blank" rel="noopener">cómo usa Google los datos de los sitios que utilizan sus servicios</a>. Los datos pueden transferirse a Estados Unidos; Google LLC está certificada en el Marco de Privacidad de Datos UE–EE.&nbsp;UU.</li>
  <li><strong>Vercel</strong>, el proveedor de alojamiento del sitio, que trata los registros técnicos (incluidas las direcciones IP) necesarios para el funcionamiento y la seguridad del sitio.</li>
  <li><strong>WhatsApp</strong>: al hacer clic en un botón de WhatsApp, sale del sitio; los mensajes que envía los gestiona WhatsApp según su propia política de privacidad.</li>
</ul>
<p>Nunca vendemos sus datos personales.</p>

<h2>7. Sus derechos</h2>
<p>Según dónde viva (por ejemplo en la Unión Europea, el Reino Unido o algunos estados de EE.&nbsp;UU.), puede tener derecho a acceder a sus datos, rectificarlos, suprimirlos o recibir una copia, a oponerse a su uso o limitarlo, y a retirar su consentimiento en cualquier momento. Para ejercer estos derechos, escríbanos por WhatsApp ({PHONE}). Como los datos de Google Analytics y Google Ads son seudónimos, no siempre podemos vincularlos a una persona concreta; lo más sencillo es entonces rechazar o retirar su consentimiento, o usar las opciones de la sección&nbsp;4, y borrar sus cookies.</p>
<p>Si considera que no se han respetado sus derechos, puede presentar una reclamación ante la autoridad de protección de datos de su país (en España, la AEPD).</p>

<h2>8. Cambios</h2>
<p>Esta política puede actualizarse, por ejemplo si se añaden nuevas herramientas al sitio. La fecha de la última actualización figura al principio de esta página.</p>
""",
"pt": """
<p>Esta página explica que dados são recolhidos quando visita o site Tâmaras Ajwa por Grosso ({SITE}/), porquê, durante quanto tempo são conservados e como exercer os seus direitos.</p>

<h2>1. Quem é responsável pelos seus dados?</h2>
<p>O responsável pelo tratamento é o editor do site Tâmaras Ajwa por Grosso. Para qualquer questão sobre os seus dados, contacte-nos no WhatsApp através do <a href="{WA}" target="_blank" rel="noopener" data-cta="whatsapp" data-cta-location="privacy">{PHONE}</a>.</p>

<h2>2. Que dados são recolhidos?</h2>
<p>Este site não tem formulários, contas de cliente nem pagamentos online. Os únicos dados recolhidos no site provêm da medição de audiência do <strong>Google Analytics&nbsp;4</strong> e da medição publicitária do <strong>Google Ads</strong>, usadas para medir as visitas e os contactos por WhatsApp. Aos visitantes do Espaço Económico Europeu, do Reino Unido e da Suíça é pedido primeiro o consentimento:</p>
<ul>
  <li>as páginas que consulta, a data e a duração da visita e a página de onde veio (motor de pesquisa, rede social, link direto);</li>
  <li>informações técnicas: tipo de dispositivo, sistema operativo, navegador, idioma, resolução do ecrã;</li>
  <li>uma localização aproximada (país, região, cidade), obtida a partir do seu endereço IP. Segundo a Google, o Google Analytics&nbsp;4 não regista nem guarda endereços IP;</li>
  <li>os cliques nos botões do WhatsApp (o local do botão na página e o endereço do link);</li>
  <li>um identificador aleatório guardado num cookie, que distingue visitas e visitantes sem saber quem é;</li>
  <li>se chegar ao site clicando num dos nossos anúncios Google, o identificador desse clique («gclid»), que mostra se a visita vinda do anúncio levou a um clique num botão do WhatsApp (uma «conversão»).</li>
</ul>
<p>Estes dados servem para estatísticas de visitas, para perceber como o site é usado e melhorá-lo, e para medir o desempenho dos nossos anúncios (quantas visitas vindas de um anúncio levam a um pedido por WhatsApp). No Espaço Económico Europeu, no Reino Unido e na Suíça, a base legal é o seu consentimento; nos restantes países, é o nosso interesse legítimo em medir e melhorar o site e os nossos anúncios, ao qual se pode opor a qualquer momento (ver secção&nbsp;4).</p>
<p>O Google Ads pode também usar as suas visitas a este site para lhe mostrar os nossos anúncios noutros sites (remarketing e publicidade personalizada). A nossa propriedade Google Analytics está associada à nossa conta Google Ads para estes fins. Pode desativar isto a qualquer momento (ver secção&nbsp;4).</p>

<h2>3. Cookies e armazenamento local</h2>
<p>A etiqueta Google (Google Analytics e Google Ads) é carregada em todas as páginas. Se estiver no Espaço Económico Europeu, no Reino Unido ou na Suíça, um banner pede o seu consentimento e, até clicar em «Aceitar» (ou se clicar em «Recusar»), o Modo de Consentimento da Google fica em «negado»: nenhum cookie do Google Analytics ou do Google Ads é criado, nenhum clique no WhatsApp é contado como conversão de anúncio, e a Google só recebe sinais agregados, sem cookies (por exemplo, que uma página foi vista), sem um identificador que o reconheça. Se chegar através de um anúncio, o identificador do clique pode ficar no endereço (URL) das páginas que consultar a seguir, sem ser guardado num cookie. Para saber se deve mostrar o banner, o site verifica o seu país a partir do endereço IP (através do nosso alojamento, a Vercel); este país não é guardado.</p>
<div class="table-wrap"><table>
  <thead><tr><th>Nome</th><th>Finalidade</th><th>Duração</th></tr></thead>
  <tbody>
    <tr><td><code>_ga</code></td><td>Cookie do Google Analytics: distingue os visitantes (identificador aleatório). No EEE, no Reino Unido e na Suíça: só depois de «Aceitar».</td><td>13&nbsp;meses no máximo</td></tr>
    <tr><td><code>_ga_&lt;id&gt;</code></td><td>Cookie do Google Analytics: guarda o estado da sessão. No EEE, no Reino Unido e na Suíça: só depois de «Aceitar».</td><td>13&nbsp;meses no máximo</td></tr>
    <tr><td><code>_gcl_au</code></td><td>Cookie do Google Ads: mede as conversões (cliques no WhatsApp) que vêm dos nossos anúncios. No EEE, no Reino Unido e na Suíça: só depois de «Aceitar».</td><td>90&nbsp;dias</td></tr>
    <tr><td><code>_gcl_aw</code></td><td>Cookie do Google Ads: guarda o identificador de um clique num dos nossos anúncios (gclid), se tiver chegado através de um anúncio. No EEE, no Reino Unido e na Suíça: só depois de «Aceitar».</td><td>90&nbsp;dias</td></tr>
    <tr><td><code>{KEY}</code></td><td>Armazenamento local do navegador (não é um cookie): memoriza a sua escolha «Aceitar» ou «Recusar» (EEE, Reino Unido e Suíça) para não lhe perguntarmos em cada página.</td><td>6&nbsp;meses</td></tr>
  </tbody>
</table></div>

<h2>4. O seu consentimento e como se opor</h2>
<p>No Espaço Económico Europeu, no Reino Unido e na Suíça, um banner pede-lhe, na primeira visita, que aceite ou recuse a medição de audiência (Google Analytics) e os cookies de publicidade (Google Ads). Recusar é tão simples como aceitar e não o impede de usar o site. A sua escolha é guardada durante 6&nbsp;meses; depois disso, o banner volta a aparecer. Pode mudar de ideias a qualquer momento: <button type="button" class="link-btn" data-consent-open>{MANAGE}</button> (também disponível no link «Gerir cookies» no fundo de cada página). Se recusar ou retirar o consentimento, os cookies do Google Analytics (<code>_ga</code>…) e do Google Ads (<code>_gcl</code>…) são apagados.</p>
<p>Esteja onde estiver, pode também opor-se:</p>
<ul>
  <li>nas definições do navegador, bloqueando ou apagando os cookies deste site (ou os cookies de terceiros);</li>
  <li>na sua conta Google, desativando os anúncios personalizados no <a href="https://myadcenter.google.com/" target="_blank" rel="noopener">Meu Centro de Anúncios (definições de anúncios Google)</a>;</li>
  <li>no caso do Google Analytics, instalando o <a href="https://tools.google.com/dlpage/gaoptout?hl=pt-PT" target="_blank" rel="noopener">extra do navegador para desativação do Google Analytics</a>.</li>
</ul>

<h2>5. Durante quanto tempo os dados são conservados</h2>
<ul>
  <li>Estatísticas do Google Analytics: 14&nbsp;meses no máximo, depois apagadas automaticamente.</li>
  <li>Cookies do Google Analytics: 13&nbsp;meses no máximo.</li>
  <li>Cookies do Google Ads: 90&nbsp;dias.</li>
  <li>A sua escolha de consentimento (EEE, Reino Unido e Suíça): 6&nbsp;meses.</li>
  <li>Mensagens que nos envia pelo WhatsApp: o tempo necessário para responder ao seu pedido e acompanhar a sua encomenda.</li>
</ul>

<h2>6. Quem recebe estes dados?</h2>
<ul>
  <li><strong>Google</strong> (Google Analytics), como prestador de serviços de medição de audiência, e <strong>Google</strong> (Google Ads), para medir o desempenho dos nossos anúncios e, quando permitido (no EEE, no Reino Unido e na Suíça, com o seu consentimento), para remarketing e publicidade personalizada. No caso do Google Ads, a Google usa também estes dados segundo as suas próprias regras: <a href="https://policies.google.com/technologies/partner-sites?hl=pt-PT" target="_blank" rel="noopener">como a Google usa os dados dos sites que utilizam os seus serviços</a>. Os dados podem ser transferidos para os Estados Unidos; a Google LLC está certificada ao abrigo do Quadro de Privacidade de Dados UE–EUA (Data Privacy Framework).</li>
  <li><strong>Vercel</strong>, o alojamento do site, que trata os registos técnicos (incluindo endereços IP) necessários ao funcionamento e à segurança do site.</li>
  <li><strong>WhatsApp</strong>: ao clicar num botão do WhatsApp, sai do site; as mensagens que envia são tratadas pelo WhatsApp segundo a sua própria política de privacidade.</li>
</ul>
<p>Nunca vendemos os seus dados pessoais.</p>

<h2>7. Os seus direitos</h2>
<p>Consoante o local onde vive (por exemplo, na União Europeia, no Reino Unido ou em certos estados dos EUA), pode ter o direito de aceder, retificar, apagar ou receber uma cópia dos seus dados, de se opor ou limitar a sua utilização e de retirar o seu consentimento a qualquer momento. Para exercer estes direitos, envie-nos uma mensagem no WhatsApp ({PHONE}). Como os dados do Google Analytics e do Google Ads são pseudónimos, nem sempre os conseguimos associar a uma pessoa concreta; a opção mais simples é então recusar ou retirar o consentimento, ou usar as opções da secção&nbsp;4, e apagar os seus cookies.</p>
<p>Se considerar que os seus direitos não foram respeitados, pode apresentar uma reclamação à autoridade de proteção de dados do seu país (em Portugal, a CNPD; no Brasil, a ANPD).</p>

<h2>8. Alterações</h2>
<p>Esta política pode ser atualizada, por exemplo se forem adicionadas novas ferramentas ao site. A data da última atualização aparece no início desta página.</p>
""",
}
