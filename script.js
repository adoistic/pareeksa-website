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

  /* ---- Reveal the floating WhatsApp and Demo buttons after the hero ---- */
  var waFloat = document.querySelector(".wa-float");
  var demoFloat = document.querySelector(".demo-float");
  if (waFloat || demoFloat) {
    var hero = document.querySelector(".hero") || document.querySelector(".page-hero");
    var toggleFloat = function () {
      var trigger = hero ? hero.offsetHeight * 0.66 : window.innerHeight * 0.7;
      var show = window.scrollY > trigger;
      if (waFloat) waFloat.classList.toggle("show", show);
      if (demoFloat) demoFloat.classList.toggle("show", show);
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

  /* ---- Demo Modal dialog trigger, open, close, accessibility ---- */
  var modal = document.getElementById("demo-modal");
  var modalClose = modal ? modal.querySelector(".modal__close") : null;
  var modalOverlay = modal ? modal.querySelector(".modal__overlay") : null;
  var lastFocusedElement = null;

  var openModal = function () {
    if (!modal) return;
    lastFocusedElement = document.activeElement;
    modal.classList.add("open");
    modal.setAttribute("aria-hidden", "false");
    
    // Focus the first input field for accessibility
    var firstInput = modal.querySelector("input:not([type=hidden]), textarea, select");
    if (firstInput) {
      setTimeout(function () { firstInput.focus(); }, 50);
    }

    document.addEventListener("keydown", trapFocus);
  };

  var closeModal = function () {
    if (!modal) return;
    modal.classList.remove("open");
    modal.setAttribute("aria-hidden", "true");
    
    // Return focus to trigger button for accessibility
    if (lastFocusedElement && typeof lastFocusedElement.focus === "function") {
      lastFocusedElement.focus();
    }

    document.removeEventListener("keydown", trapFocus);
  };

  var trapFocus = function (e) {
    if (!modal) return;
    var focusables = modal.querySelectorAll('button, [href], input:not([type=hidden]), textarea, select, [tabindex]:not([tabindex="-1"])');
    if (!focusables.length) return;
    var firstFocusable = focusables[0];
    var lastFocusable = focusables[focusables.length - 1];

    if (e.key === 'Tab') {
      if (e.shiftKey) { /* Shift + Tab */
        if (document.activeElement === firstFocusable) {
          lastFocusable.focus();
          e.preventDefault();
        }
      } else { /* Tab */
        if (document.activeElement === lastFocusable) {
          firstFocusable.focus();
          e.preventDefault();
        }
      }
    }
  };

  window.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && modal && modal.classList.contains("open")) {
      closeModal();
    }
  });

  if (demoFloat) {
    demoFloat.addEventListener("click", function (e) {
      e.preventDefault();
      openModal();
    });
  }
  if (modalClose) {
    modalClose.addEventListener("click", function (e) {
      e.preventDefault();
      closeModal();
    });
  }
  if (modalOverlay) {
    modalOverlay.addEventListener("click", function (e) {
      e.preventDefault();
      closeModal();
    });
  }

  /* ---- Shared Contact Form Validation & Submission ---- */
  var forms = document.querySelectorAll(".contact-form");

  var validateEmail = function (email) {
    var re = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return re.test(String(email).toLowerCase());
  };

  var validatePhone = function (phone) {
    var cleaned = phone.replace(/[^0-9+]/g, '');
    return cleaned.length >= 10;
  };

  forms.forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();

      var successAlert = form.querySelector(".contact-form__alert--success");
      var errorAlert = form.querySelector(".contact-form__alert--error");
      if (successAlert) {
        successAlert.classList.remove("show");
        successAlert.hidden = true;
      }
      if (errorAlert) {
        errorAlert.classList.remove("show");
        errorAlert.hidden = true;
      }

      var nameInput = form.querySelector("[name='name']");
      var phoneInput = form.querySelector("[name='phone']");
      var emailInput = form.querySelector("[name='email']");
      var orgInput = form.querySelector("[name='organization']");
      var msgInput = form.querySelector("[name='message']");
      var submitBtn = form.querySelector(".contact-form__submit");

      var name = nameInput ? nameInput.value.trim() : "";
      var phone = phoneInput ? phoneInput.value.trim() : "";
      var email = emailInput ? emailInput.value.trim() : "";
      var organization = orgInput ? orgInput.value.trim() : "";
      var message = msgInput ? msgInput.value.trim() : "";

      var errors = [];
      if (!name) {
        errors.push("Name is required.");
        if (nameInput) nameInput.focus();
      } else if (!phone) {
        errors.push("Mobile number is required.");
        if (phoneInput) phoneInput.focus();
      } else if (!validatePhone(phone)) {
        errors.push("Please enter a valid mobile number (at least 10 digits).");
        if (phoneInput) phoneInput.focus();
      } else if (!email) {
        errors.push("Email address is required.");
        if (emailInput) emailInput.focus();
      } else if (!validateEmail(email)) {
        errors.push("Please enter a valid email address.");
        if (emailInput) emailInput.focus();
      }

      if (errors.length > 0) {
        if (errorAlert) {
          errorAlert.textContent = errors.join(" ");
          errorAlert.hidden = false;
          errorAlert.classList.add("show");
        }
        return;
      }

      var inputs = form.querySelectorAll("input, textarea, button");
      inputs.forEach(function (input) { input.disabled = true; });
      var originalBtnHTML = submitBtn ? submitBtn.innerHTML : "";
      if (submitBtn) {
        submitBtn.innerHTML = "<span>Sending...</span>";
      }

      var selectedService = "General Inquiry (Homepage)";
      var h1Element = document.querySelector("h1");
      if (h1Element) {
        selectedService = h1Element.textContent.trim().replace(/\s+/g, ' ');
      }

      var submissionTime = new Date().toLocaleString("en-IN", { timeZone: "Asia/Kolkata" }) + " (IST)";
      var endpoint = form.getAttribute("action") || "https://api.web3forms.com/submit";
      var accessKeyField = form.querySelector("[name='access_key']");
      var accessKey = accessKeyField ? accessKeyField.value : "";
      var subjectLine = "New Demo Request – " + selectedService + " – " + name;

      var payload = {
        name: name,
        phone: phone,
        email: email,
        organization: organization,
        message: message,
        selected_service: selectedService,
        submission_time: submissionTime,
        subject: subjectLine
      };

      if (accessKey) {
        payload.access_key = accessKey;
      }

      fetch(endpoint, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Accept": "application/json"
        },
        body: JSON.stringify(payload)
      })
      .then(function (response) {
        if (response.ok) {
          return response.json();
        } else {
          throw new Error("Server responded with code " + response.status);
        }
      })
      .then(function (data) {
        inputs.forEach(function (input) { input.disabled = false; });
        if (submitBtn) {
          submitBtn.innerHTML = originalBtnHTML;
        }

        if (successAlert) {
          successAlert.textContent = "Thank you! Your demo request has been sent successfully. We will contact you soon.";
          successAlert.hidden = false;
          successAlert.classList.add("show");
        }

        form.reset();

        if (form.classList.contains("modal-form")) {
          setTimeout(function () {
            closeModal();
            setTimeout(function () {
              if (successAlert) {
                successAlert.classList.remove("show");
                successAlert.hidden = true;
              }
            }, 400);
          }, 2000);
        }
      })
      .catch(function (error) {
        inputs.forEach(function (input) { input.disabled = false; });
        if (submitBtn) {
          submitBtn.innerHTML = originalBtnHTML;
        }

        if (errorAlert) {
          errorAlert.textContent = "Oops! Something went wrong. Please check your connection and try again.";
          errorAlert.hidden = false;
          errorAlert.classList.add("show");
        }
      });
    });
  });

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
