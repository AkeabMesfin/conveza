const dialog = document.querySelector(".dialog");
const logOutPopUP = document.querySelector(".logout-pop-up");
function openCreate() {
  dialog.showModal();
}

function OpenLogOut() {
  logOutPopUP.showModal();
}

function CloseLogOut() {
  logOutPopUP.close();
}

function closeDialog() {
  dialog.close();
}

dialog.addEventListener("click", (event) => {
  if (event.target === dialog) {
    closeDialog();
  }
});

logOutPopUP.addEventListener("click", (event) => {
  if (event.target === logOutPopUP) {
    CloseLogOut();
  }
});