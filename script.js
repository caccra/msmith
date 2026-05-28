/**
 * M-Smith Advocates JavaScript
 * Handles Theme Toggling, Mobile Navigation, and Scroll Animations
 */

document.addEventListener('DOMContentLoaded', () => {
    // 1. Current Year for Footer
    const currentYearSpan = document.getElementById('current-year');
    if (currentYearSpan) {
        currentYearSpan.textContent = new Date().getFullYear();
    }


    // 3. Mobile Navigation Toggle
    const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
    const primaryNav = document.getElementById('primary-navigation');
    const navLinks = document.querySelectorAll('.nav-link');

    if (mobileMenuToggle && primaryNav) {
        mobileMenuToggle.addEventListener('click', () => {
            const isExpanded = mobileMenuToggle.getAttribute('aria-expanded') === 'true';

            mobileMenuToggle.setAttribute('aria-expanded', !isExpanded);
            primaryNav.classList.toggle('is-open');

            // Prevent body scrolling when menu is open
            if (!isExpanded) {
                document.body.style.overflow = 'hidden';
            } else {
                document.body.style.overflow = '';
            }
        });

        // Close mobile menu when clicking a link
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                if (window.innerWidth <= 768) {
                    mobileMenuToggle.setAttribute('aria-expanded', 'false');
                    primaryNav.classList.remove('is-open');
                    document.body.style.overflow = '';
                }
            });
        });
    }

    // Removed Header Scroll Effect based on design preference

    // 4. Expertise Dropdown (mobile toggle + click-outside)
    const dropdownParent = document.querySelector('.nav-item-dropdown');
    const dropdownToggle = document.querySelector('.dropdown-toggle');

    if (dropdownParent && dropdownToggle) {
        dropdownToggle.addEventListener('click', (e) => {
            // On mobile: prevent navigation, toggle dropdown
            if (window.innerWidth <= 768) {
                e.preventDefault();
                dropdownParent.classList.toggle('is-open');
                const expanded = dropdownParent.classList.contains('is-open');
                dropdownToggle.setAttribute('aria-expanded', expanded);
            }
        });

        // Close dropdown when clicking outside (desktop)
        document.addEventListener('click', (e) => {
            if (!dropdownParent.contains(e.target)) {
                dropdownParent.classList.remove('is-open');
                dropdownToggle.setAttribute('aria-expanded', 'false');
            }
        });

        // Close dropdown on Escape key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                dropdownParent.classList.remove('is-open');
                dropdownToggle.setAttribute('aria-expanded', 'false');
            }
        });

        // Close mobile menu when a dropdown link is clicked
        const dropdownLinks = dropdownParent.querySelectorAll('.dropdown-item, .dropdown-all-link');
        dropdownLinks.forEach(link => {
            link.addEventListener('click', () => {
                if (window.innerWidth <= 768) {
                    const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
                    const primaryNav = document.getElementById('primary-navigation');
                    if (mobileMenuToggle && primaryNav) {
                        mobileMenuToggle.setAttribute('aria-expanded', 'false');
                        primaryNav.classList.remove('is-open');
                        document.body.style.overflow = '';
                    }
                }
            });
        });
    }

    // 5. Scroll Animations (Intersection Observer)
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const animationElements = document.querySelectorAll('.animate-on-scroll');

    if (!prefersReducedMotion && 'IntersectionObserver' in window) {
        const observer = new IntersectionObserver((entries, obs) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-visible');
                    obs.unobserve(entry.target);
                }
            });
        }, { threshold: 0.05 });

        animationElements.forEach(el => {
            const rect = el.getBoundingClientRect();
            // Immediately reveal elements already in the viewport — don't wait for async IO callback
            if (rect.top < window.innerHeight && rect.bottom > 0) {
                el.classList.add('is-visible');
            } else {
                observer.observe(el);
            }
        });
    } else {
        animationElements.forEach(el => {
            el.classList.add('is-visible');
            el.style.opacity = '1';
            el.style.transform = 'none';
        });
    }

    // 6. Contact Form Submission
    const contactForm = document.getElementById('contact-form-dedicated');
    if (contactForm) {
        const submitBtn = contactForm.querySelector('.submit-btn');

        contactForm.addEventListener('submit', async (e) => {
            e.preventDefault();

            const existingMsg = contactForm.querySelector('.form-status');
            if (existingMsg) existingMsg.remove();

            const originalText = submitBtn.textContent;
            submitBtn.textContent = 'Sending…';
            submitBtn.disabled = true;

            try {
                const res = await fetch('contact.php', {
                    method: 'POST',
                    body: new FormData(contactForm)
                });
                const data = await res.json();

                const msg = document.createElement('p');
                msg.className = 'form-status';

                if (data.success) {
                    msg.style.cssText = 'padding:12px 16px;background:#f0fdf4;border:1px solid #bbf7d0;border-radius:6px;color:#166534;font-size:0.9rem;margin-top:12px;';
                    msg.textContent = 'Message sent — we will respond within 24 hours.';
                    contactForm.reset();
                } else {
                    msg.style.cssText = 'padding:12px 16px;background:#fef2f2;border:1px solid #fecaca;border-radius:6px;color:#991b1b;font-size:0.9rem;margin-top:12px;';
                    msg.textContent = data.error || 'Something went wrong. Please try again or email us directly.';
                }

                submitBtn.insertAdjacentElement('afterend', msg);
            } catch (_) {
                const msg = document.createElement('p');
                msg.className = 'form-status';
                msg.style.cssText = 'padding:12px 16px;background:#fef2f2;border:1px solid #fecaca;border-radius:6px;color:#991b1b;font-size:0.9rem;margin-top:12px;';
                msg.textContent = 'Network error. Please email us directly at info@m-smithadvocates.com.';
                submitBtn.insertAdjacentElement('afterend', msg);
            } finally {
                submitBtn.textContent = originalText;
                submitBtn.disabled = false;
            }
        });
    }

    // 7. Hero Slider (backgrounds + content panels)
    const heroSlides   = document.querySelectorAll('.hero-slide');
    const heroContents = document.querySelectorAll('.hero-content-slide');
    const heroDots     = document.querySelectorAll('.hero-dot');

    if (heroSlides.length > 1) {
        let current = 0;
        const INTERVAL = 6000;

        function goTo(index) {
            // Remove active from current
            heroSlides[current].classList.remove('active');
            heroContents[current]?.classList.remove('active');
            heroDots[current]?.classList.remove('active');
            heroDots[current]?.setAttribute('aria-selected', 'false');

            current = (index + heroSlides.length) % heroSlides.length;

            // Add active to new
            heroSlides[current].classList.add('active');
            heroContents[current]?.classList.add('active');
            heroDots[current]?.classList.add('active');
            heroDots[current]?.setAttribute('aria-selected', 'true');
        }

        heroDots.forEach((dot, i) => {
            dot.addEventListener('click', () => {
                goTo(i);
                clearInterval(timer);
                timer = setInterval(() => goTo(current + 1), INTERVAL);
            });
        });

        let timer = setInterval(() => goTo(current + 1), INTERVAL);

        // Pause on hover
        const heroSection = document.getElementById('home');
        if (heroSection) {
            heroSection.addEventListener('mouseenter', () => clearInterval(timer));
            heroSection.addEventListener('mouseleave', () => {
                timer = setInterval(() => goTo(current + 1), INTERVAL);
            });
        }
    }

    // 8. Floating WhatsApp Button (injected globally)
    const waBtn = document.createElement('a');
    waBtn.href = 'https://wa.me/256782776074';
    waBtn.className = 'whatsapp-float';
    waBtn.target = '_blank';
    waBtn.rel = 'noopener noreferrer';
    waBtn.setAttribute('aria-label', 'Chat with us on WhatsApp');
    waBtn.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>';
    document.body.appendChild(waBtn);
});
