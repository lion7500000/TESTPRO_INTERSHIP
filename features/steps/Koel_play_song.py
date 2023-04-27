from behave import given, when, then

@when('Click to song "Dark Days"')
def click_to_song(context):
    context.app.main_page.click_song()

@when('Click to play music btn')
def click_play_btn(context):
    context.app.main_page.move_mouse_click_play_btn()

@then('Wait the sound bar')
def wait_toggle_btn(context):
    context.app.main_page.wait_for_sound_bar()


