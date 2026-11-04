// Light / Dark theme toggle, replacing Hextra's Light/Dark/System menu (layouts/_partials/theme-toggle.html).
// Until the toggle is clicked the page follows the system theme, as setTheme in js/head/theme.js does.
(function () {
  const defaultTheme = '{{ site.Params.theme.default | default `system`}}'
  const themes = ["light", "dark"];
  const systemDark = window.matchMedia("(prefers-color-scheme: dark)");

  const themeToggleButtons = document.querySelectorAll(".hextra-theme-toggle");

  // The menu also stored "system": that is no choice either.
  function chosenTheme() {
    const theme = "color-theme" in localStorage ? localStorage.getItem("color-theme") : defaultTheme;
    return themes.includes(theme) ? theme : null;
  }

  function currentTheme() {
    return chosenTheme() ?? (systemDark.matches ? "dark" : "light");
  }

  function applyTheme(theme) {
    setTheme(theme);
    themeToggleButtons.forEach((btn) => btn.parentElement.dataset.theme = theme);
  }

  applyTheme(currentTheme());

  themeToggleButtons.forEach((toggler) => {
    toggler.addEventListener("click", function (e) {
      e.preventDefault();

      const theme = currentTheme() === "dark" ? "light" : "dark";
      localStorage.setItem("color-theme", theme);
      applyTheme(theme);
    });
  });

  systemDark.addEventListener("change", () => {
    if (chosenTheme() === null) {
      applyTheme(currentTheme());
    }
  });
})();
