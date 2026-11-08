(function () {
  "use strict";

  var article = document.getElementById("article-content");
  var panel = document.querySelector(".reading-panel");
  if (!article || !panel) return;

  // Count the rendered article once; settings and scrolling do not change its statistics.
  var copy = article.cloneNode(true);
  copy.querySelectorAll("script, style, pre, code, .anchorjs-link, a[href='#contents']").forEach(function (node) {
    node.remove();
  });
  copy.querySelectorAll("h2, h3").forEach(function (heading) {
    if (!/^(目录|table of contents)$/i.test(heading.textContent.trim())) return;
    var level = Number(heading.tagName.slice(1));
    var next = heading.nextElementSibling;
    while (next && !(/^H[1-6]$/.test(next.tagName) && Number(next.tagName.slice(1)) <= level)) {
      var following = next.nextElementSibling;
      next.remove();
      next = following;
    }
    heading.remove();
  });
  copy.querySelectorAll("h1, h2, h3, h4, h5, h6, p, li, td, th, blockquote, br").forEach(function (node) {
    node.after(document.createTextNode("\n"));
  });
  var text = copy.textContent;
  var han = text.match(/\p{Script=Han}/gu) || [];
  var words = text.replace(/\p{Script=Han}/gu, " ").match(/[\p{L}\p{N}]+(?:['’\-][\p{L}\p{N}]+)*/gu) || [];
  var wordCount = han.length + words.length;
  document.getElementById("article-word-count").textContent = wordCount.toLocaleString("zh-CN");
  document.getElementById("article-reading-time").textContent = "约 " + Math.max(1, Math.ceil(wordCount / 300)) + " 分钟";
  document.getElementById("article-image-count").textContent = article.querySelectorAll("img").length + " 张";

  var storageKey = "pwz-reading-preferences";
  var palettes = ["light", "paper", "sage", "night"];
  var lineHeights = [1.5, 1.75, 2];
  var preferences = { fontSize: 16, lineHeight: 1.5, theme: "light" };
  try {
    var saved = JSON.parse(localStorage.getItem(storageKey));
    if (saved && typeof saved === "object") {
      if (Number.isInteger(saved.fontSize) && saved.fontSize >= 14 && saved.fontSize <= 22) preferences.fontSize = saved.fontSize;
      if (lineHeights.indexOf(saved.lineHeight) !== -1) preferences.lineHeight = saved.lineHeight;
      if (palettes.indexOf(saved.theme) !== -1) preferences.theme = saved.theme;
    }
  } catch (error) {
    // Private browsing or blocked storage must not disable the reading controls.
  }

  var smaller = document.getElementById("reading-font-smaller");
  var larger = document.getElementById("reading-font-larger");
  var size = document.getElementById("reading-font-size");
  var leading = document.getElementById("reading-line-height");
  var themeButtons = panel.querySelectorAll("[data-reading-palette]");

  function applyPreferences(persist) {
    var root = document.documentElement;
    root.dataset.readingTheme = preferences.theme;
    root.style.setProperty("--article-font-size", preferences.fontSize + "px");
    root.style.setProperty("--article-line-height", preferences.lineHeight);
    size.textContent = preferences.fontSize + "px";
    smaller.disabled = preferences.fontSize === 14;
    larger.disabled = preferences.fontSize === 22;
    leading.value = String(preferences.lineHeight);
    themeButtons.forEach(function (button) {
      button.setAttribute("aria-pressed", String(button.dataset.readingPalette === preferences.theme));
    });
    if (persist) {
      try { localStorage.setItem(storageKey, JSON.stringify(preferences)); }
      catch (error) { /* Settings still work for this visit without storage. */ }
    }
  }

  smaller.addEventListener("click", function () {
    preferences.fontSize = Math.max(14, preferences.fontSize - 1);
    applyPreferences(true);
  });
  larger.addEventListener("click", function () {
    preferences.fontSize = Math.min(22, preferences.fontSize + 1);
    applyPreferences(true);
  });
  leading.addEventListener("change", function () {
    var value = Number(leading.value);
    if (lineHeights.indexOf(value) !== -1) preferences.lineHeight = value;
    applyPreferences(true);
  });
  themeButtons.forEach(function (button) {
    button.addEventListener("click", function () {
      preferences.theme = button.dataset.readingPalette;
      applyPreferences(true);
    });
  });
  document.getElementById("reading-reset").addEventListener("click", function () {
    preferences = { fontSize: 16, lineHeight: 1.5, theme: "light" };
    try { localStorage.removeItem(storageKey); } catch (error) { /* Optional storage. */ }
    applyPreferences(false);
  });

  var disclosure = panel.querySelector("details");
  var restore = disclosure.querySelector("summary");
  var hide = disclosure.querySelector(".panel-hide");
  disclosure.open = false;
  hide.addEventListener("click", function () {
    disclosure.open = false;
    restore.focus({ preventScroll: true });
  });
  disclosure.addEventListener("toggle", function () {
    if (disclosure.open && document.activeElement === restore) hide.focus({ preventScroll: true });
  });

  applyPreferences(false);
  panel.hidden = false;
  panel.closest(".site-shell").classList.add("has-sidebars");
}());
