def greet(language):
    language_database = [ 
        ("english", "Welcome"),
        ("czech", "Vitejte"),
        ("danish", "Velkomst"),
        ("dutch", "Welkom"),
        ("estonian", "Tere tulemast"),
        ("finnish", "Tervetuloa"),
        ("flemish", "Welgekomen"),
        ("french", "Bienvenue"),
        ("german", "Willkommen"),
        ("irish", "Failte"),
        ("italian", "Benvenuto"),
        ("latvian", "Gaidits"),
        ("lithuanian", "Laukiamas"),
        ("polish", "Witamy"),
        ("spanish", "Bienvenido"),
        ("swedish", "Valkommen"),
        ("welsh", "Croeso")
    ]
    
    
    if isinstance(language, str):
        language = language.lower()
    else:
        return "Welcome"  # Or you can handle it differently depending on the requirements
    
    for lang, greeting in language_database:
        if lang == language:
            return greeting
    
    return "Welcome"
