/* Pareeksa Technologies — interactions. No dependencies. */
(function () {
  "use strict";

  var root = document.documentElement;

  /* ---- Theme toggle (persisted; initial value set in <head>) ---- */
  var toggle = document.querySelector(".theme-toggle");
  if (toggle) {
    toggle.addEventListener("click", function () {
      var next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      try { localStorage.setItem("theme", next); } catch (e) {}
    });
  }

  /* ---- Mobile menu ---- */
  var menuBtn = document.querySelector(".menu-toggle");
  var mobileNav = document.getElementById("mobile-nav");
  if (menuBtn && mobileNav) {
    var setMenu = function (open) {
      menuBtn.setAttribute("aria-expanded", String(open));
      mobileNav.classList.toggle("open", open);
      if (open) { mobileNav.hidden = false; }
      else { mobileNav.hidden = true; }
    };
    menuBtn.addEventListener("click", function () {
      setMenu(menuBtn.getAttribute("aria-expanded") !== "true");
    });
    mobileNav.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () { setMenu(false); });
    });
    window.addEventListener("keydown", function (e) {
      if (e.key === "Escape") { setMenu(false); }
    });
  }

  /* ---- Scroll reveal ---- */
  var reveals = document.querySelectorAll(".reveal");
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduce || !("IntersectionObserver" in window)) {
    reveals.forEach(function (el) { el.classList.add("in"); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("in");
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    reveals.forEach(function (el, i) {
      // small stagger within a group for a calmer entrance
      el.style.transitionDelay = (Math.min(i % 6, 5) * 45) + "ms";
      io.observe(el);
    });
  }

  /* ---- Flow diagrams: light up the pipeline when it scrolls into view ---- */
  var flows = document.querySelectorAll(".flow");
  if (flows.length) {
    if (reduce || !("IntersectionObserver" in window)) {
      flows.forEach(function (f) { f.classList.add("in"); });
    } else {
      var fio = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("in");
            fio.unobserve(entry.target);
          }
        });
      }, { rootMargin: "0px 0px -12% 0px", threshold: 0.15 });
      flows.forEach(function (f) { fio.observe(f); });
    }
  }

  /* ---- Pipeline tabs (landing "how it works"): swap the visible flow ---- */
  var tablist = document.querySelector(".pipe-tabs");
  if (tablist) {
    var tabs = Array.prototype.slice.call(tablist.querySelectorAll("[role=tab]"));
    var panels = Array.prototype.slice.call(document.querySelectorAll(".pipe-panel"));
    var select = function (idx, focus) {
      tabs.forEach(function (t, i) {
        var on = i === idx;
        t.setAttribute("aria-selected", String(on));
        t.setAttribute("tabindex", on ? "0" : "-1");
        if (on && focus) { t.focus(); }
      });
      panels.forEach(function (p, i) {
        p.hidden = i !== idx;
        if (i === idx) {
          var flow = p.querySelector(".flow");
          if (flow) { flow.classList.remove("in"); void flow.offsetWidth; flow.classList.add("in"); }
        }
      });
    };
    tabs.forEach(function (t, i) {
      t.addEventListener("click", function () { select(i, false); });
      t.addEventListener("keydown", function (e) {
        var n = tabs.length, j = -1;
        if (e.key === "ArrowRight" || e.key === "ArrowDown") { j = (i + 1) % n; }
        else if (e.key === "ArrowLeft" || e.key === "ArrowUp") { j = (i - 1 + n) % n; }
        else if (e.key === "Home") { j = 0; }
        else if (e.key === "End") { j = n - 1; }
        if (j >= 0) { e.preventDefault(); select(j, true); }
      });
    });
    select(0, false);
  }

  /* ---- Reveal the floating WhatsApp button after the hero ---- */
  var waFloat = document.querySelector(".wa-float");
  if (waFloat) {
    var hero = document.querySelector(".hero");
    var toggleFloat = function () {
      var trigger = hero ? hero.offsetHeight * 0.66 : window.innerHeight * 0.7;
      waFloat.classList.toggle("show", window.scrollY > trigger);
    };
    var ticking = false;
    window.addEventListener("scroll", function () {
      if (!ticking) {
        window.requestAnimationFrame(function () { toggleFloat(); ticking = false; });
        ticking = true;
      }
    }, { passive: true });
    toggleFloat();
  }

  /* ---- Brand page: click a swatch to copy its hex ---- */
  document.querySelectorAll(".swatch").forEach(function (sw) {
    sw.addEventListener("click", function () {
      var hex = sw.getAttribute("data-hex");
      if (!hex) return;
      var flash = function () {
        sw.classList.add("copied");
        setTimeout(function () { sw.classList.remove("copied"); }, 900);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(hex).then(flash).catch(flash);
      } else { flash(); }
    });
  });

  /* ---- Current year ---- */
  var year = document.getElementById("year");
  if (year) { year.textContent = String(new Date().getFullYear()); }
})();
