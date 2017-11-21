init:
    define m = Character("MainCharacter")

    image weeia = "weeia.jpg"
    image bg white = "white.png"
    image side mainGirl1 = "main1.png"
    image side mainGirl2 = "main2.png"
    image side mainGirl3 = "main3.png"
    image side narrator = "first_man.png"

    define ob = Character("Obserwator", image="narrator")

    screen choices():
        hbox:
            imagebutton auto "main1_%s.png" action Jump("a")
            imagebutton auto "main2_%s.png" action Jump("b")
            imagebutton auto "main3_%s.png" action Jump("c")

label start:
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

            name = renpy.input("Jak ma się nazywać twoja studentka?")
            if not name:
                name = "Alicja"
        #Tu mozna to zapetlic jakos i wymusic "dobre imie"
        #trzeba zrobic blok if'a
        #bedzie tworzyl m w zaleznosci od i
        $ m = Character(name)
        #$ m = name
        if i == 1:
            $ m = Character(name, image="mainGirl1")
        elif i == 2:
            $ m = Character(name, image="mainGirl2")
        elif i == 3:
            $ m = Character(name, image="mainGirl3")
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

        m "Cześć, mam nadzieje, że będzie Ci się fajnie mną grało."
        m "Powodzenia."
        jump chapter1
        return
        #do tej pory bedzie, teraz jest to co sobie trenowałem:
        #gra muzyka: play music "hello.mp3"
        #wczytanie tła: scene weeia
        #pokazanie postaci po prawej stronie: show mainGirl at right
