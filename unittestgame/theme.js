(() => {
  const storageKey = "unittestgame-theme";
  const toggle = document.querySelector(".theme-toggle");
  const root = document.documentElement;
  const savedTheme = localStorage.getItem(storageKey);

  if (savedTheme === "light") {
    root.dataset.theme = "light";
  }

  if (!toggle) {
    return;
  }

  const updateToggle = () => {
    const isLight = root.dataset.theme === "light";
    toggle.setAttribute("aria-pressed", String(isLight));
    toggle.setAttribute(
      "aria-label",
      isLight ? "Switch to dark mode" : "Switch to light mode"
    );
    toggle.querySelector(".theme-toggle-icon").textContent = isLight ? "☾" : "☼";
    toggle.querySelector(".theme-toggle-label").textContent = isLight
      ? "Dark mode"
      : "Light mode";
  };

  updateToggle();

  toggle.addEventListener("click", () => {
    const isLight = root.dataset.theme === "light";
    root.dataset.theme = isLight ? "dark" : "light";
    localStorage.setItem(storageKey, root.dataset.theme);
    updateToggle();
  });
})();
