const menu = document.querySelector(".hamburger-menu");
menu.addEventListener("click", function () {
  const headerNavigation = document.querySelector(
    ".hamburger-header-navigation"
  );
  if (
    headerNavigation.style.display === "none" ||
    headerNavigation.style.display === ""
  ) {
    headerNavigation.style.display = "block";
  } else {
    headerNavigation.style.display = "none";
  }
});
