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


# do poprawy:

    -   PRZEBUDOWA SYSTEMU TŁUMACZEŃ NA WBUDOWANY W DJANGO:
        -after change django.po use command in terminal:
            django-admin compilemessages
        -sprawdzić możliwość dodawania własnych plików z tłumaczeniem oprócz django.po


    -estimated time wybierany z listy, a nie wpisywany

    -sprawdzić możliwość dodawania własnych plików z tłumaczeniem oprócz django.po

    -Rozdzielic tlumaczenia na 
        ~Ogolne
        ~Do szablonów autoryzacji
        ~Do szablonow bloga

    -ukryte pola wymagają wypełnienia. czy tworzyć posty wprowadzane bez lokalizacji?

    -tagi muszą być wprowadzone do tworzenia posta?

    -Na razie chyba zrobię żeby mi dzieliło zdjęcia na foldery przypisane do konkretnych postów, a później i tak będę 
    w tym jeszcze grzebał pewnie żeby ustawić wybieranie równego zdjęcia z kolekcji czy innych pierdółek. 
    Teraz chcę po prostu zarys zrobić żeby nie pozniej nie musiec zmieniac calej mechaniki jak już ją odbuduję.
    A przypisywanie zdjęć do miejsca też jest spoko pomysłem, może nie do katalogowania, 
    ale zrobienia filtrowania galerii wszystkich zdjęć pod względem miejsc które prezentują