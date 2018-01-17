init:
    image bg przed_weeia = "weeia.jpg"
    image bg las1 = "las1.jpg"
    image bg las2 = "las2.jpg"
    image bg szpital = "szpital.jpg"
    define Lekarz = Character("Pani Doktor", what_slow_cps=20)
label chapter4:
    scene black
    show text "{color=#FFF}{size=+30}Chapter 4\nTydzień trzeci{/size}{/color}"
    pause 2
    play music "music/bensound-rumble.ogg"
    scene bg white
    show text "{color=#000000}Poniedziałek{/color}"
    pause 2
    
    scene bg park
    if i == 1:
        show main1
    elif i == 2:
        show main2
    elif i == 3:
        show main3
    #python:
        #marta_zostala_uspokojona = False
        #ocena_kart2_pp1 = 4

    m "Co raz ciężej jest na tych studiach. Na początku myślałam, że nie będę mieć żadnych problemów. 
    Teraz muszę zweryfikować swoje poglądy."
    m "To prawda, zajęcia są bardzo ciekawe i dużo się z nich dowiedziałam, ale..."
    m "...ta presja powoli mnie wykańcza. Jeszcze ten zakład dodaje mi stresu."
    m "Może dać sobie z tym spokój i skupić się na tym co tak naprawdę ważne? Olać 
    Amandę i ściągnąć z siebie jeden ciężar?"
    m "Gdyby to było takie łatwe. Obiecałam sobie, że ją pokonam. Zniszczę jej pewność 
    siebie i udowodnię, że nie jest najlepsza. Osiągnę to, co zaplanowałam!"
    m "Zastanawiam się tylko..."

    if marta_zostala_uspokojona:
        show marta at left
        marta "Heeeej! Co taka smutna jesteś?"
        m "Hejka, Marta. Prawie zawału dostałem! Nie jestem smutna.  Zastanawiam się..."
        marta "Nad dzisiejszą kartkówką? Dzisiaj obie ją rozwalimy! Uczyłyśmy się przecież cały weekend!"
        m "O to się nie martwię. Z tym sobie na pewno poradzimy. Rozmyślam na temat Amandy..."
        marta "Coś Ci zrobiła? Co się stało?"
        m "Wiesz...jest wredna, pyszałkowata, denerwuje mnie strasznie...ale zastanawiałaś 
        się o co jej chodzi? Czemu jest taka wredna? Każdy człowiek ma jakiś powód lub motywację." 
        marta "Pochodzi z bogatej rodziny. Pewnie ją rozpieszczają strasznie i stąd takie efekty. Myślę, 
        że zadręczasz się niepotrzebnymi rzeczami. Pośpieszmy się, bo spóźnimy się na zajęcia."
        m "Chyba masz rację..."
    else:
        show adam_view at left
        adam "Hejka! Co taka smutna jesteś?"
        m "Cześć, Adam! Prawie zawału dostałam! Nie jestem smutna.  Zastanawiam się..."
        adam "Nad dzisiejszą kartkówką? Powinniśmy ją rozwalić! Sama mówiłaś, że cały weekend będziesz się do niej uczyć."
        m "O to się nie martwię. Z tym sobie na pewno poradzimy. Rozmyślam na temat Amandy..."
        adam "Coś Ci zrobiła? Co się stało?"
        m "Wiesz...jest wredna, pyszałkowata, denerwuje mnie strasznie...ale zastanawiałeś się o co jej chodzi? Czemu jest taka wredna? Każdy człowiek ma jakiś powód lub motywację." 
        adam "Pochodzi z bogatej rodziny. Pewnie ją rozpieszczają strasznie i stąd takie efekty. Myślę, że zadręczasz się niepotrzebnymi rzeczami. Pośpieszmy się, bo spóźnimy się na zajęcia."
        m "Chyba masz rację..."
    

    scene bg a123
    show stud1 at left
    "Random1" "Ej, może ten komputer się popsuł, czy coś? Strasznie nie chce mi się dzisiaj tego pisać..."
    show stud2 at right
    "Random2" "Jesteś żałosny, skoro zamiast uczyć się marnujesz czas na myślenie życzeniowe."
    "Random1" "Odczep się ode mnie, dobra? Uczyłem się, ale to nie znaczy, że nie mogę sobie trochę pomarzyć"
    "Random2" "Taa...jasne..."
    show adam_view
    adam "Dobra chłopaki, darujcie sobie. Zajęcia już się zaczynają. Powodzenia na kartkówce!"
    hide stud1
    hide stud2
    hide adam_view
    ###----------------------
    play music "music/bensound-jazzcomedy.ogg"

    show opiekun at left
    opiekunroku "Dzień dobry, wszystkim. Sądzę, że możemy od razu przejść do rzeczy. Uwińmy się z tym szybko bo mamy sporo do omówienia na wykładzie."
    hide opiekun
    show stud2
    "Random1" "Ehh....a jednak..."
    hide stud2
    show opiekun at left
    opiekunroku "JD3.0! Gotowy do działania?"
    "JD3.0" "BIP BIP BIP BIIIIIIIIIIIIIIIIIIIIIIP!"
    opiekunroku "To dobrze. Zacznijmy wreszcie kartkówkę!"
    hide opiekun
    show stud1
    "Random2" "Czy ktoś w ogóle rozumie, co ta maszyna mówi? Czuję się trochę jak w jakiś gwiezdnych wojnach..."
    stop music
    #skaczemy do kartkówki
    jump pp1_kart2
    #wracamy
