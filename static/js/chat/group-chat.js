document.addEventListener("DOMContentLoaded", function() {
    // Get the radio buttons and chat divs
    const privateRadio = document.getElementById("private");
    const groupRadio = document.getElementById("group");
    const privateChat = document.querySelector(".private-chat");
    const groupChat = document.querySelector(".group-chat");
  
    // Function to toggle chat sections
    function toggleChats() {
      if (privateRadio.checked) {
        privateChat.style.display = "flex";
        groupChat.style.display = "none";
      } else if (groupRadio.checked) {
        privateChat.style.display = "none";
        groupChat.style.display = "flex";
      }
    }
  
    // Add event listeners for the radio buttons
    privateRadio.addEventListener("change", toggleChats);
    groupRadio.addEventListener("change", toggleChats);
  
    // Initialize the correct display based on the default selected radio button
    toggleChats();
  });
  
  