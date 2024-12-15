const posts =document.querySelectorAll(".post");

posts.forEach(post => {
  const seeMore = post.querySelector(".see-more-btn");
  const postCon = post.querySelector(".post-content");
  const paragraph = postCon.querySelector("p"); 

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



});