label back_wyklad_pp1_3_cd:
    scene bg a123
    play music "music/bensound-jazzcomedy.ogg"
    show opiekun at left
    opiekunroku "Sądzę, że chyba wszyscy już skończyli. Jak zwykle po zajęciach dowiecie się, jak Wam poszło."
    hide opiekun
    show adam_view at left
    adam "Dzisiaj dowalono nam znacznie trudniejsze rzeczy. Mam nadzieję, że chociaż to zaliczę."
    show stud1 at right
    "Random3" "Ja też! Przy trzecim to ja nawet nie miałem pojęcia o co chodzi!"
    hide stud1
    hide adam_view
    show opiekun at left
    opiekunroku "Proszę wszystkich o spokój. Przejdźmy już do dzisiejszego wykładu!"

    scene black
    show text "{color=#FFF}Wykład...{/color}"
    pause 2

    scene bg a123
    show opiekun at left
    opiekunroku "Na tym dzisiaj chyba zakończymy zajęcia. Nie chcę Was aż tak torturować. 
    Macie też inne zajęcia. Widzimy się na następnych zajęciach, kochani!"
    hide opiekun
    show stud1 at right
    "Random3" "Jeej....niektórzy wykładowcy to serio dobre ziomki. Niech tylko Ikar zluzuje 
    trochę i nie będę na nic narzekać."
    show stud2 at left
    "Random2" "Ty i brak narzekań? Chciałbym to zobaczyć hhahahaha..."
    hide stud1
    hide stud2
    show opiekun at left
    opiekunroku "Byłabym zapomniała. J.D3.0 sprawdził Wasze prace. Wyświetl wyniki, J.D!"
    "J.D3.0" "BIP BIP BIP BIIIIIIIIIIIIIIIIIP BOOOOOOOOOP!"
    
    scene bg white
    show text "{color=#000000}Twoja ocena: [ocena_kart2_pp1]{/color}"
    pause 2

    scene bg korytarz
    if i == 1:
        show main1
    elif i == 2:
        show main2
    elif i == 3:
        show main3
    play music "music/bensound-sunny.ogg"
    if marta_zostala_uspokojona:
        show marta at left
        show adam_view at right
        marta "YES! YES! YES! Zaliczone!!!! To dzięki tej wspólnej nauce. Razem możemy wszystko!"
        adam "Mi też świetnie poszło.  Na początku się bałem, że nie zaliczę. Miałem dzisiaj farta!"
        marta "A Tobie ja poszło?"
        if ocena_kart2_pp1 >= 3:
            m "To była bułka z masłem! Osiągnęłam kolejny poziom! Czasem chciałabym, żeby nad 
            głowami ludzi był pasek postępu jak w grach, hahahaha"
            marta "Wiedziałam, że dobrze Ci pójdzie. Razem możemy mieć wszystko, moja droga!"
            adam "Gratuluję Wam obu. Dzisiejszy dzień należy do tych udanych."
            marta "To prawda! Chodźmy już. Spóźnimy się na następne zajęcia. Ostatnio kobitka 
            groziła, że za spóźnienia będzie odejmować punkty z egzaminu!"
            m "Racja, lećmy już. Czasem zastanawiam się, kto im wszystkim wpada na takie pomysły. 
            To musi być jeden wredny gość, co bardzo nie lubi studentów..."
        else:
            m "Cieszę się, że wam się udało. Mi niestety dzisiaj nie poszło..."
            marta "Żartujesz! To nie jest możliwe!"
            m "Jednak jest....Nie przejmujcie się mną. Nie chcę psuć Waszego tryumfu."
            adam "Daj spokój. Może pójdziesz następnym razem na godziny przyjęć? Dowiesz się co robisz 
            źle i następnym razem wyjdzie  Ci lepiej."
            marta "No właśnie! To Ci na pewno pomoże. Skoro ja potrafiłam zaliczyć to Ty tym bardziej."
            m "Pewnie macie rację. Chodźcie już. Ostatnio kobitka groziła, że za spóźnienia będzie 
            odejmować punkty z egzaminu!"
            marta "No ok. Nie poddawaj mi się tylko!"
    else:
        show adam_view at right
        adam "Lepiej mi pójść nie mogło!  Na początku się bałem, że nie zaliczę. Miałem dzisiaj farta! 
        Jak Tobie ja poszło?"
        if ocena_kart2_pp1 >= 3:
            m "To była bułka z masłem! Osiągnęłam kolejny poziom! Czasem chciałabym, żeby nad 
            głowami ludzi był pasek postępu jak w grach, hahahaha"
            adam "Wiedziałem, że dobrze Ci pójdzie. Dużo się uczyłaś i zasłużyłaś na zwycięstwo!"
            m "Dzięki! Chodźmy już. Spóźnimy się na następne zajęcia. Ostatnio kobitka groziła, że 
            za spóźnienia będzie odejmować punkty z egzaminu!"
            adam "Racja, lećmy już. Czasem zastanawiam się, kto im wszystkim wpada na takie pomysły. To 
            musi być jeden wredny gość, co bardzo nie lubi studentów..."
        else:
            m "Cieszę się, że wam się udało. Mi niestety dzisiaj nie poszło..."
            adam "Żartujesz! To nie jest możliwe! Uczyłaś się cały weekend..."
            m "Jednak jest....Nie przejmuj. Nie chcę psuć Twojego tryumfu."
            adam "Daj spokój. Może pójdziesz następnym razem na godziny przyjęć? Dowiesz się co robisz źle i
             następnym razem wyjdzie  Ci lepiej."
            m "Pewnie masz rację. Chodźmy już. Ostatnio kobitka groziła, że za spóźnienia będzie 
            odejmować punkty z egzaminu!"
            adam "No ok. Nie poddawaj mi się tylko!"

    scene bg white
    show text "{color=#000000}Wtorek{/color}"
    pause 2
    play music "music/bensound-sweet.ogg"
    scene bg korytarz
    if i == 1:
        show main1
    elif i == 2:
        show main2
    elif i == 3:
        show main3
    if marta_zostala_uspokojona:
        show marta at left
        m "Miałam dzisiaj dać sobie spokój z wykładem. Nie za dobrze się czuję."
        marta "Może zjadłaś wczoraj coś nieświeżego?"
        m "Ojciec wczoraj zrobił burrito na obiad. Zachciało mu się eksperymentować z meksykańską kuchnią."
        marta "Twój tata to naprawdę zakręcony facet. Następnym razem niech może weźmie się za kuchnię włoską. 
        Zdecydowanie lżejsza od meksykańskiej."
        m "Hhahahaha...na pewno mu przekażę"
        show dziekan casual at right
        dziekan "Przepraszam, panno Kowalska. Czy mógłbym zająć moment?"
        marta "Ja skoczę do toalety. Widzimy się na wykładzie!"
        hide marta
    else:
        show adam_view at left
        m "Miałam dzisiaj dać sobie spokój z wykładem. Nie za dobrze się czuję."
        adam "Może zjadłaś wczoraj coś nieświeżego?"
        m "Ojciec wczoraj zrobił burrito na obiad. Zachciało mu się eksperymentować z meksykańską kuchnią."
        adam "Widzę, że Twój ojciec to ciekawy facet. Następnym razem niech może weźmie się za kuchnię włoską. 
        Zdecydowanie lżejsza od meksykańskiej."
        m "Hhahahaha...na pewno mu przekażę"
        show dziekan casual at right
        dziekan "Przepraszam, panno Kowalska. Czy mógłbym zająć moment?"
        adam "Ja skoczę do toalety. Widzimy się na wykładzie!"
        hide adam_view
    
    m "Coś się stało, panie profesorze? Jak coś to jestem niewinna!"
    dziekan "Hahhaha...nic z tych rzeczy. Chciałem się zapytać, czy znasz może prof. Stanisława Kowalskiego?"
    m "Tak, znam. To jest mój ojciec."
    dziekan "Coś tak czułem, ale wolałem zapytać.  Byłem jego promotorem kiedy robił inżyniera na tej uczelni. 
    Jak mu się powodzi?"
    menu:
        "Jest dobrze":
            m "Wszystko jest w porządku. Razem z kolegą z powodzeniem rozkręcają swoją firmę MOCRAX. Nie 
            ma w tej chwili na co narzekać!"
            dziekan "Pewnie z Sobocińskim, co? Oni obaj od początku studiów mieli pociąg do systemów sieciowych."
            dziekan "Twój ojciec dobrych parę lat uczył tutaj sieciowych przedmiotów. Miał jednak wyższe ambicje 
            i dlatego wkroczył do świata biznesu."
            jump znam_dziekana
        "Nienajlepiej":
            m "Z firmą nie ma problemu, jednak dalej nie może sobie poradzić ze śmiercią mamy. Bardzo ją kochał."
            dziekan "Tak, to była wspaniała kobieta. Tym bardziej utalentowana. Wszyscy w grupie ją lubili."
            dziekan "Poznali się tutaj, ale na innych kierunkach. Pewnie Staszek Ci o tym powiedział. Kto wie, 
            może i Ty kogoś tutaj znajdziesz, hehe..."
label znam_dziekana:
    dziekan "Ehhh...trochę za nim tu tęsknię. Pozdrów go jak możesz i powiedz by się do mnie odezwał. Dawno się nie widzieliśmy."
    m "Na pewno przekażę. Proszę się o to nie martwić!"
    hide dziekan casual
    play sound "music/sounds/high_heels_footsteps.mp3"
    play music "music/bensound-scifi.ogg"
    show draco at left
    malfoy "Hahaha, no doprawdy żałosne to było widowisko."
    stop sound
    m "O czym Ty mówisz, Amanda? Co Ci się znowu ubzdurało?"
    malfoy "Próbujesz udobruchać dziekana swoimi znajomościami? A podobno to ja jestem ta zła i się wywyższam. 
    Niezła z Ciebie hipokrytka!"
    menu:
        "spław ją":
            m "Chciałabyś. Nie potrzebuję żadnych znajomości by być lepsza od Ciebie. Lepiej się pośpiesz, 
            bo spóźnisz się na wykład."
            malfoy "Nie musisz się o mnie tak troszczyć. Sama dam sobie radę, heh!"
            jump sprzeczka_malfoy123
        "kontratak":
            m "Znajomości, znajomościami. Ty tylko nimi potrafisz się chwalić. Innych umiejętności jakoś nie widzę."
            m "Mogę mieć znanego tu ojca, ale to nie przez niego tu jestem. Sama wybrałam co chcę robić w życiu i 
            swoimi siłami to osiągnę"
            jump sprzeczka_malfoy123
