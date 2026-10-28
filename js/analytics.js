/* Ajwa Dates Wholesale — Google Ads + Google Analytics 4 (account 249-707-3399), Consent Mode v2, region-specific.
   - gtag.js loads for everyone (head block). Consent is denied by default in the EEA, the UK and Switzerland
     and granted elsewhere.
   - /api/geo (Vercel geo header) tells us the visitor's country. The banner is shown only in those regions,
     or when the country is unknown or the check fails (safe side).
   - Every WhatsApp click sends "whatsapp_click" to GA4 (once a real G- ID is set). The Google Ads conversion
     "WhatsApp clic - Ajwa dates" (£50 GBP, beacon) is sent outside those regions, and inside them only after "Accept".
   - "Decline" (or withdrawing): all 4 signals denied, _ga* / _gcl* cookies deleted, page reloaded.
   Banner text in EN / FR / ES from <html lang>. Choice kept 6 months in localStorage "ajw_cookie_consent_v2". */
(function () {
  'use strict';

  /* Google Ads conversion "WhatsApp clic - Ajwa dates" (ID 7879363432). This label belongs to THIS site only. */
  var ADS_CONVERSION = { id: 'AW-18529460502', label: '_PkpCOiWlq0dEJbCxINF', value: 50, currency: 'GBP' };
  var KEY = 'ajw_cookie_consent_v2';
  var MAX_AGE = 15724800000; // 182 days
  var GEO_URL = '/api/geo/'; // trailingSlash is on: avoids a 308 redirect
  var WA_SELECTOR = 'a[data-cta="whatsapp"]';
  var REGIONS = window.AJW_CONSENT_REGIONS || [];
  var TXT = {
    en: {
      text: 'We use Google Analytics cookies (audience measurement) and Google Ads cookies (measuring our ads\' performance and personalised advertising), only if you agree.',
      privacy: 'Privacy policy', url: '/privacy/',
      decline: 'Decline', accept: 'Accept', aria: 'Cookie consent'
    },
    fr: {
      text: 'Nous utilisons des cookies Google Analytics (mesure d\u2019audience) et Google Ads (mesure de la performance de nos annonces et publicit\u00e9 personnalis\u00e9e), uniquement si vous l\u2019acceptez.',
      privacy: 'Politique de confidentialit\u00e9', url: '/fr/confidentialite/',
      decline: 'Refuser', accept: 'Accepter', aria: 'Consentement aux cookies'
    },
    es: {
      text: 'Usamos cookies de Google Analytics (medici\u00f3n de audiencia) y de Google Ads (medici\u00f3n del rendimiento de nuestros anuncios y publicidad personalizada), solo si usted lo acepta.',
      privacy: 'Pol\u00edtica de privacidad', url: '/es/privacidad/',
      decline: 'Rechazar', accept: 'Aceptar', aria: 'Consentimiento de cookies'
    }
  };
  var lang = (document.documentElement.getAttribute('lang') || 'en').slice(0, 2).toLowerCase();
  var t = TXT[lang] || TXT.en;

  window.dataLayer = window.dataLayer || [];
  var gtag = window.gtag || function () { window.dataLayer.push(arguments); };

  function readChoice() {
    try {
      var c = JSON.parse(localStorage.getItem(KEY));
      if (c && (c.v === 'granted' || c.v === 'denied') && Date.now() - c.t < MAX_AGE) return c.v;
    } catch (e) {}
    return null;
  }
  function saveChoice(v) {
    try { localStorage.setItem(KEY, JSON.stringify({ v: v, t: Date.now() })); } catch (e) {}
  }
  function updateConsent(v) {
    gtag('consent', 'update', { 'analytics_storage': v, 'ad_storage': v, 'ad_user_data': v, 'ad_personalization': v });
  }
  // Deletes Google Analytics (_ga, _ga_XXXX) and Google Ads (_gcl_au, _gcl_aw...) cookies.
  function clearGoogleCookies() {
    var parts = location.hostname.split('.');
    var domains = [''];
    for (var i = 0; i < parts.length - 1; i++) domains.push('; domain=.' + parts.slice(i).join('.'));
    document.cookie.split(';').forEach(function (c) {
      var name = c.split('=')[0].trim();
      if (/^(_ga|_gcl)/.test(name)) {
        domains.forEach(function (d) { document.cookie = name + '=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/' + d; });
      }
    });
  }

  var choice = readChoice();
  if (choice === 'denied') clearGoogleCookies();
  // Consent region: true (EEA/UK/CH, unknown or check failed), false (elsewhere), null (check still running).
  var inRegion = null;

  var banner = null;
  function hideBanner() { if (banner) banner.hidden = true; }
  function showBanner(focus) {
    if (!banner) {
      banner = document.createElement('div');
      banner.className = 'cookie-banner';
      banner.setAttribute('role', 'region');
      banner.setAttribute('aria-label', t.aria);
      banner.innerHTML =
        '<p>' + t.text + ' <a href="' + t.url + '">' + t.privacy + '</a></p>' +
        '<div class="cookie-actions">' +
        '<button type="button" class="btn-cookie" data-consent="denied">' + t.decline + '</button>' +
        '<button type="button" class="btn-cookie btn-cookie-accept" data-consent="granted">' + t.accept + '</button>' +
        '</div>';
      banner.addEventListener('click', function (e) {
        var b = e.target.closest('[data-consent]');
        if (!b) return;
        var v = b.getAttribute('data-consent');
        choice = v;
        saveChoice(v);
        updateConsent(v);
        hideBanner();
        if (v === 'denied') {
          if (window.AJW_TAGS && window.ajwGa4Ready && window.ajwGa4Ready()) window['ga-disable-' + window.AJW_TAGS.ga4] = true;
          clearGoogleCookies();
          location.reload();
        }
      });
      document.body.appendChild(banner);
    }
    banner.hidden = false;
    if (focus) banner.querySelector('button').focus();
  }

  function setRegion(country) {
    country = (country || '').toUpperCase();
    inRegion = !/^[A-Z]{2}$/.test(country) || REGIONS.indexOf(country) !== -1;
    if (inRegion && !choice) showBanner(false);
  }
  // A stored choice means the visitor already saw the banner (consent region): no geo check needed.
  if (choice) {
    inRegion = true;
  } else {
    var cached = null;
    try { cached = sessionStorage.getItem('ajw_geo'); } catch (e) {}
    if (cached !== null) {
      setRegion(cached);
    } else if (window.fetch && /^https?:$/.test(location.protocol)) {
      fetch(GEO_URL, { credentials: 'omit' })
        .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
        .then(function (d) {
          var c = (d && d.country) || '';
          try { sessionStorage.setItem('ajw_geo', c); } catch (e) {}
          setRegion(c);
        })
        .catch(function () { setRegion(''); });
    } else {
      setRegion('');
    }
  }

  document.addEventListener('click', function (e) {
    if (!e.target.closest) return;
    // "Cookie settings" reopens the banner
    if (e.target.closest('[data-consent-open]')) { e.preventDefault(); showBanner(true); return; }
    var link = e.target.closest(WA_SELECTOR);
    if (!link) return;
    var section = link.closest('section[id], header[id], footer[id], main[id]');
    // GA4: always sent; in consent regions Consent Mode keeps it cookieless until "Accept".
    if (window.ajwGa4Ready && window.ajwGa4Ready()) {
      gtag('event', 'whatsapp_click', {
        link_location: link.getAttribute('data-cta-location') || (section && section.id) || 'unknown',
        link_url: link.href,
        page_language: lang,
        transport_type: 'beacon',
        send_to: window.AJW_TAGS.ga4
      });
    }
    // Google Ads conversion: outside consent regions, or after "Accept". Unknown region = no conversion yet.
    // No preventDefault, no callback, no redirect: the link opens in a new tab as before.
    if (choice === 'granted' || inRegion === false) {
      gtag('event', 'conversion', {
        'send_to': ADS_CONVERSION.id + '/' + ADS_CONVERSION.label,
        'value': ADS_CONVERSION.value,
        'currency': ADS_CONVERSION.currency,
        'transport_type': 'beacon'
      });
    }
  });
})();
