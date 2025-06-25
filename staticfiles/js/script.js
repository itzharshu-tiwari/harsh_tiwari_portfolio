// BASE HTML JS

      //  mode plan
      const themeToggle = document.getElementById("theme-toggle");
      const body = document.body;

      // Load from localStorage
      const savedTheme = localStorage.getItem("theme");
      if (savedTheme === "dark") {
        body.classList.add("dark-mode");
        body.classList.remove("light-mode");
        themeToggle
          .querySelector("i")
          .classList.replace("bi-moon-fill", "bi-sun-fill");
      } else {
        body.classList.add("light-mode");
      }

      // Toggle theme on click
      themeToggle.addEventListener("click", () => {
        body.classList.toggle("dark-mode");
        body.classList.toggle("light-mode");

        const icon = themeToggle.querySelector("i");
        const isDark = body.classList.contains("dark-mode");

        icon.classList.toggle("bi-moon-fill", !isDark);
        icon.classList.toggle("bi-sun-fill", isDark);

        // Save preference
        localStorage.setItem("theme", isDark ? "dark" : "light");
      });
  
// ABOUT JS
 function showImage(src) {
    document.getElementById("modalImage").src = src;
  }