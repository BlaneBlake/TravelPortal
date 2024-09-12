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
    estimated time wybierany z listy, a nie wpisywany
