from behave import given, then, when
from time import sleep


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

@when('Click to profile menu')
def click_to_user_profile(context):
    context.app.main_page.click_to_user_profile()

@when('Enter email: {email}')
def update_user_email(context, email):
    context.app.main_page.update_user_email(email)

@when("Enter current password:{text}")
def input_curr_password_to_pass_fild(context, text):
    context.app.main_page.input_curr_password_to_pass_fild(text)

@when("Enter new password:{text}")
def input_new_password_to_pass_fild(context, text):
    context.app.main_page.input_new_password_to_pass_fild(text)


@when ('Click to save button')
def click_to_profile_save_btn(context):
    context.app.main_page.click_to_profile_save_btn()

@when ('Click to LogOut button')
def click_to_logout_btn(context):
    context.app.main_page.click_to_logout_btn()


@then ('Verify LogOut button present')
def verify_logout_btn(context):
    context.app.main_page.verify_Logout_btn()

@then ('Verify Home button present')
def verify_home_btn(context):
    context.app.main_page.verify_Home_btn()

@then ('Wait status logIn fail')
def wait_for_status_appear(context):
    context.app.main_page.wait_for_status_appear()

@then ('Waiting for the LogIn button to be active')
def wait_for_element_activ(context):
    context.app.main_page.wait_for_element_activ()

