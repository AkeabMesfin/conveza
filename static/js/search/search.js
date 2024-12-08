const userBtn = document.getElementById("users");
const groupBtn = document.getElementById("groups");
const userCon = document.querySelector(".user-con");
const groupCon = document.querySelector(".group-con");

// Apply the desired styles dynamically using JavaScript
function applyStyles(element) {
  element.style.display = "flex";
  element.style.flexDirection = "column";
  element.style.alignItems = "center";
  element.style.justifyContent = "flex-start";
}

// Function to toggle visibility based on which button is clicked
function toggleCon() {
  if (userBtn.checked) {
    applyStyles(userCon); // Apply the flex styles to userCon
    userCon.style.display = "flex"; // Show user content
    groupCon.style.display = "none"; // Hide group content
  } else if (groupBtn.checked) {
    applyStyles(groupCon); // Apply the flex styles to groupCon
    groupCon.style.display = "flex"; // Show group content
    userCon.style.display = "none"; // Hide user content
  }
}

// Add event listeners for changes in the button state
userBtn.addEventListener("change", toggleCon);
groupBtn.addEventListener("change", toggleCon);