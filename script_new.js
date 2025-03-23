document.addEventListener('DOMContentLoaded', function() {
    // Add custom cursor
    const cursorContainer = document.createElement('div');
    const cursor = document.createElement('div');
    const cursorFollower = document.createElement('div');
    cursor.classList.add('custom-cursor');
    cursorFollower.classList.add('custom-cursor-follower');
    cursorContainer.appendChild(cursor);
    cursorContainer.appendChild(cursorFollower);
    document.body.appendChild(cursorContainer);
    
    // Add hand gesture element
    const handGesture = document.createElement('div');
    handGesture.classList.add('hand-gesture');
    document.body.appendChild(handGesture);
    
    // Add particles container
    const particlesContainer = document.createElement('div');
    particlesContainer.id = 'particles-js';
    particlesContainer.classList.add('particles-js');
    document.body.appendChild(particlesContainer);
    
    // Initialize particles
    if (window.particlesJS) {
        particlesJS('particles-js', {
            particles: {
                number: { value: 30, density: { enable: true, value_area: 800 } },
                color: { value: '#0066cc' },
                shape: { type: 'circle' },
                opacity: { value: 0.1, random: true },
                size: { value: 5, random: true },
                move: {
                    enable: true,
                    speed: 1,
                    direction: 'none',
                    random: true,
                    out_mode: 'out'
                }
            }
        });
    }
    
    // Custom cursor tracking
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
    let lastScrollDirection = 'down';
    
    window.addEventListener('scroll', function() {
        const st = window.pageYOffset || document.documentElement.scrollTop;
        
        // Show hand gesture when scrolling
        handGesture.classList.add('visible');
        
        // Check scroll direction
        if (st > lastScrollTop) {
            // Scrolling down
            if (lastScrollDirection !== 'down') {
                handGesture.classList.remove('scrolling-up');
                handGesture.classList.add('scrolling-down');
                lastScrollDirection = 'down';
                
                // Add flip animation
                document.querySelectorAll('section:not([style="display: none;"])').forEach(section => {
                    if (isElementInViewport(section)) {
                        section.style.animation = 'flipInX 1s forwards';
                    }
                });
            }
        } else {
            // Scrolling up
            if (lastScrollDirection !== 'up') {
                handGesture.classList.remove('scrolling-down');
                handGesture.classList.add('scrolling-up');
                lastScrollDirection = 'up';
            }
        }
        
        clearTimeout(scrollTimer);
        scrollTimer = setTimeout(function() {
            handGesture.classList.remove('visible');
        }, 1500);
        
        lastScrollTop = st <= 0 ? 0 : st; // For Mobile or negative scrolling
    }, false);
    
    // GSAP animations for elements
    if (window.gsap) {
        gsap.registerPlugin(ScrollTrigger);
        
        // Animate elements on scroll
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
    }
    
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
        if (window.gsap) {
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
        } else {
            section.style.animation = 'flipInX 1s forwards';
            if (section.id === 'skills') {
                setTimeout(animateProgressBars, 1000);
            }
        }
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
            
            if (window.gsap) {
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
            } else {
                currentSection.style.opacity = 0;
                currentSection.style.transform = 'translateY(-50px)';
                
                setTimeout(() => {
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
                }, 400);
            }
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
                const categoryElement = card.querySelector('p strong');
                const categoryText = categoryElement ? categoryElement.nextSibling.textContent.trim() : '';
                
                const techElement = card.querySelector('p:nth-of-type(2) strong');
                const techText = techElement ? techElement.nextSibling.textContent.trim() : '';
                const technologies = techText.split(', ');
                
                const categoryMatch = selectedCategories.length === 0 || selectedCategories.includes(categoryText);
                const techMatch = selectedTech.length === 0 || technologies.some(tech => selectedTech.includes(tech));
                
                if (categoryMatch && techMatch) {
                    card.style.display = 'block';
                    
                    // Apply entrance animation
                    card.style.opacity = '0';
                    card.style.transform = 'translateY(20px)';
                    
                    setTimeout(() => {
                        card.style.opacity = '1';
                        card.style.transform = 'translateY(0)';
                    }, 100);
                } else {
                    card.style.display = 'none';
                }
            });
        }
        
        // Add event listeners to filters
        categoryFilter.addEventListener('change', filterProjects);
        techFilter.addEventListener('change', filterProjects);
    }
    
    // Contact form submission with Apple-style validation
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        // Add SF Pro style form interactions
        const formInputs = contactForm.querySelectorAll('input, textarea');
        
        formInputs.forEach(input => {
            // Add focus styles
            input.addEventListener('focus', function() {
                this.parentElement.classList.add('focused');
            });
            
            input.addEventListener('blur', function() {
                this.parentElement.classList.remove('focused');
                
                // Check validation
                if (this.value.trim() === '') {
                    this.classList.add('is-invalid');
                } else {
                    this.classList.remove('is-invalid');
                    this.classList.add('is-valid');
                }
            });
        });
        
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Validate all fields
            let isValid = true;
            formInputs.forEach(input => {
                if (input.value.trim() === '') {
                    input.classList.add('is-invalid');
                    isValid = false;
                }
            });
            
            if (isValid) {
                // In a real implementation, you would send the form data to a server here
                
                // Show success message
                const successMessage = document.createElement('div');
                successMessage.classList.add('alert', 'alert-success', 'mt-3');
                successMessage.innerText = 'Thank you for your message! I\'ll get back to you soon.';
                
                // Add entrance animation
                successMessage.style.opacity = '0';
                successMessage.style.transform = 'translateY(20px)';
                contactForm.appendChild(successMessage);
                
                setTimeout(() => {
                    successMessage.style.opacity = '1';
                    successMessage.style.transform = 'translateY(0)';
                }, 10);
                
                // Reset form
                contactForm.reset();
                formInputs.forEach(input => {
                    input.classList.remove('is-valid');
                });
                
                // Remove success message after 5 seconds
                setTimeout(() => {
                    successMessage.style.opacity = '0';
                    successMessage.style.transform = 'translateY(-20px)';
                    setTimeout(() => {
                        contactForm.removeChild(successMessage);
                    }, 300);
                }, 5000);
            }
        });
    }
    
    // Helper function to check if element is in viewport
    function isElementInViewport(el) {
        const rect = el.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    }
    
    // SF Pro style hover effects for all clickable elements
    const clickableElements = document.querySelectorAll('a, button, .card, .nav-link');
    
    clickableElements.forEach(element => {
        element.addEventListener('mouseenter', function() {
            this.style.transition = 'all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1)';
        });
    });
    
    // Ensure initial animations run on load
    animateProgressBars();
});

