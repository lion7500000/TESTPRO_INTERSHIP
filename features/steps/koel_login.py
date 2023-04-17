from behave import given, then, when


@given('Open Koel Log In Page')
def open_logIn_page(context):
    context.app.main_page.open_page()


@when('Input {email} to email field')
def enter_email_to_fild(context, email):
    context.app.main_page.enter_email(email)


@when('Iput {password} to password field')
def enter_pw_to_fild(context, password):
    context.app.main_page.enter_pw(password)


@when("Click to LogIn button")
def click_logIn_btn(context):
    context.app.main_page.click_LogIn_btn()

@then ('Verify LogOut button present')
def verify_logout_btn(context):
    context.app.main_page.verify_Logout_btn()
