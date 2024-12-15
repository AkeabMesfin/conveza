function handleFileChange(event) {
    const input = event.target;
    const label = document.getElementById("file-label");
    const previewImage = document.getElementById("preview-image");

    // Check if a file is selected
    if (input.files.length > 0) {
      // Update label text
      label.textContent = "Change File";
      label.classList.add("file-chosen");

      // Display the selected image
      const file = input.files[0];
      const reader = new FileReader();

      reader.onload = function (e) {
        previewImage.src = e.target.result;
        previewImage.style.display = "block"; // Show image when a file is selected
      };

      reader.readAsDataURL(file);
    } else {
      // Reset label text and hide the image if no file is selected
      label.textContent = "Choose A File";
      label.classList.remove("file-chosen");
      previewImage.src = ""; // Clear the image src
      previewImage.style.display = "none"; // Hide image if no file is selected
    }
  }