// KaTeX auto-render init
(function() {
  if (typeof renderMathInElement === "undefined") return;
  try {
    renderMathInElement(document.body, {
      delimiters: [
        {left: "$$", right: "$$", display: true},
        {left: "\\[", right: "\\]", display: true},
        {left: "\\(", right: "\\)", display: false}
      ],
      throwOnError: true
    });
  } catch (e) {
    document.body.insertAdjacentHTML("afterbegin",
      '<div style="background:red;color:#fff;padding:12px;position:fixed;top:0;left:0;right:0;z-index:99999;font:16px monospace">KATEX ERROR: ' + e.message + '</div>');
  }
})();
