# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| football_camp | home.html | ![screenshot](documentation/validation/test-home.png) | |
| football_camp | book_service.html | ![screenshot](documentation/validation/html-book-v.png) | |
| football_camp | confirm_delete_booking.html | ![screenshot](documentation/validation/html-d-book-v.png) | |
| football_camp | confirm_delete_player.html | ![screenshot](documentation/validation/html-d-player-v.png) | |
| football_camp | edit_booking.html | ![screenshot](documentation/validation/html-edit-book-v.png) | |
| football_camp | edit_player.html | ![screenshot](documentation/validation/html-edit-player-v.png) | |
| football_camp | manage_players.html | ![screenshot](documentation/validation/html-m-player-v.png) | |
| football_camp | player_profile.html | ![screenshot](documentation/validation/html-player-p-v.png) | |
| football_camp | service_page.html | ![screenshot](documentation/validation/html-service-v.png) | |
| football_camp | user_account.html | ![screenshot](documentation/validation/html-u-account-v.png) | |
| football_camp | login.html | ![screenshot](documentation/validation/html-login-v.png) | |
| football_camp | register.html | ![screenshot](documentation/validation/html-register-v.png) | |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| football_camp | style.css | ![screenshot](documentation/validation/css-valid.png) | |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| football_camp | script.js | ![screenshot](documentation/validation/js-valid.png) | |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| football_camp | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ibra8080/BSC-Hastedt-football-camp/main/football_camp/admin.py) | ![screenshot](documentation/validation/admin-py-v.png) | |
| football_camp | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ibra8080/BSC-Hastedt-football-camp/main/football_camp/forms.py) | ![screenshot](documentation/validation/form-py-v.png) | |
| football_camp | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ibra8080/BSC-Hastedt-football-camp/main/football_camp/models.py) | ![screenshot](documentation/validation/models-py-v.png) | |
| football_camp | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ibra8080/BSC-Hastedt-football-camp/main/football_camp/urls.py) | ![screenshot](documentation/validation/urls-py-f-v.png) | |
| football_camp | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ibra8080/BSC-Hastedt-football-camp/main/football_camp/views.py) | ![screenshot](documentation/validation/views-py-v.png) | |
|  | manage.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ibra8080/BSC-Hastedt-football-camp/main/manage.py) | ![screenshot](documentation/validation/manage-py-v.png) | |
| my_project | settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ibra8080/BSC-Hastedt-football-camp/main/my_project/settings.py) | ![screenshot](documentation/validation/settings-py-v.png) | |
| my_project | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ibra8080/BSC-Hastedt-football-camp/main/my_project/urls.py) | ![screenshot](documentation/validation/urls-py-v.png) | |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | Book Service | Your Account | Notes |
| --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/browsers/desk-chrome-home.png) | ![screenshot](documentation/browsers/desk-chrome-book-S.png) | ![screenshot](documentation/browsers/desk-chrome-user-A.png)| Works as expected |
| Firefox | ![screenshot](documentation/browsers/desk-fire-home.png) |  ![screenshot](documentation/browsers/desk-fire-book.png) | ![screenshot](documentation/browsers/desk-fire-user-a.png) | Works as expected |
| Safari | ![screenshot](documentation/browsers/desk-safari-home.png) | ![screenshot](documentation/browsers/desk-safari-book.png) | ![screenshot](documentation/browsers/desk-safari-user-a.png) | Minor CSS differences |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Home | Service | Book Service | User Account | Notes |
| --- | --- | --- | --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/responsiveness/Mob-home.jpeg) | ![screenshot](documentation/responsiveness/Mob-service.jpeg) | ![screenshot](documentation/responsiveness/Mob-book.jpeg) | ![screenshot](documentation/responsiveness/Mob-user-a.jpeg) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/responsiveness/Tab-home.png) | ![screenshot](documentation/responsiveness/Tab-service.png) | ![screenshot](documentation/responsiveness/Tab-book.png) | ![screenshot](documentation/responsiveness/Tab-user-a.png) | Works as expected |
| Desktop | ![screenshot](documentation/responsiveness/desk-chrome-home.png) | ![screenshot](documentation/responsiveness/Desk-service.png) | ![screenshot](documentation/responsiveness/desk-chrome-book-S.png) | ![screenshot](documentation/responsiveness/desk-chrome-user-A.png) | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/lighthouse/lighthouse-desk-home.png) | ![screenshot](documentation/lighthouse/lighthouse-mob-home.png) | Slow response time due to large images |
| Service | ![screenshot](documentation/lighthouse/lighthouse-desk-service.png) | ![screenshot](documentation/lighthouse/lighthouse-mob-sevice.png) | Some minor warnings |
| Add player | ![screenshot](documentation/lighthouse/lighthouse-desk-add-p.png) | ![screenshot](documentation/lighthouse/lighthouse-mob-add-p.png) | Some minor warnings |
| Book Service | ![screenshot](documentation/lighthouse/lighthouse-desk-book.png) | ![screenshot](documentation/lighthouse/lighthouse-mob-book.png) | Some minor warnings |

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| Home | | | | | |
| | Feature is expected to show a custom 404 page when a non-existent URL is accessed | Accessed a non-existent URL on the website | The custom 404 page was displayed as expected | Test concluded and passed | ![screenshot](documentation/defensive/404-t.png) |
| Register  | | | | | |
| | Feature is expected to prevent empty submission | Submitted an empty form | Form errors displayed for all fields: username, email, password | Test concluded and passed | ![screenshot](documentation/defensive/empty-def.png) |
| | Feature is expected to prevent invalid email submission | Submitted a form with an invalid email | Form error displayed for the email field | Test concluded and passed | ![screenshot](documentation/defensive/email-def.png) |
| Add Player | | | | | |
| | Feature is expected to prevent empty submission | Submitted an empty form | Form errors displayed for all fields | Test concluded and passed | ![screenshot](documentation/defensive/add-plyer-empty-def.png) |
| | Feature is expected to do prevent process when the player age isn’t between 8 and 15 | Tested the feature by input outrange age  | Error message displayed | Test concluded and passed | ![screenshot](documentation/defensive/age-def.png) |
| Edit player | | | | | |
| | Feature is expected to deny access when a user tries to edit a player belonging to another user | Attempted to edit a player belonging to another user | Displayed "Access Denied: You don't have permission to edit this player." and returned to home | Test concluded and passed | ![screenshot](documentation/defensive/edit-player-def.png) |

