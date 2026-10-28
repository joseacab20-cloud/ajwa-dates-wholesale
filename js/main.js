/* Ajwa Dates Wholesale — tiny UI helpers. No framework. Tracking + cookie banner live in js/analytics.js.
   Each language is its own static page (/ = EN, /fr/, /es/, /pt/); nothing is translated at runtime. */
(function () {
  'use strict';
  var body = document.body;

  // Mobile menu
  var burger = document.querySelector('.burger');
  var nav = document.getElementById('nav');
  if (burger && nav) {
    burger.addEventListener('click', function () {
      var open = burger.getAttribute('aria-expanded') === 'true';
      burger.setAttribute('aria-expanded', open ? 'false' : 'true');
      body.classList.toggle('nav-open', !open);
    });
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a')) { burger.setAttribute('aria-expanded', 'false'); body.classList.remove('nav-open'); }
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && body.classList.contains('nav-open')) { burger.click(); burger.focus(); }
    });
  }

  // Header shadow on scroll
  var header = document.querySelector('.header');
  var onScroll = function () { if (header) header.classList.toggle('is-scrolled', window.scrollY > 8); };
  window.addEventListener('scroll', onScroll, { passive: true }); onScroll();

  // Opened by double-click (file://): folder links need an explicit index.html
  if (location.protocol === 'file:') {
    document.querySelectorAll('.lang a, .legal-links a, .brand[href], .legal__back a').forEach(function (a) {
      var h = a.getAttribute('href');
      if (h && /\/$/.test(h)) a.setAttribute('href', h + 'index.html');
    });
  }

  var y = document.getElementById('year'); if (y) y.textContent = new Date().getFullYear();
})();
