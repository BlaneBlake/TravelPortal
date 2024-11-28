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
        -estimated time wybierany z listy, a nie wpisywany. 
        na razie podanie 10:00 w formularzu daje 00:10:00 w poście

        -Poprawić dodawanie lokalizacji "widok na mapie" w szczegółach postu działa 
        tylko jeśli wpiszesz w wybierz na mapie, nie działa po ustawieniu pinezki
    
        -ukryte pola wymagają wypełnienia. czy tworzyć posty wprowadzane bez lokalizacji?
    
        -tagi muszą być wprowadzone do tworzenia posta? (usunąć tę konieczność)
    
    - GALERIA:
        -wybieranie main image w galerii (przy pomocy radioset)
    
        -dodać miniaturki zdjęć i po naciśnięciu na nie wyświetlać na cały ekran, 
        ale z ogranieczeniem do wielkości monitora

        -możliwość edycji postu / usuwania i dodawania zdjec