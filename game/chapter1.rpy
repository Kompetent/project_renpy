init:
    image bg pokoj = "pokoj.jpg"
    image bg aula = "aula.jpg"
    image bg miasto = "miasto.jpg"
    image bg korytarz = "korytarz2.jpg"

    image father = "father.png"
    
    define o = Character("Ojciec") #mozna dodac font różny
    define dziekan = Character("Dziekan")
    define opiekunroku = Character("Opiekun Roku")
    define malfoy = Character("Malfoy")

    define love_u = "Uczelnia Informatyk Różnych"
    define hate_u = "Uczelnia Informatyczno-matematyczna im. P. Czybyszewa"
label chapter1:
    scene bg white

    show text "{color=#000000}Chapter 1\nPierwszy dzień na studiach{/color}"
    pause 2
    hide text

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
        o "Wstajemy!!!"
        m "Tato, co ty zrobiłeś?!"
        o "Wybacz młoda panno, ale nie dałaś mi wyboru, biegiem do łazienki."
    label obudzona:
        scene bg pokoj
        show father at left
        o "Wyglądasz ślicznie córeczko, gdyby tylko mama mogła Cię zobaczyć."
        
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

        o "Zapamiętaj, [m]. Cieszę się że jesteś bardzo ambitna i chcesz iść w moje ślady. Jestem z ciebie taki dumny..."
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

        m "Mam jeszcze 15 minut, tempo mam dobre. Całe szczęście to mam w miarę blisko tutaj."
        m "Nawet ładny ten budynek. Co prawda nie umywa się do [love_u], ale ten wygląda na bardziej zadbany."
        m "Zapomnij o [love_u], [m]. Musisz wziąć to co dało ci życie. Jeśli dobrze Ci pójdzie to będziesz mogła zrobić
        magisterkę na [love_u]. Skup się na tym co jest tu i teraz."
        m "Przedstawienie czas zacząć. Bądź zdecydowana i dumna."

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

        m "Wow, tylu ludzi w jednym miejscu na żywo jeszcze nie widziałam."
        m "Każdy z nich ma swoje cele i ambicje, każdy ma inny powód dla którego się tutaj znalazł.
        Oni wszyscy są moją przyszłą konkurencją na rynku pracy."
        m "Chciałabym mieć jakiś znajomych. Większość moich kolegów i koleżanek
        wyjechało z miasta albo z kraju."
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
        #pokaz dziekana
        dziekan "Witam świeżo upieczonych studentów. Nazywam się prof. Roman Kosior i jestem
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
        #schowaj dziekana
        "Komunikat głosowy" "Informacja dla kierunków pierwszego roku. Zaraz rozpocznie się podpisywanie 
        umów studenckich i odbierania legitymacji. Podaję numery sal: Mechatronika A123, Informatyka A128, 
        BHP A129, Automatyka i Robotyka A130,  BHP A132..."

        #pokazywanie naszej studentki
        if i == 1:
            show main1
        elif i == 2:
            show main2
        elif i == 3:
            show main3

        m "Hmm...a już myślałam, że będę mogła pójść do domu. Męczą mnie takie uroczystości. 
        W sumie nic dziwnego. Większość czasu spędzam przed komputerem."
        m "Może jak będzie już na studiach WF to się zapiszę na jakąś siłownię lub fitness. 
        Trzeba będzie trochę popracować nad kondycją."
        m "Teraz nie pora na takie rzeczy. Trzeba się udać na odbiór legitymacji.. Mam nadzieję, 
        że jakoś przeżyje w tym tłumie."

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

        m "WRESZCIE! Jejku, myślałam, że uduszę się tam. Jestem już na odpowiednim piętrze."
        m "Hmm....która to była sala?" 
        python:
            wrong = False
        label back:
            menu:
                "A123":
                    m "O...k... to była ta sala? No nic przekonajmy sie."
                    #sala wykladowa
                    #pokazywanie naszej studentki
                    m "O matko, to nie ta sala. Ale przypał. Muszę znaleźć właściwą salę."
                    python:
                        wrong = True
                    jump back
                "A129":
                    m "O...k... to była ta sala? No nic przekonajmy sie."
                    #sala wykładowa
                    #pokazywanie naszej studentki
                    m "O matko, to nie ta sala. Ale przypał. Muszę znaleźć właściwą salę."
                    python:
                        wrong = True
                    jump back
                "A128":
                    jump go
        label go:
            #sala wykladowa
            if wrong:
                #pokaz opiekuna
                #pokaz studentke
                opiekunroku "Ludzie kochani. Ilu Was się jeszcze spóźni? Coś kiepsko wróżę Waszą punktualność 
                na przyszłych zajęciach."
                #pokaz draco
                malfoy "Same nieogary na tym kierunku. widać, że moja konkurencja nie zapewni mi nawet żdżbła 
                ekscytacji w \"rywalizacji\". "
                #pokaz studentke
                m "glownabohaterka Mogłam lepiej zapamiętać numer sali. Jestem na siebie potwornie zła. Pierwszy 
                dzien na uczelni i już mi coś nie wychodzi. Muszę się bardziej starac."
                #hide all
            else:
                #pokaz studentke
                m "Chyba trafiłam do dobrej sali. Nie spodziewałam się, że aż tyle osób wybierze ten kierunek. 
                Widzę też sporo dziewczyn. Cieszę się, że jest nas co raz więcej na uczelniach technicznych."
                m "Wciąż przybywają ludzie. Pewnie wcześniej pomylili salę. Dobrze, że udało mi się zapamiętać 
                właściwy numer"
                #hide studentke
        #pokaz opiekuna roku
        opiekunroku "Mam nadzieję, że to już wszyscy. W tym roku naprawdę dużo ludzi dostało się na ten 
        kierunek. Mam nadzieję, że ta sala ogarnie nas wszystkich. Inaczej wykłady będziecie mieli na 
        podwórku."
        #dżwięk masowego śmiechu
        opiekunroku "Na początek chciałabym się wam przedstawić. Jestem doktor Matylda Kostrzewska i 
        jestem opiekunem waszego roku. Równocześnie będę miała z wami zajęcia z Podstaw Programowania."
        "Student1" "Slyszalem, ze starsze roczniki mówią na nią \"Doktor Kosa\""
        "Student2" "Czemu? Aż tak ciężko zaliczyć ten przedmiot?"
        "Student2" "Taa...słyszałem, że do programowania podchodzi bardzo poważnie. Jedna z najbardziej 
        uzdolnionych osob tutaj."
        "Student3" "Dajcie spokój. Ja tam nie wierzę starszym rocznikom. Później okazuje się, że połowa to kłamstwo."
        opiekunroku "...na uroczystości poznaliście jeszcze jedną osobę, z którą będziecie mieli zajęcia w 
        tym semestrze. Nasz dziekan będzie z wami miał Historię Informatyki."
        "Student1" "Co? Dopiero pierwszy semestr a już mamy jakieś wypełniacze w planie."
        opiekunroku "Polecam chodzić, gdyż dziekan bardzo ciekawie prowadzi zajęcia. Z tego co pamiętam to w 
        tamtym roku prawie wszyscy chodzili na zajęcia."
        "Student2" "Chyba jednak przesadzasz, chłopie. Coś czuję, że będzie ciekawie."
        opiekunroku "Plan zajęć zaraz wam przedstawię na tablicy."
        #(pojawia sie zdjecie planu zajec)
        "Stundent1" "Zaczynamy tydzień zajęciami o 8 rano? Matko, już mi się to nie podoba..."
        "Student2" "Matematyka w piątek? Nie ma to jak zepsuć sobie koniec tygodnia."
        opiekunroku "Oooo... najwidoczniej widzę się z wami już w poniedziałek. Też mi się nie podoba ta godzina, 
        ale nie ja mam na to wpływ."
        opiekunroku "Na pierwszych zajęciach poznacie zasady prowadzenia i zaliczenia przedmiotu. 
        Teraz będę wyczytywać alfabetycznie nazwiska. Kiedy kogoś wyczytam ma do mnie podejść by 
        podpisać umowe i odebrać legitymację."
        #(odglos tlumu)
        #hide opiekun roku
        #pokaz studentke
        m "Kobitka nie wydaje się zła. Nie sądzę, że będę z nia miała jakieś problemy. Uczyłam sę na własną rękę 
        programowanie jeszcze jak chodziłam do liceum."
        #pokaz malfoya
        malfoy "...ojciec poważnie rozważał by mnie wysłać na studia do Stanów. Dzięki temu nauczyłabym się więcej 
        niż w tym kraju, ale matka nie chciała bym tak daleko była od domu."
        malfoy "Mimo to, nie jest aż tak źle. Mój ojciec zna tu wielu ludzi. Kiedyś tu wykładal. 
        Z palcem w nosie zrobię magistra, a potem doktorat w USA."
        "Student3" "Wow...aale masz fajnie."
        "Student4" "Prawda. W sumie jesteś ustawiona przez całe studia."
        malfoy "Niby tak, ale to nie oznacza, że nie dam z siebie wszystkiego. Dziwię się, że aż tylu się 
        dostało. Nie jest to problemem."
        malfoy "Rozłożę tych cieniasów tak, że zmienią studia i pójdą na zarządzanie."
        "Student3" "Hhahhaha. Ty to masz gadane, Malfoy."
        m "Jezu....i z kimś takim mam studiować. Gorszej baby jeszcze nie widziałam w swoim życiu. Pewnie jest 
        tylko mocna w gębie ale nic praktycznego zrobić nie potrafi."
        malfoy "Hej, ty. Czemu się na mnie gapisz?"
        menu:
            "To tylko przypadek":
                m "Zwykly przypadek. Przewidziało Ci się najwidoczniej."
                malfoy "Nie udawaj. Widziałam, jak się na mnie lampisz. Czyżbym Cię czymś zdenerwowała?"
                menu:
                    "tak":
                        jump bezznaczenia
                    "nie":
                        jump bezznaczenia
            "Masz coś do mnie???":
                m "Patrzę z politowaniem na twoje przechwałki."
                malfoy "Patrzcie kogo my tu mamy. Masz cięty język. Możesz sobie gadać zdrów, ale i tak przemawia przez Ciebie zazdrość."
                m "Chyba coś Ci się pomyliło, kobieto."
    label bezznaczenia:
        malfoy "Dostrzegłam to. Te spojrzenie. Spojrzenie pełne zazdrości. Mnie nie zwiedziesz."
        malfoy "Masz czego mi zazdrościć, moja droga. Patrząc na Ciebie uważam, że i bez tego wszystkiego jestem 
        lepsza od Ciebie. Wydajesz się być zdeterminowana, ale ja i tak będe górą."
        m "Daj sobie na wstrzymanie, ok? Możesz sobie gadać zdrów, ale mnie to nie obchodzi. Jesteś tylko mocna w gębie."
        malfoy "Tak uważasz? Widzę, że mamy tutaj bojowniczkę. Mam pomysł. Zalóżmy się."
        m "Hę? Jaki zakład?"
        malfoy "O to, kto będzie miał lepszą średnią na koniec semestru."
        m "To trochę dziecinne. Jaka niby miałaby być nagroda."
        malfoy "Jeśli wygrasz, przyznam, że jesteś ode mnie lepsza i dam Ci spokój do konca studiów. 
        Może nawet jakiś projekt grupowy razem zrobimy."
        m "Zabawne. Co jeśli ty wygrasz?"
        malfoy "To proste. Udowodnię swoją wyższość i to, że nie jesteś godzien zainteresowania. Coś czuję, 
        że porażka dla każdej z nas będzie bolesna a wygrana słodkim triumfem."
        malfoy "To jak? Zakładamy się?"
        python:
            a = 1
    label back_malfoy:    
        menu:
            "tak":
                m "Niech Ci będzie. Skoro myślisz, że możesz ze mną rywalizować to próbuj. Nie bronię Ci."
                jump powszystkim
            "nie":
                m "Nie mam po co się zakładać. Nie jesteś godna by ze mną konkurować."
                malfoy "Czcze gadanie. Widzę, że najwyraźniej boisz się ze mną zmierzyć."
                m "Kogo jak kogo, ale Ciebie nie zamierzam się bać."
                malfoy "To udowodnij to. Samymi słowami raczej tego nie zrobisz."
                if a < 2:
                    python:
                        a = a + 1
                    jump back_malfoy
                else: 
                    jump zdenerwowana_studentka
        label zdenerwowana_studentka:
            m "Zaczynasz mnie denerwować. Jeżeli w końcu zdecyduję się na ten zakład to przestaniesz?"
            malfoy "Mi tam nie zależy aż tak. Po prostu nie nawidzę ludzi, którzy boja się sprawdzić swoje umiejętności!"
            m "Dobra, już dobra. Zgadzam sę. Zetrę ten durny uśmiech z Twojej twarzy."
        label powszystkim:
            malfoy "Hahahahahaha. No to ustalone. Pozwól, że zdradze Ci, kim jestem. Nazywam się Draco Malfoy i 
            wiedz, że ze mną tak łatwo nie wygrasz."
            m "Ja jestem [m] Kowalska. Już Ci współczuje przegranej."
            opiekunroku "Pani Kowalska, do mnie!"
            malfoy "Wołają Cię. No to do zobaczenia na zajęciach \"rywalko\". Tylko nie chwal się bardzo, 
            że się założyłyśmy. Wieść o tym, że zadaję się z taką ofiarą zepsuje mi reputację. Hahahahahha."
            #chowaj malfoya
            #pokaz opiekuna roku
            m "W co ja się wpakowałam. No nic. Muszę stawić temu czoła. Nie będzie sobie gówniara pozwalać."
            opiekunroku "Proszę tylko podpis i legitymacja jest już pani."
            m "Dobrze, już podpisuję."

            #(odglos pisania)

            opiekunroku "Oto legitymacja studencka. Powodzenia w studiowaniu i do zobaczenia w poniedziałek."
            m "Dziękuję... napewno się przyda... "
            #hide opiekun roku
            m "Mam już dość tego dnia. Lecz prawdziwy koszmar zacznie sę w poniedziałek. Nie daruję tej babie, 
            że już zrujnowała mi studia. Pokażę na co mnie stać."
            m "Najpierw jednak wrócę do wygodnego wyrka. Wstawanie o tak wczesnej porze jest nieludzkie."
            #jump chapter2
            return
