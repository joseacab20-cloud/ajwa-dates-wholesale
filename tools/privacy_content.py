# Privacy policy text (EN / FR / ES), used by tools/build.py for /privacy/, /fr/confidentialite/, /es/privacidad/.
# Modelled on the rosewaterbulk policy. No legal controller name. No cookieless pings: no Google tag
# is loaded before "Accept". {PHONE} and {KEY} are filled in by build.py.
UPDATED = {"en": "Last updated: October 28, 2026", "fr": "Dernière mise à jour : 28 octobre 2026",
           "es": "Última actualización: 28 de octubre de 2026"}

META = {
    "en": {"title": "Privacy policy | Ajwa Dates Wholesale",
           "description": "How the Ajwa Dates Wholesale website uses Google Analytics and Google Ads cookies, only with your consent, and how to manage your choice.",
           "h1": "Privacy policy", "back": "Back to home page", "manage": "Manage my cookie choices"},
    "fr": {"title": "Politique de confidentialité | Dattes Ajwa en Gros",
           "description": "Comment le site Dattes Ajwa en Gros utilise les cookies Google Analytics et Google Ads, uniquement avec votre consentement, et comment gérer votre choix.",
           "h1": "Politique de confidentialité", "back": "Retour à l'accueil", "manage": "Gérer mes choix de cookies"},
    "es": {"title": "Política de privacidad | Dátiles Ajwa al por Mayor",
           "description": "Cómo el sitio Dátiles Ajwa al por Mayor usa cookies de Google Analytics y Google Ads, solo con su consentimiento, y cómo gestionar su elección.",
           "h1": "Política de privacidad", "back": "Volver a la página de inicio", "manage": "Gestionar mis opciones de cookies"},
}

