const posts = document.querySelectorAll(".post");

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


const commentCons = document.querySelectorAll('.comment'); // Select all comment elements

commentCons.forEach(comment => { // Loop through each comment
    const commentSeeMoreBtn = comment.querySelector('.see-more-btn'); // Button to toggle see more/less
    const commentContent = comment.querySelector('.comment-content'); // Comment content
    const commentParagraph = commentContent.querySelector('p'); // Paragraph within comment content

    const commentDefaultHeight = 56; // Default height for truncation

    // Check if the paragraph exists and if the comment content exceeds the default height
    if (commentParagraph && commentContent.scrollHeight > commentDefaultHeight) {
        commentSeeMoreBtn.style.display = "block"; // Show the "See More" button
        commentContent.style.height = `${commentDefaultHeight}px`; // Set initial height
    } else {
        commentSeeMoreBtn.style.display = "none"; // Hide button if no overflow
    }

    // Add event listener to toggle "See More" and "See Less"
    commentSeeMoreBtn.addEventListener("click", () => {
        if (commentSeeMoreBtn.innerText === "See More") {
            commentSeeMoreBtn.innerText = "See Less"; // Change button text
            commentContent.style.height = "fit-content"; // Expand to full height
        } else {
            commentSeeMoreBtn.innerText = "See More"; // Change button text back
            commentContent.style.height = `${commentDefaultHeight}px`; // Collapse to default height
        }
    });
});