// Add smooth scrolling for all anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const targetId = this.getAttribute('href');
        if (targetId !== '#') {
            e.preventDefault();
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        }
    });
});

// Visitor counter function
function setupVisitorCounter() {
    // Create the visitor counter element
    const visitorCounter = document.createElement('div');
    visitorCounter.classList.add('visitor-counter');
    visitorCounter.innerHTML = `
        <span id="visitor-count-label">Total Portfolio Visitors:</span>
        <span id="visitor-count">0</span>
    `;
    document.body.appendChild(visitorCounter);
    
    // Check if counter is stored in localStorage
    let count = localStorage.getItem('visitorCount');
    
    // If this is first visit or counter doesn't exist
    if (!count) {
        count = Math.floor(Math.random() * 100) + 100; // Start with a random number between 100-199
        localStorage.setItem('visitorCount', count);
    } else {
        // Increment only if this is a new session
        if (!sessionStorage.getItem('counted')) {
            count = parseInt(count) + 1;
            localStorage.setItem('visitorCount', count);
            sessionStorage.setItem('counted', 'true');
        }
    }
    
    // Display the count
    document.getElementById('visitor-count').textContent = count;
    
    // Animate the counter
    setTimeout(() => {
        visitorCounter.classList.add('visible');
    }, 1500);
}

// Initialize visitor counter
setupVisitorCounter();