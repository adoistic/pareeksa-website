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
  var mobileDropTriggers = document.querySelectorAll(".mobile-dropdown-trigger");

  if (menuBtn && mobileNav) {
    var setMenu = function (open) {
      menuBtn.setAttribute("aria-expanded", String(open));
      mobileNav.classList.toggle("open", open);
      if (open) { mobileNav.hidden = false; }
      else {
        mobileNav.hidden = true;
        mobileDropTriggers.forEach(function (trig) {
          trig.setAttribute("aria-expanded", "false");
        });
      }
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

  /* ---- Mobile dropdown accordion ---- */
  mobileDropTriggers.forEach(function (trig) {
    trig.addEventListener("click", function (e) {
      e.preventDefault();
      var expanded = trig.getAttribute("aria-expanded") === "true";
      trig.setAttribute("aria-expanded", String(!expanded));
    });
  });

  /* ---- Desktop dropdown trigger click prevention ---- */
  document.querySelectorAll(".nav-dropdown-trigger").forEach(function (trigger) {
    trigger.addEventListener("click", function (e) {
      e.preventDefault();
    });
  });

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

  /* ---- Flow timelines: fill the spine + light up steps as you scroll ---- */
  var flowList = Array.prototype.slice.call(document.querySelectorAll(".flow"));
  var flowUpdate = function () {};
  if (flowList.length) {
    if (reduce) {
      flowList.forEach(function (f) {
        f.style.setProperty("--progress", "1");
        f.querySelectorAll(".flow-step").forEach(function (s) { s.classList.add("on"); });
      });
    } else {
      var measure = function (f) {
        var h = f.scrollHeight || 1;
        f.__steps = Array.prototype.slice.call(f.querySelectorAll(".flow-step")).map(function (s) {
          var dot = s.querySelector(".flow-num-dot");
          var center = s.offsetTop + (dot ? dot.offsetTop + dot.offsetHeight / 2 : s.offsetHeight / 2);
          return { el: s, t: center / h };
        });
      };
      flowUpdate = function () {
        var vh = window.innerHeight || 1;
        flowList.forEach(function (f) {
          if (f.offsetParent === null) return;            // skip hidden (inactive tab)
          if (!f.__steps) { measure(f); }
          var r = f.getBoundingClientRect();
          var p = (vh * 0.82 - r.top) / (r.height * 0.72);
          if (p < 0) { p = 0; } else if (p > 1) { p = 1; }
          f.style.setProperty("--progress", p.toFixed(3));
          f.__steps.forEach(function (st) {
            if (p >= st.t - 0.015) { st.el.classList.add("on"); }
          });
        });
      };
      var fTicking = false;
      window.addEventListener("scroll", function () {
        if (!fTicking) { fTicking = true; window.requestAnimationFrame(function () { flowUpdate(); fTicking = false; }); }
      }, { passive: true });
      window.addEventListener("resize", function () {
        flowList.forEach(function (f) { f.__steps = null; }); flowUpdate();
      });
      window.addEventListener("load", function () {
        flowList.forEach(function (f) { f.__steps = null; }); flowUpdate();
      });
      flowUpdate();
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
          if (flow) {
            flow.style.setProperty("--progress", "0");
            flow.querySelectorAll(".flow-step").forEach(function (s) { s.classList.remove("on"); });
            flow.__steps = null;
            window.requestAnimationFrame(function () { flowUpdate(); });
          }
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
