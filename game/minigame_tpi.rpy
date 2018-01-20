init:
    #popraw 4 i 7
    init python:
        def detective_dragged(drags, drop):
            if not drop:
                return
            store.answer = drags[0].drag_name
            #store.answer = drop.drag_name
            return True

    image bg desk = Image("desk.jpg")

    screen tpi_question1():#DONE
        draggroup:
            drag:
                drag_name "question"
                child "mini2_tpi/question1/question.png"
                draggable False
                droppable False
                dragged detective_dragged
                xpos 280 ypos 100
            drag:
                drag_name "place"
                child "mini2_tpi/place.png"
                draggable False
                droppable True
                xpos 430 ypos 400
            drag:
                drag_name "wrong1"
                child "mini2_tpi/question1/1.png"
                droppable False
                dragged detective_dragged
                xpos 1280/10 ypos 600
            drag:
                drag_name "good"
                child "mini2_tpi/question1/2.png"
                droppable False
                dragged detective_dragged
                xpos 1280*3/10 ypos 600
            drag:
                drag_name "wrong2"
                child "mini2_tpi/question1/3.png"
                droppable False
                dragged detective_dragged
                xpos 1280*5/10 ypos 600
            drag:
                drag_name "wrong3"
                child "mini2_tpi/question1/4.png"
                droppable False
                dragged detective_dragged
                xpos 1280*7/10 ypos 600

    screen tpi_question2():#DONE
        vbox xpos 310 ypos 100:
            text "Cechy Algorytmu:\n\n\n" 
            text "Uniwersalność \n\n\n\n" #dobre
            text "Jednoznaczność \n\n\n\n" #dobre
            text "Unikalność \n\n\n\n"#dobre
            text "Zbieżność "#dobre
        button xpos 200 ypos 160:
            style "checkbox_button"
            action ToggleVariable("tpi_q2_button1")
        button xpos 200 ypos 290:
            style "checkbox_button"
            action ToggleVariable("tpi_q2_button2") 
        button xpos 200 ypos 410:
            style "checkbox_button"
            action ToggleVariable("tpi_q2_button3")
        button xpos 200 ypos 530:
            style "checkbox_button"
            action ToggleVariable("tpi_q2_button4")
        textbutton "Następne" xpos 0.8 ypos 0.9 text_color "#000" text_hover_color "#047" action Jump("next_tpi_q3")
    
    screen tpi_question3():#DONE
        vbox xalign 0.5 yalign 0.70:
            text "Zaleta zapisu graficznego algorytmu"
        hbox xalign 0.5 yalign 0.75:
            textbutton "mała zwięzłość" text_color "#000000" text_hover_color "#0000FF" action Jump("next_tpi_q3_wrong")
            textbutton "bez konstrukcji formalnych" text_color "#000000" text_hover_color "#0000FF" action Jump("next_tpi_q3_wrong")
            textbutton "formalizuje zapis algorytmu" text_color "#000000" text_hover_color "#0000FF" action Jump("next_tpi_q3_good")
    #12. kompilator
    screen tpi_question4():#niezrobione
        draggroup:
            drag:
                drag_name "question"
                child "mini2_tpi/question4/question.png"
                draggable False
                droppable False
                dragged detective_dragged
                xpos 280 ypos 100
            drag:
                drag_name "place"
                child "mini2_tpi/place.png"
                draggable False
                droppable True
                xpos 430 ypos 400
            drag:
                drag_name "wrong1"
                child "mini2_tpi/question4/1.png"
                droppable False
                dragged detective_dragged
                xpos 1280/10 ypos 600
            drag:
                drag_name "wrong"
                child "mini2_tpi/question4/2.png"
                droppable False
                dragged detective_dragged
                xpos 1280*3/10 ypos 600
            drag:
                drag_name "good"
                child "mini2_tpi/question4/3.png"
                droppable False
                dragged detective_dragged
                xpos 1280*5/10 ypos 600
            drag:
                drag_name "wrong3"
                child "mini2_tpi/question4/4.png"
                droppable False
                dragged detective_dragged
                xpos 1280*7/10 ypos 600

    screen tpi_question5(): #DONE
        vbox xpos 310 ypos 100:
            text "BIOS:\n\n\n" 
            text "Podstawowy System Wejścia-wyjścia. \n\n\n\n" #dobre
            text "Posiada zestaw procedur niezbędnych do uruchomienia komputera. \n\n\n\n" #dobre
            text "Wbudowany układ w procesorze \n\n\n\n"#Złe
            text "Steruje wejściem i wyjściem"#ZŁa
        button xpos 200 ypos 160:
            style "checkbox_button"
            action ToggleVariable("tpi_q5_button1")
        button xpos 200 ypos 290:
            style "checkbox_button"
            action ToggleVariable("tpi_q5_button2") 
        button xpos 200 ypos 410:
            style "checkbox_button"
            action ToggleVariable("tpi_q5_button3")
        button xpos 200 ypos 530:
            style "checkbox_button"
            action ToggleVariable("tpi_q5_button4")
        textbutton "Następne" xpos 0.8 ypos 0.9 text_color "#000" text_hover_color "#047" action Jump("next_tpi_q6")

    screen tpi_question6():#done
        vbox xalign 0.5 yalign 0.70:
            text "1001 x 110 = ?"
        hbox xalign 0.5 yalign 0.75:
            textbutton "11 1010" text_color "#000000" text_hover_color "#0000FF" action Jump("next_tpi_q6_wrong")
            textbutton "11 0110" text_color "#000000" text_hover_color "#0000FF" action Jump("next_tpi_q6_good")
            textbutton "11 1110" text_color "#000000" text_hover_color "#0000FF" action Jump("next_tpi_q6_wrong")
    #interpreter
    screen tpi_question7():#niezrobione
        draggroup:
            drag:
                drag_name "question"
                child "mini2_tpi/question7/question.png"
                draggable False
                droppable False
                dragged detective_dragged
                xpos 280 ypos 100
            drag:
                drag_name "place"
                child "mini2_tpi/place.png"
                draggable False
                droppable True
                xpos 430 ypos 400
            drag:
                drag_name "good"
                child "mini2_tpi/question7/1.png"
                droppable False
                dragged detective_dragged
                xpos 1280/10 ypos 600
            drag:
                drag_name "wrong"
                child "mini2_tpi/question7/2.png"
                droppable False
                dragged detective_dragged
                xpos 1280*3/10 ypos 600
            drag:
                drag_name "wrong2"
                child "mini2_tpi/question7/3.png"
                droppable False
                dragged detective_dragged
                xpos 1280*5/10 ypos 600
            drag:
                drag_name "wrong3"
                child "mini2_tpi/question7/4.png"
                droppable False
                dragged detective_dragged
                xpos 1280*7/10 ypos 600

    screen tpi_question8():#DONE
        vbox xpos 310 ypos 100:
            text "Warunek końcowy (wskaż błędne):\n\n\n" 
            text "algorytm musi się zatrzymać \n\n\n\n" #złe
            text "jest to warunek wyjścia z algorytmu \n\n\n\n" #złe
            text "nie wymaga prawdziwości warunku wstępnego \n\n\n\n"#dobre
            text "jeśli jest spełniony to algorytm jest poprawny"#złe
        button xpos 200 ypos 160:
            style "checkbox_button"
            action ToggleVariable("tpi_q8_button1")
        button xpos 200 ypos 290:
            style "checkbox_button"
            action ToggleVariable("tpi_q8_button2") 
        button xpos 200 ypos 410:
            style "checkbox_button"
            action ToggleVariable("tpi_q8_button3")
        button xpos 200 ypos 530:
            style "checkbox_button"
            action ToggleVariable("tpi_q8_button4")
        textbutton "Następne" xpos 0.8 ypos 0.9 text_color "#000" text_hover_color "#047" action Jump("next_tpi_q9")
    
    screen tpi_question9(): #DONE
        vbox xalign 0.5 yalign 0.70:
            text "Wartosc 1100 (ZM) jest równa wartosci 1100 w U2?"
        hbox xalign 0.5 yalign 0.75:
            textbutton "Tak" text_color "#000000" text_hover_color "#0000FF" action Jump("next_tpi_q9_good")
            textbutton "Nie" text_color "#000000" text_hover_color "#0000FF" action Jump("next_tpi_q9_wrong")

    screen tpi_question10():#DONE
        vbox xpos 310 ypos 100:
            text "Główne zadania pamięci podręcznej\n\n\n" 
            text "minimalizacja obciążenie szyny pamięci, w celu udostępnienia jej innym urządzeniom \n\n\n\n" #dobre
            text "optymalizacja operacji wejscia/wyjscia\n\n\n\n" #zle
            text "zapewnia kopie zapasowe najwazniejszych rejonow pamieci\n\n\n\n"#zle
            text "zmniejszenie czasu dostępu do danych dla procesora "#dobre
        button xpos 200 ypos 160:
            style "checkbox_button"
            action ToggleVariable("tpi_q10_button1")
        button xpos 200 ypos 290:
            style "checkbox_button"
            action ToggleVariable("tpi_q10_button2") 
        button xpos 200 ypos 410:
            style "checkbox_button"
            action ToggleVariable("tpi_q10_button3")
        button xpos 200 ypos 530:
            style "checkbox_button"
            action ToggleVariable("tpi_q10_button4")
        textbutton "Następne" xpos 0.8 ypos 0.9 text_color "#000" text_hover_color "#047" action Jump("tpi_end")
    screen tpi_conclusion():
        vbox xalign 0.2 yalign 0.2:
            text "Wynik: [sr_tpi] %"
            text "Pytanie 1: [lista_odp_tpi[0]]"
            text "Pytanie 2: [lista_odp_tpi[1]]"
            text "Pytanie 3: [lista_odp_tpi[2]]"
            text "Pytanie 4: [lista_odp_tpi[3]]" 
            text "Pytanie 5: [lista_odp_tpi[4]]" 
            text "Pytanie 6: [lista_odp_tpi[5]]"
            text "Pytanie 7: [lista_odp_tpi[6]]"
            text "Pytanie 8: [lista_odp_tpi[7]]"
            text "Pytanie 9: [lista_odp_tpi[8]]"
            text "Pytanie 10: [lista_odp_tpi[9]]"
        textbutton "Zakończ" xpos 0.8 ypos 0.9 text_color "#000" text_hover_color "#047" action Jump("tpi_end_jump")  
    default tpi_q2_button1 = False #True
    default tpi_q2_button2 = False #True
    default tpi_q2_button3 = False #False
    default tpi_q2_button4 = False #True

    default tpi_q5_button1 = False #True
    default tpi_q5_button2 = False #True
    default tpi_q5_button3 = False #False
    default tpi_q5_button4 = False #False
    
    default tpi_q8_button1 = False #False
    default tpi_q8_button2 = False #False
    default tpi_q8_button3 = False #True
    default tpi_q8_button4 = False #False
    
    default tpi_q10_button1 = False #True
    default tpi_q10_button2 = False #False
    default tpi_q10_button3 = False #False
    default tpi_q10_button4 = False #True

    python:
        def checker_tpi(lista, para):
            if para == "good":
                lista += ["Dobra"]
            else:
                lista +=["Zła"]

