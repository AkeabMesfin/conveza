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




// * post js code
const posts = document.querySelectorAll(".post");

posts.forEach(post => {
  const seeMore = post.querySelector(".see-more-btn");
  const postCon = post.querySelector(".post-content");
  const paragraph = postCon.querySelector("p"); 
  const like = post.querySelector(".like");
  const likeIcon = post.querySelector('.like svg'); // svg element
  const save = post.querySelector(".save");
  const saveIcon = post.querySelector(".save svg")

  const defaultHeight = 180;

  if (paragraph && postCon.scrollHeight > defaultHeight) {
    seeMore.style.display = "block";
    postCon.style.height = `${defaultHeight}px`; 
  } else {
    seeMore.style.display = "none";
  }

  seeMore.addEventListener("click", () => {
    if (seeMore.innerText === "See More") {
      seeMore.innerText = "See Less";
      postCon.style.height = "fit-content"; 
    } else {
      seeMore.innerText = "See More";
      postCon.style.height = `${defaultHeight}px`; 
    }
  });

  like.addEventListener('click', () => {
    // Check the current fill color of the icon
    if (likeIcon.style.fill === "red") {
        // If it's red, change it back to the original color
        likeIcon.style.fill = "var(--text-72)";
    } else {
        // If it's not red, change it to red
        likeIcon.style.fill = "red";
    }
});

  save.addEventListener('click', () => {
    if (saveIcon.style.fill == "var(--accent)") {
      saveIcon.style.fill = "var(--text-72)"
    } else {
      saveIcon.style.fill = "var(--accent)"
    }
  })



});





const userPost = document.getElementById("user-post");
const groupOwner = document.getElementById("group-owner");

function toggleDisplay() {
  if (userPost.checked) {
    document.querySelector(".post-con").style.display = "flex";
    document.querySelector(".group-con").style.display = "none";
  } else if (groupOwner.checked) {
    document.querySelector(".post-con").style.display = "none";
    document.querySelector(".group-con").style.display = "flex";
  }
}

userPost.addEventListener("change", toggleDisplay);
groupOwner.addEventListener("change", toggleDisplay);

toggleDisplay();