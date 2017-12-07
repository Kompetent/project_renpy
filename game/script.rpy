init:
    define m = Character("MainCharacter",dynamic=True)
    define wybrana = "main1.png"
    #minigra_tpi może być
    image bg weeia = "weeia.jpg"
    image bg white = "white.png"
    
    define mainGirl1 = Image("main1.png")
    define mainGirl2 = Image("main2.png")
    define mainGirl3 = Image("main3.png")

    image side narrator = "first_man.png"
    #image wybrana:
    #    choice (i == 1):
    #            "main1.png"
    #    choice (i == 2):
    #            "main2.png"
    #    choice (i == 3):
    #            "main3.png"

    define ob = Character("Obserwator", image="narrator")

    screen choices():
        hbox:
            imagebutton auto "main1_%s.png" action Jump("a")
            imagebutton auto "main2_%s.png" action Jump("b")
            imagebutton auto "main3_%s.png" action Jump("c")
    #init python:
    #    def wybor(numer):
    #        if numer == 1:
    #            renpy.image("wybrana",mainGirl1)
    #        if numer == 2:
    #            renpy.image("wybrana",mainGirl2)
    #        if numer == 3:
    #            renpy.image("wybrana",mainGirl3)

label start:
    #jump minigame_pp1
    scene bg white

    show text "{color=#000000}Chapter 0\nStwórz swoją postać{/color}"
    with dissolve
    pause 2

    scene black
    #play sound "music/hello.mp3"
    voice "music/tutorial/1.ogg"
    "Halo? Jest tu kto?"
    #hide text
    voice "music/tutorial/2.ogg"
    "Poczekaj chwilę. Ktoś tu zgasił światło. O, chyba znalazłem!"
    #jump minigame_tpi
    scene bg white
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

            name = renpy.input("Jak ma się nazywać twoja studentka?")
            while(names.correct_name(name.encode('utf8')) == False):
                name = renpy.input("Podanego imienia nie ma w bazie.\nJak ma się nazywać twoja studentka?")

        if i == 1:
            $ m = Character(name, image="mainGirl1")
        elif i == 2:
            $ m = Character(name, image="mainGirl2")
        elif i == 3:
            $ m = Character(name, image="mainGirl3")
            #init python:
                #renpy.image("wybrana",mainGirl3)
        else:
            "cos poszlo nie tak"
            return

        voice "music/tutorial/8.ogg"
        ob "Posłuchaj mnie bardzo uważnie. Nasza [m] ma swoją historię i powody dla których zaczyna swoją przygodę z informatyką, ale to od Ciebie mój graczu zależy jak jej pójdzie."
        voice "music/tutorial/9.ogg"
        ob "Wykłady, stosunki z rówieśnikami, zabawy w akademiku, nauka i egzaminy... to wszystko jest w Twoich rękach. Za pomocą Twoich decyzji i postanowień ta rozgrywka i
        przygody naszej bohaterki będą coraz bardziej intrygujące."
        voice "music/tutorial/10.ogg"
        ob "Jakkolwiek zdecydujesz mam nadzieję, że [m] będzie szczęśliwa i zmotywowana do rozwijania samej siebie"
        voice "music/tutorial/11.ogg"
        ob "Nie przedłużajmy więc. Nasza bohaterka czeka na Ciebie. My pewnie się jeszcze zobaczymy. Wejdź do świata Wonderful Time."
        
        #pokazywanie naszej studentki
        if i == 1:
            show main1
        elif i == 2:
            show main2
        elif i == 3:
            show main3

        m "Cześć, mam nadzieje, że będzie Ci się fajnie mną grało."
        m "Powodzenia."
        jump chapter1
        return
