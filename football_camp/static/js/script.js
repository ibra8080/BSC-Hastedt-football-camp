console.log("It works!");

document.addEventListener('DOMContentLoaded', function() {
    var showPasswordCheckbox = document.getElementById('show_password');
    if (showPasswordCheckbox) {
        showPasswordCheckbox.addEventListener('change', function() {
            var passwordFields = document.querySelectorAll('input[type="password"]');
            passwordFields.forEach(field => {
                if (this.checked) {
                    field.type = 'text';
                } else {
                    field.type = 'password';
                }
            });
        });
    }
});