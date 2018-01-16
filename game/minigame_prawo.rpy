init:
    image bg desk = "desk.png"
    style checkbox_button:
        xysize (100, 100)
        background Image("buttons/unchecked.png") # Unchecked
        #hover_background Solid("#ff0000") # Unchecked Hovered (I usually increase brightness of the image by 15% unsing im. matrix manipulators)
        insensitive_background Solid("#d3d3d3") # Disabled (May not be required, I usually use im.Sepia() for images)
        selected_idle_background Image("buttons/checked.png") # Checked
        selected_hover_background Image("buttons/checked.png") # Checked Hovered
    #gotowe
    screen prawo_question1():
        vbox xpos 310 ypos 100:
            text "Przesłanki ochrony dóbr osobistych:\n\n\n\n" 
            text "istnienie dobra osobistego prawnie chronionego\n\n\n\n"#dobre
            text "fakt jego naruszenia przez cudze zachowanie\n\n\n\n"#dobre
            text "bezprawność zachowania naruszającego"#dobre
        button:
            style "checkbox_button"
            align (0.15, 0.3)
            action ToggleVariable("prawo_q1_button1")
        button:
            style "checkbox_button"
            align (0.15, 0.5)
            action ToggleVariable("prawo_q1_button2") 
        button:
            style "checkbox_button"
            align (0.15, 0.7)
            action ToggleVariable("prawo_q1_button3")
        textbutton "Następne" xpos 0.8 ypos 0.9 text_color "#000" text_hover_color "#047" action Jump("prawo_question2")
    #gotowe
    screen prawo_question2():
        vbox xpos 310 ypos 100:
            text "Szkodę dzielimy na:\n\n\n" 
            text "majątkową – strata oraz utracenie korzyści (odszkodowanie) \n\n\n\n"#dobre
            text "umyślna to z zamiarem bezpośrednim albo z zamiarem ewentualnym\n\n\n\n"#zle
            text "bezprawność zachowania naruszającego\n\n\n"#zle
            text "niemajątkową – tzw. krzywda, ból fizyczny, psychiczny, \nnegatywne moralne psychiczne doznania"#dobre
        button xpos 200 ypos 160:
            style "checkbox_button"
            action ToggleVariable("prawo_q2_button1")
        button xpos 200 ypos 290:
            style "checkbox_button"
            action ToggleVariable("prawo_q2_button2") 
        button xpos 200 ypos 410:
            style "checkbox_button"
            action ToggleVariable("prawo_q2_button3")
        button xpos 200 ypos 530:
            style "checkbox_button"
            action ToggleVariable("prawo_q2_button4")
        textbutton "Następne" xpos 0.8 ypos 0.9 text_color "#000" text_hover_color "#047" action Jump("prawo_question3")
    #jeszcze nie gotowe
    screen prawo_question3():
        vbox xpos 310 ypos 100:
            text "Autorskie prawa majątkowe. Prawo do:\n\n\n\n"
            text "korzystania z utworu\n\n\n\n" #dobre
            text "rozporządzania utworem\n\n\n\n" #dobre
            text "pobierania wynagrodzenia za korzystanie z utworu" #dobre 
        button:
            style "checkbox_button"
            align (0.15, 0.3)
            action ToggleVariable("prawo_q3_button1")
        button:
            style "checkbox_button"
            align (0.15, 0.5)
            action ToggleVariable("prawo_q3_button2") 
        button:
            style "checkbox_button"
            align (0.15, 0.7)
            action ToggleVariable("prawo_q3_button3")
        textbutton "Następne" xpos 0.8 ypos 0.9 text_color "#000" text_hover_color "#047" action Jump("prawo_question4")

    screen prawo_question4():
        vbox xpos 310 ypos 100:
            text "Wymogi formalne Patentu:\n\n\n" 
            text "posiada poziom wynalazczy \n\n\n\n"#dobre
            text "nadaje się do przemysłowego stosowania\n\n\n\n"#dobre
            text "posiadający indywidualny charakter \n\n\n\n"#zle
            text "polega na przestrzennym, wyrażonym w dowolny sposób rozplanowaniu elementów"#zle
        button xpos 200 ypos 160:
            style "checkbox_button"
            action ToggleVariable("prawo_q4_button1")
        button xpos 200 ypos 290:
            style "checkbox_button"
            action ToggleVariable("prawo_q4_button2") 
        button xpos 200 ypos 410:
            style "checkbox_button"
            action ToggleVariable("prawo_q4_button3")
        button xpos 200 ypos 530:
            style "checkbox_button"
            action ToggleVariable("prawo_q4_button4")
        textbutton "Następne" xpos 0.8 ypos 0.9 text_color "#000" text_hover_color "#047" action Jump("prawo_question5")

    screen prawo_question5():
        vbox xpos 310 ypos 100:
            text "PATENTÓW nie udziela się na\n\n\n" 
            text "Wynalazki \n\n\n\n"#zle
            text "Odmiany roślin lub rasy zwierząt\n\n\n\n"#dobre
            text "Wzór użytkowy \n\n\n\n"#zle
            text "Wzór przemysłowy"#zle
        button xpos 200 ypos 160:
            style "checkbox_button"
            action ToggleVariable("prawo_q5_button1")
        button xpos 200 ypos 290:
            style "checkbox_button"
            action ToggleVariable("prawo_q5_button2") 
        button xpos 200 ypos 410:
            style "checkbox_button"
            action ToggleVariable("prawo_q5_button3")
        button xpos 200 ypos 530:
            style "checkbox_button"
            action ToggleVariable("prawo_q5_button4")
        textbutton "Następne" xpos 0.8 ypos 0.9 text_color "#000" text_hover_color "#047" action Jump("prawo_question6")

    screen prawo_question6():
        vbox xpos 310 ypos 100:
            text "Cechy autorskich praw osobistych:\n\n\n" 
            text "są dziedziczone \n\n\n\n"#zle
            text "przysługują wyłącznie twórcy \n\n\n\n"#dobre
            text "nie są przedmiotem obrotu, nie można ich zbyć  \n\n\n\n"#dobre
            text "można ich się zrzec "#zle
        button xpos 200 ypos 160:
            style "checkbox_button"
            action ToggleVariable("prawo_q6_button1")
        button xpos 200 ypos 290:
            style "checkbox_button"
            action ToggleVariable("prawo_q6_button2") 
        button xpos 200 ypos 410:
            style "checkbox_button"
            action ToggleVariable("prawo_q6_button3")
        button xpos 200 ypos 530:
            style "checkbox_button"
            action ToggleVariable("prawo_q6_button4")
        textbutton "Następne" xpos 0.8 ypos 0.9 text_color "#000" text_hover_color "#047" action Jump("prawo_end")
    screen prawo_conclusion():
        vbox xalign 0.2 yalign 0.2:
            text "Wynik: [sr_prawo] %"
            text "Pytanie 1: [odp_pyt[0]]"
            text "Pytanie 2: [odp_pyt[1]]"
            text "Pytanie 3: [odp_pyt[2]]"
            text "Pytanie 4: [odp_pyt[3]]" 
            text "Pytanie 5: [odp_pyt[4]]" 
            text "Pytanie 6: [odp_pyt[5]]"
        textbutton "Zakończ" xpos 0.8 ypos 0.9 text_color "#000" text_hover_color "#047" action Jump("prawo_run")  
    #-------------------------------
    default prawo_q1_button1 = False #True
    default prawo_q1_button2 = False #True
    default prawo_q1_button3 = False #True
    #-------------------------------
    default prawo_q2_button1 = False #True
    default prawo_q2_button2 = False #False
    default prawo_q2_button3 = False #False
    default prawo_q2_button4 = False #True
    #-------------------------------
    default prawo_q3_button1 = False #True
    default prawo_q3_button2 = False #True
    default prawo_q3_button3 = False #True
    #-------------------------------
    default prawo_q4_button1 = False #True
    default prawo_q4_button2 = False #True
    default prawo_q4_button3 = False #False
    default prawo_q4_button4 = False #False
    #-------------------------------
    default prawo_q5_button1 = False #False
    default prawo_q5_button2 = False #True
    default prawo_q5_button3 = False #False
    default prawo_q5_button4 = False #False
    #-------------------------------
    default prawo_q6_button1 = False #False
    default prawo_q6_button2 = False #True
    default prawo_q6_button3 = False #True
    default prawo_q6_button4 = False #False
    #-------------------------------
    python:
        def varargs(keylist, *args):
            licznik = 0
            odp = []
            for arg in args:
                if arg == keylist[licznik]:
                    odp += ["Dobra"]
                else:
                    odp += ["Zla"]
                licznik = licznik + 1
            return odp

        lista_odp = [True, True, True, True, False, 
            False, True, True, True, True, True, 
            True, False, False, False, True, False, 
            False, False, True, True, False]

        def pytanie(*args):
            good = True
            for arg in args:
                if arg == "Zla":
                    return "Zła"
            return "Dobra"
        def srednia_prawo(lista_odp_pyt):
            n = len(lista_odp_pyt)
            suma = 0
            for d in lista_odp_pyt:
                if d == "Dobra":
                    suma += 1
            return round(float(suma)/n,2) * 100
                

