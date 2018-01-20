init:
    define marta = Character("Marta",what_slow_cps=20)
    define ikar = Character("Ikar",what_slow_cps=20)
    define teresa = Character("Teresa",what_slow_cps=20)
    define Izabella = Character("Pan dr",what_slow_cps=20)
    image bg park = "park2.jpg"
    image bg dziekanat = "dziekanat.jpg"

    image stud1 = "noname1.png"
    image stud2 = "noname2.png"
    image ikar = "pan2.png"
    image teresa = "pani1.png"
    image iza = "pan3.png"
    image dziekan casual = "dziekan casual.png"
    image marta = "kumpela.png"

label chapter2: #DONE
    scene black
    show text "{color=#FFF}{size=+30}Chapter 2\nPierwszy tydzień zajęć{/size}{/color}"
    pause 2
    #==================nowa_scena==================
    scene black
    show text "{color=#FFF}{size=+30}Poniedziałek{/size}{/color}"
    pause 2
    #==================nowa_scena==================
    show bg miasto
    play music "music/bensound-sweet.ogg"
    #pokazywanie naszej studentki
    if i == 1:
        show main1
    elif i == 2:
        show main2
    elif i == 3:
        show main3
    m "Kurde....mam nadzieję, że się nie spóźnię! Kto wymyslił zajęcia w poniedziałek na 8 rano?"
    m "Obym tylko zdążyła. Jeszcze tego by brakowało, żeby ta zołza śmiała się ze mnie z powodu spóźnienia."
    m "Co ja biedna myślałam, by dać się wrobić w ten nieszczęsny zakład. Czyżbym nie potrafiła panować nad swoimi emocjami?"
    m "Nie dam jej satysfakcji. Nie będę reagować na jej zaczepki. Pokonam ją i udowodnię, że nie potrzeba być z wielkiego 
    domu by radzić sobie w życiu."
    #==================nowa_scena==================
    scene bg a123
    if i == 1:
        show main1
    elif i == 2:
        show main2
    elif i == 3:
        show main3
    m "No nareszcie. Zdążyłam na styk. Biegusiem do sali wykładowej."
    if i == 1:
        hide main1
    elif i == 2:
        hide main2
    elif i == 3:
        hide main3
    $ opiekunroku = Character("prof. dr hab. Matylda Kostrzewska",what_slow_cps=20)
    show opiekun:
        xpos 200
    play music "music/bensound-jazzcomedy.ogg"
    opiekunroku "Witajcie, moi mili. Pozwólcie, że przedstawię się tym, których nie było na immatrykulacj. Nazywam się 
    Matylda Kostrzewska i będę miała z wami Podstawy Programowania."
    opiekunroku "Zasady zaliczenia przedmiotu są proste. Na każdych zajęciach(nie licząc tych) będzie króciutka 
    kartkówka z ostatniego wykładu. Łącznie będzie ich 4."
    opiekunroku "Jeżeli będziecie mieli minimum 2 zaliczone to będziecie mogli podejść do egzaminu. W przeciwnym razie 
    będziecie musieli ten przedmiot powtarzać."
    hide opiekun
    show stud1 at left
    "Student1" "To niemożliwe! Kto wymyślał te zasady?"
    show stud2 at right
    "Student2" "To nie do pomyślenia. Jesteśmy dopiero na pierwszym semestrze..."
    hide stud1
    hide stud2
    show opiekun:
        xpos 200
    opiekunroku "Widzę, że nieszczególnie cieszycie się z tych reguł. Uwierzcie mi, że są one tylko da waszego dobra. 
    Chodzi o motywację!"
    opiekunroku "Umiejętność programowania jest najważniejsza dla informatyka. Dlatego chcę żebyście przyłożyli się 
    do nauki tego przedmiotu. Tutaj nie ma miejsca dla leniów."
    hide opiekun
    if i == 1:
        show main1
    elif i == 2:
        show main2
    elif i == 3:
        show main3
    m "No i to rozumiem. To jest konkretna kobieta. Mam nadzieję, że dużo się od niej nauczę."
    if i == 1:
        hide main1
    elif i == 2:
        hide main2
    elif i == 3:
        hide main3
    show opiekun:
        xpos 200
    opiekunroku "Nie martwcie się na zapas. Postaram się z wami wszystko na spokojnie przerobić. Głęboko wierzę, 
    że każde z was sobie poradzi."
    opiekunroku "Na dzisiejszych zajęciach zrobimy wstęp do języka C. Edukację w dziedzinie programowania najlepiej 
    zacząć właśnie od niego albo Pascala. Na tej uczelni jednak uważamy, że język C lepiej was przygotuje do dalszej 
    przygody z programowaniem."
    opiekunroku "No to zaczynamy zajęcia!"
    #==================nowa_scena==================
    scene black
    show text "{color=#FFF}{size=+30}temat lekcji: historia i cechy jezyka C, typy zmiennych, podstawy algorytmow-grafy, \nhello world, wprowadzanie danych, instrukcja IF{/size}{/color}"
    pause 5
    hide text
    #==================nowa_scena==================
    show bg korytarz
    if i == 1:
        show main1:
            xpos 300
    elif i == 2:
        show main2:
            xpos 300
    elif i == 3:
        show main3:
            xpos 300
    play music "music/bensound-scifi.ogg"
    m "Wow...to był potężny wykład. Widać kobieta ma pasję do programowania. To się ceni."
    show draco:
        xpos 700
    malfoy "Hej, Kowalska! Jak tam po pierwszym wykładzie? Już nie dajesz sobie rady?"
    menu:
        "Rozmawiaj":
            m "Widzę, że się bardzo o mnie martwisz. Niepotrzebnie. Nie mogłabym być gorsza od kogoś takiego jak ty!"
            malfoy "Hahahahaha. Gadkę to ty masz niezłą. Oby twoje wyniki były takie same."
            jump wybor12
        "Spław ją":
            m "Daj mi spokój kobieto.  Nie chcę mi się z tobą gadać."
            malfoy "Hahhaha.  Chyba jednak coś jest na rzeczy. Zaczynam wygrywać a nawet się nie staram."
            jump wybor12
    #(odglos chodu)
    label wybor12:
        m "Ta kobieta zawsze musi mi psuć humor. Ehh...dobra wracam do domu. Muszę się odstresować. "
        m "Ciężko mi się będzie z kimś zakumplować, jeżeli ona wciąż będzie to robić. Niech ten zakład już się skończy..."
    #==================nowa_scena==================
    scene black
    show text "{color=#FFF}{size=+30}Wtorek{/size}{/color}"
    pause 2
    #==================nowa_scena==================
    scene bg park
    play music "music/bensound-sweet.ogg"
    if i == 1:
        show main1
    elif i == 2:
        show main2
    elif i == 3:
        show main3
    m "Przynajmniej zajęcia nie są na 8 rano. Spokojnie sobie dotrę na zajęcia."
    m "Podstawy elektroniki, he. Pamiętam tylko, że na fizyce miałam rzeczy z prądu elektrycznego, ale to tyle. 
    Nie wiem, czy będzie mi to potrzebne do życia."
    m "Może w następnych semestrach będziemy projektować i programować układy elektroniczne? Nie byłam nigdy 
    dobra w robótkach ręcznych. Oj będzie ciężko."
    m "Pamiętaj to co ci powiedział kiedyś tata."
    #==================nowa_scena==================
    scene bg pokoj
    play music "music/bensound-memories.ogg"
    show father:
        xpos 200
    o "Nie ważne co będzie w przyszłości. Skup się na tym co tu i teraz. Reszta przyjdzie w swoim czasie."
    m "Mój tata mógłby pisać książki z mądrościami w stylu Paulo Coelho. Dobra, wchodzimy."
    #==================nowa_scena==================
    #(jezeli da rade to dobre bylyby tu drzwi w tle, jak je nacisniesz to otwieraja sie i pojawia sie tlo uczelni)
    scene bg korytarz
    #m "Za dużo się nie nachodzę. Sala jest dosyć blisko."
    show dziekan casual: #casual:
        xpos 200
    show draco:
        xpos 800
    play music "music/bensound-thejazzpiano.ogg"
    dziekan "Z moim zdrowiem wszystko w porządku. Lepiej mi powiedz co słychać u Andrzeja?"
    malfoy "Och, z tatą wszystko dobrze. Obecnie pojechał na tygodniową delegację do Tokio. Jego firma otwiera się 
    na rynek wschodni. W ciągu 5 lat planowane jest stworzenie trzech oddziałów w Japonii."
    dziekan "Hahahaha, cały Andrzej. Zawsze wiedziałem, że ma głowę do interesów. Bill Gates Europy Wschodniej. Trochę 
    brakuje mi go na uczelni, ale skoro realizuje się jako przedsiębiorca i promuje nasz wspaniały kraj za granicą to 
    mogę mu tylko życzyć powodzenia."
    malfoy "Na pewno przekażę mu te słowa. Ucieszy się, że go tu pamiętają."
    dziekan "Oczywiście, że pamiętam. Jego firma po części finansuje naszą uczelnię. Dzieki niemu w tym roku otworzyliśmy 5 
    zaawansowanych pracowni.  Złoty człowiek z niego."
    dziekan "O, to już ta godzina. Trzeba już zacząć zajęcia. Wchodzimy, studenciaki, Wchodzimy, hehehe."
    hide dziekan casual
    if i == 1:
        show main1:
            xpos 200
    elif i == 2:
        show main2:
            xpos 200
    elif i == 3:
        show main3:
            xpos 200
    play music "music/bensound-scifi.ogg"
    m "Oho, dodatkowo jej ojciec jest sponsorem. Naprawdę szkoda, że nie dostałam się do [love_u]."
    malfoy "No co, wieśniaro. Masz jakiś problem?"
    menu:
        "reagujesz":
            m "Żaden. Patrzę z politowaniem na twój wielce zadufany nos. Jeszcze więcej wywyższania się i osiągnie 
            on rozmiary piłki tenisowej."
            malfoy "Grrr....jesteś mocna tylko w gębie. Daruj sobie riposty i bardziej skup się na nauce."
            m "Haha. Nie umiesz odszczekać, więc punkt idzie do mnie. Wchodźmy do sali. Jeżeli masz mnie pokonać to lepiej byś uważała na zajęciach."
            malfoy "..."
            jump w13
        "idziesz do sali":
            m "..."
            malfoy "Muszę ci jakiś pseudonim wymyślić. Nie możesz mnie ciągle ignorować, hahaha."
            jump w13
    #(tlo sali wykladowej)
    #==================nowa_scena==================
