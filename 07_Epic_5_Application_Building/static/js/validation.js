// validation.js - Apex Bank Client-side Validation Checks

(function () {
    'use strict'
    
    window.addEventListener('load', function () {
        // Fetch all the forms we want to apply custom Bootstrap validation styles to
        var forms = document.getElementsByClassName('needs-validation');
        var loadingOverlay = document.getElementById('loadingOverlay');
        
        // Loop over them and prevent submission
        Array.prototype.filter.call(forms, function (form) {
            form.addEventListener('submit', function (event) {
                var isLogicalValid = validateLogicalConstraints();
                
                if (form.checkValidity() === false || !isLogicalValid) {
                    event.preventDefault();
                    event.stopPropagation();
                } else {
                    // Form is valid - display the loading processing overlay spinner
                    loadingOverlay.classList.remove('d-none');
                }
                form.classList.add('was-validated');
            }, false);
        });
        
        // Logical cross-validation fields triggers
        var ageInput = document.getElementById('age');
        var employedInput = document.getElementById('employed_years');
        var childrenInput = document.getElementById('children');
        var familyInput = document.getElementById('family_members');
        var incomeTypeInput = document.getElementById('income_type');
        var occTypeInput = document.getElementById('occupation_type');
        
        if (ageInput && employedInput) {
            employedInput.addEventListener('input', checkEmploymentLimit);
            ageInput.addEventListener('input', checkEmploymentLimit);
        }
        
        if (childrenInput && familyInput) {
            childrenInput.addEventListener('input', checkFamilySizeLimits);
            familyInput.addEventListener('input', checkFamilySizeLimits);
        }
        
        if (incomeTypeInput && occTypeInput) {
            incomeTypeInput.addEventListener('change', autoCheckPensioner);
        }
        
        function checkEmploymentLimit() {
            var age = parseFloat(ageInput.value) || 0;
            var emp = parseFloat(employedInput.value) || 0;
            
            if (emp > (age - 14)) {
                employedInput.setCustomValidity("Employment years exceed logical work lifespan starting from age 14.");
            } else {
                employedInput.setCustomValidity("");
            }
        }
        
        function checkFamilySizeLimits() {
            var children = parseInt(childrenInput.value) || 0;
            var family = parseInt(familyInput.value) || 0;
            
            // Family size must be at least children count + 1 (the applicant)
            if (family < (children + 1)) {
                familyInput.setCustomValidity("Family size must be at least children count + 1 (the applicant).");
            } else {
                familyInput.setCustomValidity("");
            }
        }
        
        function autoCheckPensioner() {
            var type = incomeTypeInput.value;
            if (type === 'Pensioner') {
                if (employedInput) {
                    employedInput.value = 0;
                    employedInput.setCustomValidity("");
                }
            }
        }

        function validateLogicalConstraints() {
            checkEmploymentLimit();
            checkFamilySizeLimits();
            return ageInput.checkValidity() && employedInput.checkValidity() && childrenInput.checkValidity() && familyInput.checkValidity();
        }
    }, false);
})();
