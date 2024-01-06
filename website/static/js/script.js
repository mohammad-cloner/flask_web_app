const navBar = document.querySelector(".navbar");
let prevScrollPos = window.scrollY;

window.addEventListener("scroll", function () {
  let currScrollPos = window.scrollY;

  if (currScrollPos > prevScrollPos) {
    navBar.style.transform = `translateY(-105%)`;
  } else {
    navBar.style.transform = `translateY(0%)`;
  }

  prevScrollPos = currScrollPos;
});

const sidebarBtn = document.querySelector(".toggle-btn");
const sidebar = document.querySelector("aside");

sidebarBtn.addEventListener("click", () => {
  document.body.classList.toggle("active");
});
