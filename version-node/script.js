function toggleMenu() {
  var menuItems = document.getElementById('mobile-menu-items');
  if (menuItems.style.display === "none") {
    menuItems.style.display = "block";
  } else {
    menuItems.style.display = "none";
  }
}