label minigame_tpi:
    scene black
    show text "{color=#FFF}{size=+30}Egzamin z TPI{/size}{/color}"
    pause 2
    hide text

    scene bg desk
    python:
        lista_odp_tpi = []
    $ answer = "wrong"
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(45.1, ui.jumps("next_tpi_q2"))
    call screen tpi_question1
label next_tpi_q2:
    python:
        checker_tpi(lista_odp_tpi, answer)
    scene bg desk
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(45.1, ui.jumps("next_tpi_q3"))
    call screen tpi_question2
label next_tpi_q3:
    python:
        lista_odp_tpi_q2_correct = [True, True, False, True]
        lista_odp_tpi_q2 = varargs(lista_odp_tpi_q2_correct, tpi_q2_button1, tpi_q2_button2, 
            tpi_q2_button3, tpi_q2_button4)
        lista_odp_tpi += [ pytanie(lista_odp_tpi_q2[0],lista_odp_tpi_q2[1],lista_odp_tpi_q2[2],lista_odp_tpi_q2[3]) ]
    scene bg desk
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(45.1, ui.jumps("next_tpi_q3_wrong"))
    call screen tpi_question3
label next_tpi_q3_wrong:
    python:
        lista_odp_tpi += ["Zła"]
    jump next_tpi_q4
