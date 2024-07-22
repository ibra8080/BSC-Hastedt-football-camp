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

## Automated Testing

I have conducted a series of automated tests on my application.

I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### JavaScript (Jest Testing)

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Adjust the code below (file names, etc.) to match your own project files/folders.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

I have used the [Jest](https://jestjs.io) JavaScript testing framework to test the application functionality.

In order to work with Jest, I first had to initialize NPM.

- `npm init`
- Hit `enter` for all options, except for **test command:**, just type `jest`.

Add Jest to a list called **Dev Dependencies** in a dev environment:

- `npm install --save-dev jest`

**IMPORTANT**: Initial configurations

When creating test files, the name of the file needs to be `file-name.test.js` in order for Jest to properly work.

Without the following, Jest won't properly run the tests:

- `npm install -D jest-environment-jsdom`

Due to a change in Jest's default configuration, you'll need to add the following code to the top of the `.test.js` file:

```js
/**
 * @jest-environment jsdom
 */

const { test, expect } = require("@jest/globals");
const { function1, function2, function3, etc. } = require("../script-name");

beforeAll(() => {
    let fs = require("fs");
    let fileContents = fs.readFileSync("index.html", "utf-8");
    document.open();
    document.write(fileContents);
    document.close();
});
```

Remember to adjust the `fs.readFileSync()` to the specific file you'd like you test.
The example above is testing the `index.html` file.

Finally, at the bottom of the script file where your primary scripts are written, include the following at the bottom of the file.
Make sure to include the name of all of your functions that are being tested in the `.test.js` file.

```js
if (typeof module !== "undefined") module.exports = {
    function1, function2, function3, etc.
};
```

Now that these steps have been undertaken, further tests can be written, and be expected to fail initially.
Write JS code that can get the tests to pass as part of the Red-Green refactor process.

Once ready, to run the tests, use this command:

- `npm test`

**NOTE**: To obtain a coverage report, use the following command:

- `npm test --coverage`

Below are the results from the tests that I've written for this application:

| Test Suites | Tests | Screenshot |
| --- | --- | --- |
| 1 passed | 16 passed | ![screenshot](documentation/tests/js-test-coverage.png) |
| x | x | repeat for all remaining tests |

#### Jest Test Issues

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Use this section to list any known issues you ran into while writing your Jest tests.
Remember to include screenshots (where possible), and a solution to the issue (if known).

This can be used for both "fixed" and "unresolved" issues.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

### Python (Unit Testing)

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Adjust the code below (file names, etc.) to match your own project files/folders.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

I have used Django's built-in unit testing framework to test the application functionality.

In order to run the tests, I ran the following command in the terminal each time:

`python3 manage.py test name-of-app`

To create the coverage report, I would then run the following commands:

`pip3 install coverage`

`pip3 freeze --local > requirements.txt`

`coverage run --omit=*/site-packages/*,*/migrations/*,*/__init__.py,env.py manage.py test`

`coverage report`

To see the HTML version of the reports, and find out whether some pieces of code were missing, I ran the following commands:

`coverage html`

`python3 -m http.server`

Below are the results from the various apps on my application that I've tested:

| App | File | Coverage | Screenshot |
| --- | --- | --- | --- |
| Bag | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-bag-forms.png) |
| Bag | test_models.py | 89% | ![screenshot](documentation/tests/py-test-bag-models.png) |
| Bag | test_urls.py | 100% | ![screenshot](documentation/tests/py-test-bag-urls.png) |
| Bag | test_views.py | 71% | ![screenshot](documentation/tests/py-test-bag-views.png) |
| Checkout | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-checkout-forms.png) |
| Checkout | test_models.py | 89% | ![screenshot](documentation/tests/py-test-checkout-models.png) |
| Checkout | test_urls.py | 100% | ![screenshot](documentation/tests/py-test-checkout-urls.png) |
| Checkout | test_views.py | 71% | ![screenshot](documentation/tests/py-test-checkout-views.png) |
| Home | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-home-forms.png) |
| Home | test_models.py | 89% | ![screenshot](documentation/tests/py-test-home-models.png) |
| Home | test_urls.py | 100% | ![screenshot](documentation/tests/py-test-home-urls.png) |
| Home | test_views.py | 71% | ![screenshot](documentation/tests/py-test-home-views.png) |
| Products | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-products-forms.png) |
| Products | test_models.py | 89% | ![screenshot](documentation/tests/py-test-products-models.png) |
| Products | test_urls.py | 100% | ![screenshot](documentation/tests/py-test-products-urls.png) |
| Products | test_views.py | 71% | ![screenshot](documentation/tests/py-test-products-views.png) |
| Profiles | test_forms.py | 99% | ![screenshot](documentation/tests/py-test-profiles-forms.png) |
| Profiles | test_models.py | 89% | ![screenshot](documentation/tests/py-test-profiles-models.png) |
| Profiles | test_urls.py | 100% | ![screenshot](documentation/tests/py-test-profiles-urls.png) |
| Profiles | test_views.py | 71% | ![screenshot](documentation/tests/py-test-profiles-views.png) |
| x | x | x | repeat for all remaining tested apps/files |

#### Unit Test Issues

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Use this section to list any known issues you ran into while writing your unit tests.
Remember to include screenshots (where possible), and a solution to the issue (if known).

