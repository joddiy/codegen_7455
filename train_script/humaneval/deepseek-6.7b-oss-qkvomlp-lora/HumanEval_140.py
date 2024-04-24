def fix_spaces(text):
    # Replace all spaces with underscores
    text = text.replace(' ', '_')
    
    # Replace consecutive spaces with -
    while '  ' in text:
        text = text.replace('  ', '-')
    
    return text