label w13:
    play music "music/bensound-thejazzpiano.ogg"
    scene bg a128
    show dziekan casual at left
    dziekan "Witajcie, drodzy studenci. My się już znamy (a na pewno Ci co byli na inauguracji hehehe) ale przedstawię 
    się wam jeszcze raz. Nazywam się Stanisław Meister i będę miał z Wami w tym semestrze zajęcia z Podstaw elektroniki."
    $ dziekan = Character("prof. dr hab. Stanisław Meister",what_slow_cps=20)
    hide dziekan casual
    show stud1:
        xpos 200
    "Student1" "Z wielką szychą mamy te zajęcia. Będzie ciekawie."
    show stud2:
        xpos 800
    "Student2" "O czym ty mówisz?"
    "Student1" "Widać, że mało cię obchodzi świat zawodowy, ziom. Ekipa Meistera ma na swoim koncie wiele interesujących patentów. 
    Z tego co słyszałem to sam Meister pomagał przy tworzeniu niebieskiego laseru."
    "Student3" "Wow, to niesamowite. Ta uczelnia ma dużo ciekawych ludzi. Czym się obecnie zajmują."
    "Student1" "Z tego co pamiętam, to pracują nad własnym procesorem grafenowym, jako odpowiedź na procesor IBMu."
    "Student2" "Tacy ludzie tylko inspirują do większego zaangażowania się w naukę..."
    hide stud1
    hide stud2
    show dziekan casual at left
    dziekan "Zapewne wielu z was zastanawia się po co ten kierunek ma taki przedmiot. Być może traktują go jako wypełniacz 
    albo sposób na ograniczenie listy studentów."
    dziekan "Ci, którzy tak myślą są oczywiście w błędzie. Informatyka jest bardzo szeroką dziedziną. Każdy z was na pewnym 
    etapie zdcecyduje w jakim kierunku będzie się dalej kształcić, ale nauka podstaw Wam pomoże."
    dziekan "Dzięki takim przedmiotom jak ten będziecie mogli zdecydować co was bardziej rajcuje w informatyce. Osobiście też 
    uważam, że znajomość podstaw elektroniki jest obowiązkowa dla tych co z nią pracują."
    dziekan "Nie martwcie się też o poziom trudności. Dopiero na odpowiednich specjalizacjach bardziej się zagłębicie w ten 
    temat. Dlatego radziłbym wam na spokojnie podejść do tego przedmiotu."
    dziekan "Zasady zaliczenia są proste: nie robię żadnych kartkówek w trakcie wykładu. Istnieje tylko jedno kolokwium na koniec 
    semestru. Tylko te rzeczy co będą na wykładzie. Nie wymagam od was nadprogramowej wiedzy. To dopiero pierwszy semestr."
    hide dziekan casual
    if i == 1:
        show main1
    elif i == 2:
        show main2
    elif i == 3:
        show main3
    m "Widać, że człowiek jest konkretny i rozumiejący studentów. Już mi się to podoba."
    if i == 1:
        hide main1
    elif i == 2:
        hide main2
    elif i == 3:
        hide main3
    show dziekan casual at left
    dziekan "Dodatkowo będę sprawdzał obecność na wykładzie. Jeśli będziecie mieli obecność na wszystkich to automatycznie 3. 
    Ci, którzy chcą wyższą ocenę lub lubią dłużej pospać będą musieli napisać kolokwium."
    hide dziekan casual
    show stud1:
        xpos 200
    "Student1" "O kurde, ale super. Pochodzę na wykłady i ideolo. Trójeczka murowana!"
    hide stud1
    show dziekan casual at left
    dziekan "Jest tylko mały haczyk. Jeśli podejdziecie do kolokwium to ta gwarantowana trójka zanika. Jeżeli nie zaliczycie 
    kolokwium do dostajecie 2 zamiast 3."
    hide dziekan casual
    show stud1:
        xpos 200
    "Student2" "Jejku, teraz tak trochę odechciało mi się walczyć o więcej."
    hide stud1
    if i == 1:
        show main1
    elif i == 2:
        show main2
    elif i == 3:
        show main3
    m "Hmm...zastanawiam się jak powinnam postąpić. No nic, pomyślę o tym później."
    if i == 1:
        hide main1
    elif i == 2:
        hide main2
    elif i == 3:
        hide main3
    show dziekan casual at left
    dziekan "Robię to z tego powodu, że chcę Was czegoś dodatkowego nauczyć. Jeśli chcecie wyjść poza tłum zawsze narażacie 
    się na pewne ryzyko. Musicie umieć oceniać swoje możliwości. To wam się przyda w dorosłym życiu."
    hide dziekan casual
    if i == 1:
        show main1
    elif i == 2:
        show main2
    elif i == 3:
        show main3
    m "To rzeczywiście ma sens. Ten Meister dobrze sobie to przemyślał. Widać, że zależy mu na nas..."
    if i == 1:
        hide main1
    elif i == 2:
        hide main2
    elif i == 3:
        hide main3
    show dziekan casual at left
    dziekan "Będziecie zadowoleni z tego co macie, czy wyjdziecie ze swojej strefy komfortu i spróbujecie osiągnąć coś więcej. 
    Ambicja to niebezpieczna rzecz. Trzeba z nią uważać. Ci, którzy to potrafią, osiągną wiele w życiu."
    dziekan "Wybaczcie, że się tak zagadałem. No nic, zacznijmy prawdziwe zajęcia."
    #---------------------------------------dodokonczenia-------------------------------------------------------------
    #==================nowa_scena==================
    #(zdjecie korytarza)
    scene black
    show text "{color=#FFF}{size=+30}Wstępne omówienie programu PSpice{/size}{/color}"
    pause 2
    play music "music/bensound-rumble.ogg"
    scene bg korytarz
    if i == 1:
        show main1
    elif i == 2:
        show main2
    elif i == 3:
        show main3
    m "Wow, to było coś ekstra. Zaczynam uwielbiać tego wykładowcę. Dzięki temu wykładowi wreszcie zdecydowałam co zrobię."
    m "Będę starać się chodzić na wszystkie wykłady i zgarnąć najwyższą ocenę z tego przedmiotu."
    if i == 1:
        hide main1
    elif i == 2:
        hide main2
    elif i == 3:
        hide main3
    play music "music/bensound-scifi.ogg"
    show marta at right
    show draco at left
    marta "Hejka. [malfoy], tak? Ja jestem Marta. Chciałabym cię prosić o pomoc. Trochę nie ogarniam tego programowania i 
    myślałam, ze może pomogłabyś mi w zrozumieniu go."
    marta "Widziałam jak dobrze radziłaś sobie na wykładach. Oczywiście odwdzięczyłabym się..."
    malfoy "Co? Hahhahahhaha. Takie proste rzeczy i ich nie ogarniasz? Co ty robisz na tych studiach kobieto? Może powinnaś się przepisać na pedagogikę?"
    marta "Dopiero zaczynam swoją przygodę z informatyką. Jeśli nie chcesz mi pomóc to wystarczyło powiedzieć nie. Nie musisz być taka niemiła."
    malfoy "Oczywiście, że nie chcę. Po pierwsze, nie mam zamiaru użerać się z takimi nieogarami. Po drugie, nie byłoby cię stać na moje korepetycje."
    marta "Jesteś zepsutą osobą, [malfoy]."
    malfoy "Mogę być. Przynajmniej nie jestem takim nieukiem jak ty. Na kogoś takiego czekają tylko wózki widłowe a nie poważana uczelnia. 
    Spadam, bo jeszcze twoja głupota na mnie przejdzie."
    hide draco
    marta "Chlip....Jak ona śmiała....Chlip. Nikt mnie w życiu jeszcze tak nie potraktował...."
    if i == 1:
        show main1:
            xpos 200
    elif i == 2:
        show main2:
            xpos 200
    elif i == 3:
        show main3:
            xpos 200
    hide marta
    play music "music/bensound-pianomoment.ogg"
    m "Matko...co za potwór z tej dziewczyny. Nie każdy musi być super inteligentny jak ona. Co powinnam zrobić?"
    menu:
        "Uspokój Martę":
            python:
                marta_zostala_uspokojona = True
            m "Nawet nie powinnam się nad tym zastanawiać. Trzeba ją jakoś pocieszyć."
            show marta:
                xpos 700
            m "Hej. Jesteś Marta, tak? Nie przejmuj się tą jędzą. Ona jest taka dla wszystkich. Nawet ja poczułam na sobie kim ona jest."
            marta "Chlip...jak ona może sobie tak pozwalać? Ja wiem, że to moja wina, że nie ogarniam jeszcze wszystkiego. Tylko dlaczego 
            musiała mnie tak potraktować."
            m "Chce się poczuć lepsza, tyle. Takimi ludźmi nie warto się przejmować. Ja ci pomogę zrozumieć materiał."
            marta "Nie musisz się nade mną litować, serio. Dziękuję ci za te słowa, ale to chyba nie ma sensu."
            m "Oczywiscie, ze jest sens. Od teraz będziemy siedzieć razem na wykładach i będę ci pomagać. Jeżeli będzie trzeba to i po 
            zajęciach ci będę tłumaczyc."
            m "Pokażesz jej, że guzik wie o tobie i jeszcze ją kiedyś zmasakrujesz. Nie możesz się mazać z jej powodu."
            marta "Masz rację! Taka gnida nie zasługuje na moje łzy. Jeszcze zobaczy z kim zadarła. Dziękuję ci za pomoc. Na pewno ci się 
            odwdzięczę. Jak się nazywasz?"
            m "Nazywam się [m]. Już coś nas łączy. Też mam na pieńku z tą babą."
            marta "Widzę, że nie jestem jedyna. Jeszcze raz dziękuję. Coś czuję, że to początek dobrej przyjaźni."
            m "Wiesz co, Marto? Czuję dokładnie to samo."
            jump w14
        "Idziesz do domu":
            python:
                marta_zostala_uspokojona = False
            m "Nie wiem, czy potrafię jej pomóc. To chyba nie moja sprawa. Bidulka. Mam nadzieję, że sobie poradzi..."
            jump w14
    label w14:
    #==================nowa_scena==================
    scene black
    show text "{color=#FFF}{size=+30}Środa{/size}{/color}"
    pause 2
    #==================nowa_scena==================
    scene bg korytarz
    if i == 1:
        show main1
    elif i == 2:
        show main2
    elif i == 3:
        show main3
    m "Mam nadzieję, że ta Marta już doszła do siebie. Ta [malfoy] jest jakaś chora."
    m "Nie ogarniam tego człowieka. Wielka szkoda, że mam z nią zajęcia."
    m "Nienawidzę mieć zajęć od 8 rano. Poniedziałek już udowodnił to, że to źle na mnie wpływa."
    if marta_zostala_uspokojona:
        play music "music/bensound-sweet.ogg"
        show marta at right
        marta "Hejka. Dzięki jeszcze raz za wczoraj. Ogarnęłam się i jestem gotowa na kolejne uczelniane wyzwania."
        m "Tak trzymać. Cieszę się, że widzę cię w takim stanie. Chodźmy, bo spóźnimy się na zajęcia."
        marta "Dobrze, chodźmy."
    else:
        m "To dziwne, nie widzę Marty. Może nie mogła dzisiaj przyjść."
        m "No nic, lecę na zajęcia. Nie chcę się spóźnić."
    #==================nowa_scena==================
    scene bg a129
    play music "music/bensound-straight.ogg"
    show ikar at left
    ikar "Dzień dobry uczniownie. Proszę o zajęcie miejsc. Zaraz zaczynamy wykład."
    hide ikar
    show stud1:
        xpos 200
    "Student1" "Jejku, co to za gościu. Takiego wykładowcy jeszcze nie widziałeś."
    show stud2:
        xpos 800
    "Student2" "Jest dopiero środa, ciołku. Wielu rzeczy na tych studiach jeszcze nie widziałeś."
    "Student1" "Ale popatrz na niego i jego maniery. Zachowuje się jak automat."
    hide stud1
    hide stud2
    show ikar at left
    ikar "Wydaje mi się, że już wszyscy przyszli. Chciałbym się wam przedstawić. Jestem dr Grzegorz Ikar 
    i prowadzę zajęcia z Teoretycznych Podstaw Informatyki."
    $ ikar = Character("dr Grzegorz Ikar",what_slow_cps=20)
    hide ikar
    if i == 1:
        show main1:
            xpos 800
    elif i == 2:
        show main2:
            xpos 800
    elif i == 3:
        show main3:
            xpos 800
    if marta_zostala_uspokojona:
        show marta:
            xpos 200
        marta "Nie wydaje Ci się, że on jest trochę...dziwny?"
        m "Nie wiem jak to nazwać. Gościu ma jakąś dziwną....aurę czy coś..."
        hide marta
    else:
        m "Gościu jest jakiś dziwny. Nie umiem tego określić słowami. Ma taką jakby....dziwną aurę...."
    if i == 1:
        hide main1
    elif i == 2:
        hide main2
    elif i == 3:
        hide main3
    show ikar at left
    ikar "Moim zadaniem jest was nauczyć tych rzeczy, które każdy, kto chce wiązać przyszłość z informatyką powinien wiedzieć."
    hide ikar
    show stud1 at right
    "Student1" "Czy każdy przedmiot nie powinien być taki, panie doktorze?"
    hide stud1
    show ikar at left
    ikar "Mój przedmiot prawdopodobnie jest najważniejszy ze wszystkich na pierwszym semestrze. Bez podstaw, 
    które poznacie tutaj nie poradzicie sobie z innymi przedmiotami."
    ikar "Proszę też o nie przerywanie mi podczas wykładu. Kiedy będę chciał byście byli aktywni, dam wam znać. 
    Przerywanie mi oznacza koniec wykładu dla takiego delikwenta."
    ikar "Moje zajęcia są nieobowiązkowe. Wy musicie je tylko zaliczyć. Nie musicie przychodzić. Ja poświęcam 
    czas tylko dla tych, którzy poważnie traktują te studia."
    hide ikar
    if i == 1:
        show main1
    elif i == 2:
        show main2
    elif i == 3:
        show main3
    m "Koleś jest surowy. To chyba będzie najgorszy wykładowca na tym semestrze."
    if i == 1:
        hide main1
    elif i == 2:
        hide main2
    elif i == 3:
        hide main3
    show ikar at left
    ikar "Zasady zaliczenia mojego przedmiotu są proste. Na trzecim wykładzie zrobię kartkówkę. Jeśli ją zaliczycie 
    to możecie podejść do egzaminu. W innym przypadku powtarzacie przedmiot."
    hide ikar
    show stud1:
        xpos 200
    "Student2" "Matko, ten gościu jest za surowy dla nas...."
    show stud2:
        xpos 800
    "Student3" "Jak on nam to może robić?"
    hide stud1
    hide stud2
    show ikar at left
    ikar "Ta kartkówka ma pokazać jedną rzecz: czy uczycie się na bieżąco. Temat nie będzie trudny. Tutaj chodzi 
    tylko o sprawdzenie jakości waszego uczenia się."
    ikar "Kiedyś ta kartkówka była niezapowiedziana, ale w efekcie niewielu ludzi mogło podejść do egzaminu, 
    więc szefostwo zadecydowało bym zmienił swój zwyczaj. Osobiście uważam, że tamta metoda była lepsza niż ta."
    ikar "Jeżeli nie nauczycie się samodyscypliny to nie poradzicie sobie w świecie IT. Moim zadaniem jest nie 
    tylko nauczyć was teorii informatyki, ale też i podstawowych zasad dorosłego życia."
    hide ikar
    #show studentka
    if i == 1:
        show main1
    elif i == 2:
        show main2
    elif i == 3:
        show main3
    if marta_zostala_uspokojona:
        show marta at right
        marta "W dużym skrócie jest to taki Meister tylko, że z odwrotnymi metodami, tak?"
        m "Chyba lepiej bym tego nie nazwała."
        hide marta
    else:
        m "Heh...czyli jest to taka odwrotność Meistera. Będzie grubo na jego zajęciach..."
    #hide studentka
    if i == 1:
        hide main1
    elif i == 2:
        hide main2
    elif i == 3:
        hide main3
    show ikar at left
    ikar "Mam nadzieję, że wszyscy zrozumieli to, co im teraz przekazałem. Obyście na wykładach mieli też takie 
    zrozumienie. Przejdźmy do tematu zajęć."
    scene black
    show text "{color=#FFF}{size=+30}Algorytmy i sposoby ich opisu{/size}{/color}"
    pause 2
    #-------------------------------dodokonczenia-------------------------------
    #==================nowa_scena==================
    scene bg korytarz
    if i == 1:
        show main1
    elif i == 2:
        show main2
    elif i == 3:
        show main3
    if marta_zostala_uspokojona:
        play music "music/bensound-rumble.ogg"
        show marta at left
        m "Ehh....co to były za zajęcia. Podejście tego gościa do studentów jest masakryczne."
        marta "Zgadzam się z tobą. Muszę ci się do czegoś przyznać. Mimo tego wszystkiego ogarniałam na tych zajęciach."
        menu:
            "Naprawdę? Jak to?":
                jump w17
            "No ba. Wiedziałam, że zaczniesz sobie radzić":
                jump w17
        label w17:
        marta "Hmm...myślę, że to dzięki tobie. Poprawiłaś mi samoocenę. Zaczynam wierzyć, że będę sobie radzić."
        m "I o to chodzi! Jestem z ciebie dumna."
        show draco at right
        play music "music/bensound-scifi.ogg"
        malfoy "Co ja tu słyszę? Czyżby niedorajda zaczęła sobie radzić?"
        marta "Odczep się ode mnie, [malfoy]."
        malfoy "Współczuję ci, [marta], że musisz użerać się z kimś takim. Ile ci zajęło by zrozumiała jak się 
        pisze Hello world w C?"
        m "Zapewne mniej niż tobie. Zaczynasz mnie męczyć, kobieto. Weź zatruwaj życie komuś innemu."
        malfoy "Biedactwa nie radzą sobie z prawdą. W pracy będziecie miały jeszcze gorzej. Lepiej od razu 
        przepiszcie się na Zarządzanie zanim stres was do reszty zje hahahahaha."
        hide draco
        play music "music/bensound-rumble.ogg"
        marta "Mówiłaś, że z toba też ma na pieńku. O co chodzi?"
        m "Nic takiego. Wkurzała mnie swoja wyniosłością i tak wyszło, że się założyłyśmy. Ta, która będzie miała 
        lepsze oceny, wygra."
        marta "W niezły bigos się wpakowałaś. Słyszałam, że ona jest naprawdę dobra. Będziesz miała ciężko."
        m "Dam sobie radę. Nie pozwolę, by dalej zachowywała się tak, jakby ta uczelnia należała do niej."
        marta "Jeżeli ją pokonasz, to ona nie zniesie tej porażki. Wierzę, że dasz radę ją pokonać."
        marta "Skoro postawiłaś sobie taki cel to chyba nie powinnam prosić cię tak często o pomoc. Marnuję twój czas, 
        który mogłabyś spożytkować na naukę."
        menu:
            "Masz rację":
                m "Masz chyba trochę racji, ale nie chcę zostawiać cię na lodzie. Mam pomysł. Może będę ci pomagać wtedy, 
                kiedy ostatecznie nie będziesz sobie dawać rady."
                m "Dzięki temu poćwiczysz swoje zdolności i umiejętności rozwiązywania problemów."
                jump w15
            "Nie masz racji":
                m "Zgłupiałaś? Możesz na mnie liczyć. Chcę byś ty też utarła nosa tej [malfoy].
                Jak razem ją pokonamy to będzie to dla niej podwójna klęska."
                jump w15
        label w15:
            marta "Sądzę, że to jest genialny pomysł. Dziękuję ci, za chęć pomocy. Jesteś dla mnie za dobra"
            m "Daj spokój. Przez ciebie zaczynam się rumienić. Chodźmy na następne zajęcia, bo się spóźnimy."
            marta "Mówię tylko to co czuję. Ruszajmy!"
    else:
        play music "music/bensound-sweet.ogg"
        m "Ehh....co to były za zajęcia. Podejście tego gościa do studentów jest masakryczne. 
        Dopiero początek dnia a już jestem zdenerwowana."
        m "Lepiej od razu ruszę na zajęcia. Nie chcę, by ta [malfoy] jeszcze bardziej popsuła mi dzień."
        m "Jeśli ta Marta nie pojawi się jutro, to zainteresuje się tematem. Mam złe przeczucia..."
    #==================nowa_scena==================
    scene black
    show text "{color=#FFF}{size=+30}Czwartek{/size}{/color}"
    pause 2
    #==================nowa_scena==================
    show bg park
    if i == 1:
        show main1
    elif i == 2:
        show main2
    elif i == 3:
        show main3
    play music "music/bensound-acousticbreeze.ogg"
    if marta_zostala_uspokojona:
        #(dzwonek telefonu)
        m "Hmm sms od Marty. Ne może być na wykładzie bo ma o tej porze denstystę. Spoko, będzie miała 
        ode mnie notatki. To tylko Prawo inżynierskie. Sama teoria bez zrozumienia."
        m "Dzieki poznaniu Marty zaczynam realizować się towarzysko. Kiedys musimy zrobić jakiś wypad do baru."
        m "Pamietaj tylko, by nie przesłoniło Ci to Twojego celu. Musisz też radzić sobie na studiach. 
        Jesteś ambitną osobą. Nie skop tego."
    else:
        m "Hmmm... Dzisiejszy dzień zaczynamy Prawem Inżynierskim. Sama teoria. Prawdopodobnie będę się tylko nudzić."
        m "Studia zaczynają się rozkręcać. Mam nadzieję, że sobie poradzę. Ta [malfoy] jeszcze zobaczy na co mnie stać."
        m "Szkoda tylko, że nie utrzymuję bliższych kontaktów z innymi studentami. Są tu same paczki znajomych. 
        Ciężko będzie się w którąś wkręcić."

    #==================nowa_scena==================
    scene bg korytarz
    if i == 1:
        show main1
    elif i == 2:
        show main2
    elif i == 3:
        show main3
    if marta_zostala_uspokojona:
        m "Dziś nie chce mi się siedzieć i notować. Przedmiot wydaje się nudny. Marta będzie mi 
        musiała dużą czekoladę kupić za te notatki."
        m "Skoro postawiłam sobie motywację, to muszę iść na wykład. Nie ma bata."
    else:
        m "Hmmm....znowu nie widzę Marty. Zaczynam się niepokoić. Co jeśli posłuchała tej [malfoy]? Popytam innych 
        po wykładzie. Może coś wiedzą."
        m "Dobra, wszystko ustalone. Czas zmierzyć się z nowym przedmiotem."
    #==================nowa_scena==================
    scene bg a123
    if i == 1:
        show main1
    elif i == 2:
        show main2
    elif i == 3:
        show main3
    m "Mimo pierwszych zajęć z tego przedmiotu mało kto dziś przyszedł. Każdy chyba uznał, że przedmiot jest nudny."
    show stud2 at right
    "Student1" "Słyszałem, że wykład jest niemiłosiernie nudny. Profesorka dobrze o tym wie, dlatego co roku zmienia 
    formę wykładu i zaliczenie. Ma to spowodować większą frekwencje."
    m "Jak widzę i taka metoda zbytnio nie działa. Musi wykombinować coś innego."
    "Student1" "Lepiej by sobie darowała. Chcę to zaliczyć jak najszybciej. Takie wypełniacze zwykle są trudniejsze 
    do zaliczenia niż pełnoprawne przedmioty."
    hide stud2
    m "No nic. Zobaczmy co w tym roku nam pokaże. Chciałabym już wrócić do domu."
    if i == 1:
        hide main1
    elif i == 2:
        hide main2
    elif i == 3:
        hide main3
    play music "music/bensound-psychedelic.ogg"
    show teresa at left
    teresa "Dzień dobry wszystkim. Widzę, że frekwencja nie jest za duża dzisiaj. No nic, jakoś sobie poradzimy. Nie 
    dziwię się Wam. To najprawdopodobniej najnudniejszy przedmiot w tym semestrze."
    teresa "Mimo to sądzę, że warto go wykładać. Wielu inżynierów ma nikła wiedzę o prawie technicznym co potem owocuje 
    nieprzyjemnościami. Będę z was dumna jeśli zapamiętacie to co wam tutaj wyłożę."
    hide teresa
    show stud1:
        xpos 200
    "Student2" "W sumie ma rację. Prawo to rzecz święta w cywilizowanym społeczeństwie."
    show stud2:
        xpos 800
    "Student3" "Zabrało ci się na mądrości, chłopie? Daj sobie spokój."
    hide stud1
    hide stud2
    show teresa at left
    teresa "Miejmy formalności za sobą. Jestem Teresa Lowerska i mam z wami w tym semestrze Prawo Inżynierskie. Mam 
    nadzieję, że wszyscy zaliczą ten przedmiot by potem nie musieć go niepotrzebnie powtarzać."
    $ teresa = Character("dr Teresa Lowerska", what_slow_cps=20)
    teresa "Moje zaliczenie jest proste. Na koniec semestru odbędzie się krótkie kolokwium. Jeżeli będziecie sumiennie 
    robić notatki to powinniście bez problemu zaliczyć."
    hide teresa
    if i == 1:
        show main1
    elif i == 2:
        show main2
    elif i == 3:
        show main3
    m "Może i jest to mało istotny przedmiot, ale nie mogę go olać. Każda ocena przyda mi się by móc pokonać [malfoy]."
    if i == 1:
        hide main1
    elif i == 2:
        hide main2
    elif i == 3:
        hide main3
    show teresa at left
    teresa "Choćbym nie wiem jak chciała nie uda mi się uatrakcyjnić wykładu o prawie. To jest teoria i nic więcej z 
    wami nie zrobię. Mam jednak nadzieję, że czegoś ciekawego się dowiecie."
    hide teresa
    show stud2
    "Student1" "Ciekawego? Dajcie spokój..."
    hide stud2
    show teresa at left
    teresa "No dobrze. Skoro wszyscy jesteśmy gotowi to zacznijmy to co nieuniknione." 
    #------------------------------------dodokonczenia----------------------------------------------------------
    #==================nowa_scena==================
    scene black
    show text "{color=#FFF}{size=+30}Ochrona własności intelektualnej{/size}{/color}"
    pause 2
    scene bg korytarz
    if i == 1:
        show main1
    elif i == 2:
        show main2
    elif i == 3:
        show main3
    play music "music/bensound-acousticbreeze.ogg"
    if marta_zostala_uspokojona:
        m "Ehhh aż mnie plecy bolą od tego siedzenia. Prawie usnęłam na tym wykładzie. Dobrze, że wszystko zanotowałam."
        m "Już się nie mogę doczekać tej czekolady od Marty. W pełni na nią zasłużyłam."
        m "Mam pomysł. Może zrobimy tak, ze naprzemiennie będziemy chodzić na ten wykład. Więcej godzin spania co dwa 
        tygodnie brzmi obiecująco. Napisze później do niej."
        m "[malfoy] nie przyszła na wykład. Pewnie uznała, że to nie jest warte zachodu. Zastanawiam się kto 
        wyszedł na plus po tym wykładzie: ja czy ona?"
        m "No nic. Następne zajęcia mam w innym budynku. Trochę się rozruszam po tym wykładzie..."
    else:
        m "Ehhh aż mnieplecy bolą od tego siedzenia. Prawie usnęłam na tym wykładzie. Dobrze, że wszystko zanotowałam."
        m "Teraz musze dowiedzieć się co z tą Martą. Nie wiem, z kim się trzymała. Będzie ciężko zacząć."
        show draco at right
        play music "music/bensound-scifi.ogg"
        malfoy "Co tam, przegrywie? Wyglądasz jakbyś kogoś szukała. Może mnie? Jak coś to jestem do usług hahahhaha."
        menu:
            "ignoruj ją":
                m "Nie twój interes. Przestań mnie nachodzić, bo gorzko tego pożałujesz."
                malfoy "Oj, bo się ciebie wystraszę. Mam nadzieję, że się nie popłaczesz z emocji tak jak tamta. 
                Chociaż to już jest nieistotne."
                m "Mowisz o Marcie, tak? O co ci chodzi?"
                malfoy "Wali mnie jak się ona nazywa. Na szczęście już jej nie zobaczymy tutaj. To nie moja liga....ani twoja."
                m "Co masz na myśli mówiąc \"już jej nie zobaczymy\"?"
                jump w16
            "zapytaj o Martę":
                m "Chcę się dowiedzieć co się stała z Martą. Tą dziewczyną, która tak chamsko potraktowałaś."
                malfoy "Tamta? Oj, obawiam się, że twoje poszukiwania nie mają sensu. Już nie."
                m "Co masz na myśli?"
                jump w16
        label w16:
        malfoy "Ta kretynka wreszcie pomyślała i uznała, że nie ma sensu by tutaj dalej studiowała. Z tego co 
        słyszałam miała złożyć podanie o wykreślenie."
        m "Kłamiesz. To nie jest prawda. Nie może być."
        malfoy "Nie mam interesu w tym by cię oszukiwać. Czym się przejmujesz? Dobrze zrobiła według mnie."
        m "Nie....nie...to niemożliwe.....mogłam pomóc....coś zrobić....."
        malfoy "A to tym się przejmujesz. Jakby było czym. Jak chcesz, to jej szukaj. Widziałam ją w kolejce do 
        dziekanatu. Według mnie dobrze jest jak jest."
        m "Czemu? Czemu tak uważasz? Jak możesz tak mówić?"
        malfoy "Jakbyś nagadała jej bzdur to by uroiła sobie, że się tu nadaje. Potem upadek byłby cięższy. Dobrze
        zrobiłaś, że ją olałaś. Wyświadczyłaś jej przysługę."
        malfoy "Wreszcie nadajesz na podobnych falach co ja. Może jesteś mi bliższa niż myślisz?"
        menu:
            "Uderz ją":
                m "Nigdy mnie do siebie nie porównuj. To wszystko twoja wina! >TRZASK<"
                #(oglos uderzenia)
                malfoy "Czy Ty jesteś wariatką? Ja...krwawię...z nosa....krew. Pożałujesz tego. Twoja kariera na 
                tej uczelni...jest już skończona!"
                m "O nie. Co ja zrobiłam? CO JA ZROBIŁAM? TO NIE TAK MIAŁO BYĆ!!!!!!!!!"
                #(tlo zaczyna sie sciemniac az do czerni, pojawia sie obserwator)
                scene black
                show narrator at left
                play music "music/bensound-extremeaction.ogg"
                ob "Z powodu słusznego doniesienia o pobiciu, nasza studentka została wyrzucona z uczelni." 
                ob "Dodatkowo musi zapłacić wysokie odszkodowanie tamtej dziewczynie. Ojciec bohaterki nigdy tak bardzo nie czuł wstydu z powodu zachowania swojej córki..."
                ob "Zawiodła go na całej linii. Obawiam się, że to Twoja wina. Zawiodłem się na Tobie. Gra została skończona!"
                
                scene black
                show text "{color=#FF0000}{size=+30}GAME OVER{/size}{/color}"
                pause 5
                return
            "Biegnij do dziekanatu":
                m "Nigdy....tak...nie mów...."
                #==================nowa_scena==================
                scene black
                show text "{color=#FFF}{size=+30}Parę chwil później{/size}{/color}"
                pause 2
                #==================nowa_scena==================
                scene bg dziekanat
                play music "music/bensound-pianomoment.ogg"
                if i == 1:
                    show main1
                elif i == 2:
                    show main2
                elif i == 3:
                    show main3
                m "Oby tu jeszcze była. Błagam, bądź tu jeszcze."
                show marta at right
                m "Dzieki Bogu, jesteś. Marta, nie rób tego!"
                marta "Słucham?"
                m "Jestem [m]. Z Twojego rocznika. Widziałam, jak [malfoy] cię potraktowała. Chciałam do ciebie podejśc, pomóc jakoś. 
                Nie potrafiłam. Nie wiem czemu...."
                m "Wybacz, że nie podeszłam. Mogłabym ci wtedy pomóc...Błagam, zostań na uczelni..."
                marta "Wiem kim jesteś, mimo że nie pomogłaś mi wtedy to bardzo ci dziękuje za te słowa. Bardzo ich potrzebowałam."
                marta "Mimo tego wszystkiego [malfoy] jednak miała rację. Ja serio nie nadaję się tutaj."
                m "Daj spokój. Jakbym pomogła ci w nauce to w mig byś wszystko....."
                marta "Może tak, może nie...nie dowiemy się tego. Poprawię maturę i jeszcze raz postaram się złożyć papiery do 
                wymarzonej uczelni. Nic straconego."
                m "Przepraszam....nigdy sobie tego nie wybaczę."
                marta "Przestań. Nie obwiniaj się. Dzięki twojej interwencji poprawiłaś moją wiarę w siebie. Dziękuję."
                m "Powiedz co mogę zrobic byś zmieniła zdanie."
                marta "Prawdopodobnie nic. Jeśli jednak serio chcesz coś dla mnie zrobić to zrób jedno: pokonaj [malfoy]."
                marta "Cały rocznik wie o waszym zakładzie. Nie pozwól jej zwyciężyć. Jeśli ją pokonasz to wreszcie może przejrzy 
                na oczy i zrozumie, że nie jest pępkiem świata. Nie daj się jej."
                m "Obiecuję, że ją pokonam. Zwyciężę za wszelką cenę."
                marta "Hahahaha. Widzę, że jesteś zdeterminowana. To dobry znak. Widzę po tobie, że jesteś inna niż ona. Szkoda, 
                że wcześniej się nie poznaliśmy. Niestety na razie nie będzie okazji by się bliżej poznać."
                marta"Zaśmiałam się. To chyba dobry znak. [m] nie przejmuj się mną. Ja sobie ułożę życie tak jak powinnam. Ty natomiast 
                nie poddawaj się i dąż do spełnienia swoich celów. Daj znać kiedy pokonasz tę [malfoy]."
                m "Możesz na mnie liczyć. Kiedy będą ferie może pójdziemy na piwo czy coś?"
                marta "Trzymam cię za słowo. Obalimy twój sukces. Życzę ci powodzenia."
                m "Dziękuję. Tym razem cię nie zawiodę."
                #==================nowa_scena==================
                scene black
                show text "{color=#FFF}{size=+30}Kilka chwil później{/size}{/color}"
                pause 2
                #==================nowa_scena==================
                scene bg korytarz
                play music "music/bensound-scifi.ogg"
                show draco:
                    xpos 300
                if i == 1:
                    show main1:
                        xpos 800
                elif i == 2:
                    show main2:
                        xpos 800
                elif i == 3:
                    show main3:
                        xpos 800
                malfoy "I co tam? Znalazłaś tę niedojdę?"
                m "[malfoy]! Mam ci tylko jedno do powiedzenia. Brzydzę się tobą i twoim zachowaniem. Nie przegram z kimś takim jak ty. 
				Usunę ten paskudny uśmiech z tej paskudnej twarzy."
                malfoy "Zobaczymy, zobaczymy. Mimo to podtrzymuję swoje słowa. Jesteśmy do siebie podobne. Czas pokaże kto będzie górą."
                m "Nawet nie wiesz jak bardzo nie mogę się tego doczekać...."
    #==================nowa_scena==================
    scene black
    show text "{color=#FFF}{size=+30}Piątek{/size}{/color}"
    pause 2
    #==================nowa_scena==================
    scene bg korytarz
    play music "music/bensound-sunny.ogg"
    if i == 1:
        show main1
    elif i == 2:
        show main2
    elif i == 3:
        show main3
    if marta_zostala_uspokojona:
        show marta at right
        m "Ehh to już trzeci dzień, kiedy mam zajęcia na 8 rano. Boże, czemuś mnie pokarał takim planem?"
        marta "Skoro wzywasz Boga to widać, że coś zaczyna się dziać."
        m "O hej. Po prostu nie wysypiam się na tych zajęciach. Chyba muszę do tego przywyknąć. Jak dentysta?"
        marta "Kobieto, to był horror. Leczenie kanałowe to istny koszmar. Dodatkowo dentystka skopała znieczulenie 
        i strasznie mnie bolało podczas zabiegu."
        m "Nie żartuj. Aż tak? Rany...współczuję ci bardzo. Dzielna jesteś skoro to wytrzymałaś."
        marta "Daj spokój. Nic takiego. Jeszcze raz dzięki za notatki. Po zajęciach pójdziemy do sklepu i wybierzesz sobie taką czekoladę jaką chcesz."
        m "Yay. Od razu poprawił mi się humor. Dzięki, jesteś kochana."
        marta "Nic takiego. Ty dla mnie więcej zrobiłaś. O, jest już 8:14. Wchodźmy do sali."
        m "Racja. Nie chcę się spóźnić na matematykę."
    else:
        m "Ehh to już trzeci dzień, kiedy mam zajęcia na 8 rano. Boże, czemuś mnie pokarał takim planem?"
        m "Nie wolno Ci marudzić. Masz ważny cel do osiągnięcia. Obiecałaś, że go wypełnisz. Sobie....i Marcie."
        m "Dopiero jak pokonam tę krowę to dopiero będę mogła sobie wybaczyć to wszystko. Wtedy będę miała czyste sumienie."
        m "Mimo tego nauczyłam się czegoś ważnego. Nie uciekaj od pomagania innym!"
        m "No, zaraz się zaczną zajęcia. Nie mogę pozwolić by coś mnie rozpraszało. Matematyka to bardzo pokrętna dziedzina. Muszę być czujna."
    #==================nowa_scena==================
    scene bg a128
    show stud1:
        xpos 100
    "Student1" "Nie sądziłem, że znowu będę musiał się uczyć tej znienawidzonej matematyki"
    show stud2:
        xpos 800
    "Student2" "Poszedłeś na infę i myślałeś, że bez matmy się obejdzie? Człowieku ogarnij się."
    "Student1" "No co? Pomarzyć zawsze można. Pewnie i tak nam się to w przyszłości nie przyda."
    "Student2" "Ta, jasne. Jak będą macierze w programowaniu to zmienisz śpiewkę."
    "Student1" "Macierze? A co to?"
    "Student2" "Tak myślałem. Zacznij lepiej uważać na algebrze liniowej."
    show draco:
        xpos 500
    malfoy "Możecie się przesunąć? Od waszego pitolenia rozbolała mnie głowa."
    "Student1" "Nie jest za miła, co? Tylko do wykładowców potrafi się uśmiechnąć. Przyjaciół tutaj chyba nie znajdzie..."
    "Student2" "Teraz mogę w 100 procentach się z tobą zgodzić. Dawaj, zajmijmy dobre miejsca."
    hide stud1
    hide stud2
    hide draco
    play music "music/bensound-house.ogg"
    show iza at left
    Izabella "Dzień dobry. Nie mam pojęcia kto nam dał te zajęcia o 8 rano, ale chyba nie myślał nad tym za długo. 
    By móc przystąpić do matematyki potrzebny jest świeży i czysty umysł."
    hide iza
    if i == 1:
        show main1 at left
    elif i == 2:
        show main2 at left
    elif i == 3:
        show main3 at left
    if marta_zostala_uspokojona:
        show marta at right
        marta "Widzisz? Nawet on cię popiera!"
        m "Taa...ale zobaczmy najpierw z jakiej gliny jest ona ulepiony."
        hide marta
    else:
        m "O, chociaż podziela moje poglądy na ten temat."
    if i == 1:
        hide main1
    elif i == 2:
        hide main2
    elif i == 3:
        hide main3
    show iza at left
    Izabella "Od razu przejdę do rzeczy. Nazywam się Miguel Anajewski i będę wam wykładać Analizę Matematyczną. 
	Możecie narzekać na ten przedmiot, ale nie martwcie się: następne matematyczne przedmioty będą o wiele trudniejsze."
    $ Izabella = Character("dr hab. Miguel Anajewski",what_slow_cps=20)
    hide iza
    show stud1:
        xpos 200
    "Student1" "Marna pociecha..."
    show stud2:
        xpos 800
    "Student2" "A Ty dalej swoje?"
    hide stud1
    hide stud2
    show iza at left
    Izabella "Zaliczenie jest następujące. Co zajęcia będziecie mieli na początku wykładu kartkówkę. Będzie to jedno 
    zadanie do policzenia. Ma to sprawdzić, czy uczycie się na bieżąco."
    Izabella "Musicie zaliczyć 2 by móc podejść do egzaminu. Egzamin będzie naturalnie trudniejszy od tych kartkówek, 
    ale jeśli przyłożycie się do nich to egzamin będzie dla was o wiele łatwiejszy."
    hide iza
    show stud1 at left
    "Student1" "Zachciało mi się inżyniera..."
    hide stud1
    show iza at left
    Izabella "Sądzę, że chyba wszystko powiedziałem. Zacznijmy więc zajęcia."
    scene black
    show text "{color=#FFF}{size=+30}Pochodne{/size}{/color}"
    pause 2