This can be used for both "fixed" and "unresolved" issues.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

## Bugs

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

This section is primarily used for JavaScript and Python applications,
but feel free to use this section to document any HTML/CSS bugs you might run into.

It's very important to document any bugs you've discovered while developing the project.
Make sure to include any necessary steps you've implemented to fix the bug(s) as well.

**PRO TIP**: screenshots of bugs are extremely helpful, and go a long way!

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

- JS Uncaught ReferenceError: `foobar` is undefined/not defined

    ![screenshot](documentation/bugs/bug01.png)

    - To fix this, I _____________________.

- JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).

    ![screenshot](documentation/bugs/bug02.png)

    - To fix this, I _____________________.

- Python `'ModuleNotFoundError'` when trying to import module from imported package

    ![screenshot](documentation/bugs/bug03.png)

    - To fix this, I _____________________.

- Django `TemplateDoesNotExist` at /appname/path appname/template_name.html

    ![screenshot](documentation/bugs/bug04.png)

    - To fix this, I _____________________.

- Python `E501 line too long` (93 > 79 characters)

    ![screenshot](documentation/bugs/bug04.png)

    - To fix this, I _____________________.

### GitHub **Issues**

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

An improved way to manage bugs is to use the built-in **Issues** tracker on your GitHub repository.
To access your Issues, click on the "Issues" tab at the top of your repository.
Alternatively, use this link: https://github.com/ibra8080/BSC-Hastedt-football-camp/issues

If using the Issues tracker for your bug management, you can simplify the documentation process.
Issues allow you to directly paste screenshots into the issue without having to first save the screenshot locally,
then uploading into your project.

You can add labels to your issues (`bug`), assign yourself as the owner, and add comments/updates as you progress with fixing the issue(s).

Once you've sorted the issue, you should then "Close" it.

When showcasing your bug tracking for assessment, you can use the following format:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

**Fixed Bugs**

[![GitHub issue custom search](https://img.shields.io/github/issues-search?query=repo%3Aibra8080%2FBSC-Hastedt-football-camp%20label%3Abug&label=bugs)](https://github.com/ibra8080/BSC-Hastedt-football-camp/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

All previously closed/fixed bugs can be tracked [here](https://github.com/ibra8080/BSC-Hastedt-football-camp/issues?q=is%3Aissue+is%3Aclosed).

| Bug | Status |
| --- | --- |
| [JS Uncaught ReferenceError: `foobar` is undefined/not defined](https://github.com/ibra8080/BSC-Hastedt-football-camp/issues/1) | Closed |
| [Python `'ModuleNotFoundError'` when trying to import module from imported package](https://github.com/ibra8080/BSC-Hastedt-football-camp/issues/2) | Closed |
| [Django `TemplateDoesNotExist` at /appname/path appname/template_name.html](https://github.com/ibra8080/BSC-Hastedt-football-camp/issues/3) | Closed |

**Open Issues**

[![GitHub issues](https://img.shields.io/github/issues/ibra8080/BSC-Hastedt-football-camp)](https://github.com/ibra8080/BSC-Hastedt-football-camp/issues)
[![GitHub closed issues](https://img.shields.io/github/issues-closed/ibra8080/BSC-Hastedt-football-camp)](https://github.com/ibra8080/BSC-Hastedt-football-camp/issues?q=is%3Aissue+is%3Aclosed)

Any remaining open issues can be tracked [here](https://github.com/ibra8080/BSC-Hastedt-football-camp/issues).

| Bug | Status |
| --- | --- |
| [JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).](https://github.com/ibra8080/BSC-Hastedt-football-camp/issues/4) | Open |
| [Python `E501 line too long` (93 > 79 characters)](https://github.com/ibra8080/BSC-Hastedt-football-camp/issues/5) | Open |

## Unfixed Bugs

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

You will need to mention unfixed bugs and why they were not fixed.
This section should include shortcomings of the frameworks or technologies used.
Although time can be a big variable to consider, paucity of time and difficulty understanding
implementation is not a valid reason to leave bugs unfixed.

If you've identified any unfixed bugs, no matter how small, be sure to list them here.
It's better to be honest and list them, because if it's not documented and an assessor finds the issue,
they need to know whether or not you're aware of them as well, and why you've not corrected/fixed them.

Some examples:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

- On devices smaller than 375px, the page starts to have `overflow-x` scrolling.

    ![screenshot](documentation/bugs/unfixed-bug01.png)

    - Attempted fix: I tried to add additional media queries to handle this, but things started becoming too small to read.

- For PP3, when using a helper `clear()` function, any text above the height of the terminal does not clear, and remains when you scroll up.

    ![screenshot](documentation/bugs/unfixed-bug02.png)

    - Attempted fix: I tried to adjust the terminal size, but it only resizes the actual terminal, not the allowable area for text.

- When validating HTML with a semantic `section` element, the validator warns about lacking a header `h2-h6`. This is acceptable.

    ![screenshot](documentation/bugs/unfixed-bug03.png)

    - Attempted fix: this is a known warning and acceptable, and my section doesn't require a header since it's dynamically added via JS.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

If you legitimately cannot find any unfixed bugs or warnings, then use the following sentence:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

> [!NOTE]  
> There are no remaining bugs that I am aware of.
