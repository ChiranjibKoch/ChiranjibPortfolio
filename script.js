document.addEventListener('DOMContentLoaded', function() {
    // Custom cursor
    const cursor = document.querySelector('.custom-cursor');
    const cursorFollower = document.querySelector('.custom-cursor-follower');
    const handGesture = document.querySelector('.hand-gesture');
    
    document.addEventListener('mousemove', function(e) {
        cursor.style.left = e.clientX + 'px';
        cursor.style.top = e.clientY + 'px';
        
        setTimeout(function() {
            cursorFollower.style.left = e.clientX + 'px';
            cursorFollower.style.top = e.clientY + 'px';
        }, 80);
    });
    
    document.addEventListener('mousedown', function() {
        cursor.classList.add('active');
    });
    
    document.addEventListener('mouseup', function() {
        cursor.classList.remove('active');
    });
    
    // Hand gesture scroll effect
    let lastScrollTop = 0;
    let scrollTimer;
    window.addEventListener('scroll', function() {
        const st = window.pageYOffset || document.documentElement.scrollTop;
        
        // Show hand gesture when scrolling
        handGesture.classList.add('visible');
        
        // Check scroll direction
        if (st > lastScrollTop) {
            // Scrolling down
            handGesture.classList.remove('scrolling-up');
            handGesture.classList.add('scrolling-down');
        } else {
            // Scrolling up
            handGesture.classList.remove('scrolling-down');
            handGesture.classList.add('scrolling-up');
        }
        
        clearTimeout(scrollTimer);
        scrollTimer = setTimeout(function() {
            handGesture.classList.remove('visible');
        }, 1500);
        
        lastScrollTop = st <= 0 ? 0 : st; // For Mobile or negative scrolling
    }, false);
    
    // GSAP animations for elements
    gsap.registerPlugin(ScrollTrigger);
    
    // Animate cards
    gsap.utils.toArray('.card').forEach(card => {
        gsap.from(card, {
            y: 50,
            opacity: 0,
            duration: 0.8,
            ease: "power2.out",
            scrollTrigger: {
                trigger: card,
                start: "top 80%",
                toggleActions: "play none none none"
            }
        });
    });
    
    // Animate progress bars (for visible sections only)
    function animateProgressBars() {
        const visibleSection = document.querySelector('section[style="display: block;"]');
        if (visibleSection) {
            const progressBars = visibleSection.querySelectorAll('.progress-bar');
            progressBars.forEach(bar => {
                const width = bar.style.width;
                bar.style.width = '0%';
                setTimeout(() => {
                    bar.style.width = width;
                }, 100);
            });
        }
    }
    
    // Navigation with smooth transitions
    const navLinks = document.querySelectorAll('.sidebar .nav-link');
    const sections = document.querySelectorAll('section');
    
    // Show home section by default
    sections[0].style.display = 'block';
    
    // Flip animation for section transitions
    function flipInSection(section) {
        gsap.fromTo(section, 
            { opacity: 0, rotateX: 90 },
            { 
                duration: 0.8, 
                opacity: 1, 
                rotateX: 0,
                ease: "power2.out",
                onComplete: function() {
                    if (section.id === 'skills') {
                        animateProgressBars();
                    }
                }
            }
        );
    }
    
    // Navigation click handler with advanced animations
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Lightning flash effect on nav click
            const lightning = document.createElement('div');
            lightning.classList.add('lightning-flash');
            this.appendChild(lightning);
            setTimeout(() => this.removeChild(lightning), 300);
            
            // Remove active class from all links
            navLinks.forEach(l => l.classList.remove('active'));
            
            // Add active class to clicked link
            this.classList.add('active');
            
            // Get target section
            const targetId = this.getAttribute('href').substring(1);
            const targetSection = document.getElementById(targetId);
            
            // Fade out current section
            const currentSection = document.querySelector('section[style="display: block;"]');
            gsap.to(currentSection, {
                duration: 0.4,
                opacity: 0,
                y: -50,
                ease: "power2.in",
                onComplete: function() {
                    // Hide all sections
                    sections.forEach(section => section.style.display = 'none');
                    
                    // Show and animate target section
                    targetSection.style.display = 'block';
                    targetSection.style.opacity = 0;
                    flipInSection(targetSection);
                    
                    // Scroll to top with smooth animation
                    window.scrollTo({
                        top: 0,
                        behavior: 'smooth'
                    });
                }
            });
        });
    });
    
    // Project filtering functionality
    const categoryFilter = document.getElementById('categoryFilter');
    const techFilter = document.getElementById('techFilter');
    const projectCards = document.querySelectorAll('.projects-container .card');
    
    if (categoryFilter && techFilter) {
        // Function to filter projects
        function filterProjects() {
            const selectedCategories = Array.from(categoryFilter.selectedOptions).map(option => option.value);
            const selectedTech = Array.from(techFilter.selectedOptions).map(option => option.value);
            
            projectCards.forEach(card => {
                const category = card.querySelector('p strong:contains("Category:")').nextSibling.textContent.trim();
                const technologies = card.querySelector('p strong:contains("Technologies:")').nextSibling.textContent.trim().split(', ');
                
                const categoryMatch = selectedCategories.length === 0 || selectedCategories.includes(category);
                const techMatch = selectedTech.length === 0 || technologies.some(tech => selectedTech.includes(tech));
                
                card.style.display = (categoryMatch && techMatch) ? 'block' : 'none';
            });
        }
        
        // Add event listeners to filters
        categoryFilter.addEventListener('change', filterProjects);
        techFilter.addEventListener('change', filterProjects);
    }
    
    // Contact form submission
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // In a real implementation, you would send the form data to a server here
            
            // Show success message
            alert('Thank you for your message! I\'ll get back to you soon.');
            
            // Reset form
            contactForm.reset();
        });
    }
    
    // Fix for :contains selector (not natively supported)
    jQuery.expr[':'].contains = function(a, i, m) {
        return jQuery(a).text().toUpperCase().indexOf(m[3].toUpperCase()) >= 0;
    };
});

// Add smooth scrolling
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});