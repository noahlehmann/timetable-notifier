
def has_changes(html_response):
    no_content = 'keine Termine'
    return no_content.lower() not in html_response.lower()
