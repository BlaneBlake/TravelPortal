# TravelPortal

# .env instruction:

    need .env file with:
        """
        DATABASE_PASS = 'database_password'
        DATABASE_NAME = 'database_name'
        DATABASE_USER = 'user_name'
        """

    how to apply:
        """
        import os
        from dotenv import load_dotenv
        
        load_dotenv()
        
        print(os.getenv('DATABASE_PASS'))
        """

# Installation of required programs
    in requirements.txt is every needed programs to install on server
    >> pip install -r requirements. txt 

# TextsMixin must be declared before View in another case texts doesn't work on site
    class ClassView(TextsMixin, LoginRequiredMixin, TemplateView):
        template_name = 'template.html'

# tags support via django-taggit library

# !!! on production server probably must change media files configuration, now it works in developer mode

# Translation system
    after change django.po, use command in terminal:
            django-admin compilemessages

# do poprawy:

    - PRZEBUDOWA SYSTEMU TŁUMACZEŃ NA WBUDOWANY W DJANGO:
        -sprawdzić możliwość dodawania własnych plików z tłumaczeniem oprócz django.po

    - POSTY:
        -estimated time  sprawdzić jak działają liczebniki w plkikach tłumaczeń

        -Poprawić dodawanie lokalizacji "widok na mapie" w szczegółach postu działa 
        tylko jeśli wpiszesz w wybierz na mapie, nie działa po ustawieniu pinezki

        -niech po wybraniu lokalizacji bedzie ustawiany jakiś place_name. 
        Obecnie ustawia None
        Brak pola w PostForm
    
        -ukryte pola wymagają wypełnienia.
            -(SOLVED) możliwe tworzenie bez lokalizacji (trzeba w js dodać wartości domyślne w razie niewybrania pola na mapie)
                (obecnie usstawiona wartość default przy niewidocznych polach w templatce),
            -niech puste pola zwracają komunikat "do uzupełnienia" w liście postów danego użytkownika
            -możliwość usuwania własnego posta po zalogowaniu (niech usuwa też zdjęcia i galerię)
            -możliwość edytowania własnego posta po zalogowaniu
    
    - GALERIA:

        -wybieranie main image w galerii (przy pomocy radioset)

        -możliwość edycji postu / usuwania i dodawania zdjec
    
        -dodać miniaturki zdjęć i po naciśnięciu na nie wyświetlać na cały ekran, 
        ale z ogranieczeniem do wielkości monitora