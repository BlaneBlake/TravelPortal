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
            -(SOLVED) możliwe tworzenie bez lokalizacji 
                (obecnie usstawiona wartość default przy niewidocznych polach w templatce),
                (trzeba w js dodać wartości domyślne w razie niewybrania pola na mapie)
            - post z ustawioną lokalizacją na mapie w czasie edycji:
                wymaga kolejnego ustawienia lokalizacji
                niech wczytuje tą z bazy danych jeśli to możliwe
 
        -niech puste pola zwracają komunikat "do uzupełnienia" w liście postów danego użytkownika
        -możliwość usuwania własnego posta po zalogowaniu (niech usuwa też zdjęcia i galerię)
        
        

    - GALERIA:

        -przy tworzeniu miniatur zachować ich proporcje, nadac tylko max szerokość np
 
        -po naciśnięciu na nie wyświetlać na cały ekran, ale z ogranieczeniem do wielkości monitora


    -SOLVED (do sprawdzenia po czasie)
        Poniższe po czyszczeniu bazy danych i media wstępnie działa i usuwa pliki z media
        sprawdzić po czasie
        -usuwanie zdjęć nie usuwa pliku zdjęcia z dysku, jedynie z bazy danych
        -dodawanie zdjęć zapisanych na serwerze do wyświetlania w poście jeśli nie ma.
        -pernamentne usuwanie zdjęć z serwera na etapie edytowania zawartości bazy danych.