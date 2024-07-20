console.log("It works!");

document.addEventListener('DOMContentLoaded', function() {
    const showPasswordCheckbox = document.getElementById('show_password');
    const passwordFields = document.querySelectorAll('input[type="password"]');

    showPasswordCheckbox.addEventListener('change', function() {
        const type = this.checked ? 'text' : 'password';
        passwordFields.forEach(field => {
            field.setAttribute('type', type);
        });
    });

    const telephoneField = document.querySelector('input[name="telephone"]');
    telephoneField.addEventListener('input', function() {
        this.value = this.value.replace(/\D/g, '');
    });
});