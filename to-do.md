# do poprawy:

    ##- PRZEBUDOWA SYSTEMU TŁUMACZEŃ NA WBUDOWANY W DJANGO:
        -sprawdzić możliwość dodawania własnych plików z tłumaczeniem oprócz django.po

    ##- POSTY:
        -estimated time  sprawdzić jak działają liczebniki w plikach tłumaczeń

        -niech po wybraniu lokalizacji bedzie ustawiany jakiś place_name.
        Obecnie ustawia None
        Brak pola w PostForm

        -ukryte pola wymagają wypełnienia.
            -(SOLVED) możliwe tworzenie bez lokalizacji
                (obecnie ustawiona wartość default przy niewidocznych polach w template),
                (trzeba w js dodać wartości domyślne w razie niewybrania pola na mapie)
            - post z ustawioną lokalizacją na mapie w czasie edycji:
                wymaga kolejnego ustawienia lokalizacji
                niech wczytuje tą z bazy danych jeśli to możliwe

        -migrować na AdvancedMarkerElement

        -niech puste pola zwracają komunikat "do uzupełnienia" w liście postów danego użytkownika

        -możliwość usuwania własnego posta po zalogowaniu (niech usuwa też zdjęcia i galerię)



    ##- GALERIA:

        -SOLVED (do sprawdzenia po czasie)
            Poniższe po czyszczeniu bazy danych i media wstępnie działa i usuwa pliki z media
            sprawdzić po czasie
            -usuwanie zdjęć nie usuwa pliku zdjęcia z dysku, jedynie z bazy danych