## User Story Testing

| User Story | Screenshot |
| --- | --- |
| As a parent, I can view available football training services so that I can choose one that fits my needs.| ![screenshot](documentation/features/service_listing.png) |
| As a parent, I can create an account so that I can manage my children for the football camp.| ![screenshot](documentation/features/user_registration.png) |
| As a parent, I can log in so that I can access my account and manage my profile. | ![screenshot](documentation/features/user_login.png) |
| As an admin, I can view all bookings so that I can manage and oversee the booking system efficiently. | ![screenshot](documentation/features/admin_booking_management.png) |
| As an admin, I can view all players so that I can monitor and manage the registrations of all users. | ![screenshot](documentation/features/admin_player_management.png) |
| As a Admin I can edit or delete existing services so that I can update the offerings as needed. | ![screenshot](documentation/features/admin_service_management.png) |
| As a admin I can create new services so that I can offer various training options to the children. | ![screenshot](documentation/features/admin-add-sevice.png) |
| As a parent, I can book services for my children so that they can attend training sessions and camps. | ![screenshot](documentation/features/desk-safari-book.png) |
| As a parent, I can add and manage player profiles so that I can register multiple children. | ![screenshot](documentation/features/account_management.png) |

## Bugs

- Django `DoesNotExist` at /book_service/ when trying to query a player**

    ![screenshot](documentation/bugs/bug01.png)

    - To fix this, I ensured that the query to fetch the player was correctly written and verified that the player exists in the database before attempting to fetch it. Specifically, I added error handling for the `DoesNotExist` exception to provide a more user-friendly message or redirect the user to a relevant page if the player does not exist.

- Django **`TypeError` at /admin_create_service/ when trying to create a service**

    ![screenshot](documentation/bugs/bug02.png)

    - To fix this, I checked the `Service` model definition to ensure that the field `name` exists and is correctly defined. I found that the `Service` model did not have a field named `name`. Therefore, I either corrected the field name in the model definition to match the expected keyword argument or updated the keyword argument in the view to match the actual field name in the `Service` model.


- Django `TemplateDoesNotExist` at /register/ when trying to load template

    ![screenshot](documentation/bugs/bug03.png)

    - To fix this, I ensured that the `registration/register.html` template exists in the correct directory. I verified the template path and created the missing template file in the `templates/registration/` directory if it was not already present. Additionally, I checked the `TEMPLATES` setting in `settings.py` to ensure it includes the correct directories.### GitHub.

- Django `Improper HTML rendering` at homepage when trying to display programs

    ![screenshot](documentation/bugs/bug04.png)

    - To fix this, I updated my template elements to include the `|safe` filter in Django to ensure that the HTML content is rendered correctly without escaping the HTML tags. This allowed the content to display as intended with the appropriate formatting and styling.

- Django `AttributeError` at /register/ when trying to access the profile attribute of a User object

    ![screenshot](documentation/bugs/bug05.png)

    - To fix this, I ensured that the `User` model has a related `Profile` model using a OneToOneField relationship. I verified that the `Profile` object is created whenever a `User` object is created. Additionally, I checked if the `User` object is being correctly referenced and accessed in the view or form where the error occurred.

- CSS `Improper checkbox rendering` for selecting services

    ![screenshot](documentation/bugs/bug06.png)

    - To fix this, I updated the CSS to ensure proper alignment and styling of the checkboxes and their labels. I added styles to adjust the margin, padding, and font size for better readability and visual appeal.

- Django `NameError` at /edit_booking/ when trying to access a URL that isn't mine

    ![screenshot](documentation/bugs/bug07.png)

    - To fix this, I imported `HttpResponseForbidden` in the `views.py` file and added a `django.messages.error` for user feedback.

## Unfixed Bugs
> [!NOTE]  
> There are no remaining bugs that I am aware of.
