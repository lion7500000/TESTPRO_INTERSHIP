from behave import given, then, when


@when ('Input serch text {text} in search fild')
def input_search_text(context, text):
    context.app.main_page.input_text_to_serch_fild(text)

@then ('Verify search text {text} is present')
def verify_search_text_in(context, text):
    context.app.search_page.verify_search_text(text)

@then ('Verify search Artist {text} is present')
def verify_search_text_in(context, text):
    context.app.search_page.verify_artist_search_text(text)

@then ('Verify search Artist {text}')
def verify_serch_text_not_found(context, text):
    context.app.search_page.verify_artist_in_text(text)