BODY = {
"en": """
<p>This page explains what data is collected when you visit the Ajwa Dates Wholesale website ({SITE}/), why, how long it is kept and how to exercise your rights.</p>

<h2>1. Who is responsible for your data?</h2>
<p>The data controller is the publisher of the Ajwa Dates Wholesale website. For any question about your data, contact us on WhatsApp at <a href="{WA}" target="_blank" rel="noopener" data-cta="whatsapp" data-cta-location="privacy">{PHONE}</a>.</p>

<h2>2. What data is collected?</h2>
<p>This site has no forms, no customer accounts and no online payments. The only data collected on the site comes from <strong>Google Analytics&nbsp;4</strong> audience measurement and <strong>Google Ads</strong> advertising measurement, and only if you accept it:</p>
<ul>
  <li>the pages you view, the date and length of your visit, and the page you came from (search engine, social network, direct link);</li>
  <li>technical information: device type, operating system, browser, language, screen resolution;</li>
  <li>an approximate location (country, region, city), derived from your IP address. According to Google, Google Analytics&nbsp;4 does not log or store IP addresses;</li>
  <li>clicks on the WhatsApp buttons (where the button is on the page and the link address);</li>
  <li>a random identifier stored in a cookie, which tells visits and visitors apart without knowing who you are;</li>
  <li>if you reach the site by clicking one of our Google ads, the identifier of that ad click ("gclid"), which shows whether the visit from the ad led to a click on a WhatsApp button (a "conversion").</li>
</ul>
<p>This data is used for visit statistics, to understand how the site is used and improve it, and to measure the performance of our ads (how many visits from an ad lead to a WhatsApp enquiry). Where the law requires it (for example in the European Union or the United Kingdom), the legal basis is your consent.</p>
<p>With your consent, Google Ads may also use your visits to this site to show you our ads on other sites (remarketing and personalised advertising). Our Google Analytics property is linked to our Google Ads account for these purposes. You can decline or withdraw this consent at any time through the cookie banner or the "Manage cookies" link at the bottom of every page.</p>

<h2>3. Cookies and local storage</h2>
<p>Until you click "Accept", or if you click "Decline", no Google tag is loaded: nothing is sent to Google Analytics or Google Ads and no Google Analytics or Google Ads cookie is set. If you arrive from an ad, the ad click identifier may stay in the address (URL) of the pages you then view on the site, without being stored in a cookie.</p>
<div class="table-wrap"><table>
  <thead><tr><th>Name</th><th>Purpose</th><th>Duration</th></tr></thead>
  <tbody>
    <tr><td><code>_ga</code></td><td>Google Analytics cookie: tells visitors apart (random identifier). Set only after "Accept".</td><td>13&nbsp;months maximum</td></tr>
    <tr><td><code>_ga_&lt;id&gt;</code></td><td>Google Analytics cookie: keeps the session state. Set only after "Accept".</td><td>13&nbsp;months maximum</td></tr>
    <tr><td><code>_gcl_au</code></td><td>Google Ads cookie: measures conversions (WhatsApp clicks) that come from our ads. Set only after "Accept".</td><td>90&nbsp;days</td></tr>
    <tr><td><code>_gcl_aw</code></td><td>Google Ads cookie: keeps the identifier of a click on one of our ads (gclid), if you arrived from an ad. Set only after "Accept".</td><td>90&nbsp;days</td></tr>
    <tr><td><code>{KEY}</code></td><td>Your browser's local storage (not a cookie): remembers your "Accept" or "Decline" choice so you are not asked on every page.</td><td>6&nbsp;months</td></tr>
  </tbody>
</table></div>

<h2>4. Your consent and how to withdraw it</h2>
<p>On your first visit, a banner asks you to accept or decline audience measurement (Google Analytics) and advertising cookies (Google Ads). Declining is as easy as accepting and does not stop you from using the site. Your choice is kept for 6&nbsp;months, after which the banner appears again.</p>
<p>You can change your mind at any time: <button type="button" class="link-btn" data-consent-open>{MANAGE}</button> (also available through the "Manage cookies" link at the bottom of every page). If you decline or withdraw your consent, the Google Analytics cookies (<code>_ga</code>…) and Google Ads cookies (<code>_gcl</code>…) are deleted. You can also clear cookies and site data in your browser settings.</p>

<h2>5. How long data is kept</h2>
<ul>
  <li>Google Analytics statistics: 14&nbsp;months maximum, then deleted automatically.</li>
  <li>Google Analytics cookies: 13&nbsp;months maximum.</li>
  <li>Google Ads cookies: 90&nbsp;days.</li>
  <li>Your consent choice: 6&nbsp;months.</li>
  <li>Messages you send us on WhatsApp: as long as needed to answer your request and follow up on your order.</li>
</ul>

<h2>6. Who receives this data?</h2>
<ul>
  <li><strong>Google</strong> (Google Analytics), as a service provider for audience measurement, and <strong>Google</strong> (Google Ads), for measuring the performance of our ads and, with your consent, remarketing and personalised advertising. For Google Ads, Google also uses this data under its own rules: <a href="https://policies.google.com/technologies/partner-sites" target="_blank" rel="noopener">how Google uses data from sites that use its services</a>. Data may be transferred to the United States; Google LLC is certified under the EU–US Data Privacy Framework.</li>
  <li><strong>Vercel</strong>, the site's host, which processes technical logs (including IP addresses) needed to run and secure the site.</li>
  <li><strong>WhatsApp</strong>: when you click a WhatsApp button, you leave the site; the messages you send are handled by WhatsApp under its own privacy policy.</li>
</ul>
<p>We never sell your personal data.</p>

<h2>7. Your rights</h2>
<p>Depending on where you live (for example in the European Union, the United Kingdom or certain US states), you may have the right to access, correct, delete or receive a copy of your data, to object to or restrict its use, and to withdraw your consent at any time. To exercise these rights, message us on WhatsApp ({PHONE}). Because Google Analytics and Google Ads data is pseudonymous, we cannot always link it to a specific person; the simplest option is then to decline or withdraw your consent and delete your cookies.</p>
<p>If you believe your rights have not been respected, you can file a complaint with your local data protection authority.</p>

<h2>8. Changes</h2>
<p>This policy may be updated, for example if new tools are added to the site. The date of the last update is shown at the top of this page.</p>
""",
"fr": """
<p>Cette page explique quelles données sont collectées lorsque vous visitez le site Dattes Ajwa en Gros ({SITE}/fr/), pourquoi, combien de temps elles sont conservées et comment exercer vos droits.</p>

<h2>1. Qui est responsable de vos données ?</h2>
<p>Le responsable du traitement est l'éditeur du site Dattes Ajwa en Gros. Pour toute question sur vos données, contactez-nous sur WhatsApp au <a href="{WA}" target="_blank" rel="noopener" data-cta="whatsapp" data-cta-location="privacy">{PHONE}</a>.</p>

<h2>2. Quelles données sont collectées ?</h2>
<p>Ce site n'a ni formulaire, ni compte client, ni paiement en ligne. Les seules données collectées sur le site proviennent de la mesure d'audience <strong>Google Analytics&nbsp;4</strong> et de la mesure publicitaire <strong>Google Ads</strong>, et uniquement si vous l'acceptez :</p>
<ul>
  <li>les pages consultées, la date et la durée de la visite, et la page d'où vous venez (moteur de recherche, réseau social, lien direct) ;</li>
  <li>des informations techniques : type d'appareil, système d'exploitation, navigateur, langue, résolution d'écran ;</li>
  <li>une localisation approximative (pays, région, ville), déduite de votre adresse IP. Selon Google, Google Analytics&nbsp;4 n'enregistre ni ne conserve les adresses IP ;</li>
  <li>les clics sur les boutons WhatsApp (emplacement du bouton dans la page et adresse du lien) ;</li>
  <li>un identifiant aléatoire stocké dans un cookie, qui distingue les visites et les visiteurs sans savoir qui vous êtes ;</li>
  <li>si vous arrivez en cliquant sur l'une de nos annonces Google, l'identifiant de ce clic (« gclid »), qui indique si la visite issue de l'annonce a mené à un clic sur un bouton WhatsApp (une « conversion »).</li>
</ul>
<p>Ces données servent aux statistiques de visite, à comprendre l'utilisation du site pour l'améliorer, et à mesurer la performance de nos annonces (combien de visites issues d'une annonce mènent à une demande sur WhatsApp). Lorsque la loi l'exige (par exemple dans l'Union européenne ou au Royaume-Uni), la base légale est votre consentement.</p>
<p>Avec votre consentement, Google Ads peut aussi utiliser vos visites sur ce site pour vous montrer nos annonces sur d'autres sites (remarketing et publicité personnalisée). Notre propriété Google Analytics est associée à notre compte Google Ads à ces fins. Vous pouvez refuser ou retirer ce consentement à tout moment via le bandeau cookies ou le lien « Gérer les cookies » en bas de chaque page.</p>

<h2>3. Cookies et stockage local</h2>
<p>Tant que vous n'avez pas cliqué sur « Accepter », ou si vous cliquez sur « Refuser », aucune balise Google n'est chargée : rien n'est envoyé à Google Analytics ni à Google Ads et aucun cookie Google Analytics ou Google Ads n'est déposé. Si vous arrivez depuis une annonce, l'identifiant du clic peut rester dans l'adresse (URL) des pages que vous consultez ensuite sur le site, sans être enregistré dans un cookie.</p>
<div class="table-wrap"><table>
  <thead><tr><th>Nom</th><th>Finalité</th><th>Durée</th></tr></thead>
  <tbody>
    <tr><td><code>_ga</code></td><td>Cookie Google Analytics : distingue les visiteurs (identifiant aléatoire). Déposé uniquement après « Accepter ».</td><td>13&nbsp;mois maximum</td></tr>
    <tr><td><code>_ga_&lt;id&gt;</code></td><td>Cookie Google Analytics : conserve l'état de la session. Déposé uniquement après « Accepter ».</td><td>13&nbsp;mois maximum</td></tr>
    <tr><td><code>_gcl_au</code></td><td>Cookie Google Ads : mesure les conversions (clics WhatsApp) issues de nos annonces. Déposé uniquement après « Accepter ».</td><td>90&nbsp;jours</td></tr>
    <tr><td><code>_gcl_aw</code></td><td>Cookie Google Ads : conserve l'identifiant d'un clic sur l'une de nos annonces (gclid), si vous venez d'une annonce. Déposé uniquement après « Accepter ».</td><td>90&nbsp;jours</td></tr>
    <tr><td><code>{KEY}</code></td><td>Stockage local de votre navigateur (pas un cookie) : mémorise votre choix « Accepter » ou « Refuser » pour ne pas vous le redemander à chaque page.</td><td>6&nbsp;mois</td></tr>
  </tbody>
</table></div>

<h2>4. Votre consentement et comment le retirer</h2>
<p>Lors de votre première visite, un bandeau vous demande d'accepter ou de refuser la mesure d'audience (Google Analytics) et les cookies publicitaires (Google Ads). Refuser est aussi simple qu'accepter et ne vous empêche pas d'utiliser le site. Votre choix est conservé 6&nbsp;mois, après quoi le bandeau réapparaît.</p>
<p>Vous pouvez changer d'avis à tout moment : <button type="button" class="link-btn" data-consent-open>{MANAGE}</button> (aussi accessible par le lien « Gérer les cookies » en bas de chaque page). Si vous refusez ou retirez votre consentement, les cookies Google Analytics (<code>_ga</code>…) et Google Ads (<code>_gcl</code>…) sont supprimés. Vous pouvez aussi effacer les cookies et données du site dans les réglages de votre navigateur.</p>

<h2>5. Durée de conservation</h2>
<ul>
  <li>Statistiques Google Analytics : 14&nbsp;mois maximum, puis suppression automatique.</li>
  <li>Cookies Google Analytics : 13&nbsp;mois maximum.</li>
  <li>Cookies Google Ads : 90&nbsp;jours.</li>
  <li>Votre choix de consentement : 6&nbsp;mois.</li>
  <li>Messages que vous nous envoyez sur WhatsApp : le temps nécessaire pour répondre à votre demande et suivre votre commande.</li>
</ul>

<h2>6. Qui reçoit ces données ?</h2>
<ul>
  <li><strong>Google</strong> (Google Analytics), en tant que prestataire de mesure d'audience, et <strong>Google</strong> (Google Ads), pour mesurer la performance de nos annonces et, avec votre consentement, pour le remarketing et la publicité personnalisée. Pour Google Ads, Google utilise aussi ces données selon ses propres règles : <a href="https://policies.google.com/technologies/partner-sites?hl=fr" target="_blank" rel="noopener">comment Google utilise les données des sites qui utilisent ses services</a>. Les données peuvent être transférées aux États-Unis ; Google LLC est certifiée au titre du Data Privacy Framework UE–États-Unis.</li>
  <li><strong>Vercel</strong>, l'hébergeur du site, qui traite les journaux techniques (dont les adresses IP) nécessaires au fonctionnement et à la sécurité du site.</li>
  <li><strong>WhatsApp</strong> : en cliquant sur un bouton WhatsApp, vous quittez le site ; les messages que vous envoyez sont traités par WhatsApp selon sa propre politique de confidentialité.</li>
</ul>
<p>Nous ne vendons jamais vos données personnelles.</p>

<h2>7. Vos droits</h2>
<p>Selon votre lieu de résidence (par exemple l'Union européenne, le Royaume-Uni ou certains États américains), vous pouvez avoir le droit d'accéder à vos données, de les rectifier, de les effacer ou d'en recevoir une copie, de vous opposer à leur utilisation ou de la limiter, et de retirer votre consentement à tout moment. Pour exercer ces droits, écrivez-nous sur WhatsApp ({PHONE}). Les données Google Analytics et Google Ads étant pseudonymes, nous ne pouvons pas toujours les relier à une personne précise ; le plus simple est alors de refuser ou retirer votre consentement et de supprimer vos cookies.</p>
<p>Si vous estimez que vos droits ne sont pas respectés, vous pouvez déposer une réclamation auprès de l'autorité de protection des données de votre pays (en France, la CNIL).</p>

<h2>8. Modifications</h2>
<p>Cette politique peut être mise à jour, par exemple si de nouveaux outils sont ajoutés au site. La date de la dernière mise à jour figure en haut de cette page.</p>
""",
"es": """
<p>Esta página explica qué datos se recogen cuando visita el sitio Dátiles Ajwa al por Mayor ({SITE}/es/), para qué, cuánto tiempo se conservan y cómo ejercer sus derechos.</p>

<h2>1. ¿Quién es responsable de sus datos?</h2>
<p>El responsable del tratamiento es el editor del sitio Dátiles Ajwa al por Mayor. Para cualquier pregunta sobre sus datos, escríbanos por WhatsApp al <a href="{WA}" target="_blank" rel="noopener" data-cta="whatsapp" data-cta-location="privacy">{PHONE}</a>.</p>

<h2>2. ¿Qué datos se recogen?</h2>
<p>Este sitio no tiene formularios, ni cuentas de cliente, ni pagos en línea. Los únicos datos recogidos en el sitio proceden de la medición de audiencia de <strong>Google Analytics&nbsp;4</strong> y de la medición publicitaria de <strong>Google Ads</strong>, y solo si usted lo acepta:</p>
<ul>
  <li>las páginas que visita, la fecha y duración de la visita, y la página de procedencia (buscador, red social, enlace directo);</li>
  <li>información técnica: tipo de dispositivo, sistema operativo, navegador, idioma, resolución de pantalla;</li>
  <li>una ubicación aproximada (país, región, ciudad), deducida de su dirección IP. Según Google, Google Analytics&nbsp;4 no registra ni almacena direcciones IP;</li>
  <li>los clics en los botones de WhatsApp (ubicación del botón en la página y dirección del enlace);</li>
  <li>un identificador aleatorio guardado en una cookie, que distingue visitas y visitantes sin saber quién es usted;</li>
  <li>si llega al sitio haciendo clic en uno de nuestros anuncios de Google, el identificador de ese clic («gclid»), que indica si la visita desde el anuncio terminó en un clic en un botón de WhatsApp (una «conversión»).</li>
</ul>
<p>Estos datos sirven para las estadísticas de visitas, para entender cómo se usa el sitio y mejorarlo, y para medir el rendimiento de nuestros anuncios (cuántas visitas desde un anuncio terminan en una consulta por WhatsApp). Cuando la ley lo exige (por ejemplo en la Unión Europea o el Reino Unido), la base legal es su consentimiento.</p>
<p>Con su consentimiento, Google Ads también puede usar sus visitas a este sitio para mostrarle nuestros anuncios en otros sitios (remarketing y publicidad personalizada). Nuestra propiedad de Google Analytics está vinculada a nuestra cuenta de Google Ads con estos fines. Puede rechazar o retirar este consentimiento en cualquier momento desde el aviso de cookies o el enlace «Gestionar cookies» al pie de cada página.</p>

<h2>3. Cookies y almacenamiento local</h2>
<p>Mientras no haga clic en «Aceptar», o si hace clic en «Rechazar», no se carga ninguna etiqueta de Google: no se envía nada a Google Analytics ni a Google Ads y no se instala ninguna cookie de Google Analytics o Google Ads. Si llega desde un anuncio, el identificador del clic puede quedar en la dirección (URL) de las páginas que visite después en el sitio, sin guardarse en una cookie.</p>
<div class="table-wrap"><table>
  <thead><tr><th>Nombre</th><th>Finalidad</th><th>Duración</th></tr></thead>
  <tbody>
    <tr><td><code>_ga</code></td><td>Cookie de Google Analytics: distingue a los visitantes (identificador aleatorio). Solo tras «Aceptar».</td><td>13&nbsp;meses como máximo</td></tr>
    <tr><td><code>_ga_&lt;id&gt;</code></td><td>Cookie de Google Analytics: mantiene el estado de la sesión. Solo tras «Aceptar».</td><td>13&nbsp;meses como máximo</td></tr>
    <tr><td><code>_gcl_au</code></td><td>Cookie de Google Ads: mide las conversiones (clics en WhatsApp) que proceden de nuestros anuncios. Solo tras «Aceptar».</td><td>90&nbsp;días</td></tr>
    <tr><td><code>_gcl_aw</code></td><td>Cookie de Google Ads: guarda el identificador de un clic en uno de nuestros anuncios (gclid), si llegó desde un anuncio. Solo tras «Aceptar».</td><td>90&nbsp;días</td></tr>
    <tr><td><code>{KEY}</code></td><td>Almacenamiento local del navegador (no es una cookie): recuerda su elección «Aceptar» o «Rechazar» para no preguntarle en cada página.</td><td>6&nbsp;meses</td></tr>
  </tbody>
</table></div>

<h2>4. Su consentimiento y cómo retirarlo</h2>
<p>En su primera visita, un aviso le pide aceptar o rechazar la medición de audiencia (Google Analytics) y las cookies publicitarias (Google Ads). Rechazar es tan fácil como aceptar y no le impide usar el sitio. Su elección se conserva 6&nbsp;meses; después, el aviso vuelve a aparecer.</p>
<p>Puede cambiar de opinión en cualquier momento: <button type="button" class="link-btn" data-consent-open>{MANAGE}</button> (también desde el enlace «Gestionar cookies» al pie de cada página). Si rechaza o retira su consentimiento, se eliminan las cookies de Google Analytics (<code>_ga</code>…) y de Google Ads (<code>_gcl</code>…). También puede borrar las cookies y los datos del sitio en los ajustes de su navegador.</p>

<h2>5. Plazos de conservación</h2>
<ul>
  <li>Estadísticas de Google Analytics: 14&nbsp;meses como máximo; después se eliminan automáticamente.</li>
  <li>Cookies de Google Analytics: 13&nbsp;meses como máximo.</li>
  <li>Cookies de Google Ads: 90&nbsp;días.</li>
  <li>Su elección de consentimiento: 6&nbsp;meses.</li>
  <li>Mensajes que nos envía por WhatsApp: el tiempo necesario para responder a su solicitud y dar seguimiento a su pedido.</li>
</ul>

<h2>6. ¿Quién recibe estos datos?</h2>
<ul>
  <li><strong>Google</strong> (Google Analytics), como proveedor de medición de audiencia, y <strong>Google</strong> (Google Ads), para medir el rendimiento de nuestros anuncios y, con su consentimiento, para remarketing y publicidad personalizada. Para Google Ads, Google también usa estos datos según sus propias normas: <a href="https://policies.google.com/technologies/partner-sites?hl=es" target="_blank" rel="noopener">cómo usa Google los datos de los sitios que utilizan sus servicios</a>. Los datos pueden transferirse a Estados Unidos; Google LLC está certificada en el Marco de Privacidad de Datos UE–EE.&nbsp;UU.</li>
  <li><strong>Vercel</strong>, el proveedor de alojamiento del sitio, que trata los registros técnicos (incluidas las direcciones IP) necesarios para el funcionamiento y la seguridad del sitio.</li>
  <li><strong>WhatsApp</strong>: al hacer clic en un botón de WhatsApp, sale del sitio; los mensajes que envía los gestiona WhatsApp según su propia política de privacidad.</li>
</ul>
<p>Nunca vendemos sus datos personales.</p>

<h2>7. Sus derechos</h2>
<p>Según dónde viva (por ejemplo en la Unión Europea, el Reino Unido o algunos estados de EE.&nbsp;UU.), puede tener derecho a acceder a sus datos, rectificarlos, suprimirlos o recibir una copia, a oponerse a su uso o limitarlo, y a retirar su consentimiento en cualquier momento. Para ejercer estos derechos, escríbanos por WhatsApp ({PHONE}). Como los datos de Google Analytics y Google Ads son seudónimos, no siempre podemos vincularlos a una persona concreta; lo más sencillo es entonces rechazar o retirar su consentimiento y borrar sus cookies.</p>
<p>Si considera que no se han respetado sus derechos, puede presentar una reclamación ante la autoridad de protección de datos de su país (en España, la AEPD).</p>

<h2>8. Cambios</h2>
<p>Esta política puede actualizarse, por ejemplo si se añaden nuevas herramientas al sitio. La fecha de la última actualización figura al principio de esta página.</p>
""",
}
