init:
    image bg niebo = "niebo3.jpg"
label chapter5:
    scene black
    show text "{color=#FFF}{size=+30}Chapter 5\nZakończenie{/size}{/color}"
    pause 2
    #ważne zmienne:
    #--- zyciowe:
    #piwo_piatek2
    #piwo_piatek3
    #pomoglas_amandzie
    #marta_zostala_uspokojona
    #--- ocenowe:
    #ocena_egz_pp1
    #ocena_egz_prawo
    #ocena_egz_tpi
    #ocena_egz_mat
    #ocena_egz_pe
    
    scene bg niebo
    show narrator at left
    $ zaliczone = 0
    ob "Ho ho ho. Widzę, że Twoja przygoda z Wonderful time dobiega już końca. Cieszę się, że mogłem śledzić Twje poczynania"
    ob "Mówiłem Ci kiedyś, że jeszcze si zobaczymy. Oto jestem, bym mógł podsumować całą Twoją rozgrywkę."
    ob "O, tak! Mam już Twoje wyniki z egzaminów, ale nie tylko na nich się skupię."
    ob "Hmm? Nerwy? Hahaha. Typowe studenckie zachowanie!"
    #(kolo ob pojawia sie nazwa przedmiotu i ocena)
    #Podstawy Programowania
    #----------------------------------------------------------------------------------------
    if ocena_egz_pp1 >= 3:
        python:
            zaliczone += 1
        ob "Podstawy Programowania poszły Ci dobrze. To ważna rzecz. Zapamiętaj jedno. Umiejętność programowania jest najważniejszą umiejętnością informatyka. Chylę czoła."
    else:
        ob "Widzę, że Podstawy Programowania nie poszły Ci najlepiej.Doktor Matylda też pewnie jest z tego powodu smutna."
        ob "Programowanie to najważniejsza umiejętność informatyka. Przyłóż się do niej, jeśli planujesz przyszłość w tej branży!"
    #----------------------------------------------------------------------------------------------
    #Podstawy Elektroniki
    if ocena_egz_pe >= 3:
        python:
            zaliczone += 1
        ob "Popatrzmy na Podstawy Elektroniki. Całkiem, całkiem Ci to wyszło! Dziekan to naprawdę miała..."
        ob "osoba, co nie? Mając takie podejście do studentów można z nimi osiągnąć wiele wspaniałych rzeczy. Chciałabyś go kiedyś bliżej poznać."
    else:
        ob "Popatrzmy na Podstawy Elektroniki. Oj...nie wygląda to dobrze. Wielka szkoda. Elektronika też jest bardzo przydatna jeśli chodzi o IT."
        ob "Co raz więcej programistów zapomina o tym, że wiedza na temat sprzetu jest istotna. Mam nadzieję, że następnym raem będziesz uważniej słuchać Dziekana!"
    #----------------------------------------------------------------------------------------------
    #Teoretyczne Podstawy Informatyki
    if ocena_egz_tpi >= 3:
        python:
            zaliczone += 1
        ob "Co my tu mamy? Ahh...Teoretyczne Podstawy informatyki. Niezły wynik, gratuluję!"
        ob "Doktor Ikar to nie jest najlepsza postać do naśladowania. Kto wie, ile podobnych numerów"
        ob "jak ten ostatni poszło mu płazem. Nie patrz na wykładowców przez pryzmat Ikara. Żli ludzie zdarzają się wszędzie."
        ob "Trzeba być czujnym by w miarę szybko ich dostrzec."
    else:
        ob "Przedmiot doktora Ikara? Dalej nie wierzę w to co zrobił. Niestety nie udało się tym razem."
        ob "Wiem, że każdy chciały uczyć się poprzez praktykę, ale bez teori dalek sie nie zajedzie."
        ob "Przyłóż się pilniej do tego przedmiotu. Gwarantuję , że wyjdziesz na tym na dobre!"
    #---------------------------------------------------------------------------------------------------------
    #Prawo inżynierskie
    if ocena_egz_prawo >= 3:
        python:
            zaliczone += 1
        ob "Haha...Prawo inżynierskie. Jestem zadowolony z Twojego wyniku. Nie wiem, czy mógłym dodać tutaj coś więcej."
        ob "Prosty, ale istotny przedmiot! Pamiętaj, że nieznajomość prawa szkodzi."
    else:
        ob "Prawo inżynierski...niestety dość kiepsko Ci poszło. Zdaję sobię sprawę, że przedmiot nie był jakiś porywający, ale to nie znaczy, że można go olać!"
        ob "Pamiętaj, że nieznajomość paragrafów prawnych nie zwalnia z ich przestrzegania. Taka wiedza, może w przyszłości Ci bardzo pomóc."
    #-----------------------------------------------------------------------------------------------------------
    #Analiza matematyczna
    if ocena_egz_mat >= 3:
        python:
            zaliczone += 1
        ob "Na ostatnim miejscu mamy analizę matematyczną. Dobrze, została zaliczona."
        ob "Matematyka jest bardzo potrzebna programistom. Dzięki niej rozszerzą się Twoje możliwości!"
        ob "Matematyka to język, w którym został zaprogramowany świat, hehe..."
    else:
        ob "Ostatni przedmiot, czyli Analiza Matematyczna. Ojć, niedobrze. Widzę, że masz dużo braku w wiedzy. Bez matematyki daleko nie zajedziesz. "
        ob "Matematyka rozwija logiczne myślenie i pomaga w programowaniu. Sądzę, że arto do niej przysiąść."
