document.addEventListener('DOMContentLoaded', function() {
    // Active navigation item functionality
    var currentPage = window.currentPage;
    var navItems = document.querySelectorAll('.nav ul li');
    navItems.forEach(function(item) {
        if (item.querySelector('a').id === 'nav-' + currentPage) {
            item.classList.add('active');
        }
    });
});