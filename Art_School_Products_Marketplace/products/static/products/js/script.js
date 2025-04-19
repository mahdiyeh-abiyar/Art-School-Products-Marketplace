/* ==========================================
Hamburger menu
========================================== */
document.addEventListener('DOMContentLoaded', function() {
  const mobileNav = document.getElementById("mobile-nav");
  const backDrop = document.getElementById("backdrop");
  const menuBar = document.getElementById("menubar");
  const menuBarIcon = menuBar.querySelector("i");
  
  const toggleMenu = () => {
    const isOpen = mobileNav.classList.toggle("h-0");
    mobileNav.classList.toggle("h-[calc(100vh-100px)]");
    menuBarIcon.classList.toggle("fa-bars");
    menuBarIcon.classList.toggle("fa-xmark");
    backDrop.classList.toggle("hidden");
    document.body.classList.toggle("overflow-hidden");
    
    // Update aria-expanded for accessibility
    menuBar.setAttribute("aria-expanded", isOpen ? "false" : "true");
  };

  menuBar.addEventListener("click", toggleMenu);
  backDrop.addEventListener("click", toggleMenu);
});


function toggleAccordion(id) {
  const section = document.getElementById(id);
  const parent = section.parentElement;
  const icon = parent.querySelector('.icon');
  const question = parent.querySelector('.question');

  // اگر پاسخ مخفی است، آن را نشان بده و پس‌زمینه را به رنگ آبی تغییر بده
  if (section.classList.contains('hidden')) {
    section.classList.remove('hidden');
    
    // حذف bg-light-gray قبلی
    parent.classList.remove('bg-light-gray');
    
    // افزودن bg-teal-500 و text-white
    parent.classList.add('bg-teal', 'text-white');

    // چرخاندن + به ضربدر و تغییر رنگ پس‌زمینه
    icon.classList.remove('bg-Orange');
    icon.classList.add('bg-white', 'rotate-90', 'text-Orange');
    icon.innerHTML = '×';

    question.classList.remove('text-grayblue');
    question.classList.add('text-white');
  } else {
    // اگر پاسخ نمایش داده شده است، آن را مخفی کن و پس‌زمینه را به رنگ طوسی تغییر بده
    section.classList.add('hidden');
    
    // حذف bg-teal-500 و text-white
    parent.classList.remove('bg-teal', 'text-white');
    
    // افزودن دوباره bg-light-gray
    parent.classList.add('bg-light-gray');

    // بازگشت به حالت اولیه آیکون
    icon.classList.remove('bg-white', 'rotate-90', 'text-Orange');
    icon.classList.add('bg-Orange');
    icon.innerHTML = '+';

    question.classList.remove('text-white');
    question.classList.add('text-grayblue');
  }
}
