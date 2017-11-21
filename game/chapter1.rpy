init:
    image bg pokoj = "pokoj.jpg"
    image bg aula = "aula.jpg"
    image bg miasto = "miasto.jpg"

    image side father = "father.png"
    define o = Character("Ojciec", image="father")
    define dziekan = Character("Dziekan")
    define love_u = "Uczelnia Informatyk Różnych"
    define hate_u = "Uczelnia Informatyczno-matematyczna im. P. Czybyszewa"
label chapter1:
    scene bg white

    show text "{color=#000000}Chapter 1\nPierwszy dzień na studiach{/color}"
    pause 2
    hide text

    scene black
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

        o "Wyglądasz ślicznie córeczko, gdyby tylko mama mogła Cię zobaczyć."
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

        m "Wow, tylu ludzi w jednym miejscu na żywo jeszcze nie widziałam."
        m "Każdy z nich ma swoje cele i ambicje, każdy ma inny powód dla którego się tutaj znalazł.
        Oni wszyscy są moją przyszłą konkurencją na rynku pracy."
        m "Chciałabym mieć jakiś znajomych. Większość moich kolegów i koleżanek
        wyjechało z miasta albo z kraju."
        m "Czy serio potrzebuje kogoś mieć? Czy nie powinnam skupić się na własnej karierze?
        Ojciec chyba ma rację, nie mogę zmarnować tego czasu, który mam. Będziesz ze mnie
        dumny tato i... mamo. "

        #podniosła muzyka

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

    #jump chapter2
    return
