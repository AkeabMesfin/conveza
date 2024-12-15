// Function to toggle theme
function toggleTheme() {
  const currentTheme = document.documentElement.getAttribute("data-theme");
  const newTheme = currentTheme === "light" ? "dark" : "light";
  document.documentElement.setAttribute("data-theme", newTheme);
  localStorage.setItem("theme", newTheme); // Save the theme in localStorage
}

// Event listener for theme toggle button
document.addEventListener("DOMContentLoaded", () => {
  const themeToggle = document.getElementById('theme-toggle');
  if (themeToggle) {
      themeToggle.addEventListener("click", toggleTheme);
  }

  // Load the saved theme from localStorage if available
  const savedTheme = localStorage.getItem("theme") || "light"; // Default to light theme
  document.documentElement.setAttribute("data-theme", savedTheme);
});


function historyBack() {
  window.history.back();
}