label sprzeczka_malfoy123:
    play sound "music/sounds/high_heels_footsteps.mp3"
    if i == 1:
        hide main1
    elif i == 2:
        hide main2
    elif i == 3:
        hide main3
    malfoy "O Ty mała.....nie dam sobą tak pomiatać. Pozbawię  Cię dumy i pewności siebie, którymi się tak chwalisz."
    stop sound
    malfoy "Hmm...spokojnie. Coś na pewno wymyślę hahahahahaha!"

    scene bg a128
    play music "music/bensound-thejazzpiano.ogg"
    show dziekan casual at left
    dziekan "Witajcie, kochani na kolejnym wykładzie. Dzisiaj nie będziemy mieli aż tak napiętych zajęć. Za niedługo 
    mam posiedzenie rady dlatego skończymy wcześniej nasze elektryczne pogaduchy"
    play sound "music/sounds/audience_laughter1.mp3"
    dziekan "No nic. Zacznijmy jak najszybciej, to mniej będziemy musieli nadrabiać za tydzień!"
    
    scene black
    show text "{color=#FFF}Wykład...{/color}"
    pause 2

    scene bg a128
    show dziekan casual at left
    dziekan "Ja muszę szybko znikać. Widzimy się na następnym wykładzie. Trzymajcie się i do zobaczenia!"
    hide dziekan casual
    if i == 1:
        show main1 at left
    elif i == 2:
        show main2 at left
    elif i == 3:
        show main3 at left
    play music "music/bensound-rumble.ogg"
    if marta_zostala_uspokojona:
        show marta at right
        marta "Czego chciał od Ciebie dziekan?"
        m "Pogadać o moim ojcu. Znają się, ale dawno ze sobą nie gadali. Pytał tylko co u niego słychać."
        marta "Wow...jak myślisz taka znajomość pomoże Ci tutaj?"
        m "Nawet jeśli to nie zamierzam z takiej pomocy korzystać. Swoimi siłami chcę wszystko pozaliczać. 
        Nie chcę być jak Amanda!"
        marta "No i tego się po Tobie spodziewałam, tygrysico! Tak trzymać!"
        m "Tygrysico? O, kurde. Niezłą mi ksywę wymyśliłaś!"
        marta "No co? Idealnie do Ciebie pasuje, hehhehe. Oby jutrzejszy kolos poszedł nam jak najlepiej. 
        Będę mogła się trochę wyluzować"
        m "Prawda. Po zajęciach od razu do nauki. Nie chcę by ten Ikar mnie uwalił..."
    else:
        show adam_view at right
        adam "Czego chciał od Ciebie dziekan?"
        m "Pogadać o moim ojcu. Znają się, ale dawno ze sobą nie gadali. Pytał tylko co u niego słychać."
        adam "Wow...jak myślisz taka znajomość pomoże Ci tutaj?"
        m "Nawet jeśli to nie zamierzam z takiej pomocy korzystać. Swoimi siłami chcę wszystko pozaliczać. 
        Nie chcę być jak Amanda!"
        adam "No i dobrze. Widać, że jesteś porządną osobą!"
        m "Dzięki, Adam. Ostatnio często rzucasz mi komplementami..."
        adam "Komplementy? No coś Ty! Ja jestem po prostu szczery. Oby jutrzejszy kolos poszedł nam jak 
        najlepiej. Będę mógł się trochę odstresować."
        m "Prawda. Po zajęciach od razu do nauki. Nie chcę by ten Ikar mnie uwalił..."
    
    scene bg white
    show text "{color=#000000}Środa{/color}"
    pause 2
    
    scene bg a129
    play music "music/bensound-straight.ogg"
    show ikar at left
    ikar "Tak jak już wcześniej mówiłem, dzisiaj macie kolokwium decydujące o waszym podejściu do egzaminu."
    ikar "Według moich statystyk co roku zdaje ok. 50 procent studentów. Prędzej spodziewam się po Was gorszych 
    ocen niż w ubiegłych latach, ale kto wie? Może w tym roku zostanę zaskoczony."
    #gwar
    hide ikar
    show stud1 at left
    "Random1" "Za takie podejście powinien być od razu wywalony z uczelnii..."
    show stud2 at right
    "Random2" "Szkoda, że prawdopodobnie jest to awykonalne. Nienawidzę gościa."
    hide stud1
    hide stud2
    show ikar at left
    
    ikar  "Proszę o spokój. Za rozmawianie będę wyrzucał z sali!"
    #(sala cichnie)
    ikar "Rozumiem, że wszyscy się uspokoili. Zacznijmy wreszcie kolokwium."
    stop music
    jump tpi_kart1

