(function ($) {
    "use strict";

    // Theme Switcher
    function initThemeSwitcher() {
        // Load saved theme or use default
        const savedTheme = localStorage.getItem('selectedTheme') || 'warm-professional';
        setTheme(savedTheme);
        
        // Handle theme option clicks
        $('.theme-option').on('click', function(e) {
            e.preventDefault();
            const theme = $(this).data('theme');
            setTheme(theme);
            localStorage.setItem('selectedTheme', theme);
        });
    }
    
    function setTheme(theme) {
        // Remove all theme classes
        $('html').removeAttr('data-theme');
        
        // Apply new theme
        if (theme !== 'warm-professional') {
            $('html').attr('data-theme', theme);
        }
        
        // Update active state in dropdown
        $('.theme-option').removeClass('active');
        $(`.theme-option[data-theme="${theme}"]`).addClass('active');
        
        // Update theme transition for smooth switching
        $('*').css('transition', 'var(--theme-transition)');
    }
    
    // Initialize theme switcher
    initThemeSwitcher();

    // Font Switcher
    function initFontSwitcher() {
        // Load saved font or use default
        const savedFont = localStorage.getItem('selectedFont') || 'default';
        setFont(savedFont);
        
        // Handle font option clicks
        $('.font-option').on('click', function(e) {
            e.preventDefault();
            const font = $(this).data('font');
            setFont(font);
            localStorage.setItem('selectedFont', font);
        });
    }
    
    function setFont(font) {
        // Remove all font classes
        $('body').removeClass('font-serif font-sans font-modern font-elegant font-corporate font-minimal font-creative');
        
        // Apply new font class
        if (font !== 'default') {
            $('body').addClass(`font-${font}`);
        }
        
        // Update active state in dropdown
        $('.font-option').removeClass('active');
        $(`.font-option[data-font="${font}"]`).addClass('active');
    }
    
    // Initialize font switcher
    initFontSwitcher();


    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();
    
    
    // Initiate the wowjs
    new WOW().init();


    // Fixed Navbar
    $(window).scroll(function () {
        if ($(window).width() < 992) {
            if ($(this).scrollTop() > 45) {
                $('.fixed-top').addClass('bg-dark shadow');
            } else {
                $('.fixed-top').removeClass('bg-dark shadow');
            }
        } else {
            if ($(this).scrollTop() > 45) {
                $('.fixed-top').addClass('bg-dark shadow').css('top', -45);
            } else {
                $('.fixed-top').removeClass('bg-dark shadow').css('top', 0);
            }
        }
    });
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Causes progress
    $('.causes-progress').waypoint(function () {
        $('.progress .progress-bar').each(function () {
            $(this).css("width", $(this).attr("aria-valuenow") + '%');
        });
    }, {offset: '80%'});


    // Counter Animation with waypoint trigger
    $('.counter').waypoint(function () {
        $('.counter').each(function () {
            var $this = $(this);
            var countTo = $this.attr('data-target');
            
            $({ countNum: $this.text() }).animate({
                countNum: countTo
            },
            {
                duration: 2000,
                easing: 'linear',
                step: function () {
                    $this.text(Math.floor(this.countNum));
                },
                complete: function () {
                    $this.text(this.countNum);
                }
            });
        });
    }, {offset: '80%'});


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: false,
        smartSpeed: 1000,
        center: true,
        dots: false,
        loop: true,
        nav : true,
        navText : [
            '<i class="bi bi-arrow-left"></i>',
            '<i class="bi bi-arrow-right"></i>'
        ],
        responsive: {
            0:{
                items:1
            },
            768:{
                items:2
            }
        }
    });

    // Team carousel
    $(".team-carousel").owlCarousel({
        autoplay: true,
        autoplayTimeout: 4500,
        autoplayHoverPause: true,
        smartSpeed: 800,
        center: true,
        dots: true,
        nav: true,
        navText : [
            '<i class="bi bi-arrow-left"></i>',
            '<i class="bi bi-arrow-right"></i>'
        ],
        margin: 18,
        stagePadding: 80,
        loop: true,
        responsive: {
            0:{ items:1, stagePadding:40 },
            576:{ items:1, stagePadding:60 },
            768:{ items:2, stagePadding:80 },
            992:{ items:3, stagePadding:120 }
        }
    });

})(jQuery);

