init:
    define m = Character("MainCharacter",dynamic=True)
    define wybrana = "main1.png"

    image bg weeia = "weeia.jpg"
    image bg white = "white.png"
    
    define mainGirl1 = Image("main1.png")
    define mainGirl2 = Image("main2.png")
    define mainGirl3 = Image("main3.png")

    image narrator = "first_man.png"
    #image wybrana:
    #    choice (i == 1):
    #            "main1.png"
    #    choice (i == 2):
    #            "main2.png"
    #    choice (i == 3):
    #            "main3.png"

    define ob = Character("Obserwator", what_slow_cps=20)

    screen choices():
        hbox:
            imagebutton auto "main1_%s.png" action Jump("a")
            imagebutton auto "main2_%s.png" action Jump("b")
            imagebutton auto "main3_%s.png" action Jump("c")
    screen propozycje():
        vbox xalign 0.45 yalign 0.45:
            text "Popełniono za dużo błędów, \nwybierz sobie jedno z 3 przygotowanych przez nas" 
        hbox xalign 0.45 yalign 0.55:
            textbutton "Ania" action Jump("Ania")
            textbutton "Iza" action Jump("Iza")
            textbutton "Małgorzata" action Jump("Malgorzata")
    #init python:
    #    def wybor(numer):
    #        if numer == 1:
    #            renpy.image("wybrana",mainGirl1)
    #        if numer == 2:
    #            renpy.image("wybrana",mainGirl2)
    #        if numer == 3:
    #            renpy.image("wybrana",mainGirl3)
#---wyłącza to wszystkie dziwne rzeczy:
    $ config.keymap['skip'].remove('K_RCTRL')
    $ config.keymap['skip'].remove('K_LCTRL')
    $ config.keymap['toggle_skip'].remove('K_TAB')
    $ config.keymap['rollback'].remove('K_PAGEUP')
    $ config.keymap['rollback'].remove('repeat_K_PAGEUP')
    $ config.keymap['rollback'].remove('K_AC_BACK')
    $ config.keymap['rollback'].remove('mousedown_4')
    
label start:
    $ _game_menu_screen = None
    #zrobic wersje na androida
    #jump minigame_mat #zrobione
    #jump minigame_tpi #zrobione
    #jump minigame_prawo #zrobione
    #jump minigame_pp1 #zrobione
    #jump minigame_pe #zrobione
    #jump exams
    scene bg white

    show text "{color=#000000}Chapter 0\nStwórz swoją postać{/color}"
    with dissolve
    pause 2

    scene black
    play music "music/bensound-deepblue.ogg"
    voice "music/tutorial/1.ogg"
    "Halo? Jest tu kto?"
    #hide text
    voice "music/tutorial/2.ogg"
    "Poczekaj chwilę. Ktoś tu zgasił światło. O, chyba znalazłem!"
    #jump minigame_tpi
    scene bg white
    show narrator at left
    voice "music/tutorial/3.ogg"
    ob "Nareszcie ci się udało! Witaj! Pewnie masz do mnie sporo pytań?"
    menu:
        "Kim jesteś?":
            jump onelabel
        "Co to za miejsce?":
            jump onelabel
        "Kiedy rozpocznie się gra?":
            jump onelabel

    label onelabel:
        voice "music/tutorial/4.ogg"
        ob "Hmm... Zacznijmy może od początku. Możesz nazywać mnie obserwatorem. Jestem tu po to by wprowadzić Cię w ten świat
        i obserwować Twoje postępy. Witaj w Wonderful Time."
        voice "music/tutorial/5.ogg"
        ob "To może najpierw powiem na czym to bedzie polegac."
        voice "music/tutorial/6.ogg"
        ob "Ty mój drogi/moja droga (wybacz, nie wziąłem ze sobą okularów) będziesz mógł wcielić się w świeżo upieczoną studentkę informatyki oraz pokierować
        jej poczynani podczas tego szalonego okresu jakim jest studiowanie."
        voice "music/tutorial/7.ogg"
        ob "Wybierz sobie teraz jedną z trzech dostępnych w grze postaci."
        hide textbox
        hide narrator

        show screen choices
        pause 30

        label a:
            hide screen choices
            python:
                i = 1
            jump next
        label b:
            hide screen choices
            python:
                i = 2
            jump next
        label c:
            hide screen choices
            python:
                i = 3
            jump next
    label next:
        voice "music/tutorial/jakieimie.ogg"
        python:
            import names
            licznik = 0
            name = renpy.input("Jak ma się nazywać twoja studentka?")
            while(names.correct_name(name.encode('utf8')) == False and licznik < 2):
                name = renpy.input("Podanego imienia nie ma w bazie.\nJak ma się nazywać twoja studentka?")
                licznik = licznik + 1
        
        if licznik == 2:
            show screen propozycje
            pause 30
        jump next1

    label Ania:
        $ name = "Ania"
        jump next1
    label Iza:
        $ name = "Iza"
        jump next1
    label Malgorzata:
        $ name = "Małgorzata"
        jump next1

    label next1:
        hide screen propozycje
        if i == 1:
            $ m = Character(name, image="mainGirl1",what_slow_cps=20)
        elif i == 2:
            $ m = Character(name, image="mainGirl2",what_slow_cps=20)
        elif i == 3:
            $ m = Character(name, image="mainGirl3",what_slow_cps=20)
            #init python:
                #renpy.image("wybrana",mainGirl3)
        else:
            "cos poszlo nie tak"
            return
        show narrator at left
        voice "music/tutorial/8.ogg"
        ob "Posłuchaj mnie bardzo uważnie. Nasza [m] ma swoją historię i powody dla których zaczyna swoją przygodę z informatyką, ale to od Ciebie mój graczu zależy jak jej pójdzie."
        voice "music/tutorial/9.ogg"
        ob "Wykłady, stosunki z rówieśnikami, zabawy w akademiku, nauka i egzaminy... to wszystko jest w Twoich rękach. Za pomocą Twoich decyzji i postanowień ta rozgrywka i
        przygody naszej bohaterki będą coraz bardziej intrygujące."
        voice "music/tutorial/10.ogg"
        ob "Jakkolwiek zdecydujesz mam nadzieję, że [m] będzie szczęśliwa i zmotywowana do rozwijania samej siebie"
        voice "music/tutorial/11.ogg"
        ob "Nie przedłużajmy więc. Nasza bohaterka czeka na Ciebie. My pewnie się jeszcze zobaczymy. Wejdź do świata Wonderful Time."
        hide narrator
        #pokazywanie naszej studentki
        if i == 1:
            show main1
        elif i == 2:
            show main2
        elif i == 3:
            show main3

        m "Cześć, mam nadzieje, że będzie Ci się fajnie mną grało."
        m "Powodzenia."
        stop music
        jump chapter1
        return
