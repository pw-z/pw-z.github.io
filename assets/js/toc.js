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

    var parentItem = null;
    var childList = null;
    var headings = article.querySelectorAll("h2, h3");

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
        var id = base;
        var suffix = 1;
        while (document.getElementById(id)) {
          id = base + "-" + suffix++;
        }
        heading.id = id;
      }

      var item = document.createElement("li");
      var link = document.createElement("a");
      link.textContent = title;
      link.href = "#" + encodeURIComponent(heading.id);
      item.appendChild(link);

      if (heading.tagName === "H2") {
        list.appendChild(item);
        parentItem = item;
        childList = null;
      } else if (parentItem) {
        if (!childList) {
          childList = document.createElement("ol");
          childList.className = "toc-sublist";
          parentItem.appendChild(childList);
        }
        childList.appendChild(item);
      } else {
        // A document can start at h3 without an enclosing h2.
        list.appendChild(item);
      }
    });

    if (!list.children.length) return;

    var wideScreen = window.matchMedia("(min-width: 1280px)");
    function updateDisclosure() {
      disclosure.open = wideScreen.matches;
    }
    updateDisclosure();
    wideScreen.addEventListener("change", updateDisclosure);
    disclosure.addEventListener("toggle", function () {
      if (wideScreen.matches && !disclosure.open) disclosure.open = true;
    });

    sidebar.hidden = false;
    shell.classList.add("has-toc");
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", buildTableOfContents);
  } else {
    buildTableOfContents();
  }
}());
