const fileInput = document.getElementById("group-photo");
const imageDisplay = document.getElementById("group-image");

fileInput.addEventListener("change", function (event) {
  const file = event.target.files[0]; // Get the selected file
  if (file) {
    const reader = new FileReader();
    // Set up the FileReader to update the image display
    reader.onload = function (e) {
      imageDisplay.src = e.target.result; // Update the src of the image
    };
    reader.readAsDataURL(file); // Read the file as a data URL
  }
});

document
  .getElementById("group-photo")
  .addEventListener("change", function (event) {
    const [file] = event.target.files;
    if (file) {
      document.getElementById("group-image").src =
        URL.createObjectURL(file);
    }
  });