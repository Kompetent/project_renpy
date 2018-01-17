init:
    image bg pokoj = "pokoj.jpg"
    image bg aula = "aula.jpg"
    image bg miasto = "miasto.jpg"
    image bg korytarz = "korytarz2.jpg"
    image bg a128 = "sala1.jpg"
    image bg a129 = "sala2.jpg"
    image bg a123 = "sala3.jpg"

    image father = "father.png"
    image draco = "draco.png"
    image dziekan = "dziekan.png"
    image opiekun = "matylda.png"
    
    define o = Character("Ojciec",what_slow_cps=20) #mozna dodac font różny
    define dziekan = Character("Dziekan",what_slow_cps=20)
    define opiekunroku = Character("Opiekun Roku",what_slow_cps=20)
    define malfoy = Character("Amanda",what_slow_cps=20)

    define love_u = "Uczelnia Informatyk Różnych"
    define hate_u = "Uczelnia Informatyczno-matematyczna im. P. Czybyszewa"
label chapter1: #DONE
    #jump chapter2 #pokazujemy tylko progres
    scene black
    show text "{color=#FFF}{size=+30}Chapter 1\nPierwszy dzień na studiach{/size}{/color}"
    pause 2
    hide text
    play music "music/bensound-happiness.ogg"
    scene black
    show father at left
    o "Kochanie, obudź się, już 8"
    menu:
        "Śpij dalej":
            jump dalej1
        "Obudź się":
            jump obudzona

    label dalej1:
        o "[m] wstawaj, nie chcemy przecież się spóźnić."
        menu:
            "Śpij dalej":
                jump dalej2
            "Obudź się":
                jump obudzona
    label dalej2:
        #odgłos wylanej wody
        play sound "music/sounds/water_splash1.mp3"
        o "Wstajemy!!!"
        m "Tato, co ty zrobiłeś?!"
        o "Wybacz, młoda damo, ale nie dałaś mi wyboru, biegiem do łazienki."
    label obudzona:
        scene bg pokoj
        show father at left
        o "Wyglądasz ślicznie, córeczko, gdyby tylko mama mogła Cię zobaczyć."
        
        #pokazywanie naszej studentki
        if i == 1:
            show main1
        elif i == 2:
            show main2
        elif i == 3:
            show main3

        menu:
            "Tato, przestań...":
                m "Tato, przestań. Naprawdę nie lubię jak tak mówisz."
                o "Wiesz, że nie potrafię kryć się z uczuciami."
            "Dziękuje tato...":
                m "Dziękuje tato, też chciałabym aby mama z nami była."
            "(cisza)":
                m "..."
        o "Zjesz może coś przed uroczystością?"
        menu:
            "Jesz":
                m "W sumie zjadłabym coś..."
                o "To sobie coś zrobisz, ja idę zaraz do pracy."
            "Nie jesz":
                m "Nie, dzięki, zjem coś jak wrócę."
                o "Weź trochę pieniędzy i zjedz coś na mieście.
                Dzisiaj późno wrócę, a lodówka pusta."
        o "Oj, jestem taki dumny, moja mała córeczka idzie się uczyć. Mam nadzieje,
         że poznasz tam grzecznych i poukładanych
         ludzi. Studia na [hate_u] to jedna z najlepszych opcji dla rozwoju
         przyszłych programistów."
        menu:
            "Bez przesady tato...":
                m "Bez przesady tato, to tylko immatrykulacja, trochę posiedzę i wrócę do domu."
                o "Możesz mi wierzyć słonko, ale czuję, że to nie będzie zwykła uroczystość"
            "Prawda, jednak...":
                m "Prawda, jednak wolałabym dostać się na [love_u]. To najlepsza uczelnia w kraju."
                o "Ostatnimi czasy ma dość słabą reputację. Znam tych ludzi, dobrze się stało, że dostałaś się jednak tutaj.
                Uczelnia jest w naszym mieście i dodatkowo jest pełna wielu wartościowych specjalistów."

        o "Zapamiętaj, [m]. Cieszę się, że jesteś bardzo ambitna i chcesz iść w moje ślady. Jestem z ciebie taki dumny..."
        o "Studia to najlepszy okres życia, wykorzystaj to!"
        menu:
            "pasywnie":
                m "Nie martw się tato, dam sobie radę, nie sprawię Ci zawodu"
            "agresywnie":
                m "Dam radę, pokażę im wszystkim na co mnie stać"
        o "O to akurat najmniej się martwię, leć już, bo się spóźnisz. Miłego dnia. "

        scene black
        show text "{color=#FFFFFF}Uczelnia - godzina 10{/color}"
        pause 2
        hide text

        scene bg miasto

        #pokazywanie naszej studentki
        if i == 1:
            show main1
        elif i == 2:
            show main2
        elif i == 3:
            show main3

        m "Mam jeszcze 15 minut, tempo mam dobre. Całe szczęście mam tutaj w miarę blisko."
        m "Nawet ładny ten budynek. Co prawda nie umywa się do [love_u], ale ten wygląda na bardziej zadbany."
        m "Zapomnij o [love_u], [m]. Musisz wziąć to co dało ci życie. Jeśli dobrze ci pójdzie to będziesz mogła zrobić
        magisterkę na [love_u]. Skup się na tym co jest tu i teraz."
        m "Przedstawienie czas zacząć. Bądź zdecydowana i dumna."
        stop music
        #wyciemniony ekren, dźwięk otwierania drzwi
        #czarne tło, napis: immatrykulacja uczelnia hate_u

        scene black

        show text "{color=#FFFFFF}Immatrykulacja - [hate_u]{/color}"
        pause 2
        hide text

        #wnętrze sali wykładowej, głos gwary
        scene bg aula

        #pokazywanie naszej studentki
        if i == 1:
            show main1
        elif i == 2:
            show main2
        elif i == 3:
            show main3
        play music "music/bensound-anewbeginning.ogg"
        m "Wow, tylu ludzi w jednym miejscu na żywo jeszcze nie widziałam."
        m "Każdy z nich ma swoje cele i ambicje, każdy ma inny powód dla którego się tutaj znalazł.
        Oni wszyscy są moją przyszłą konkurencją na rynku pracy."
        m "Chciałabym mieć jakichś znajomych. Większość moich kolegów i koleżanek
        wyjechała z miasta albo z kraju."
        m "Czy serio potrzebuje kogoś mieć? Czy nie powinnam skupić się na własnej karierze?
        Ojciec chyba ma rację, nie mogę zmarnować tego czasu, który mam. Będziesz ze mnie
        dumny tato i... mamo. "

        #ukrywanie naszej studentki
        if i == 1:
            hide main1
        elif i == 2:
            hide main2
        elif i == 3:
            hide main3

        #podniosła muzyka
        show dziekan at left
        dziekan "Witam świeżo upieczonych studentów. Nazywam się prof. Stanisław Meister i jestem
        dziekanem Wydziału Informatycznego."
        dziekan "Nasza uczelnia z roku na rok dokłada starań by każdy jej absolwent
         dumnie nas reprezentował poza murami tej instytucji."
        dziekan "Wiem, że każde z was jest bardzo ambitne i chce jak najlepiej
        wykorzystać ten wspaniały czas do samodoskonalenia. Pamiętajcie też, że mimo
        siły jednostki czasami trzeba połączyć siły z innymi by osiągnąć dany cel."
        dziekan "Oczywiście moje słowa nie dotyczną ściągania"
        #dzwięk śmiechu masowego
        dziekan "Nie bójcie się nawiązywać nowych kontaktów i pomagać sobie wzajemnie.
        Wierzę, że mnie nie zawiedziecie i każde z was będzie mogło pochwalić się dyplomem
        ukończenia naszej placówki."
        dziekan "Teraz każdy kierunek będzie miał rozmowę ze swoim
        opiekunem, który omówi najważniejsze elementy waszej przyszłej nauki.
        Do zobaczenia na zajęciach."
        hide dziekan
        #schowaj dziekana
        "Komunikat głosowy" "Informacja dla kierunków pierwszego roku. Zaraz rozpocznie się podpisywanie 
        umów studenckich i odbieranie legitymacji. Podaję numery sal: Mechatronika A123, Informatyka A128, 
        BHP A129, Automatyka i Robotyka A130,  BHP A132..."

        #pokazywanie naszej studentki
        if i == 1:
            show main1
        elif i == 2:
            show main2
        elif i == 3:
            show main3
        play music "music/bensound-sweet.ogg"
        m "Hmm...a już myślałam, że będę mogła pójść do domu. Męczą mnie takie uroczystości. 
        W sumie nic dziwnego. Większość czasu spędzam przed komputerem."
        m "Może jak będzie już na studiach WF to się zapiszę na jakąś siłownię lub fitness. 
        Trzeba będzie trochę popracować nad kondycją."
        m "Teraz nie pora na takie rzeczy. Trzeba się udać po odbiór legitymacji.. Mam nadzieję, 
        że jakoś przeżyję w tym tłumie."
        label zmiany:
        #odgłos tłumu
        scene black
        show text "{color=#FFFFFF}Kilka minut później...{/color}"
        pause 2
        hide text

        scene bg korytarz
        #pokazywanie naszej studentki
        if i == 1:
            show main1
        elif i == 2:
            show main2
        elif i == 3:
            show main3

        m "WRESZCIE! Jejku, myślałam, że się tam uduszę. Jestem już na odpowiednim piętrze."
        m "Hmm....która to była sala?" 
        python:
            wrong = False
        label back:
            scene bg korytarz
            menu:
                "A123":
                    if i == 1:
                        show main1
                    elif i == 2:
                        show main2
                    elif i == 3:
                        show main3
                    m "O...k... to była ta sala? No nic, przekonajmy sie."
                    #sala wykladowa
                    show bg a123
                    #pokazywanie naszej studentki
                    if i == 1:
                        show main1
                    elif i == 2:
                        show main2
                    elif i == 3:
                        show main3
                    m "O matko, to nie ta sala. Ale przypał. Muszę znaleźć właściwą salę."
                    python:
                        wrong = True
                    jump back
                "A129":
                    if i == 1:
                        show main1
                    elif i == 2:
                        show main2
                    elif i == 3:
                        show main3
                    m "O...k... to była ta sala? No nic, przekonajmy sie."
                    #sala wykladowa
                    show bg a129
                    #pokazywanie naszej studentki
                    if i == 1:
                        show main1
                    elif i == 2:
                        show main2
                    elif i == 3:
                        show main3
                    m "O matko, to nie ta sala. Ale przypał. Muszę znaleźć właściwą salę."
                    python:
                        wrong = True
                    jump back
                "A128":
                    jump go
        label go:
            #sala wykladowa
            show bg a128
            if wrong:
                play music "music/bensound-scifi.ogg"
                #pokazywanie naszej studentki
                if i == 1:
                    show main1
                elif i == 2:
                    show main2
                elif i == 3:
                    show main3
                #pokaz opiekuna
                show opiekun at left
                opiekunroku "Ludzie kochani. Ilu was się jeszcze spóźni? Coś kiepsko wróżę waszą punktualność 
                na przyszłych zajęciach."
                hide opiekun
                #schowaj opiekuna
                #pokaz draco
                show draco at right
                malfoy "Same nieogary na tym kierunku. Widać, że moja konkurencja nie zapewni mi nawet źdźbła 
                ekscytacji w \"rywalizacji\". "
                #pokaz studentke
                m "Mogłam lepiej zapamiętać numer sali. Jestem na siebie potwornie zła. Pierwszy 
                dzień na uczelni i już mi coś nie wychodzi. Muszę się bardziej starać."
                hide draco
                if i == 1:
                    hide main1
                elif i == 2:
                    hide main2
                elif i == 3:
                    hide main3
            else:
                #pokazywanie naszej studentki
                if i == 1:
                    show main1
                elif i == 2:
                    show main2
                elif i == 3:
                    show main3
                m "Chyba trafiłam do dobrej sali. Nie spodziewałam się, że aż tyle osób wybierze ten kierunek. 
                Widzę też sporo dziewczyn. Cieszę się, że jest nas co raz więcej na uczelniach technicznych."
                m "Wciąż przybywają ludzie. Pewnie wcześniej pomylili salę. Dobrze, że udało mi się zapamiętać 
                właściwy numer"
                if i == 1:
                    hide main1
                elif i == 2:
                    hide main2
                elif i == 3:
                    hide main3
        #pokaz opiekuna roku
        play music "music/bensound-jazzcomedy.ogg"
        show opiekun at left
        opiekunroku "Mam nadzieję, że to już wszyscy. W tym roku naprawdę dużo ludzi dostało się na ten 
        kierunek. Mam nadzieję, że ta sala pomieści nas wszystkich. Inaczej wykłady będziecie mieli na 
        podwórku."
        #dżwięk masowego śmiechu
        opiekunroku "Na początek chciałabym się wam przedstawić. Jestem doktor Matylda Kostrzewska i 
        jestem opiekunem waszego roku. Równocześnie będę miała z wami zajęcia z Podstaw Programowania."
        hide opiekun
        show stud1 at left
        "Student1" "Słyszałem, ze starsze roczniki mówią na nią \"Doktor Kosa\""
        show stud2 at right
        "Student2" "Czemu? Aż tak ciężko zaliczyć ten przedmiot?"
        "Student2" "Taa...słyszałem, że do programowania podchodzi bardzo poważnie. Jedna z najbardziej 
        uzdolnionych osob tutaj."
        "Student3" "Dajcie spokój. Ja tam nie wierzę starszym rocznikom. Później okazuje się, że połowa to kłamstwo."
        hide stud1
        hide stud2
        show opiekun at left
        opiekunroku "...na uroczystości poznaliście jeszcze jedną osobę, z którą będziecie mieli zajęcia w 
        tym semestrze. Nasz dziekan będzie z wami miał Historię Informatyki."
        hide opiekun
        show stud1 at right
        "Student1" "Co? Dopiero pierwszy semestr a już mamy jakieś wypełniacze w planie."
        hide stud1
        show opiekun at left
        opiekunroku "Polecam chodzić, gdyż dziekan bardzo ciekawie prowadzi zajęcia. Z tego co pamiętam to w 
        tamtym roku prawie wszyscy chodzili na zajęcia."
        hide opiekun
        show stud2 at right
        "Student2" "Chyba jednak przesadzasz, chłopie. Coś czuję, że będzie ciekawie."
        hide stud2
        show opiekun at left
        opiekunroku "Plan zajęć zaraz wam przedstawię na tablicy."
        show plan_zajec: 
            xalign 0.8 yalign 0.25
        opiekunroku "Oooo... najwidoczniej widzę się z wami już w poniedziałek. Też mi się nie podoba ta godzina, 
        ale nie ja mam na to wpływ."
        opiekunroku "Na pierwszych zajęciach poznacie zasady prowadzenia i zaliczenia przedmiotu. 
        Teraz będę wyczytywać alfabetycznie nazwiska. Kiedy kogoś wyczytam ma do mnie podejść by 
        podpisać umowę i odebrać legitymację."
        hide plan_zajec
        #(odglos tlumu)
        hide opiekun
        #pokazywanie naszej studentki
        if i == 1:
            show main1
        elif i == 2:
            show main2
        elif i == 3:
            show main3
        play music "music/bensound-scifi.ogg"
        m "Kobitka nie wydaje się zła. Nie sądzę, że będę z nią miała jakieś problemy. Uczyłam sę na własną rękę 
        programowania jak jeszcze chodziłam do liceum."
        show draco at right
        malfoy "...ojciec poważnie rozważał by mnie wysłać na studia do Stanów. Dzięki temu nauczyłabym się więcej 
        niż w tym kraju, ale matka nie chciała bym była tak daleko od domu."
        malfoy "Mimo to, nie jest aż tak źle. Mój ojciec zna tu wielu ludzi. Kiedyś tu wykładał. 
        Z palcem w nosie zrobię magistra, a potem doktorat w USA."
        "Student3" "Wow...aale masz fajnie."
        show stud1 at left
        "Student4" "Prawda. W sumie jesteś ustawiona przez całe studia."
        malfoy "Niby tak, ale to nie oznacza, że nie dam z siebie wszystkiego. Dziwię się, że aż tylu się 
        dostało. Nie jest to problemem."
        malfoy "Rozłożę tych cieniasów tak, że zmienią studia i pójdą na zarządzanie."
        "Student3" "Hhahhaha. Ty to masz gadane, Amanda."
        m "Jezu....i z kimś takim mam studiować. Gorszej baby jeszcze nie widziałam w swoim życiu. Pewnie jest 
        tylko mocna w gębie ale nic praktycznego zrobić nie potrafi."
        malfoy "Hej, ty. Czemu się na mnie gapisz?"
        menu:
            "To tylko przypadek":
                m "Zwykly przypadek. Przewidziało ci się najwidoczniej."
                malfoy "Nie udawaj. Widziałam, jak się na mnie lampisz. Czyżbym cię czymś zdenerwowała?"
                menu:
                    "tak":
                        jump bezznaczenia
                    "nie":
                        jump bezznaczenia
            "Masz coś do mnie???":
                m "Patrzę z politowaniem na twoje przechwałki."
                malfoy "Patrzcie kogo my tu mamy. Masz cięty język. Możesz sobie gadać zdrowa, ale i tak przemawia przez ciebie zazdrość."
                m "Chyba coś ci się pomyliło, kobieto."
    label bezznaczenia:
        malfoy "Dostrzegłam to. To spojrzenie. Spojrzenie pełne zazdrości. Mnie nie zwiedziesz."
        malfoy "Masz czego mi zazdrościć, moja droga. Patrząc na ciebie uważam, że i bez tego wszystkiego jestem 
        lepsza. Wydajesz się być zdeterminowana, ale ja i tak będe górą."
        m "Daj sobie na wstrzymanie, ok? Możesz sobie gadać zdrowa, ale mnie to nie obchodzi. Jesteś tylko mocna w gębie."
        malfoy "Tak uważasz? Widzę, że mamy tutaj bojowniczkę. Mam pomysł. Załóżmy się."
        m "Hę? Jaki zakład?"
        malfoy "O to, kto będzie miał lepszą średnią na koniec semestru."
        m "To trochę dziecinne. Jaka niby miałaby być nagroda."
        malfoy "Jeśli wygrasz, przyznam, że jesteś ode mnie lepsza i dam ci spokój do konca studiów. 
        Może nawet jakiś projekt grupowy razem zrobimy."
        m "Zabawne. Co jeśli ty wygrasz?"
        malfoy "To proste. Udowodnię swoją wyższość i to, że nie jesteś godna zainteresowania. Coś czuję, 
        że porażka dla każdej z nas będzie bolesna a wygrana słodkim triumfem."
        malfoy "To jak? Zakładamy się?"
        python:
            a = 1
    label back_malfoy:    
        menu:
            "tak":
                m "Niech ci będzie. Skoro myślisz, że możesz ze mną rywalizować to próbuj. Nie bronię ci."
                jump powszystkim
            "nie":
                m "Nie mam po co się zakładać. Nie jesteś godna by ze mną konkurować."
                malfoy "Czcze gadanie. Widzę, że najwyraźniej boisz się ze mną zmierzyć."
                m "Kogo jak kogo, ale ciebie nie zamierzam się bać."
                malfoy "To udowodnij to. Samymi słowami raczej tego nie zrobisz."
                if a < 2:
                    python:
                        a = a + 1
                    jump back_malfoy
                else: 
                    jump zdenerwowana_studentka
        label zdenerwowana_studentka:
            m "Zaczynasz mnie denerwować. Jeżeli w końcu zdecyduję się na ten zakład to przestaniesz?"
            malfoy "Mi tam aż tak nie zależy. Po prostu nienawidzę ludzi, którzy boja się sprawdzić swoje umiejętności!"
            m "Dobra, już dobra. Zgadzam sę. Zetrę ten durny uśmiech z twojej twarzy."
        label powszystkim:
            malfoy "Hahahahahaha. No to ustalone. Pozwól, że zdradzę ci, kim jestem. Nazywam się [malfoy] i 
            wiedz, że ze mną tak łatwo nie wygrasz."
            m "Ja jestem [m] Kowalska. Już ci współczuję przegranej."
            opiekunroku "Pani Kowalska, do mnie!"
            malfoy "Wołają cię. No to do zobaczenia na zajęciach \"rywalko\". Tylko nie chwal się bardzo, 
            że się założyłyśmy. Wieść o tym, że zadaję się z taką ofiarą zepsuje mi reputację. Hahahahahha."
            hide draco
            hide stud1
            play music "music/bensound-jazzcomedy.ogg"
            #chowaj malfoya
            #pokaz opiekuna roku
            show opiekun at left
            m "W co ja się wpakowałam. No nic. Muszę stawić temu czoła. Nie będzie sobie gówniara pozwalać."
            opiekunroku "Proszę tylko podpis i legitymacja jest już pani."
            m "Dobrze, już podpisuję."

            play sound "music/sounds/writing.mp3"

            opiekunroku "Oto legitymacja studencka. Powodzenia w studiowaniu i do zobaczenia w poniedziałek."
            m "Dziękuję... na pewno się przyda... "
            hide opiekun roku
            m "Mam już dość tego dnia. Lecz prawdziwy koszmar zacznie sę w poniedziałek. Nie daruję tej babie, 
            że już zrujnowała mi studia. Pokażę na co mnie stać."
            m "Najpierw jednak wrócę do wygodnego wyrka. Wstawanie o tak wczesnej porze jest nieludzkie."
            stop music
            jump chapter2
            return