label minigame_prawo:
    scene bg white
    show text "{color=#000000}Egzamin z Prawa{/color}"
    pause 2
    hide text

    scene bg desk
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(30.1, ui.jumps("prawo_question2"))
    call screen prawo_question1
label prawo_question2:
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(30.1, ui.jumps("prawo_question3"))
    call screen prawo_question2
label prawo_question3:
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(30.1, ui.jumps("prawo_question4"))
    call screen prawo_question3
label prawo_question4:
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(30.1, ui.jumps("prawo_question5"))
    call screen prawo_question4
label prawo_question5:
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(30.1, ui.jumps("prawo_question6"))
    call screen prawo_question5
label prawo_question6:
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(30.1, ui.jumps("prawo_end"))
    call screen prawo_question6
label prawo_end:
    scene bg desk
    python:
        odpowiedzi = varargs(lista_odp, prawo_q1_button1, prawo_q1_button2, prawo_q1_button3,
            prawo_q2_button1, prawo_q2_button2, prawo_q2_button3, prawo_q2_button4,
            prawo_q3_button1, prawo_q3_button2, prawo_q3_button3, prawo_q4_button1,
            prawo_q4_button2, prawo_q4_button3, prawo_q4_button4, prawo_q5_button1,
            prawo_q5_button2, prawo_q5_button3, prawo_q5_button4, prawo_q6_button1,
            prawo_q6_button2, prawo_q6_button3, prawo_q6_button4)
        odp_pyt = []
        odp_pyt += [ pytanie(odpowiedzi[0], odpowiedzi[1], odpowiedzi[2]) ]
        odp_pyt += [ pytanie(odpowiedzi[3], odpowiedzi[4], odpowiedzi[5], odpowiedzi[6]) ]
        odp_pyt += [ pytanie(odpowiedzi[9], odpowiedzi[7], odpowiedzi[8]) ]
        odp_pyt += [ pytanie(odpowiedzi[13], odpowiedzi[10], odpowiedzi[11], odpowiedzi[12]) ]
        odp_pyt += [ pytanie(odpowiedzi[17], odpowiedzi[14], odpowiedzi[15], odpowiedzi[16]) ]
        odp_pyt += [ pytanie(odpowiedzi[21], odpowiedzi[18], odpowiedzi[19], odpowiedzi[20]) ]
        sr_prawo = srednia_prawo(odp_pyt)
        ocena_egz_prawo = srednia_egzamin("Dobra", odp_pyt[0], odp_pyt[1], odp_pyt[2], odp_pyt[3], odp_pyt[4], odp_pyt[5])
    call screen prawo_conclusion
label prawo_run:
    jump exams_back3
    return
