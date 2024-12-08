document.addEventListener("DOMContentLoaded", () => {
    const faqItems = document.querySelectorAll(".faq-item");

    faqItems.forEach((item) => {
      item.querySelector(".faq-question").addEventListener("click", () => {
        // Toggle the active class
        item.classList.toggle("active");
      });
    });
  });