label back_wyklad_tpi_3_cd:
    scene bg a129
    play music "music/bensound-straight.ogg"
    show ikar at left
    ikar "Czas się skończył. Więcej i tak już nie napiszecie. Po wykładzie dostaniecie wyniki Waszych sprawdzianów"
    show adam_view at right
    adam "Będzie pan sprawdzał nasze prace i jednocześnie prowadził wykład?"
    ikar "Nie bądź niemądry, Czyżewski. Poprosiłem dr Matyldę, by z Wami miała dzisiaj zajęcia. 
    Ja na spokojnie sprawdzę te wypociny..."
    hide adam_view
    #(dzwiek telefonu)
    ikar "Poczekajcie chwilę..."
    hide ikar
    show stud1 at right
    "Random1" "Bojku, ten kolos to była masakra!"
    show stud2 at left
    "Random2" "Zgadzam się z Tobą. Chyba czas oszczędzać pieniądze na punkty."
    hide stud1
    hide stud2
    show ikar at left
    ikar "Muszę natychmiast spotkać się z dziekanem. Sprawa nie cierpiąca zwłoki"
    show draco at right
    malfoy "Może panu pomóc, panie profesorze?"
    ikar "Hmm...możesz się przydać. Zanieść kolokwia i książki do mojego gabinetu. 
    Powinien tam być jeszcze Zawadzki."
    malfoy "Nie ma problemu, profesorze."
    ikar "Tylko żadnych sztuczek, Morawska! Twój ojciec byłby bardzo niezadowolony jakbyś podstępem 
    poprawiała swoją pracę..."

    play sound "music/sounds/high_heels_footsteps.mp3"
    hide ikar
    hide draco

    show stud1 at right
    "Random1" "Wystrzelił jak burza. Ciekawe czego dziekan chce od niego?"
    show stud2 at left
    "Random2" "Może go wreszcie wywali?"
    show adam_view
    adam "Byłoby ciekawie, ale nie sądzę. Jego stąd nikt nie ruszy. Na razie."
    hide stud1
    hide stud2
    hide adam_view
    play music "music/bensound-jazzcomedy.ogg"
    show opiekun at left
    opiekunroku "Witajcie, moi drodzy. Dr Ikar pewnie Wam już powiedział, ale będę miała dzisiaj zastępstwo za niego."
    hide opiekun
    show stud1 at left
    "Random1" "Przynajmniej jeden wykład z tego będzie normalny."
    show stud2 at right
    "Random2" "Na którym i tak się nie skupię, bo za bardzo się stresuję wynikami kolosa."
    show adam_view
    adam "Dajmy sobie na wstrzymanie. Nic już nie zrobimy. Cieszmy się wolnym dniem od Ikara."
    "Random3" "Święte słowa ziomek"
    scene bg a129
    show opiekun at left
    opiekunroku "No dobrze. Możemy już zacząć wykład."
    
    scene black
    show text "{color=#FFF}Wykład...{/color}"
    pause 2

    scene bg a129

    show opiekun at left
    opiekunroku "Na tym dziś zakończymy. Tylko tyle dr Ikar prosił bym z Wami przerobiła. Za parę minut przyjdzie 
    tutaj z wynikami. Życzę powodzenia!"
    hide opiekun
    play music "music/bensound-straight.ogg"
    show ikar at left
    ikar "Jestem z powrotem. Muszę później jeszcze raz podziękować dr Matyldzie. Oszczędziła mi dziś moje gardło i nerwy. "
    ikar "Nie popisaliście się zbytnio. Mówiłem, by więcej się uczyć. Niestety nie wszyscy chyba poważnie traktują 
    ten przedmiot. Dlatego to jest cena za Wasza obojętność."
    ikar "Według moich wyliczeń ok. 20\% zdało kolokwium. Ci, którzy dostali 3 muszą się ostro wziąć do nauki bo 
    egzamin tak prosty nie będzie. Tylko 2 osoby dostały więcej niż 4. Godne pochwały..."
    ikar "Oto Wasze wyniki. Ja muszę zająć się ważniejszymi sprawami...."
    #python:
        #ocena_kart1_tpi = 3
    scene bg white
    show text "{color=#000000}Twoja ocena: [ocena_kart1_tpi]{/color}"
    pause 2

    scene bg korytarz
    play music "music/bensound-acousticbreeze.ogg"
    if i == 1:
        show main1
    elif i == 2:
        show main2
    elif i == 3:
        show main3
    
    if marta_zostala_uspokojona:
        show adam_view at left
        adam "Dzięki niech będą Niebiosom. Zmieściłem się w progu! Mogę się wreszcie uspokoić. Jak tobie poszło?"
        if ocena_kart1_tpi >= 3:
            m "Mi też się udało! Cieszę się ogromnie! Przez cały wykład byłam bardzo zestresowana. 
            Czuję się jakby ktoś zabrał olbrzymi ciężar z moich pleców."
            adam "Ja tak samo. Cieszę się, że mamy już to za sobą."
            m "Powinniśmy to jakoś uczcić. Może skoczymy do baru po zajęciach?"
            adam "Dobry pomysł. Widziałaś gdzieś Martę?"
            show marta at right
            marta "TO SĄ JAKIEŚ BZDURY!"
            m "Marta! Co się stało?"
            marta "Byłam zobaczyć moją pracę. Myślałam, że może jakimś cudem brakło mi punkta. 
            Przejrzałam swój arkusz. TO NIE BYŁY MOJE ODPOWIEDZI!"
            adam "Ale jak to? O czym Ty mówisz?"
            marta "Pamiętam dokładnie jak wypełniłam swoją pracę. W paru miejscach ktoś zmienił 
            mi moje odpowiedzi. Przez to zabrakło mi punktów."
            m "To nie możliwe. Kto niby mógłby coś takiego zrobić."
            marta "Amanda, a kto? Miała dostęp do mojej pracy. Mogła to zrobić."
            adam "Ta hipoteza ma sens. Powiedziałaś o tym Ikarowi?"
            marta "Oczywiście! Niestety nie chce mi uwierzyć. Nie mam żadnego dowodu, ze to była ona. 
            Powiedział, że zrobi mi wielką łaskę i przepyta mnie w następnym tygodniu, ale nie wierzę, że się uda."
            m "Razem Ci pomożemy. Wyuczysz się tego na blachę!"
            adam "Dokładnie! Jesteśmy z Toba."
            marta "Dziekuję Wam, ale teraz chcę o tym zapomnieć. Idę do domu. Zobaczymy się jutro."
            #(odglos krokow)
            m "Może tym razem damy sobie spokój ze świętowaniem. Przełóżmy to na inny termin."
            adam "Dobry pomysł. Mam nadzieję, że Marta razem z nami będzie świętować..."
        else:
            m "Mi się jednak nie udało...Cieszę się, że dobrze Ci poszło. Szkoda, że nie mogę dołączyć 
            do Twojego świętowania."
            adam "Jest mi niezmiernie przykro. Mam pomysł. Idź na konsultacje do niego. Wiem jaki jest 
            Ikar, ale słyszałem o przypadkach którym się udało."
            m "Brzmi jak jakaś akademicka legenda. Zobaczę, może pójdę. Mną się nie przejmuj. Na końcu 
            i tak zwyciężę!"
            adam "Bardzo mądre słowa. Widziałaś gdzieś Martę?"
            show marta at right
            marta "TO SĄ JAKIEŚ BZDURY!"
            m "Marta! Co się stało?"
            marta "Byłam zobaczyć moją pracę. Myślałam, że może jakimś cudem brakło mi punktu. Przejrzałam 
            swój arkusz. TO NIE BYŁY MOJE ODPOWIEDZI!"
            adam "Ale jak to? O czym Ty mówisz?"
            marta "Pamiętam dokładnie jak wypełniłam swoją pracę. W paru miejscach ktoś zmienił mi moje 
            odpowiedzi. Przez to zabrakło mi punktów."
            m "To nie możliwe. Kto niby mógłby coś takiego zrobić."
            marta "Amanda, a kto? Miała dostęp do mojej pracy. Mogła to zrobić."
            adam "Ta hipoteza ma sens. Powiedziałaś o tym Ikarowi?"
            marta "Oczywiście! Niestety nie chce mi uwierzyć. Nie mam żadnego dowodu, ze to była ona. 
            Powiedział, że zrobi mi wielką łaskę i przepyta mnie niedługo, ale nie wierzę, że się uda."
            m "Razem Ci pomożemy. Wyuczysz się tego na blachę!"
            adam "Dokładnie! Jesteśmy z Tobą."
            marta "Dziękuję Wam, ale teraz chcę o tym zapomnieć. Idę do domu. Zobaczymy się jutro."
            #(odglos krokow)
            m "Jeżeli Nam się uda to zrobimy wielką imprezę"
            adam "Dobry pomysł. Naprawdę chciałbym byście to zaliczyły..."
    else:
        if ocena_kart1_tpi >= 3:
            m "Udało! Cieszę się ogromnie! Przez cały wykład byłam bardzo zestresowana. Czuję się 
            jakby ktoś zabrał olbrzymi ciężar z moich pleców."
            m "Takie zwycięstwo należy uczcić! Hmm....gdzie jest Adam?"
            show adam_view at left
            adam "TO SĄ JAKIEŚ BZDURY!"
            m "Adam! Co się stało?"
            adam "Byłem zobaczyć moją pracę. Myślałem, że może jakimś cudem brakło mi punktu. 
            Przejrzałem swój arkusz. TO NIE BYŁY MOJE ODPOWIEDZI!"
            m "Ale jak to? O czym Ty mówisz?"
            adam "Pamiętam dokładnie jak wypełniłem swoją pracę. W paru miejscach ktoś zmienił 
            mi moje odpowiedzi. Przez to zabrakło mi punktów."
            m "To nie możliwe. Kto niby mógłby coś takiego zrobić."
            adam "Amanda, a kto? Miała dostęp do mojej pracy. Mogła to zrobić."
            m "Ta hipoteza ma sens. Powiedziałaś o tym Ikarowi?"
            adam "Oczywiście! Niestety, nie chce mi uwierzyć. Nie mam żadnego dowodu, ze to była ona. 
            Powiedział, że zrobi mi wielką laskę i przepyta mnie w następnym tygodniu, ale nie wierzę, że się uda."
            m "Pomogę Ci z tym. Wyuczysz się tego na blachę!"
            adam "Dziekuję Ci, ale teraz chcę o tym zapomnieć. Idę do domu. Zobaczymy się jutro."
            #(odglos krokow)
            m "Może tym razem dam sobie spokój ze świętowaniem. Przełożę to na inny termin. Mam nadzieję, że Adam razem ze mną będzie mógł świętować..."
        else:
            m "Mi się jednak nie udało...Cieszę się, że dobrze Ci poszło. Szkoda..."
            show adam_view at left
            adam "TO SĄ JAKIEŚ BZDURY!"
            m "Adam! Co się stało?"
            adam "Byłem zobaczyć moją pracę. Myślałem, że może jakimś cudem brakło mi punkta. Przejrzałem swój arkusz. 
            TO NIE BYŁY MOJE ODPOWIEDZI!"
            m "Ale jak to? O czym Ty mówisz?"
            adam "Pamiętam dokładnie jak wypełniłem swoją pracę. W paru miejscach ktoś zmienił mi moje odpowiedzi. 
            Przez to zabrakło mi punktów."
            m "To nie możliwe. Kto niby mógłby coś takiego zrobić."
            adam "Amanda, a kto? Miała dostęp do mojej pracy. Mogła to zrobić."
            m "Ta hipoteza ma sens. Powiedziałaś o tym Ikarowi?"
            adam "Oczywiście! Niestety, nie chce mi uwierzyć. Nie mam żadnego dowodu, ze to była ona. Powiedział, że 
            zrobi mi wielką łaskę i przepyta mnie w następnym tygodniu, ale nie wierzę, że się uda."
            m "Pomogę Ci z tym. Wyuczysz się tego na blachę!"
            adam "Dziekuję Ci, ale teraz chcę o tym zapomnieć. Idę do domu. Zobaczymy się jutro."
            #(odglos krokow)
            m "Może tym razem dam sobie spokój ze świętowaniem. Przełożę to na inny termin. Mam nadzieję, że Adam 
            razem ze mną będzie mógł świętować..."

    scene bg white
    show text "{color=#000000}Czwartek{/color}"
    pause 2
    play music "music/bensound-sunny.ogg"
    scene bg korytarz
    if i == 1:
        show main1
    elif i == 2:
        show main2
    elif i == 3:
        show main3
    if marta_zostala_uspokojona:
        show marta at left
        m "I jak? Lepiej się już czujesz?"
        marta "Tak, doszłam już do siebie. Dogadałam się w sprawie terminu. Jeszcze raz dzięki za pomoc."
        m "Od tego są przyjaciele. Zastanawiam się co Amanda miałaby tym zyskać..."
        marta "Myślałam o tym i wpadłam na pewną hipotezę. Chodzi o Ciebie."
        m "Jakby chodziło o mnie, to chyba mi by takiego psikusa zrobiła, co nie?"
        marta "No właśnie nie. Ciebie chce pobić uczciwie, by pokazać, że jesteś gorsza od niej. Mnie zaatakowała by Cię zdenerwować."
        m "Brzmi jak typowa Amanda. Chyba masz rację. Nie chcę jej dzisiaj widzieć. Chyba bym ją rozerwała na kawałki."
        show draco at right
        play music "music/bensound-scifi.ogg"
        malfoy "Ktoś mnie wołał?"
        marta "Ty wredna małpo! Zapłacisz za to wszystko!"
        malfoy "Nie wiem o czym mówisz. Nie moja wina, że nie zaliczyłaś. Mogłabyś uczciwie przyznać, że zawaliłaś, a nie wymyślać jakieś bajeczki." 
        malfoy "Podobno Ikar po Twojej wizycie przez pół godziny nie mógł powstrzymać śmiechu, hahaha"
        marta "Już ja Ci pokażę, zołzo!"
        m "Marta, uspokój się! Nie jest tego warta. Czego chcesz, Amanda? Pośmiać się, czy może dla odmiany coś mądrego powiesz."
        malfoy "Przynajmniej jedna potrafi trzymać nerwy na wodzy. Mam dla Ciebie wiadomość, Kowalska. Ty i ja jedziemy jutro na seminarium do Mainsoftu."
        m "My? Czemu? O co Ci chodzi?"
        marta "Znowu jakieś sztuczki?"
        malfoy "Z Tobą nie gadam, wieśniaro. Dr Matylda powiedziała, że jesteśmy najlepsze w grupie na laboratoriach i dlatego chce Nas zabrać na wykład dotyczący inżynierii programowania."
        malfoy "Wierz mi, nie uśmiecha mi się z Tobą tam jechać. Mimo to, warto tam przybyć Takie seminarium może Cię wiele nauczyć."
        m "Czy Ty aby nie wkręcasz mnie? Może chcesz mnie wyrolować?"
        malfoy "Jak mi nie wierzysz to idź do dr Matyldy. Ja tylko przekazuję. 8:30 pod budynkiem szkoły. Na razie, frajerki. "
        hide draco
        m "Mam naprawdę mieszane uczucia. Z jednej strony cieszę się, ze mnie wybrano a z drugiej...."
        marta "Amanda, tak? Olej jej obecność i tyle. Powinnaś skorzystać z okazji. Dzięki temu możesz rozwinąć swoją wiedzę."
        m "Masz rację. Pojadę na to seminarium. Trzeba korzystać z tego co daje Ci życie."
        marta "I oto chodzi. Gratuluję Ci, że zostałaś wybrana. Zasłużyłaś na to!"
    else:
        show adam_view at left
        m "I jak? Lepiej się już czujesz?"
        adam "Tak, doszedłem już do siebie. Dogadałem się w sprawie terminu. Jeszcze raz dzięki za pomoc."
        m "Nie ma za co. Zastanawiam się co Amanda miałaby tym zyskać..."
        adam "Myślałem o tym i wpadłem na pewną hipotezę. Chodzi o Ciebie."
        m "Jakby chodziło o mnie, to chyba mi by takiego psikusa zrobiła, co nie?"
        adam "No właśnie nie. Ciebie chce pobić uczciwie, by pokazać, że jesteś gorsza od niej. Mnie zaatakowała by Cię zdenerwować."
        m "Brzmi jak typowa Amanda. Chyba masz rację. Nie chcę jej dzisiaj widzieć. Chyba bym ją rozerwała na kawałki."
        show draco at right
        play music "music/bensound-scifi.ogg"
        malfoy "Ktoś mnie wołał?"
        adam "Ty wredna małpo! Zapłacisz za to wszystko!"
        malfoy "Nie wiem o czym mówisz. Nie moja wina, że nie zaliczyłeś. Mógłbyś uczciwie przyznać, że zawaliłeś, a nie wymyślać jakieś bajeczki." 
        malfoy "Podobno Ikar po Twojej wizycie przez pół godziny nie mógł powstrzymać śmiechu, hahaha"
        adam "Już ja Ci pokaże, zołzo!"
        m "Adam, dość tego! Nie jest tego warta. Czego chcesz, Amanda? Pośmiać się, czy może dla odmiany coś mądrego powiesz?"
        malfoy "Przynajmniej jedna potrafi trzymać nerwy na wodzy. Mam dla Ciebie wiadomość, Kowalska. Ty i ja jedziemy jutro na seminarium do Mainsoftu."
        m "My? Czemu? O co Ci chodzi?"
        adam "Znowu jakieś sztuczki?"
        malfoy "Z Tobą nie gadam, wieśniaku. Dr Matylda powiedziała, że jesteśmy najlepsze w grupie na laboratoriach i dlatego chce Nas zabrać na wykład dotyczący inżynierii programowania."
        malfoy "Wierz mi, nie uśmiecha mi się z Tobą tam jechać. Mimo to, warto tam przybyć. Takie seminarium może Cię wiele nauczyć."
        m "Czy Ty aby nie wkręcasz mnie? Może chcesz mnie wyrolować?"
        malfoy "Jak mi nie wierzysz to idź do dr Matyldy. Ja tylko przekazuję. 8:30 pod budynkiem szkoły. Na razie, frajerzy. "
        hide draco
        m "Mam naprawdę mieszane uczucia. Z jednej strony cieszę się, ze mnie wybrano a z drugiej...."
        adam "Amanda, tak? Olej jej obecność i tyle. Powinnaś skorzystać z okazji. Dzięki temu możesz rozwinąć swoją wiedzę."
        m "Masz rację. Pojadę na to seminarium. Trzeba korzystać z tego co daje Ci życie."
        adam "I oto chodzi. Gratuluję Ci, że zostałaś wybrana. Zasłużyłaś na to!"
    scene bg a123
    play music "music/bensound-house.ogg"
    show teresa at left
    teresa "Witajcie, wszyscy. Mam nadzieję, że każdy dostał wiadomość, że dzisiaj mamy analizę."
    hide teresa
    show stud1 at left
    "Random1" "O kurde, zapomniałem! Ciekawe jak mi pójdzie kartkówka..."
    show stud2 at right
    "Random2" "Spoko, ja się uczyłem. Będę Ci podpowiadał jak coś."
    hide stud1
    hide stud2
    show teresa at left
    teresa "Ok, JD3.0 jest już gotowy do działania. Prawda, JD? "
    "JD3.0 ""BIP BOOOP BIB BOOOP BIP!"
    teresa "No to możemy zaczynać. Specjalnie dałam prosty przykład ze względu na zmianę terminu zajęć. 
    Do roboty, kochani!"
    stop music
    jump mat_kart2
