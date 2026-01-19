class LoginPageLocators:
    USERNAME_INPUT = "input[name='username']"
    PASSWORD_INPUT = "input[name='password']"

    LOGIN_BUTTON = "button[type='submit']"
    LOGIN_FORGOT = "div[class='orangehrm-login-forgot']"

    LOGO = "img[alt='company-branding']"

    SIDE_LOGO = "div[class='orangehrm-login-logo']"

    USERNAME_REQUIRED_ERROR = (
        "div.oxd-input-group:has(label:text('Username')) "
        "span.oxd-input-field-error-message"
    )

    PASSWORD_REQUIRED_ERROR = (
        "div.oxd-input-group:has(label:text('Password')) "
        "span.oxd-input-field-error-message"
    )

    CRED_ALERT = "div[role='alert']"

