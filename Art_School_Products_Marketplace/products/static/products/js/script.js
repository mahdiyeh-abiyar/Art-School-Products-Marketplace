// Mobile Menu
function setupMobileMenu() {
  const menuButton = document.getElementById('menuButton');
  const mobileMenu = document.getElementById('mobileMenu');
  const closeButton = document.getElementById('closeButton');
  const backdrop = document.getElementById('backdrop');

  // مخفی کردن منو هنگام لود صفحه (برای اطمینان)
  mobileMenu.classList.add('hidden');

  menuButton.addEventListener('click', function() {
    mobileMenu.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
  });

  closeButton.addEventListener('click', function() {
    mobileMenu.classList.add('hidden');
    document.body.style.overflow = 'auto';
  });

  backdrop.addEventListener('click', function() {
    mobileMenu.classList.add('hidden');
    document.body.style.overflow = 'auto';
  });
}

// فقط یکبار رویداد DOMContentLoaded را ثبت کنید
document.addEventListener('DOMContentLoaded', function() {
  setupMobileMenu();
});