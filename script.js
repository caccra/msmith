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
    // Only apply if user hasn't requested reduced motion
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    if (!prefersReducedMotion && 'IntersectionObserver' in window) {
        const animationElements = document.querySelectorAll('.animate-on-scroll');

        const observerOptions = {
            root: null,
            rootMargin: '0px',
            threshold: 0.1
        };

        const observer = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-visible');
                    // Stop observing once animated
                    observer.unobserve(entry.target);
                }
            });
        }, observerOptions);

        animationElements.forEach(el => observer.observe(el));
    } else {
        // Fallback or if reduced motion is preferred, show all immediately
        const animationElements = document.querySelectorAll('.animate-on-scroll');
        animationElements.forEach(el => {
            el.classList.add('is-visible');
            el.style.opacity = '1';
            el.style.transform = 'none';
        });
    }
});
