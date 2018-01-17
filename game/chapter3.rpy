init:
    define adam = Character("Ziomeczek", what_slow_cps=20)
    image adam_view = "przyjaciel.png"
label chapter3: #DONE
    play music "music/bensound-sunny.ogg"
    scene black
    show text "{color=#FFF}{size=+30}Chapter 3\nTydzień drugi{/size}{/color}"
    pause 2

    scene bg white
    show text "{color=#000000}Poniedziałek{/color}"
    pause 2
    #python:
        #marta_zostala_uspokojona = False
        #piwo_piatek2 = False
    scene bg miasto
    if i == 1:
        show main1
    elif i == 2:
        show main2
    elif i == 3:
        show main3
    
    if marta_zostala_uspokojona:
        m "Ehh...zaczynam się chyba powtarzać, ale nie ogarniam, 
        kto wpadł na pomysł by zaczynać tydzień tak wcześnie."
        show marta:
            xpos 100
        marta "Marudzenie w niczym nam nie pomoże. Mimo, że masz absolutną rację."
        m "W dodatku programowanie. Zamiast tego mogłoby być bo ja wiem...prawo?"
        marta "Stawiam 5 zł, że robią to specjalnie. Chodźmy szybciej bo się spóźnimy."
        scene bg korytarz
        if i == 1:
            show main1
        elif i == 2:
            show main2
        elif i == 3:
            show main3
        show marta:
            xpos 100
        m "Ciekawe jak na uczelni jest z nieobecnościami prowadzących. 
        Odwołują wykład czy jest zastępstwo?"
        marta "Z tego co wiem to częściej odwołują wykład. Mają dla nas choć trochę litości."
        show draco:
            xpos 600
        play music "music/bensound-scifi.ogg"
        malfoy "O jejku. Popatrzcie na te biedne dziewczynki. Już studia zaczęły boleć?"
        marta "Idealne zaczęcie nowego tygodnia. Dzięki, Amanda."
        malfoy "Do usług. Mam nadzieję, że nauczyłyście się na kartkówkę. Chcę chociaż 
        trochę poczuć ekscytacji związanej z naszym wykładem"
        marta "O kurde...zupełnie o tym zapomniałam. Pamiętałaś?"
        menu:
            "Tak":
                m "Jasne, mam dobrą pamięć. Jak zawsze!"
                marta "Jak widzę zawsze przygotowana. Pokaż Amandzie gdzie raki zimują!"
                malfoy "Zaczynam się czuć jakbym brała udział w niskolotnej powieści Spadam stąd."
                marta "Hmm...powietrze zrobiło się czystsze. Chodźmy, czas zacząć to co nieuniknione."
                jump wyklad_pp1_2 
            "Nie":
                m "Eee...wypadło mi. Skupiłam się w weekend nad czymś zupełnie innym"
                marta "Myślałam, ze chociaż Ty będziesz pamiętać. Mam nadzieję, że nic z naszych 
                głów nie wyleciało przez ten weekend"
                malfoy "To się robi co raz bardziej załosne. Spadam stąd. Powodzenia, frajerki."
                marta "Przynajmniej ją mamy z głowy. Chodź, trzeba obalić tę kartkówkę."
                jump wyklad_pp1_2
    else:
        m "Ehh...zaczynam się chyba powtarzać, ale nie ogarniam, kto wpadł na 
        pomysł by zaczynać tydzień tak wcześnie."
        m "W dodatku programowanie. Zamiast tego mogłoby być bo ja wiem...prawo?"
        m "Stawiam 5 zł, że robią to specjalnie. Muszę się pośpieszyć, bo się spóźnię."
        scene bg korytarz
        if i == 1:
            show main1
        elif i == 2:
            show main2
        elif i == 3:
            show main3
        m "Dzisiaj mam pierwszą kartkówkę. Rywalizacja oficjalnie się zaczęła. Muszę 
        dotrzymać obietnicy. O tak!!!!!"
        m "Nie dam sobie pomiatać tej Amandzie."
label wyklad_pp1_2:
    play music "music/bensound-jazzcomedy.ogg"
    scene bg a123
    show opiekun:
        xpos 100
    opiekunroku "Witajcie, moi mili. Jak zapewne pamiętacie dzisiaj mamy kartkówkę"
    hide opiekun
    show stud1 at left
    "Random1" "Myślałem, ze zapomni. Boli mnie głowa od wczorajszej libacji."
    show stud2 at right
    "Random2" "Imprezować w niedzielę? Chłopie, gdzie Ty masz głowę?"
    "Random1" "Sądząc po tym jak się czuję to chyba w betoniarce..."
    hide stud1
    hide stud2
    show opiekun at left
    opiekunroku "Nie martwcie się, dzisiaj zrobiłam w miarę proste polecenia. Czuję, ze większość 
    z Was to zaliczy"
    hide opiekun
    show stud1 at left
    "Random1" "Poproszę o lód na głowę i dam radę..."
    hide stud1
    show opiekun at left
    opiekunroku "Nie przedłużając. Zaczynamy zaliczenie!"
    jump pp1_kart1