label back_wyklad_mat_3_cd:
    #python:
        #ocena_kart2_mat = 3
    #jump kolo_mat2
    #label back
    play music "music/bensound-house.ogg"
    scene bg a123
    show teresa at left
    teresa "Sądzę, że wszyscy już skończyli. Widzę po waszych twarzach, że w miarę Wam poszło. 
    Mówiłam, że dam coś łatwego."
    hide teresa
    show stud1 at left
    "Random1" "Nawet nie musiałeś mi pomagać. Serio, tym razem dał coś łatwego!"
    show stud2 at right
    "Random2" "Widzisz? Nie trzeba było się tak stresować."
    "Random3" "Ja już wiem, że mam przechlapane. Nie mogę się jakoś wyuczyć tych wzorów na pamięć..."
    hide stud1
    hide stud2
    show teresa at left
    teresa "No dobrze, zacznijmy już wykład. Dzisiaj przechodzimy do trudniejszych rzeczy, więc radzę wszystkim uważać. 
    Dzisiaj zaczynamy całki!"
    
    scene black
    show text "{color=#FFF}Całki nieoznaczone{/color}"
    pause 2

    scene bg a123
    show teresa at left
    teresa "Rozprawiliśmy się z tematem szybciej nim myślałam. Dobrze, że w tym roku mam tak fajną grupę"
    teresa "JD już sprawdził Wasze prace. Zaraz Wam je pokażę. Widzę że większość zaliczyła. Tak trzymać! Dajesz,  JD!"
    "JD3.0" "BIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIP BOOP!"
    teresa "Do całek wrócimy dopiero w następnym tygodniu. Trzymajcie się i do zobaczenia!"
    
    scene bg white
    show text "{color=#000000}Twoja ocena: [ocena_kart1_tpi]{/color}"
    pause 2

    scene bg korytarz
    if i == 1:
        show main1
    elif i == 2:
        show main2
    elif i == 3:
        show main3
    play music "music/bensound-sweet.ogg"
    if marta_zostala_uspokojona:
        show stud1 at left
        "Random1" "Tak mnie zawsze straszono całkami, a nie wyglądają na aż takie trudne."
        show stud2 at right
        "Random2" "To dopiero pikuś. Poczekaj na oznaczone. Z nimi to będzie mordęga."
        hide stud1
        hide stud2
        show adam_view at left
        adam "No, dobrze, że mi te pochodne dobrze poszły.  Będę mógł w weekend się trochę polenić."
        show marta at right
        marta "Ja też. Serio zaczynam nieźle radzić sobie z matmą. Wszystko, dzięki mojej najlepszej przyjaciółce! 
        Jak Ci poszło, kochana?"
        if ocena_kart2_mat > 2:
            m "Nie ma problemu. Poszło świetnie. Dla mnie matma to najwidoczniej pikuś!"
            marta "No i idealnie. Z czystą głową możesz pojechać na to seminarium."
            adam "Marta mi mówiła. Zazdroszczę Ci bardzo. Sam kiedyś chciałbym pracować w Mainsofcie!"
            m "Słyszałam, że dosyć często przyjmują studentów. Kto wie? Może kiedyś będziemy tam pracować."
            marta "Byłoby super! Teraz lepiej chodźmy na laborki. Jeszcze nie oddałam tych programów, które zadała. Mam nadzieję, że kobitka nie będzie zła..."
        else:
            m "Trochę mi brakło, ale chyba da radę to zaliczyć. Sądzę, że uda mi się wyciągnąć 3"
            marta "Zrób tak. Dostałaś w sumie najtrudniejsze zadanie z kierunku. Powinien Ci to podciągnąć."
            adam "Po następnych zajęciach idź do niego. Może się uda."
            marta "Dokładnie. Będziesz mogła potem na spokojnie przygotować się na to seminarium."
            adam "Marta mi mówiła. Zazdroszczę Ci bardzo. Sam kiedyś chciałbym pracować w Mainsofcie!"
            m "Słyszałam, że dosyć często przyjmują studentów. Kto wie? Może kiedyś będziemy tam pracować."
            marta "Byłoby super! Teraz lepiej chodźmy na laborki. Jeszcze nie oddałam tych programów, które zadała. 
            Mam nadzieję, że kobitka nie będzie zła..."
    else:
        show adam_view at left
        adam "No, dobrze, że mi te pochodne dobrze poszły.  Będę mógł w weekend się trochę polenić. Jak u Ciebie?"
        if ocena_kart2_mat > 2:
            m "Nie ma problemu. Poszło świetnie. Dla mnie matma to najwidoczniej pikuś!"
            adam "No i idealnie. Z czystą głową możesz pojechać na to seminarium."
            adam "Zazdroszczę Ci bardzo. Sam kiedyś chciałbym pracować w Mainsofcie!"
            m "Słyszałam, że dosyć często przyjmują studentów. Kto wie? Może kiedyś będziemy tam pracować."
            adam "Byłoby super! Teraz lepiej chodźmy na laborki. Jeszcze nie oddałem tych programów, które zadała. 
            Mam nadzieję, że kobitka nie będzie zła..."
        else:
            m "Trochę mi brakło, ale chyba da radę to zaliczyć. Sądzę, że uda mi się wyciągnąć 3"
            adam "Zrób tak. Dostałaś w sumie najtrudniejsze zadanie z kierunku. Powinien Ci to podciągnąć."
            m "Po następnych zajęciach pójdę do niego. Może się uda."
            adam "Dokładnie. Będziesz mogła potem na spokojnie przygotować się na to seminarium."
            adam " Zazdroszczę Ci bardzo. Sam kiedyś chciałbym pracować w Mainsofcie!"
            m "Słyszałam, że dosyć często przyjmują studentów. Kto wie? Może kiedyś będziemy tam pracować."
            adam "Byłoby super! Teraz lepiej chodźmy na laborki. Jeszcze nie oddałem tych programów, które zadała. 
            Mam nadzieję, że kobitka nie będzie zła..."
    
    scene bg white
    show text "{color=#000000}Piątek{/color}"
    pause 2
    play music "music/bensound-happiness.ogg"
    scene bg pokoj
    show father at left
    o "No i jak kochanie gotowa do drogi?"

    menu:
        "Tak":
            jump wstajemy
        "Nie za bardzo":
            m "Tak tato....hrrrrrr"
            m "Wróciłabym do łóżka...."
