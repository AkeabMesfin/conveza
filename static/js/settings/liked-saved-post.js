// Select all posts with the class 'post' (for backward compatibility)
const posts = document.querySelectorAll(".post");

// Loop through each post element
posts.forEach((post) => {
  // Select the button for the "See More" feature
  const seeMore = post.querySelector(".see-more-btn");
  const postCon = post.querySelector(".post-content");
  const paragraph = postCon?.querySelector("p");
  const defaultHeight = 180;

  if (paragraph && postCon.scrollHeight > defaultHeight) {
    seeMore.style.display = "block";
    postCon.style.height = `${defaultHeight}px`;
  } else {
    seeMore.style.display = "block";
  }

  // Toggle "See More"/"See Less"
  if (seeMore) {
    seeMore.addEventListener("click", () => {
      if (seeMore.innerText === "See More") {
        seeMore.innerText = "See Less";
        postCon.style.height = "fit-content";
      } else {
        seeMore.innerText = "See More";
        postCon.style.height = `${defaultHeight}px`;
      }
    });
  }
});

const posts1 = document.querySelectorAll(".post1");

posts1.forEach((post) => {
  const seeMore1 = post.querySelector(".see-more-btn1");
  const postCon1 = post.querySelector(".post-content1");
  const paragraph1 = postCon1?.querySelector("p");

  const defaultHeight = 180;

  if (seeMore1 && postCon1 && paragraph1) {
    if (paragraph1 && postCon1.scrollHeight > defaultHeight) {
      seeMore1.style.display = "block";
      postCon1.style.height = `${defaultHeight}px`;
    } else {
      seeMore1.style.display = "block";
    }

    // Toggle "See More" and "See Less" functionality
    seeMore1.addEventListener("click", () => {
      if (seeMore1.innerText === "See More") {
        seeMore1.innerText = "See Less";
        postCon1.style.height = "fit-content";
      } else {
        seeMore1.innerText = "See More";
        postCon1.style.height = `${defaultHeight}px`;
      }
    });
  }
});

const likedCon = document.querySelector(".liked-posts-con");
const savedCon = document.querySelector(".saved-posts-con");
const likedBtn = document.getElementById("liked");
const savedBtn = document.getElementById("saved");

function toggleDisplay() {
  if (likedBtn.checked) {
    likedCon.style.display = "flex";
    savedCon.style.display = "none";
  } else {
    likedCon.style.display = "none";
    savedCon.style.display = "flex";
  }
}

likedBtn.addEventListener("click", toggleDisplay);
savedBtn.addEventListener("click", toggleDisplay);

toggleDisplay();