label back_wyklad_pp1_2_cd:
    play music "music/bensound-jazzcomedy.ogg"
    scene bg a123
    show opiekun at left
    opiekunroku "No dobrze. Czas się skończył. Wyniki poznacie na koniec wykładu."
    show stud2 at right
    "Random2" "Przepraszam, skoro pani będzie prowadzić wykład, to kto je teraz sprawdzi?"
    hide stud2
    opiekunroku "Hahaha, dobrze, że pan pyta. Czas Wam przedstawić system JD3.0"
    "JD3.0" "BIP BOOP BIP BOOOOP"
    opiekunroku "Tworzony 5 lat przez studentów naszego działu komputerowy system JD3.0 nie służy tylko 
    do sprawdzania kolokwiów i prac domowych."
    opiekunroku "Ma zdecydowanie więcej zastosowań. Podczas tego semestru JD będzie testowany w różnych 
    dziedzinach, w tym i analiza danych. Oczywiście egzaminy będę sprawdzała ja."
    hide opiekun
    show stud1 at left
    "Random1" "Te filmy z ubiegłych lat dotyczące przyszłości zaczynają się sprawdzać."
    show stud2 at right
    "Random3" "Witamy w przyszłości, ziom."
    hide stud2
    hide stud1
    show opiekun at left
    opiekunroku "No dobrze, zacznijmy wreszcie wykład."
    
    scene black
    show text "{color=#FFF}Wykład...{/color}"
    pause 2
    
    scene bg a123
    show opiekun at left
    opiekunroku "Na tym chyba dziś zakończymy.  JD! Pokaż wyniki kartkówek."
    "JD3.0 BIP" "BIIIIIIIIIIIIIIIIIIIIP"
    opiekunroku "Hmmm....miałam rację. Większość z Was zaliczyła. Jestem z Was dumna. 
    Dla tych, co nie zaliczyli mam jedną radę: Więcej pracy!  Dziękuję za wykład. Do zobaczenia!"
    #testowanie wariant1
    #python:
        #ocena_kart1_pp1 = 3
    scene bg white
    show text "{color=#000000}Twoja ocena: [ocena_kart1_pp1]{/color}"
    pause 2

    scene bg a123
    play music "music/bensound-sweet.ogg"
    if i == 1:
        show main1
    elif i == 2:
        show main2
    elif i == 3:
        show main3
    if marta_zostala_uspokojona:
        show marta at left
        marta "Ufff....jakimś cudem mi się udało. Dzięki Ci, Boże. Jak u Ciebie?"
        if ocena_kart1_pp1 == 3:
            m "Też mi się udało, ale powinnam lepiej wypaść, by pokonać Amandę..."
            marta "Daj spokój. Ona pewnie tego nie zaliczyła..."
            show draco at right
            malfoy "Jednak nie, dostałam 4. Kurde, ta rywalizacja idzie łatwiej niż sądziłam. Hahahahaha"
            hide draco
            marta "Nie słuchaj jej. To dopiero początek. Spójrz na to inaczej. Masz 
            większą motywacje, by ją prześcignąć. Pamiętaj też, że najważniejsze są egzaminy!"
            m "Masz rację. Jest dobrze. Chodźmy na następne zajęcia."
        elif ocena_kart1_pp1 > 3:
            m "Nawet wysoką ocenę dostałam. Ciekawe co na to Amanda."
            show draco at right
            malfoy "Nienajgorzej Ci poszło. Ja dostałam 4. Nie sądzę, żebyśmy musiały porównywać 
            każdą kartkówkę. Egzaminy są najważniejsze."
            malfoy "Chociaż, kto wie? Może takie proste kartkóweczki poprawiają Twoją samoocenę? Trzymajcie się frajerki."
            hide draco
            marta "Ona nawet zwycięstwo potrafi zepsuć. Jest dobrze. Idziesz na szczyt, moja droga."
            m "Dzięki, Marta. Chodźmy na następne zajęcia."
        else: #2
            m "Nie tym razem. Dałam ciała. Jestem do niczego...."
            marta "Daj spokój. Ona pewnie tego też nie zaliczyła..."
            play music "music/bensound-scifi.ogg"
            show draco at right
            malfoy "Jednak nie, dostałam 4. Kurde, ta rywalizacja idzie łatwiej niż sądziłam. Hahahahaha"
            malfoy "Jeśli chceszs ię już poddać to nie ma problemu. Widać, że już na starcie Ci nie idzie."
            hide draco
            marta "Nie słuchaj jej. To dopiero początek. Spójrz na to inaczej. Masz większą motywacje, by ją prześcignąć. 
            Pamiętaj też, że najważniejsze są egzaminy! Możesz jeszcze to zaliczyć!"
            m "Masz rację. Jest dobrze. Dzięki, Marta. Chodźmy na następne zajęcia."
    else:
        if ocena_kart1_pp1 == 3:
            m " Udało mi się, ale powinnam lepiej wypaść, by pokonać Amandę..."
            show draco at right
            malfoy "Jednak nie, dostałam 4. Kurde, ta rywalizacja idzie łatwiej niż sądziłam. Hahahahaha"
            m "Zdobyłaś pierwszy punkt w naszej rywalizacji. Czas na kolejne!"
        elif ocena_kart1_pp1 > 3:
            m "Nawet wysoką ocenę dostałam. Ciekawe co na to Amanda?"
            show draco at right
            malfoy "Nienajgorzej Ci poszło. Ja dostałam 4. Nie sądzę, żebyśmy musiały porównywać każdą kartkówkę. Egzaminy są najważniejsze."
            hide draco
            m "Udało mi się. Muszę pracować jeszcze ciężej!"
        else:
            m "Dałam ciała. Jestem do niczego...."
            m "Ciekawe jak tamtej poszło. Dobrze by było jakby też tego nie zaliczyła..."
            play music "music/bensound-scifi.ogg"
            show draco at right
            malfoy "Jednak nie, dostałam 4. Kurde, ta rywalizacja idzie łatwiej niż sądziłam. Hahahahaha"
            malfoy "Jeśli chcesz się już poddać to nie ma problemu. Widać, że już na starcie Ci nie idzie."
            hide draco
            m "Nie mogę zawieść Marty. Dam sobie radę. Czas na następne zajęcia."

    scene bg white
    show text "{color=#000000}Wtorek{/color}"
    pause 2
    play music "music/bensound-sunny.ogg"
    scene bg park
    if i == 1:
        show main1
    elif i == 2:
        show main2
    elif i == 3:
        show main3
    m "Dzisiaj znowu zajęcia z dziekanem. Nie mogę się doczekać wykładu. Może powinnam zmienić kierunek? Hahahaha"
    m "Zaczynam co raz bardziej żyć studenckim życiem. Tata byłby dumny."
    m "Nie mogę się rozleniwić. Mam zakład do wygrania."
    scene bg korytarz
    if i == 1:
        show main1
    elif i == 2:
        show main2
    elif i == 3:
        show main3
    if marta_zostala_uspokojona:
        m "Hmm...nie ma dziś Marty.  Nic mi nie pisała, ze robi sobie wolne. Niech uważa, bo przepadnie jej gwarantowana trójka."
        m "Nie widzę też Amandy. W sumie dobrze. Potrzebuję trochę od niej odpocząć."
    else:
        m "Mało dziś ludzi jest. Czyżby zapomnieli o gwarantowanej trójce za obecność? Nie mój interes w sumie."
        m "Nie widzę też Amandy. W sumie dobrze. Potrzebuję trochę od niej odpocząć."
    scene bg a128
    play music "music/bensound-thejazzpiano.ogg"
    show dziekan casual at left
    dziekan "Witajcie, studenci. Widzę, że coś mało Was dzisiaj. Trochę się tego nie spodziewałem, po ostatnim wykładzie."
    dziekan "Przekażcie reszcie, by jednak na ten wykład chodzili. W tym semestrze mam zdecydowanie za wiele na głowie i nie będę miał czasu sprawdzać wszystkim zaliczenia"
    
    play sound "music/sounds/audience_laughter1.mp3"
    
    dziekan "Mówiąc o zaliczeniach. Widzieliście juz JD3.0 w akcji?"
    show stud1 at right
    "Random1" "Tak, wczoraj sprawdzał nasze kartkówki."
    hide stud1
    dziekan "Hohoho. Cieszę się, że dobrze sobie radzi. To ważna rzecz na naszej uczelni. Grupa studentów pod kierownictwem dr Zawadzkiego przez 5 lat pracowała nad tym systemem."
    dziekan "Jego pełna nazwa to Java Data Analyzer Calibrated with Self-Learning Machine System. Nazwa bardzo długa, a skrót byłby zupełnie idiotyczny. Dlatego zostaliśmy przy JD do czasu, aż ktoś wpadnie na lepszy pomysł."
    dziekan "Nie pytajcie, kto wymyślił tę nazwę. Na naszym wydziale zawsze jest ciężko z nazewnictwem."
    play sound "music/sounds/audience_laughter1.mp3"
    dziekan "Projektowanie sztucznej inteligencji to nie jest takie hop siup. Zresztą sami zobaczycie na 3 roku jak będziecie mieli zajęcia z doktorem Zawadzkim."
    hide dziekan casual
    show stud1 at left
    "Random2" "Super...straszcie nas dalej. Nie wiadomo nawet czy przejdziemy na drugi semestr..."
    show stud2 at right
    "Random3" "Zawsze byłeś bardzo optymistycznie nastawiony do życia. Radość aż z Ciebie się wylewa."
    hide stud1
    hide stud2
    show dziekan casual at left
    dziekan "No dobrze. Chyba nikt już nie dojdzie. Zacznijmy wreszcie wykład"
    
    scene black
    show text "{color=#FFF}Wykład...{/color}"
    pause 2
    
    scene bg a128
    show dziekan casual at left
    dziekan "Na dzisiaj chyba zakończymy. Do zobaczenia na następnym wykładzie. Przekażcie moją wiadomość nieobecnym, hehehehe."
    
    scene bg korytarz
    play music "music/bensound-sweet.ogg"
    if i == 1:
        show main1
    elif i == 2:
        show main2
    elif i == 3:
        show main3

    if marta_zostala_uspokojona:
        show marta at left
        marta "Uch och.....hejka. Wybacz, że mnie nie było. Zaspałam."
        m "Witaj. Spoko, mam notatki jak coś. Uważaj następnym razem. Jeśli chcesz mieć gwarantowane 3 to powinnaś chodzić na te wykłady."
        marta "Wiem, wiem. Budzik ostatnio mi w telefonie wariuje. Raz dzwoni a raz nie."
        m "Jeśli chcesz, to mogę do Ciebie dzwonić rano, do czasu, aż wszystko wróci do normy."
        marta "Naprawdę? Dzięki, kochana. Idziemy na następne zajęcia?"
        m "Tak, chodźmy. Mam dla Ciebie dobrą wiadomość. Chyba Amandy dzisiaj nie będzie..."
    else:
        m "Wykład znowu bardzo ciekawy. Mam nadzieję, że moje notatki będą dobre"
        m "Czas na kolejne zajęcia. Chociaż tak się dziś czuję, że wróciłabym do domu"
        m "Jedyne co dziś mnie trzyma to moja motywacja. Nie mogę mieć żadnych zaległości."
        m "Chyba Amandy dzisiaj nie będzie. Warto wykorzystać jakoś ten cud..."

    scene bg white
    show text "{color=#000000}Środa{/color}"
    pause 2
    play music "music/bensound-rumble.ogg"
    scene bg park
    if i == 1:
        show main1
    elif i == 2:
        show main2
    elif i == 3:
        show main3

    if marta_zostala_uspokojona:
        show marta at left
        m "Środa....a co to oznacza?"
        marta "Ikar...nie lubię tego gościa. Czuję, że będziemy mieli za tydzień przewalone u niego"
        m "Z takim podejściem to na pewno. Musimy wziąć się w garść. Trzeba to obalić."
        show adam_view at right
        adam "Podziwiam Wasze zaparcie, ale musicie być bardzo czujne podczas zaliczenia u niego."
        menu:
            "Kim jesteś?":
                m "Dzięki za ostrzeżenie...kimkolwiek jesteś..."
                marta "O, cześć Adam. Wy się jeszcze nie znacie. To jest Adam. Poznaliśmy się na WFie."
                $ adam = Character("Adam", what_slow_cps=20) 
                m "Miło mi poznać. Wybacz, za takie przywitanie. Miało być żartobliwe."
                adam "Hahaha, załapałem od razu. Mnie też miło Cię poznać."
                jump po_przywitanie_adam
            "Chyba nie może być aż tak źle?":
                m " Chyba nie może być aż tak źle, co?"
                marta "O, cześć Adam. Wy się jeszcze nie znacie. To jest Adam. Poznaliśmy się na WFie."
                $ adam = Character("Adam",what_slow_cps=20)
                m "Miło mi Cie poznać, Adamie."
                adam "Mnie również miło. Zaintrygowała mnie Wasza rozmowa dlatego dołączyłem."
        label po_przywitanie_adam:
            adam "O Ikarze mnóstwo złych rzeczy słyszałem Podobno uczy tu z przymusu."
            marta "Jakoś mnie to nie dziwi, wiesz..."
            adam "Nie wiem o co poszło, ale podobno przez parę przewinień Rektor kazał mu nauczać kilku przedmiotów. Wcześniej tylko realizował się tutaj naokoło."
            m "Sądzisz, że chce tak na odwal się prowadzić te zajęcia by szefostwo dało mu spokój."
            adam "Tak się mówi. Nawet wśród wykładowców nie jest on lubiany. Facet za wielkie mniemanie o sobie."
            marta "Warto wiedzieć. Będziemy musieli bardziej się przyłożyć na tych zajęciach..."
    else:
        m "Środa....a co to oznacza? Ikar..."
        m "Nie lubię tego gościa. Czuję, że będę miała za tydzień przewalone u niego"
        m "Muszę wziąć się w garść. Trzeba obalić tego kolosa."
        show adam_view at right
        adam "Podziwiam determinację, ale musisz być bardzo czujna podczas zaliczenia u niego."
        m "Dzięki za ostrzeżenie...kimkolwiek jesteś..."
        adam "Wybacz, jestem Adam. Słyszałem Twoje narzekania i dlatego się wtrąciłem."
        $ adam = Character("Adam",what_slow_cps=20)
        m "Miło mi poznać. Wybacz, za takie przywitanie. Miało być żartobliwe."
        adam "Hahaha, załapałem od razu. Mnie też miło Cię poznać."
        adam "O Ikarze mnóstwo złych rzeczy słyszałem Podobno uczy tu z przymusu."
        m "Jakoś mnie to nie dziwi, wiesz..."
        adam "Nie wiem o co poszło, ale podobno przez parę przewinień Rektor kazał mu nauczać kilku przedmiotów. Wcześniej tylko realizował się tutaj naokoło."
        m "Sądzisz, że chce tak na odwal się prowadzić te zajęcia by szefostwo dało mu spokój."
        adam "Tak się mówi. Nawet wśród wykładowców nie jest on lubiany. Facet za wielkie mniemanie o sobie."
        m "Warto wiedzieć. Będziemy musieli bardziej się przyłożyć na tych zajęciach..."
    
    scene bg a129
    play music "music/bensound-straight.ogg"
    show ikar at left
    ikar "Jakże miło mi Was znów widzieć. Jestem zaszczycony. Chciałbym przypomnieć, że za tydzień kolokwium decydujące o Waszym podejsciu do egzaminu."
    ikar "Mam nadzieję, że do tego się przyłożycie Nie będę później wysłuchiwał błagań o podwyższenie oceny i innych takich. Brakuje punkta? No to trudno."
    hide ikar
    show stud1 at left
    "Random2" "Nie mogę patrzeć na tego gościa. Dziwne, że nikt go jeszcze nie zgłosił."
    show stud2 at right
    "Random3" "On co roku figuruje w ankietach. Jednak nikt nie chce go stąd ruszyć."
    "Random1" "Panie profesorze, czy te kolokwia, też będzie sprawdzał JD3.0?"
    hide stud1
    hide stud2
    show ikar at left
    ikar "Hahhhahahaha, nie. Osobiście będę sprawdzał Wasze wypociny. Sprzęt Zawadzkiego może i jest dobry, ale nie sądzę by podołał doczytaniu się to studenckich wywijasów."
    hide ikar
    #pokazywanie głównej postaci
    if i == 1:
        show main1
    elif i == 2:
        show main2
    elif i == 3:
        show main3
    m "Świetnie. Chyba sprawia mu przyjemność uwalanie studentów. Dlatego nie może tego zostawić maszynie."
    if i == 1:
        hide main1
    elif i == 2:
        hide main2
    elif i == 3:
        hide main3
    show ikar at left
    ikar "Drogocenny czas wykładu mija. Jeśli czegoś nie zdążymy przerobić to będziecie musieli sami sobie poradzić. 
    Student przede wszystkim sam powinien się uczyć."
    hide ikar
    #pokazywanie głównej postaci
    if i == 1:
        show main1
    elif i == 2:
        show main2
    elif i == 3:
        show main3
    m "Niech ten wykład jak najszybciej się skończy..."
    scene black
    show text "{color=#FFF}Wykład...{/color}"
    pause 2

    scene bg korytarz
    play music "music/bensound-rumble.ogg"
    #pokazywanie głównej postaci
    if i == 1:
        show main1
    elif i == 2:
        show main2
    elif i == 3:
        show main3
    if marta_zostala_uspokojona:
        show marta at left
        show adam_view at right
        m "Gościu nawet się z nami nie pożegnał. Trochę kiepski przykład daje innym."
        marta "Coś czuję, że dzień przed kolosem będę miała srogie koszmary."
        m "Razem się pouczymy i jakoś damy sobie z tym radę."
        adam "Można by powiedzieć, że zachowujecie się prawie jak siostry, hehehe."
        marta "Jeżeli to komplement to bardzo za niego dziękujemy. To miłe."
        m "Zgadzam się."
        hide adam_view
        play music "music/bensound-scifi.ogg"
        show draco at right
        malfoy "Bardzo miłe...siostrzyczki sierotki."
        menu:
            "zareaguj":
                m "Jak ja bardzo za Tobą tęskniłam. Już myślałam, że może ten Twój charakter uległ zmianie"
                malfoy "Daruj sobie takie teksty. Zobaczymy jak sobie poradzicie za tydzień. nie mogę się doczekać 
                Waszych zapłakanych min"
                jump sprzeczka_draco_11
            "nic nie rób":
                hide marta
                show adam_view at left
                adam "Daj im spokój, kobieto. Idź być toksyczna gdzie indziej."
                malfoy "Brawo. Dorobiłyście się własnego obrońcy. Czyżbyście już nie radziły sobie ze mną same?"
                hide adam_view
                show marta at left
                marta "Amanda,  ja bardzo za Tobą tęskniłam. Już myślałam, że może ten Twój charakter uległ zmianie"
                malfoy "Daruj sobie takie teksty. Zobaczymy jak sobie poradzicie za tydzień. nie mogę się doczekać 
                Waszych zapłakanych min."
                jump sprzeczka_draco_11
        label sprzeczka_draco_11:
            hide draco
            hide marta
            hide adam_view
            show marta at left
            show adam_view at right
            marta "Chodźmy. Rzygać mi się chcę, jak ją widzę."
            adam "Macie dosyć ciekawego wroga. Uważajcie. Ta dziewczyna ma tutaj niezłe wpływy."
            m "Wiemy, wiemy. Chody nie pomogą jej zaliczyć ten przedmiot. Ikar nikogo nie będzie faworyzował."
            marta "Jedyna rzecz, za którą można go lubić. Adam, skąd Ty taki obeznany w uczelnianych plotkach?"
            adam "Akademik. Jedno słowo, a mówi tak wiele."
            m "Hahaha...taka wiedza też się przydaje. Oprócz wiedzy technicznej uczymy się jak przetrwać."
            marta "Przyda Nam się to, jak będziemy pracować w jakimś korpo. Dobra, to co teraz mamy?"
    else:
        show adam_view at left
        m "Gościu nawet się z nami nie pożegnał. Trochę kiepski przykład daje innym."
        adam "Coś czuję, że dzień przed kolosem będę miała srogie koszmary."
        m "Musimy zmaksymalizować nasze szanse na zdanie. Jak zaczniemy się wcześniej uczyć, to damy rade"
        adam "Słowo daję, Jesteś największą optymistką jaką znam."
        m "Jeżeli to komplement to bardzo za niego dziękuję. To miłe."
        play music "music/bensound-scifi.ogg"
        show draco at right
        malfoy "Heyo. Grupa wsparcia przed nieuchronnym oblaniem?"
        adam "Daj nam spokój, kobieto. Idź być toksyczna gdzie indziej."
        malfoy "Brawo. Dorobiłaś się własnego obrońcy. Czyżbyś już nie radziła sobie ze mną sama?"
        m "Amanda,  ja bardzo za Tobą tęskniłam. Już myślałam, że może ten Twój charakter uległ zmianie"
        malfoy "Daruj sobie takie teksty. Zobaczymy jak sobie poradzicie za tydzień. nie mogę się doczekać Waszych zapłakanych min."
        m "Chodźmy. Rzygać mi się chcę, jak ją widzę."
        hide draco
        adam "Macie dosyć ciekawego wroga. Uważaj. Ta dziewczyna ma tutaj niezłe wpływy."
        m "Wiem, wiem. Chody nie pomogą jej zaliczyć ten przedmiot. Ikar nikogo nie będzie faworyzował."
        m "Heh...jedyna rzecz, za którą można go lubić. Adam, skąd Ty taki obeznany w uczelnianych plotkach?"
        adam "Akademik. Jedno słowo, a mówi tak wiele."
        m "Hahaha...taka wiedza też się przydaje. Oprócz wiedzy technicznej uczymy się jak przetrwać."
        adam "Taa...Przyda Nam się to, jak będziemy pracować w jakimś korpo. Dobra, to co teraz mamy?"
    #KONIEC ŚRODY
    #CZWARTEK
    scene bg white
    show text "{color=#000000}Czwartek{/color}"
    pause 2
    scene bg korytarz
    play music "music/bensound-acousticbreeze.ogg"
    #pokazanie glownej bohaterki
    if i == 1:
        show main1 at left
    elif i == 2:
        show main2 at left
    elif i == 3:
        show main3 at left
    show adam_view at right
    if marta_zostala_uspokojona:
        adam "Marty dzisiaj nie ma?"
        m "Oficjalnie dała sobie spokój z wykładem. Mam jej robić notatki i znich będzie się uczyć na zaliczenie"
        adam "Dostaniesz coś w zamian?"
        m "Jasne. Co tydzień dostaję dużą mleczną czekoladę."
        adam "Hahah...brzmi jak niezły biznes. Chodźmy, zajęcia się zaczynają."
    else:
        adam "Co raz mniej ludzi widzę na tym wykładzie"
        m "Jest nudny jak flaki z olejem. W sumie im się nie dziwię."
        adam "Więc czemu przyszłaś, hę?"
        m "Mogę w tym czasie bez skrupułów czytać książki i uczyć się na inne przedmioty"
        adam "Hahah...brzmi jak niezły plan. Chodźmy, zajęcia się zaczynają."
    scene bg a123
    play music "music/bensound-psychedelic.ogg"
    show teresa at left
    teresa "O widzę, że znowu mała frekwencja na wykładzie. Dalej mnie to nie dziwi."
    teresa "Szczerze? Dałabym Wam ten skrypt i kazała nie przychodzic, no ale za coś mi płacą, tak?"
    play sound "music/sounds/audience_laughter1.mp3"
    teresa "Lekki żart na poprawę humoru i jedziemy z następnym tematem"
    
    scene black
    show text "{color=#FFF}Wykład...{/color}"
    pause 2
    scene bg a123
    show teresa at left 
    teresa "Ok, dłużej męczyć Was nie będę. Do zobaczenia w następnym tygoniu!"
    hide teresa
    show stud1 at right
    "Random1" "Mimo, że wykład nudny jak flaki z olejem, to kobitka całkiem w porządku."
    hide stud1
    if i == 1:
        show main1 at left
    elif i == 2:
        show main2 at left
    elif i == 3:
        show main3 at left
    play music "music/bensound-sunny.ogg"
    show adam_view at right
    if marta_zostala_uspokojona:
        adam "Racja, dlatego chodzę na ten wykład. Jakby było inaczej to bym to odpuścił sobie."
        m "Co z notatkami?"
        adam "Mam notatki z tamtego roku od kolegów. Przeglądając je widzę, że nic się na ten moment nie zmieniło"
        m "Akademikowa brać silna jest jak widzę. Pożyczysz mi notatki? Może i ja odpuszczę sobie ten wykład. Mogłabym w domu więcej się pouczyć."
        adam "Zgłupiałaś? Zmarnujesz szansą na tony czekolady."
        m "Na śmierć zapomniałam. Rzuciłeś mocnym argumentem."
        adam "Zaczynam robić za głos rozsądku hehehe."
    else:
        adam "Racja, dlatego chodzę na ten wykład. Jakby było inaczej to bym to odpuścił sobie."
        m "Co z notatkami?"
        adam "Mam notatki z tamtego roku od kolegów. Przeglądając je widzę, że nic się na ten moment nie zmieniło"
        m "Akademikowa brać silna jest jak widzę. Pożyczysz mi notatki? Może i ja odpuszczę sobie ten wykład. Mogłabym w domu więcej się pouczyć."
        adam "Popytam, czy mogę. Jeśli tak to nie widzę problemu."
        m "Dzięki wielkie. Teraz tylko wytrwać do piątku i weekend...."
        adam "Który będzie zawalony nauką na Ikara. Bombowo....."
    
    scene bg white
    show text "{color=#000000}Piątek{/color}"
    pause 2
    play music "music/bensound-rumble.ogg"
    scene bg korytarz
    if i == 1:
        show main1
    elif i == 2:
        show main2
    elif i == 3:
        show main3
    if marta_zostala_uspokojona:
        show marta at left
        marta "Zieeeew....Uczyłam się całą noc na matmę. Mam nadzieję, że sobie poradzimy."
        m "Damy radę, trzeba zetrzeć ten uśmiech z twarzy Amandy. Nie sądzę byśmy miały jakieś trudności z tym."
        play music "music/bensound-scifi.ogg"
        show draco at right
        malfoy "Na moje oko wyglądacie na takie co nawet tabliczki mnożenia nie potrafią się nauczyć."
        marta "Musisz irytować? Próbuję się skupić na powtarzaniu."
        malfoy "To i tak Ci nic nie da. Lepiej myśl już o zapłaceniu za powtarzanie."
        menu:
            "Zareaguj":
                m "Musisz nam przeszkadzać bo inaczej bys z niami przegrała, co?"
                malfoy "Nie rozśmieszaj mnie. Lat świetlnych by wam nie starczyło do osiągnięcia mojego poziomu."
                m "Lata świetlne to jednostka odległości..."
                malfoy "Argh....dajcie mi spokój..."
                marta "Gratulacje. Trzeba częściej ją kontrować i będziemy mieć spokojniejsze studia. Chodźmy, zaraz się zacznie."
                jump sprzeczka_draco_12
            "Idziesz do sali":
                m "Dajmy sobie spokój. Niech sobie pogada z kimś na jej poziomie. Na przykład ścianą."
                malfoy "Mocna tylko w gębie..."
                jump sprzeczka_draco_12
    else:
        show adam_view at left

        m "Zieeeew....Uczyłam się całą noc na matmę. Mam nadzieję, że sobie poradzę."
        adam "Damy radę, trzeba zetrzeć ten uśmiech z twarzy Amandy. Nie sądzę byśmy miały jakieś trudności z tym."
        play music "music/bensound-scifi.ogg"
        show draco at right
        malfoy "Na moje oko wyglądacie na takich co nawet tabliczki mnożenia nie potrafią się nauczyć."
        m "Musisz irytować? Próbuję się skupić na powtarzaniu."
        malfoy "To i tak Ci nic nie da. Lepiej myśl już o zapłaceniu za powtarzanie."
        menu:
            "Zareaguj":
                m "Musisz nam przeszkadzać bo inaczej bys z niami przegrała, co?"
                malfoy "Nie rozśmieszaj mnie. Lat świetlnych by wam nie starczyło do osiągnięcia mojego poziomu."
                m "Lata świetlne to jednostka odległości..."
                malfoy "Argh....dajcie mi spokój..."
                adam "Gratulacje. Trzeba częściej ją kontrować i będziemy mieć spokojniejsze studia. Chodźmy, 
                zaraz się zacznie."
                jump sprzeczka_draco_12
            "Idziesz do sali":
                m "Dajmy sobie spokój. Niech sobie pogada z kimś na jej poziomie. Na przykład ścianą."
                malfoy "Mocna tylko w gębie..."
                jump sprzeczka_draco_12

