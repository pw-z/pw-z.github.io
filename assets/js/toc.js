(function () {
  "use strict";

  function buildTableOfContents() {
    var article = document.getElementById("article-content");
    var sidebar = document.querySelector(".article-toc");

    if (!article || !sidebar) return;

    var list = sidebar.querySelector(".toc-list");
    var disclosure = sidebar.querySelector(".toc-disclosure");
    var shell = sidebar.closest(".site-shell");

    if (!list || !disclosure || !shell) return;

    var parentSection = null;
    var sections = [];
    var entries = [];
    var headings = article.querySelectorAll("h2, h3");

    function uniqueId(base) {
      var id = base;
      var suffix = 1;
      while (document.getElementById(id)) id = base + "-" + suffix++;
      return id;
    }

    function setExpanded(section, expanded) {
      if (!section.children) return;
      section.children.hidden = !expanded;
      section.toggle.setAttribute("aria-expanded", String(expanded));
      section.toggle.setAttribute("aria-label", (expanded ? "收起：" : "展开：") + section.title);
    }

    function addBranch(section) {
      section.children = document.createElement("ol");
      section.children.className = "toc-sublist";
      section.children.id = uniqueId("toc-branch-" + sections.length);
      section.item.classList.add("toc-branch");
      section.item.appendChild(section.children);

      section.toggle = document.createElement("button");
      section.toggle.type = "button";
      section.toggle.className = "toc-toggle";
      section.toggle.setAttribute("aria-controls", section.children.id);
      section.row.insertBefore(section.toggle, section.link);
      setExpanded(section, false);
      section.toggle.addEventListener("click", function () {
        var expanded = section.children.hidden;
        // Remember deliberate expansions when following the reader elsewhere.
        section.manualOpen = expanded;
        setExpanded(section, expanded);
      });
    }

    headings.forEach(function (heading) {
      // AnchorJS may have added its own link; only use the heading's text.
      var label = heading.cloneNode(true);
      label.querySelectorAll(".anchorjs-link").forEach(function (anchor) {
        anchor.remove();
      });
      var title = label.textContent.replace(/\s+/g, " ").trim();

      if (!title || heading.hasAttribute("data-toc-skip") ||
          /^(目录|table of contents)$/i.test(title)) return;

      // Jekyll normally supplies unique IDs. Keep them, including Chinese IDs.
      if (!heading.id) {
        var base = title.toLowerCase().replace(/\s+/g, "-")
          .replace(/[^\p{L}\p{N}_-]/gu, "") || "section";
        heading.id = uniqueId(base);
      }

      var item = document.createElement("li");
      var row = document.createElement("div");
      row.className = "toc-row";
      var link = document.createElement("a");
      link.className = "toc-link";
      link.textContent = title;
      link.title = title;
      link.href = "#" + encodeURIComponent(heading.id);
      row.appendChild(link);
      item.appendChild(row);
      var entry = { heading: heading, item: item, row: row, link: link, title: title };

      if (heading.tagName === "H2") {
        list.appendChild(item);
        parentSection = entry;
        entry.section = entry;
        sections.push(entry);
      } else if (parentSection) {
        if (!parentSection.children) addBranch(parentSection);
        parentSection.children.appendChild(item);
        entry.section = parentSection;
      } else {
        // A document can start at h3 without an enclosing h2.
        list.appendChild(item);
        entry.section = entry;
      }
      entries.push(entry);
    });

    if (!entries.length) return;

    var wideScreen = window.matchMedia("(min-width: 1280px)");
    var activeEntry = null;
    var activeSection = null;
    var updateQueued = false;

    function revealSection(section) {
      sections.forEach(function (candidate) {
        if (candidate === section) setExpanded(candidate, true);
        else if (!candidate.manualOpen) setExpanded(candidate, false);
      });
    }

    function markActive(entry) {
      if (entry === activeEntry) return;
      if (activeEntry) activeEntry.link.removeAttribute("aria-current");
      entry.link.setAttribute("aria-current", "location");
      activeEntry = entry;

      if (entry.section !== activeSection) {
        if (activeSection) activeSection.item.classList.remove("is-active-section");
        activeSection = entry.section;
        activeSection.item.classList.add("is-active-section");
        // Expanding inline navigation during a mobile scroll would move the text.
        if (wideScreen.matches) revealSection(activeSection);
      }
    }

    function updateActive() {
      updateQueued = false;
      var current = entries[0];
      entries.forEach(function (entry) {
        if (entry.heading.getBoundingClientRect().top <= 120) current = entry;
      });
      markActive(current);
    }

    function queueUpdate() {
      if (updateQueued) return;
      updateQueued = true;
      window.requestAnimationFrame(updateActive);
    }

    function entryForHash() {
      var id;
      try { id = decodeURIComponent(window.location.hash.slice(1)); }
      catch (error) { return null; }
      var target = id && document.getElementById(id);
      if (!target || !article.contains(target)) return null;
      var exact = entries.find(function (entry) { return entry.heading === target; });
      if (exact) return exact;

      // Old hand-written anchors sit immediately before their section headings.
      if (target.tagName === "A" && !target.textContent.trim()) {
        return entries.find(function (entry) {
          return target.compareDocumentPosition(entry.heading) & Node.DOCUMENT_POSITION_FOLLOWING;
        }) || entries[entries.length - 1];
      }
      var preceding = entries[0];
      entries.forEach(function (entry) {
        if (entry.heading.compareDocumentPosition(target) & Node.DOCUMENT_POSITION_FOLLOWING) preceding = entry;
      });
      return preceding;
    }

    function updateDisclosure() {
      disclosure.open = wideScreen.matches;
      if (wideScreen.matches && activeSection) revealSection(activeSection);
      queueUpdate();
    }
    updateDisclosure();
    wideScreen.addEventListener("change", updateDisclosure);
    disclosure.addEventListener("toggle", function () {
      if (wideScreen.matches && !disclosure.open) disclosure.open = true;
    });

    sidebar.hidden = false;
    shell.classList.add("has-toc");
    markActive(entryForHash() || entries[0]);
    // Also provide a useful starting branch inside the mobile disclosure.
    revealSection(activeSection);
    window.addEventListener("scroll", queueUpdate, { passive: true });
    window.addEventListener("resize", queueUpdate);
    window.addEventListener("load", queueUpdate);
    window.addEventListener("hashchange", function () {
      var entry = entryForHash();
      if (entry) markActive(entry);
      else queueUpdate();
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", buildTableOfContents);
  } else {
    buildTableOfContents();
  }
}());
