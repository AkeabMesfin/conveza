const inputs = document.querySelectorAll(".profile-details input");
const instructions = document.querySelectorAll(".instruction");

inputs.forEach((input, index) => {
  instructions[index].style.display = "none"; // Hide instructions initially

  input.addEventListener("focus", () => {
    instructions[index].style.display = "inline"; // Show instruction when input is focused
  });

  input.addEventListener("blur", () => {
    instructions[index].style.display = "none"; // Hide instruction when input is blurred
  });
});

const userPost = document.getElementById("user-post");
const groupMember = document.getElementById("group-member");

function toggleDisplay() {
  if (userPost.checked) {
    document.querySelector(".post-con").style.display = "flex";
    document.querySelector(".group-con").style.display = "none";
  } else if (groupMember.checked) {
    document.querySelector(".post-con").style.display = "none";
    document.querySelector(".group-con").style.display = "flex";
  }
}

userPost.addEventListener("change", toggleDisplay);
groupMember.addEventListener("change", toggleDisplay);

toggleDisplay();

// * post js code
const posts = document.querySelectorAll(".post");

posts.forEach((post) => {
  const seeMore = post.querySelector(".see-more-btn");
  const postCon = post.querySelector(".post-content");
  const paragraph = postCon.querySelector("p");
  const like = post.querySelector(".like");
  const likeIcon = post.querySelector(".like svg"); // svg element
  const save = post.querySelector(".save");
  const saveIcon = post.querySelector(".save svg");

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

  like.addEventListener("click", () => {
    // Check the current fill color of the icon
    if (likeIcon.style.fill === "red") {
      // If it's red, change it back to the original color
      likeIcon.style.fill = "var(--text-72)";
    } else {
      // If it's not red, change it to red
      likeIcon.style.fill = "red";
    }
  });

  save.addEventListener("click", () => {
    if (saveIcon.style.fill == "var(--accent)") {
      saveIcon.style.fill = "var(--text-72)";
    } else {
      saveIcon.style.fill = "var(--accent)";
    }
  });
});

const profilePicInput = document.getElementById("profilePicInput");
const profilePicPreview = document.getElementById("profilePicPreview");

profilePicInput.addEventListener("change", function () {
  const file = profilePicInput.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = function (e) {
      profilePicPreview.src = e.target.result;
    };
    reader.readAsDataURL(file);
  }
});


const userPost1 = document.getElementById("user-post1");
const groupMember1 = document.getElementById("group-member1");

function toggleDisplay1() {
  if (userPost1.checked) {
    document.querySelector(".post-con1").style.display = "flex";
    document.querySelector(".group-con1").style.display = "none";
  } else if (groupMember1.checked) {
    document.querySelector(".post-con1").style.display = "none";
    document.querySelector(".group-con1").style.display = "flex";
  }
}

userPost1.addEventListener("change", toggleDisplay1);
groupMember1.addEventListener("change", toggleDisplay1);

toggleDisplay1();