label sprzeczka_draco_12:
    scene bg a128
    play music "music/bensound-house.ogg"
    show iza at left
    Izabella  "Witajcie, kochani. Czas na kolejny wykład z analizy. Czeka nas dużo pracy, więc zacznijmy temat jak najszybciej."
    hide iza
    show stud1 at left
    "Random1" "Hej...czyżby zapomniał o kolosie?"
    show stud2 at right
    "Random2" "W sumie to dobrze. Nie miałem czasu się przygotować."
    hide stud1
    hide stud2
    show iza at left
    Izabella "Oj....wybaczcie. Przypomniało mi się, że mamy kolosa. Szykujcie kartki a ja przygotuję JD3.0."
    show stud1 at right
    "Random1" "Wykrakałem."
    hide stud1
    Izabella "Zasady są proste. Macie do policzenia jedną granicę. JD3.0 oceni jak Wam poszło. Gotowi? Czas start!"
    jump mat_kart1
label back_wyklad_mat_2_cd:
    
    scene bg a128
    show iza at left
    Izabella "Widzę, że wszyscy już skończyli. Teram możemy zająć się kolejnym tematem zajęć."
    Izabella "Radzę Wam się skupić, gdyż temat jest dosyć istotny. Zacznijmy więc."

    scene black
    show text "{color=#FFF}Wykład...{/color}"
    pause 2
    
    scene bg a128
    show iza at left
    Izabella "No dobrze. Myślę, że możemy na dziś zakończyć. Jak tam kartkówki, JD?"
    "JD3.0" "BiP BIP BIP BOOOOOOOOOOOOOOOOOOP"
    Izabella "Wszystko jest już sprawdzone. Nawet nieźle Wam poszło. Mam nadzieję, że następna pójdzie jeszcze 
    lepiej. Trzymajcie ciepło moje kruszynki się."
    
    #testowa wartosc
    #python:
        #ocena_kart1_mat = 3
    hide iza

    scene bg white
    show text "{color=#000000}Twoja ocena: [ocena_kart1_mat]{/color}"
    pause 5

    scene bg a128
    if i == 1:
        show main1
    elif i == 2:
        show main2
    elif i == 3:
        show main3
    play music "music/bensound-acousticbreeze.ogg"
    if marta_zostala_uspokojona:
        show marta at left
        marta "Jak Ci poszło?"
        if ocena_kart1_mat > 2:
            m "Bez problemu zaliczone. Nie było to aż takie trudne. Jak u Ciebie?"
            marta "No, tym razem mi nie poszło. Nie przejmuj się. Na następnej sobie poradzę"
            m "Na następnej to będziesz lepiej przygotowana. Pomogę Ci."
            if piwo_piatek2 == False:
                marta "Jesteś kochana. Chciałabyś wyjść na piwo? Uczcimy Twój sukces."
                menu:
                    "tak":
                        $ piwo_piatek3 = True
                        marta "Zobaczysz, bedzie Super"
                        jump end_chapter3
                    "nie":
                        $ piwo_piatek3 = False
                        m "Muszę odmówić.  Po tym wszystkim jestem padnięta. Potrzebuję się zdrzemnąć. Innym razem."
                        marta "Też się chyba zdrzemnę. Trzymaj się. Widzimy się w poniedziałek!"
                        jump end_chapter3
            else:
                marta "Razem na pewno damy sobie radę. Muszę znikać. Jadę dziś do babci na weekend. Widzimy się w poniedziałek!"
                m "Pa pa. Baw się dobrze!"
                jump end_chapter3
        else:
            m "Nie udało się. Najwidoczniej za mało umiem. A Tobie?"
            marta "No, tym razem mi nie poszło. Nie przejmuj się. Na następnej sobie poradzimy"
            show draco at right
            malfoy "Słyszałam, że podwyższyli opłatę za powtarzanie, wiesz? Na Twoim miejscu bym już zbierała forsę, hehehe...."
            hide draco
            m "Na następnej będziemy lepiej przygotowane! Nie damy się tak łatwo. Razem będziemy się uczyć"
            if piwo_piatek2 == False:
                marta "No i to rozumiem. Chciałabyś wyjść na piwo? Trochę się wyluzujemy."
                menu:
                    "tak":
                        $ piwo_piatek3 = True
                        marta "Zobaczysz, bedzie Super"
                        jump end_chapter3
                    "nie":
                        $ piwo_piatek3 = False
                        m "Muszę odmówić.  Po tym wszystkim jestem padnięta. Potrzebuję się zdrzemnąć. Innym razem."
                        marta "Też się chyba zdrzemnę. Trzymaj się. Widzimy się w poniedziałek!"
                        jump end_chapter3
            else:
                marta "Razem na pewno damy sobie radę. Muszę znikać. Jadę dziś do babci na weekend. Widzimy się w poniedziałek!"
                m "Pa pa. Baw się dobrze!"
    else:
        show adam_view at left
        adam "Jak Ci poszło?"
        if ocena_kart1_mat > 2:
            m "Bez problemu zaliczone. Nie było to aż takie trudne. Jak u Ciebie?"
            adam "Mi też. Nie było problemu. Dosyć łatwe dziś dał."
            m "Cieszę się, że Nam się udało. Kolejny stopień do zwycięstwa!"
            adam "Super!  Dzień można uznać za udany. Chciałabyś wyjść na piwo? Uczcimy Twój sukces."
            menu:
                "tak":
                    $ piwo_piatek3 = True
                    jump end_chapter3
                "nie":
                    $ piwo_piatek3 = False
                    m "Muszę odmówić.  Po tym wszystkim jestem padnięta. Potrzebuję się zdrzemnąć. Innym razem."
                    adam "Też się chyba zdrzemnę. Trzymaj się. Widzimy się w poniedziałek!"
                    jump end_chapter3
        else:
            m "Nie udało się. Najwidoczniej za mało umiem. A Tobie?"
            adam "Mi się jakoś udało. Nie bierz tego aż tak do siebie. musisz po prostu więcej popracować."
            show draco at right
            malfoy "Słyszałam, że podwyższyli opłatę za powtarzanie, wiesz? Na Twoim miejscu bym już zbierała forsę, hehehe...."
            hide draco
            adam "Na następnej będziesz lepiej przygotowana! Nie dawaj się tak łatwo. Pomogę Ci w razie czego."
            m "Och, dzięki wielkie. Jesteś super. Masz rację. Tanio skóry nie sprzedam. "
            adam "No i to rozumiem. Chciałabyś wyjść na piwo? Trochę się wyluzować?"
            menu:
                "tak":
                    $ piwo_piatek3 = True
                    jump end_chapter3
                "nie":
                    $ piwo_piatek3 = False
                    m "Muszę odmówić.  Po tym wszystkim jestem padnięta. Potrzebuję się zdrzemnąć. Innym razem."
                    adam "Też się chyba zdrzemnę. Trzymaj się. Widzimy się w poniedziałek!"
                    jump end_chapter3
label end_chapter3:
    jump chapter4
    return