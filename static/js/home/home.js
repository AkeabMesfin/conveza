document.addEventListener("DOMContentLoaded", () => {
    const faqItems = document.querySelectorAll(".faq-item");

    faqItems.forEach((item) => {
      item.querySelector(".faq-question").addEventListener("click", () => {
        // Toggle the active class
        item.classList.toggle("active");
      });
    });
  });

  const menuBtn = document.querySelector(".menu-btn");
  const linkCon = document.querySelector(".link-con");

  // Toggle the dropdown menu when the menu button is clicked
  menuBtn.addEventListener("click", (event) => {
    event.stopPropagation(); // Prevent click from propagating to document
    linkCon.classList.toggle("show");
  });

  // Close the dropdown when clicking anywhere outside the menu
  document.addEventListener("click", (event) => {
    if (!linkCon.contains(event.target) && !menuBtn.contains(event.target)) {
      linkCon.classList.remove("show");
    }
  });