label wstajemy:
    if i == 1:
        show main1
    elif i == 2:
        show main2
    elif i == 3:
        show main3
    o "Hahahaha....normalnie jakbym siebie za młodu widział. Naprawdę jestem dumny, że to Ciebie wybrano."
    m "Nie tylko mnie wybrano, tato.  Jeszcze taką jedną Morawską wzięli."
    o "Morawska? Masz na myśli córkę Antoniego Morawskiego?"
    m "Nie mam pojęcia. Raz widziałam, jak rozmawiała z Dziekanem. Podobno zna jej ojca."
    o "Czyli się nie pomyliłem. Nigdy zbytni gościa nie lubiłem. Po trupach do celu było jego mottem. Ciągle chciał być perfekcyjny..."
    m "Widać odziedziczyła to i owo po tatusiu. Niezbyt ją lubię."
    o "Kto wie? Może nie jest aż tak zła jak Ci się wydaje. Dopiero jak odkryjesz co siedzi w drugim człowieku możesz go w pełni zrozumieć."
    m "Dobrze, dobrze Paulo Coelho. Ja lecę. Będę pod telefonem!"
    o "Co ja z Tobą mam, hehehe. Baw się dobrze!"
    #(pod szkola)
    scene bg przed_weeia
    play music "music/bensound-jazzcomedy.ogg"
    if i == 1:
        show main1
    elif i == 2:
        show main2
    elif i == 3:
        show main3
    m "Chyba wyrobiłam się! O, widzę już dr Matyldę."
    show opiekun at left
    show draco at right
    opiekunroku "Dobrze, że już jesteś. Jesteśmy w komplecie! Za chwilę wyruszamy!"    
    malfoy "Chyba powinnyśmy ruszać natychmiast. Zapowiada się straszna ulewa, a mamy spory kawał do przejechania."
    opiekunroku "Dobrze kombinujesz, Amanda. Wskakujcie, dziewczyny. Jedziemy!"

    scene black
    show text "{color=#FFF}PÓŁ GODZINY PÓŹNIEJ{/color}"
    pause 2

    scene bg miasto
    if i == 1:
        show main1
    elif i == 2:
        show main2
    elif i == 3:
        show main3
    show draco at left
    show opiekun at right
    m "Jak długo zajmie nam podróż.  Jak daleko stąd jest placówka Mainsoftu?"
    malfoy "Nigdy w Warszawie nie byłaś? Matko i córko. Ty to serio jakaś dziwna jesteś..."
    opiekunroku "Amanda, uspokój się. Inaczej porozmawiam sobie z Twoim ojcem!"
    malfoy "D-dobrze..."
    opiekunroku "Tak lepiej. Za godzinę powinnyśmy być już na miejscu, ale wolę jechać wolniej. Droga jest strasznie śliska."
    m "Akurat w taki dzień trafiła nam taka pogoda. Dzień zapowiada się super..."
    opiekunroku "Spokojnie, spokojnie. Jak dotrzemy na miejsce to zobaczycie, że było warto."
    malfoy "Pani profesor, dlaczego jedziemy przez takie zad....to znaczy przez takie pustkowie?"
    opiekunroku "No, no, no...Jedziemy skrótem. Przez pogodę musiałam wybrać inną scieżkę."
    #(odglos burzy)
    opiekunroku "Ajjjjj, jeszcze burzy nam brakowało. Jeżeli będzie jeszcze taka okazja, to pojedziemy pociągiem"
    m "Jestem za!"
    malfoy "Niechętnie to mówię, ale zgadzam się z Tobą..."
    
    scene black
    show text "{color=#FFF}PÓŁ GODZINY PÓŹNIEJ{/color}"
    pause 2
    
    scene bg las1
    if i == 1:
        show main1
    elif i == 2:
        show main2
    elif i == 3:
        show main3
    show draco at left
    show opiekun at right
    m "Pani profesor, dlaczego jedziemy przez las?"
    opiekunroku "Chol...kurde...GPS pokazuje, że to dobra droga! Chciałam wyznaczyć najkrótszą drogę. Chyba się popsuł"
    malfoy "Wszystko jest dobrze, za parę minut wyjedziemy na autostradę. Przy takim tempie za ok. 30 minut będziemy na miejscu."
    opiekunroku "Wszystko pod kontrolą! Zaraz wyjedziemy z tego lasu. Nie ma się czym przej..."
    #(odglos grzmotu)
    #(odglos poteznego uderzenia)
    #(tlo robi sie cale biale na parenascie sekund)
    scene bg white
    ""
    scene bg las1
    if i == 1:
        show main1
    elif i == 2:
        show main2
    elif i == 3:
        show main3
    m "Khe Khe Khe....co się stało?"
    play music "music/bensound-sadday.ogg"
    #(cisza)
    m "Pani profesor! Amanda! Wszystko w porządku!"
    #(cisza)
    m "Pani Matyldo!"
    show draco at right
    malfoy "Nie drzyj się tak! Bębenki mi zaraz pękną."
    m "Amanda, Ty żyjesz. Nigdy nie spodziewałam się, że będę się cieszyć, że cię słyszę."
    malfoy "Bardzo zabawne...musimy się stąd wydostać i zadzwonić po pomoc."
    m "Wytłumacz mi, co się stało!"
    malfoy "Tak w dużym skrócie: piorun walnął w drzewo, a drzewo w Nas. Wyciągnijmy dr Matyldę. 
    Mam nadzieję, że jest tylko nieprzytomna. Arghhhh!"
    m "Co Ci jest?"
    malfoy "Najprawdopodobniej nogę złamałam. Jakoś żyję. Wyciągnij Matyldę. Spróbuję Ci pomóc...ohhh jak boli"
    
    scene black
    show text "{color=#FFF}CHWILE PÓŹNIEJ{/color}"
    pause 2

    show bg las2
    if i == 1:
        show main1
    elif i == 2:
        show main2
    elif i == 3:
        show main3
    m "Wygląda na to, że jest tylko nieprzytomna. Na całe szczęście. Jak Twoja noga?"
    show draco at right
    malfoy "Daruj sobie! Żyję, nie widać? Zadzwoniłam po pomoc. Za niedługo tu będą."
    m "Trzeba Ci tę nogę unieruchomić. Pozwól mi sobie pomóc!"
    malfoy "Jak przyjadą to mi pomogą. Martw się o siebie! Arghhhhhh....ale wali!"
    hide draco
    if i == 1:
        hide main1
    elif i == 2:
        hide main2
    elif i == 3:
        hide main3
    menu:
        "Pomóż Amandzie":
            if i == 1:
                show main1
            elif i == 2:
                show main2
            elif i == 3:
                show main3
            m "Nie udawaj takiej twardej. Mi o dziwo nic nie jest. Dawaj tę nogę. Ostrzegam, może boleć"
            python:
                pomoglas_amandzie = True
            jump nieistony_x
        "Zostaw ją w spokoju":
            if i == 1:
                show main1
            elif i == 2:
                show main2
            elif i == 3:
                show main3
            python:
                pomoglas_amandzie = False
            m "Jak sobie chcesz. Twoja noga, twój wybór..."

