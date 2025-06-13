// Icon toggling functionality
document.addEventListener('DOMContentLoaded', () => {
  const observerOptions = {
    root: null, // viewport
    rootMargin: '0px',
    threshold: 0.15, // trigger when 15% of the element is visible
  };

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('show');
        observer.unobserve(entry.target); // stop observing once shown
      }
    });
  }, observerOptions);

  document.querySelectorAll('.fade-in-slide').forEach(el => {
    observer.observe(el);
  });
});
// Hamburger menu functionality 
document.addEventListener('DOMContentLoaded', function () {
  const hamburger = document.getElementById('hamburger');
  const mobileNav = document.getElementById('mobile-nav');
  const closeBtn = document.getElementById('closeBtn');

  hamburger.addEventListener('click', () => {
    mobileNav.classList.add('active');
  });

  closeBtn.addEventListener('click', () => {
    mobileNav.classList.remove('active');
  });
});

