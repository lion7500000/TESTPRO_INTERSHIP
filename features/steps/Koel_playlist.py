from behave import given, then, when

@when ('Move mose to sin "Create new playlist"')
def hover_to_create_new_pl(context):
    context.app.playlist_page.move_mouse_to_create_playlist()

@when ('Click to create new playlist')
def create_new_pl(context):
    context.app.playlist_page.click_create_new_playlist()

@when ('Click to menu new smart playlist')
def select_new_smart_playlist(context):
    context.app.playlist_page.click_smart_playlist_menu()

@when ('Enter smart playlist name {text}')
def enter_smart_pl_name(context,text):
    context.app.playlist_page.enter_name_smpl(text)

@when ('Select fist (model) rule "Title"')
def enter_smpl_rule_model(context):
    context.app.playlist_page.select_rul_title()

@when ('Select second (operator) rule "is"')
def enter_smpl_rule_operator(context):
    context.app.playlist_page.select_rul_operator()

@when ('Enter third (value) rule {text}')
def enter_smpl_rule_value(context, text):
    context.app.playlist_page.enter_rul_value(text)

@when ('Click to Playlist "SAVE" button')
def click_pl_save_btn(context):
    context.app.playlist_page.click_save_pl_btn()

@then ('Verify playlist {name} is created')
def verify_playlist_create(context, name):
    context.app.playlist_page.verify_playlist_create(name)
