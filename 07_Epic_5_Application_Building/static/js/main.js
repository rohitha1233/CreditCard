// main.js - Apex Bank General Front-end Controllers

document.addEventListener('DOMContentLoaded', function() {
    console.log("[INFO] Apex Bank Credit Eligibility System ready.");
    
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Automatic alert timeout dismissal after 6 seconds
    const alerts = document.querySelectorAll('.alert-dismissible');
    alerts.forEach(function(alert) {
        setTimeout(function() {
            try {
                const bsAlert = new bootstrap.Alert(alert);
                bsAlert.close();
            } catch (err) {
                // Fail silently if Bootstrap object is not active
            }
        }, 6000);
    });
});
