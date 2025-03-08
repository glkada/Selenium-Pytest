class AuthPage:
    login = "//button[span='Login'][1]"
    register = "//button[span='Register'][1]"
    username = "//label[text()='Email'][2]//following-sibling::input"
    password = "//label[text()='Password'][2]//following-sibling::input"
    submit_login_creds = "//form/button[span=' Login ']"
    submit_registration_creds = "//form/button[span=' Register ']"
    home_btn = "//button[span='Home']"
    login_status_snackbar = "//div[@class='v-snackbar__content']"