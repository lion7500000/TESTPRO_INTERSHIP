from behave import given, then, when
from time import sleep

@when ('User selects the theme "Violet" on Profile')
def Select_color(context):
    context.app.profile_page.click_color_violet()

@when ('User selects the theme "Rocky" on Profile')
def Select_color(context):
    context.app.profile_page.click_color_rocky()

@when ('User marks checkbox "Confirm before closing Koel"')
def mark_checkbox_confirm(context):
    context.app.profile_page.click_checkbox_confirm()

@then ('The frame appears')
def Verify_color(context):
    context.app.profile_page.wait_for_element_activ()