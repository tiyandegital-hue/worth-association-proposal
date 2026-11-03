/* WORTH pitch concept — progressive enhancement only; page is fully readable with JS off. */
(function () {
  'use strict';
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* Mobile nav */
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.main-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  /* FAQ accordion */
  var items = document.querySelectorAll('.faq-item');
  items.forEach(function (item) {
    var btn = item.querySelector('.faq-q');
    var panel = item.querySelector('.faq-a');
    if (!btn || !panel) return;
    btn.setAttribute('aria-expanded', 'false');
    btn.addEventListener('click', function () {
      var isOpen = item.classList.contains('open');
      items.forEach(function (other) {
        other.classList.remove('open');
        other.querySelector('.faq-q').setAttribute('aria-expanded', 'false');
        other.querySelector('.faq-a').style.maxHeight = null;
      });
      if (!isOpen) {
        item.classList.add('open');
        btn.setAttribute('aria-expanded', 'true');
        panel.style.maxHeight = panel.scrollHeight + 'px';
      }
    });
  });

  /* Count-up numbers (verified figures only) */
  var counters = document.querySelectorAll('[data-count]');
  function runCounter(el) {
    var target = parseFloat(el.getAttribute('data-count'));
    var prefix = el.getAttribute('data-prefix') || '';
    var suffix = el.getAttribute('data-suffix') || '';
    if (reduceMotion) { el.textContent = prefix + target.toLocaleString('en-US') + suffix; return; }
    var dur = 1400, start = null;
    function frame(ts) {
      if (!start) start = ts;
      var p = Math.min((ts - start) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      var val = Math.round(target * eased);
      el.textContent = prefix + val.toLocaleString('en-US') + suffix;
      if (p < 1) requestAnimationFrame(frame);
    }
    requestAnimationFrame(frame);
  }

  /* Dial needle sweep */
  function sweepNeedle() {
    var needle = document.getElementById('dial-needle');
    if (!needle) return;
    if (reduceMotion) { needle.setAttribute('transform', 'rotate(38 200 190)'); return; }
    var start = null, dur = 1600, from = -55, to = 38;
    function frame(ts) {
      if (!start) start = ts;
      var p = Math.min((ts - start) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 4);
      // gentle settle: small overshoot then rest
      var over = p >= 1 ? 0 : Math.sin(p * Math.PI) * 0;
      var angle = from + (to - from) * eased + over;
      needle.setAttribute('transform', 'rotate(' + angle.toFixed(1) + ' 200 190)');
      if (p < 1) requestAnimationFrame(frame);
    }
    requestAnimationFrame(frame);
  }

  if ('IntersectionObserver' in window) {
    var seen = new WeakSet();
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting && !seen.has(e.target)) {
          seen.add(e.target);
          if (e.target.hasAttribute('data-count')) runCounter(e.target);
          if (e.target.id === 'dial-needle' || e.target.querySelector('#dial-needle')) sweepNeedle();
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.35 });
    counters.forEach(function (c) { io.observe(c); });
    var dial = document.getElementById('dial-svg');
    if (dial) io.observe(dial);
  } else {
    counters.forEach(runCounter);
    sweepNeedle();
  }

  /* Footer year */
  var year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();

  /* Demo forms: honest notice instead of a fake submit */
  document.querySelectorAll('form[data-demo]').forEach(function (form) {
    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      var note = form.querySelector('.form-notice');
      if (note) {
        note.hidden = false;
        note.focus();
      }
    });
  });
})();