label next_tpi_q3_good:
    python:
        lista_odp_tpi += ["Dobra"]
    jump next_tpi_q4
label next_tpi_q4:
    scene bg desk
    $ answer = "wrong"
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(45.1, ui.jumps("next_tpi_q5"))
    call screen tpi_question4
label next_tpi_q5:
    python:
        checker_tpi(lista_odp_tpi, answer)
    scene bg desk
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(45.1, ui.jumps("next_tpi_q6"))
    call screen tpi_question5    
label next_tpi_q6:
    python:
        lista_odp_tpi_q5_correct = [True, True, False, False]
        lista_odp_tpi_q5 = varargs(lista_odp_tpi_q5_correct, tpi_q5_button1, tpi_q5_button2, 
            tpi_q5_button3, tpi_q5_button4)
        lista_odp_tpi += [ pytanie(lista_odp_tpi_q5[0],lista_odp_tpi_q5[1],lista_odp_tpi_q5[2],lista_odp_tpi_q5[3]) ]
    scene bg desk
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(45.1, ui.jumps("next_tpi_q6_wrong"))
    call screen tpi_question6
label next_tpi_q6_wrong:
    python:
        lista_odp_tpi += ["Zła"]
    jump next_tpi_q7
label next_tpi_q6_good:
    python:
        lista_odp_tpi += ["Dobra"]
    jump next_tpi_q7
