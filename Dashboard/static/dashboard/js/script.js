const toggleBtn = document.getElementById('menu-toggle');
const sidebar = document.getElementById('sidebar');
const labels = document.querySelectorAll('.label');
const menuIcon = document.getElementById('menu-icon');
const mainContent = document.getElementById('main-content');

let isOpen = false;

toggleBtn.addEventListener('click', () => {
  isOpen = !isOpen;

  // نمایش یا مخفی‌کردن لیبل‌ها
  labels.forEach(label => {
    label.classList.toggle('hidden', !isOpen);
  });

  if (isOpen) {
    sidebar.classList.remove('w-12');
    sidebar.classList.add('w-64', 'z-50', 'shadow-lg', 'right-0');

    // حذف موقعیت‌های قبلی
    sidebar.classList.remove('fixed', 'top-[64px]', 'relative', 'top-0');

    if (window.innerWidth >= 1024) {
      // اگر تو حالت lg هستیم: position عادی و بدون فاصله از بالا
      sidebar.classList.add('relative');
    } else {
      // در حالت موبایل: fixed با فاصله از بالا
      sidebar.classList.add('fixed', 'top-[64px]');
    }

    mainContent.classList.add('opacity-50', 'pointer-events-none');

    menuIcon.innerHTML = `<path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />`;
    menuIcon.classList.add('text-red-500');
  } else {
    sidebar.classList.remove(
      'w-64', 'z-50', 'shadow-lg', 'fixed', 'relative',
      'top-[64px]', 'top-0', 'right-0'
    );
    sidebar.classList.add('w-12');

    mainContent.classList.remove('opacity-50', 'pointer-events-none');

    menuIcon.innerHTML = `<path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h16" />`;
    menuIcon.classList.remove('text-red-500');
  }
});


const sidebarButtons = document.querySelectorAll('.sidebar-btn');

sidebarButtons.forEach(btnGroup => {
  const btn = btnGroup.querySelector('button');
  const icon = btn.querySelector('svg');

  btn.addEventListener('click', () => {
    if (icon.classList.contains('text-Orange')) {
      // اگر قرمز بود → برگرد به dark-teal
      icon.classList.remove('text-Orange');
      icon.classList.add('text-dark-teal'); // یا text-teal-700
    } else {
      // اگر dark-teal بود → قرمزش کن
      icon.classList.remove('text-dark-teal'); // یا text-teal-700
      icon.classList.add('text-Orange');
    }
  });
});



const editSections = document.querySelectorAll('.edit-btn');

  editSections.forEach((button, index) => {
    const row = button.closest('div.flex');
    const input = row.querySelector('.editable-input');
    const iconContainer = row.querySelector('.icon-container');

    let isEditing = false;

    function setIcon(type) {
      let svg = '';
      switch (type) {
        case 'edit':
          svg = `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M16.862 4.487L18.549 2.799C18.9007 2.44733 19.3777 2.24976 19.875 2.24976C20.3723 2.24976 20.8493 2.44733 21.201 2.799C21.5527 3.15068 21.7502 3.62766 21.7502 4.125C21.7502 4.62235 21.5527 5.09933 21.201 5.451L6.832 19.82C6.30332 20.3484 5.65137 20.7367 4.935 20.95L2.25 21.75L3.05 19.065C3.26328 18.3486 3.65163 17.6967 4.18 17.168L16.863 4.487H16.862ZM16.862 4.487L19.5 7.125" stroke="#015551" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>`;
          break;
        case 'plus':
          svg = `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M12 4.5V19.5M19.5 12H4.5" stroke="#015551" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>`;
          break;
        case 'check':
          svg = `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M4.5 12.75L10.5 18.75L19.5 5.25" stroke="#015551" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
          `;
          break;
      }
      iconContainer.innerHTML = svg;
    }

    function updateIcon() {
      if (isEditing) {
        setIcon('check');
      } else {
        if (input.value.trim() === '') {
          setIcon('plus');
        } else {
          setIcon('edit');
        }
      }
    }

    input.addEventListener('input', updateIcon);
    updateIcon();

    button.addEventListener('click', () => {
      if (!isEditing) {
        input.removeAttribute('readonly');
        input.focus();
        isEditing = true;
      } else {
        input.setAttribute('readonly', true);
        isEditing = false;
      }
      updateIcon();
    });
  });

const logoutLink = document.getElementById("logout-link");
  const alertBox = document.getElementById("custom-alert");
  const cancelBtn = document.getElementById("cancel-btn");
  const confirmBtn = document.getElementById("confirm-logout-btn");

  logoutLink.addEventListener("click", (e) => {
    e.preventDefault();
    alertBox.classList.remove("hidden");
  });

  cancelBtn.addEventListener("click", () => {
    alertBox.classList.add("hidden");
  });

  confirmBtn.addEventListener("click", () => {
    alertBox.classList.add("hidden");
    // اینجا خروج واقعی رو پیاده کن:
    window.location.href = "/logout";
  });


  document.getElementById("close-alert").addEventListener("click", () => {
    document.getElementById("custom-alert").classList.add("hidden");
  });

  document.getElementById("cancel-btn").addEventListener("click", () => {
    document.getElementById("custom-alert").classList.add("hidden");
  });

function showTab(tabName) {
    const tabs = ['current', 'delivered', 'cancelled'];

    tabs.forEach(name => {
      document.getElementById(name).classList.add('hidden');

      const btn = document.getElementById(`tab-${name}`);
      btn.classList.remove('text-orange-500', 'border-orange-500');
      btn.classList.add('text-gray-600', 'border-transparent');
    });

    document.getElementById(tabName).classList.remove('hidden');

    const activeBtn = document.getElementById(`tab-${tabName}`);
    activeBtn.classList.add('text-orange-500', 'border-orange-500');
    activeBtn.classList.remove('text-gray-600', 'border-transparent');
  }