#---------------------------------------------------temat zajęć: Granice------------------------------------------------------ 
    scene bg korytarz
    play music "music/bensound-sweet.ogg"
    if i == 1:
        show main1:
            xpos 200
    elif i == 2:
        show main2:
            xpos 200
    elif i == 3:
        show main3:
            xpos 200
    if marta_zostala_uspokojona:
        show marta at right
        marta "Jejku, to było męczące. Czy mi się wydaje, czy nudziłaś się na tym wykładzie."
        m "W sumie, tak. Miałam już to w liceum. Byłam na profilu matematyczno-przyrodniczym."
        marta "Jejku, Ty to musisz mieć łeb. Te pochodne nie wydają się aż tak trudne."
        m "Bo nie są. Jak dojdziemy do całek to zaczniemy narzekać."
        marta "Weź nie strasz mnie na zapas, co?"
        m "Hhahahahaha, wybacz. Tylko żartowałam. Co planujesz na weekend?"
        marta "Jadę do babci. Dawno się z nią nie widziałam. Potrzebuje pomocy w remoncie i muszę jej pomóc."
        m "Pozdrów babcię, czy coś. Ja w ten weekend powtórzę sobie cały tygodniowy materiał."
        marta "Pamiętaj, że odpoczynek jest również ważny. Może skoczyłybyśmy na piwo na koniec dnia. Trochę się wyluzujemy?"
        menu:
            "Tak":
                m "No dobra, chodźmy"
                $ piwo_piatek2 = True
                jump chapter3
            "Nie":
                m "Dzisiaj zbytnio nie dam rady. Jadę zaraz z tatą na zakupy. Innym razem spróbujmy."
                marta "Ok, innym razem. Do zobaczenia w poniedziałek."
                m "Trzymaj się!"
                $ piwo_piatek2 = False
                jump chapter3
    else:
        m "Matko, co za nudy. Miałam już to w liceum. No nic, mniej do nauki mi zostało."
        m "Wyszłabym na piwo trochę się wyluzować, ale nie mam z kim. Samemu pić to byłoby dziwne."
        m "Mówi się trudno. Spróbuję może następnym razem wkręcić się na jakiś wypad. Teraz będę się uczyć. 
        Mam zadanie do wykonania!"
        $ piwo_piatek2 = False
    jump chapter3

#strona 26