label next_tpi_q7:
    scene bg desk
    $ answer = "wrong"
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(45.1, ui.jumps("next_tpi_q8"))
    call screen tpi_question7
    #niegotowe
label next_tpi_q8:
    python:
        checker_tpi(lista_odp_tpi, answer)
    scene bg desk
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(45.1, ui.jumps("next_tpi_q9"))
    call screen tpi_question8
label next_tpi_q9:
    python:
        lista_odp_tpi_q8_correct = [False, False, True, False]
        lista_odp_tpi_q8 = varargs(lista_odp_tpi_q8_correct, tpi_q8_button1, tpi_q8_button2, 
            tpi_q8_button3, tpi_q8_button4)
        lista_odp_tpi += [ pytanie(lista_odp_tpi_q8[0],lista_odp_tpi_q8[1],lista_odp_tpi_q8[2],lista_odp_tpi_q8[3]) ]
    scene bg desk
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(45.1, ui.jumps("next_tpi_q9_wrong"))
    call screen tpi_question9
label next_tpi_q9_wrong:
    python:
        lista_odp_tpi += ["Zła"]
    jump next_tpi_q10
label next_tpi_q9_good:
    python:
        lista_odp_tpi += ["Dobra"]
    jump next_tpi_q10
label next_tpi_q10:
    scene bg desk
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(45.1, ui.jumps("tpi_end"))
    call screen tpi_question10
label tpi_end:
    python:
        lista_odp_tpi_q10_correct = [True, False, False, True]
        lista_odp_tpi_q10 = varargs(lista_odp_tpi_q10_correct, tpi_q10_button1, tpi_q10_button2, 
            tpi_q10_button3, tpi_q10_button4)
        lista_odp_tpi += [ pytanie(lista_odp_tpi_q10[0],lista_odp_tpi_q10[1],lista_odp_tpi_q10[2],lista_odp_tpi_q10[3]) ]
        sr_tpi = srednia_prawo(lista_odp_tpi)
        ocena_egz_tpi = srednia_egzamin("Dobra",lista_odp_tpi[0],lista_odp_tpi[1],lista_odp_tpi[2],lista_odp_tpi[3],
            lista_odp_tpi[4],lista_odp_tpi[5],lista_odp_tpi[6],lista_odp_tpi[7],lista_odp_tpi[8],lista_odp_tpi[9])
    scene bg desk
    call screen tpi_conclusion
label tpi_end_jump:
    jump exams_back2
    return
    #niegotowe
#WYMYŚLAM PYTANIA

#4. Specyfikacja:
#wyraża, co algorytm ma robić, i określa związek miedzy jego danymi wejściowymi oraz wyjściowymi. 
#poprawności algorytmu opiera się na jego specyfikacji, która jest czymś niezależnym od kodu programu realizującego algorytm.

#6.Całkowitej poprawności Całkowitej poprawności algorytmu można dowodzić przez dodatkowe: 
#ustalenie zbieżnika (wielkości zależnej od zmiennych i danych, która jest zbieżna) 
#dowiedzenie, że po skończonej liczbie iteracji algorytm zatrzyma się w ostatnim punkcie kontrolnym.

#7. Niezmiennik pętli Niezmiennik pętli
#Niezmiennik pętli to wyrażenie logiczne, którego wartość nie zmienia się podczas wykonywania pętli.
#Określa warunki jakie muszą być zawsze spełnione przez zmienne w pętli, a także przez wartości 
#wczytane lub wypisane. 
#Warunki te muszą być prawdziwe przed pierwszym wykonaniem pętli oraz po każdym jej obrocie.
#8. Podział pętli: 
#pętla z wartownikiem: czyta i przetwarza dane aż do momentu napotkania niedozwolonego elementu 
#pętla z licznikiem: z góry wiadomo ile  razy pętla będzie wykonana 
#pętle ogólne: wszystkie inne