label nieistony_x:
    scene black
    show text "{color=#FFF}CHWILE PÓŹNIEJ{/color}"
    pause 2

    scene bg las2
    if i == 1:
        show main1 at left
    elif i == 2:
        show main2 at left
    elif i == 3:
        show main3 at left
    show draco at right
    malfoy "Nic gorszego mnie chyba nie spotka dzisiaj. Utknęłam w lesie i to w dodatku z Tobą!"
    m "W sumie do jest dobry moment na wyjaśnienie sobie paru spraw. Czemu się mnie uczepiłaś. Co Ci takiego zrobiłam"
    #(cisza)
    m "Odpowiadaj jak do Ciebie mówię!"
    malfoy "Powiedz mi lepiej, czemu mi pomogłaś skoro Cię tak nienawidzę."
    m "To chyba jasne, tak? Widać, że potrzebujesz pomocy. Znam się na pierwszej pomocy!"
    malfoy "NIE! NIE! NIE!"
    malfoy "To nie tak powinno być!"
    m "O co Ci chodzi?"
    malfoy "Nie powinnaś mi pomagać! Czuję się...taka...beznadziejna..."
    m "Dalej roztrząsasz tę naszą niby rywalizację? Obudź się. Mamy poważniejszy problem."
    malfoy "Ehh....prawdopodobnie nigdy mnie nie zrozumiesz. Szkoda marnować energię..."
    m "Spróbuj...jak nie spróbujesz to się nie dowiesz."
    malfoy "Taa...w sumie i tak czekamy na pomoc. Zaraz będziesz mogła się ze mnie pośmiać."
    #(cisza)
    malfoy "Osobiście nic do Ciebie tak naprawdę nie mam. Nawet Cię dobrze nie znam. Nie lubię Cię, bo nienawidzę samej siebie."
    m "Jesteś pewna, że nie uderzyłaś się w głowę podczas wypadku?"
    malfoy "Ehhh....od początku wiedziałam kim jesteś. Mój ojciec pracował kiedyś z Twoim. To są w sumie wielkie szychy w świecie IT."
    malfoy "Mnie ojciec od samego początku widział przy sobie jako jego przyszłą prawą rękę. Chciał miec idealnego spadkobiercę swojej firmy."
    malfoy "Tata zawsze dążył do perfekcji. ZAWSZE. W moim przypadku było tak samo. Żadnych ustepstw od normy. Kiedy coś szło nie tak, surowo mnie karał."
    malfoy "Lubię branżę IT. Widzę się w bazach danych. Od dawna mnie to interesuje. Tylko ja nie mam wolnego wyboru.  Jeśli mam kiedyś zastąpić ojca to muszę robić to, co on każe."
    malfoy "Kiedy zobaczyłam Ciebie....poczułam zazdrość. Sama wybrałaś sobie cel w życiu. Nie miałaś nad sobą wiecznie spoglądającego na Ciebie ojca. Sama decydujesz, kim chcesz być."
    malfoy "Widziałam w Tobie samą siebie. Taką jaką zawsze chciałam być. To zabolało. Bardzo zabolało. Chciałam zniszczyć ten ból. Dlatego wymyśliłam ten zakład. Chciałam sama sobie udowodnić, że jestem słaba"
    #(cisza)
    m "Nie wiem co powiedzieć..."
    malfoy "Nie ma sensu...dodatkowo widziałam jak się dobrze dogadujesz z innymi. Sama tak bym chciała. Niestety, szkoła tatusia nauczyła mnie by być zawsze pewnym swoich umiejętności i majątku. Aż do przesady."
    malfoy "Nic dziwnego, że nikt nie chciał się ze mną zadawać..."
    m "To prawda, że podrobiłaś wtedy wyniki."
    malfoy "Chciałam, ale to byłoby głupie. Nie mam z tym nic wspólnego. Myślałam nad paroma psikusami, ale nie zdążyłam ich zrealizować."
    m "Mówisz prawdę, czy blefujesz? Teraz to przyjmę wszystko na klatę."
    malfoy "Nie mam z tym nic wspólnego. Obiecuję."
    #(cisza)
    m "Wierzę Ci. Poważnie."
    malfoy "Przepraszam za wszystkie obelgi i kpiny. Teraz jestem w pełni świadoma swoich czynów. Zazdrość potrafi 
    porządnie zaślepić człowieka. "
    if pomoglas_amandzie:
        malfoy "Chciałabym też Ci podziękować. Za nogę..."
        m "To nic takiego, naprawdę"
        malfoy "Owszem ,jest. Ja bym pewnie czegoś takiego nie potrafiła. Jesteś lepsza ode mnie. 
        Przyznaję to szczerze."
    m "Z Ciebie jeszcze porządna kobieta wyrośnie. Musisz tylko trochę nad sobą poćwiczyć."
    malfoy "Hahahahahhaha poćwiczyć...hahahaha"
    m "Znowu się nabijasz ze mnie?"
    malfoy "Nie. To pierwszy szczery śmiech od bardzo dawna. Strasznie mi tego brakowało..."
    show opiekun at center
    opiekunroku "Ahhh moja głowa. Co się stało?"
    m "Pani profesor! Jak się pani czuje?"
    opiekunroku "Głowa mi tylko strasznie dokucza. Jesteście całe, dziewczyny?"
    malfoy "Żyjemy proszę się nie martwić. Zaraz przyjedzie pomoc."
    #(odglos karetki)
    "łiułiu"
    m "O wilku mowa! Jesteśmy uratowane"
    
    scene black
    show text "{color=#FFF}Kilka godzin później{/color}"
    pause 2
    play music "music/bensound-rumble.ogg"
    scene bg szpital
    if i == 1:
        show main1
    elif i == 2:
        show main2
    elif i == 3:
        show main3

    Lekarz "Z panią Kowalską nie ma żadnych problemów. Natomiast pozostałe panie czeka trochę dłuższy pobyt w szpitalu. 
    Nie ma powodu do obaw. Nic poważnego im nie jest"
    show opiekun at left
    show draco at right
    opiekunroku "Ajć, dziewczyny przypomnijcie mi następnym razem, że lepiej jechać pociągiem"
    malfoy "Na pewno będę pani o tym przypominać!"
    m "Cieszę się, że nic Wam poważnego nie jest. Nie wiem jakim cudem wyszłam z tego bez szwanku..."
    opiekunroku "Nie narzekaj, Kowalska. Mieć szczęście po swojej stronie do dobra rzecz. Hmm...zastanawiam się kto powinien mnie zastąpić podczas mojej nieobecności..."
    opiekunroku "Już wiem! Poproszę dr Ikara by miał z Wami zastępstwo aż do mojego powrotu!"
    m "NIEEEEEEEEEEEEEE!"
    malfoy "NIEEEEEEEEEEEEEE!"
    opiekunroku "Hahahaha, tylko żartowałam!"
    
    scene black
    show text "{color=#FFF}Jakis czas później{/color}"
    pause 2

    scene bg korytarz
    if i == 1:
        show main1
    elif i == 2:
        show main2
    elif i == 3:
        show main3

    m "Ten semestr zapamiętam do końca życia. W sumie trochę szkoda, że się kończy. Ciekawe co przyniesie następny."
    m "Podobno Ikara wywalili z uczelni. Wreszcie znaleźli na niego coś dobrego."
    m "Zmieniać odpowiedzi w kolokwiach?  Tylko diabeł mógłby wpaść na coś takiego."
    if marta_zostala_uspokojona:
        m "Nigdy nie zapomnę miny Marty, kiedy musiała przepraszać Amandę, za błędne oskarżenia"
    else:
        m "Nigdy nie zapomnę miny Adama, kiedy musiał przepraszać Amandę, za błędne oskarżenia"
    m "Amanda w sumie jest całkiem w porządku, jak się ją lepiej pozna. Sądzę, że warto utrzymywać z nią więź. Ona potrzebuje pomocy. Mojej pomocy. Chyba tylko ja mogę to zrobić."
    if marta_zostala_uspokojona:
        m "Miałeś rację tato. Potrzebowałam zobaczyć co się w niej kryje, by ją w pełni zrozumieć. 
        Może Marta też się do niej przekona... kiedyś."
    else:
        m "Miałeś rację tato. Potrzebowałam zobaczyć co się w niej kryje, by ją w pełni zrozumieć. 
        Może Adam też się do niej przekona... kiedyś."
    m "To był zwariowany semsestr...hehehe"
    m "Teraz przyszedł czas na ostateczny sprawdzian mojej wiedzy. Nadeszła SESJA!"
    #(odglos grzmotu)
    if i == 1:
        hide main1
    elif i == 2:
        hide main2
    elif i == 3:
        hide main3
    show narrator at left
    ob "Witaj, mój graczu. Widzimy się ponownie. Nadszedł czas by sprawdzić wiedzę, jaką zdobyłeś podczas tego semestru"
    ob "Jeszcze z Tobą nie skonczyłem. Zobaczymy się na końcu naszej podróży. Powodzenia!"
    jump exams
    #TO CO POTEM BEDZIE DOGRAMY WSPOLNIE WRAZ Z MINIGIERKAMI(CHODZI GLOWNIE O ACHI I TEKSTY OBSERWATORA)
    #strona 65