#--------------------------------------------------------------------------------------------------------
    if zaliczone == 0:
        ob "Muszę przyznać, że jestem rozczarowany. Nie spodziewałem się takich wyników. Widać, że nie potraktowałeś moich rad poważnie. Nie jestem zły. Jest mi tylko"
        ob "bardzo przykro. Oto koniec Twojej przygody z Wonderful Time. Jeśli kiedyś choć trochę nad sobą popracujesz to wróc tutaj. Będę na Ciebie czekał..."
        scene black
        show text "{color=#F00} GAME OCER {/color}"
        pause 5
        return
    #(gra sie konczy, tyle; to co nizej sie nie wydarza)
    ob"Sprawę studiów mamy już z głowy! Pogadajmy jeszcze przez chwilę o innym aspekcie."
    ob "Podczas tego semstru przewinęło się wielu interesujących ludzi. Zatrzymajmy się przy nich."
    #--------------------------------------------------------------------------------------------------------
    if marta_zostala_uspokojona:
        ob "Cieszę się, że pomogłeś/pomogłaś Marcie. To fajna dziewczyna i jeszcze lepsza przyjaciółka. Czuję, że Wasza przyjaźń będzie bardzo silna. Niczym stal!"
    else:
        ob "Szkoda, że jednak nie pomogłaś Marcie. Wiem, że tego żałujesz, ale musisz zawsze pamiętać o konsekwencjach woich decyzji. Na tym polega dorosłe życie."
    #----------------------------------------------------------------------------------------------------------
    ob "Adam...dosyć ciekawy młodzieniec. Widać po nim, że jest to materiał na dobrego i wiernego przyjaciela. W dzisiejszych czaseach ze świecą takich szukać. Cieszę się, że go poznałeś/poznałaś."
    #------------------------------------------------------------------------------------------------------------------
    #jezeli poszlismy do baru z Marta/Adamem:
    if piwo_piatek2 or piwo_piatek3:
        ob "Dobrze, że zbliżyłeś/zbliżyłaś się do ludzi. Osiągnięcie postawionych sobie celów"
        ob "jest bardzo ważne, ale kontakty międzyludzkie też. Z kim będziesz świętować swoje sukcesy? Kto będzie Cię wspierał podczas trudnych chwil?"
        ob "Przyjaciele to ważna rzecz. Cieszę się, że nie zostali oni przez Ciebie zapomniani!"
    else:
        ob "Mimo wielu poznanycch ludzi nie zbliżyłeś/zbliżyłaś się do nich. To bardzo smutne. siągnięcie postawionych sobie celów"
        ob "jest bardzo ważne, ale kontakty międzyludzkie też. Z kim będziesz świętować swoje sukcesy? Kto będzie Cię wspierał podczas trudnych chwil?"
        ob "Pamiętaj, nie jesteś sama!"
    #---------------------------------------------------------------------------------------------------------------------
    if pomoglas_amandzie:
        ob "Ahh...Amanda. Ciekawa osobistość z niej. Cieszę się, że mimo nienawiści,jaka była przez Ciebie gromadzona od początku semestru pomogłeś/pomogłaś jej w tak ciężkiej sytuacji. Masz serce po właściwej stronie!"
    else:
        ob "Ahh...Amanda. Ciekawa osobistość z niej. Sądzę, że mimo jej wielkiej upartości powinieneś/powinnaś jej pomóc. Nie obwiniam Cię za brak pomocy."
        ob "Myślę jednak, że taki gest byłby początkiem czegoś wielkiego. Szkoda, że się nie udało...."
    #-------------------------------------------------------------------------------------------------------------------
    ob "Przypadek Amandy jest bardzo dołujący. Jej charakter został nakreślony przez jej starającego sę być zawsze idealnym ojczluka."
    ob "Myślę, że jeśli dasz jej szansę się otwozyć to będzie można pomóc się jej zmienić. Głęboko w to wierzę!"

    if zaliczone == 5:
        play music "music/bensound-love.ogg"
        scene bg white
        show text "EPILOG"
        pause 2

        scene bg korytarz
        show draco at left
        if i == 1:
            show main1 at right
        elif i == 2:
            show main2 at right
        elif i == 3:
            show main3 at right
        malfoy "Widziałam Twoje oceny. Gratuluję Ci."
        m "Heh, dzięki. Jk Tobie poszło? Musimy sprawdzić kto wygrał!"
        malfoy "Daj spokój. Oceny nie są istotne. Już Ci mówiłam. Jesteś lepsza ode mnie. Masz serce po właściwej stronie."
        m "Nie jesteś stracona. Ty również możesz je takie mieć."
        malfoy "Sądzisz, że jest jeszcze sens mnie naprostowywać?"
        m "Sądzę, że jest. Udowodniłaś mi to podczas nasego wypadku."
        malfoy "Dziękuję...zdajesz sobie sprawę z jakim beznadziejnym uczniem będziesz miała doczynienia?"
        m "Hahaha...nie od razu Rzym zbudowano. Twierdzę jednak, że warto poświęcić trochę czasu i wysiłku na Ciebie."
        #(cisza)
        #(cisza)
        #(cisza)

        #(odgłos placzu)
        malfoy "Dziękuję Ci. Dziękuje Ci, że jesteś."
        #(ekran się cały ściemnia)
        m "Jeżeli w następnym semestrze będę musiała znowu wstawać na 8 rano to chyba oszaleję..."
    else:
        ob "Dobrze obserwowało się Twoje poczynania. Sądzę jednak, że mogło Ci pójć znacznie lepiej. Lepsze oceny albo wykorzystanie pojawiających się możliwości."
        ob "Sądzę, że jeszcze zostały Ci jeszcze pewne rzeczy do zrobienia. Może też chcesz zobaczyć co stanie się, jak podejmiesz inne decyzje?"
        ob "Poczekam tu na Ciebie, aż skonczysz wszytko to, co Wonderful Time ma do zaoferowania. Zobaczymy się wkrótce."
        ob "Hmm, czy wspominałem, że potrafię podrózować w czasie? Nie? No to popatrz na to!"

    scene black
    show text "{color=#FFF} Dziękujemy za grę {/color}"
    pause 5
    return