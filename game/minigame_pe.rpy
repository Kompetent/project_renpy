init:

    image bg pe_q1 = "mini3_pe/question1.png"

    screen pe_question1():#DONE
        text "Jaki element nalezy \nwstawic, by dioda \npracowala poprawnie?" xalign 0.05 yalign 0.2
        draggroup:
            drag:
                drag_name "place"
                child "mini3_pe/nieznane.png"
                draggable False
                droppable True
                xpos 420 ypos 30
            drag:
                drag_name "wrong1"
                child "mini3_pe/dioda.png"
                droppable False
                dragged detective_dragged
                xpos 1280/10 ypos 520
            drag:
                drag_name "good"
                child "mini3_pe/rezystor.png"
                droppable False
                dragged detective_dragged
                xpos 1280*3/10 ypos 520
            drag:
                drag_name "wrong2"
                child "mini3_pe/kondensator.png"
                droppable False
                dragged detective_dragged
                xpos 1280*5/10 ypos 520
            drag:
                drag_name "wrong3"
                child "mini3_pe/cewka.png"
                droppable False
                dragged detective_dragged
                xpos 1280*7/10 ypos 520
    screen pe_question2():#DONE
        hbox xalign 0.2 yalign 0.2:
            text "Prawo "
            input default "(uzupelnij)":
                style "wpis"
        vbox xalign 0.3 yalign 0.3:
            text "Stosunek natężenia prądu płynącego przez przewodnik do "
            text "napięcia panującego między końcami przewodnika "
            text "jest stały."
    screen pe_question3():
        text "Jak nazywa się przedstawiony element?" xalign 0.2 yalign 0.3
        draggroup:
            drag:
                drag_name "question"
                child "mini3_pe/kondensator.png"
                draggable False
                droppable False
                dragged detective_dragged
                xpos 1280/4 ypos 300
            drag:
                drag_name "place"
                child "mini3_pe/nieznane.png"
                draggable False
                droppable True
                xpos 1280/2 ypos 300
            drag:
                drag_name "good"
                child "mini3_pe/kondensator_odp.png"
                droppable False
                dragged detective_dragged
                xpos 1280/10 ypos 520
            drag:
                drag_name "wrong1"
                child "mini3_pe/rezystor_odp.png"
                droppable False
                dragged detective_dragged
                xpos 1280*3/10 ypos 520
            drag:
                drag_name "wrong2"
                child "mini3_pe/zrodlo_odp.png"
                droppable False
                dragged detective_dragged
                xpos 1280*5/10 ypos 520
            drag:
                drag_name "wrong3"
                child "mini3_pe/cewka_odp.png"
                droppable False
                dragged detective_dragged
                xpos 1280*7/10 ypos 520
    screen pe_question4():
        vbox xalign 0.5 yalign 0.70:
            text "Kazdy prąd gałęziowy i każde napięcie gałęziowe jest kombinacją liniową napięć i "
            text "prądów źródłowych. Jakie to twierdzenie?"
        hbox xalign 0.5 yalign 0.75:
            textbutton "I prawo Kirchoffa" text_color "#000000" text_hover_color "#0000FF" action Jump("next_pe_q4_wrong")
            textbutton "Prawo Tellegena" text_color "#000000" text_hover_color "#0000FF" action Jump("next_pe_q4_wrong")
            textbutton "Metoda superpozycji" text_color "#000000" text_hover_color "#0000FF" action Jump("next_pe_q4_good")
    screen pe_question5():#DONE
        hbox xalign 0.2 yalign 0.2:
            text "Prawo "#II Kirchhoffa, 2 Kirchoffa, Drugie Kirchoffa
            input default "(dwa-słowa)":
                style "wpis"
        vbox xalign 0.3 yalign 0.3:
            text "W zamkniętym obwodzie suma spadków napięć na oporach równa "
            text "jest sumie sił elektromotorycznych występujących w tym obwodzie"
    screen pe_question6():#DONE
        text "Jak nazywa się przedstawiony element?" xalign 0.2 yalign 0.3
        draggroup:
            drag:
                drag_name "question"
                child "mini3_pe/cewka.png"
                draggable False
                droppable False
                dragged detective_dragged
                xpos 1280/4 ypos 300
            drag:
                drag_name "place"
                child "mini3_pe/nieznane.png"
                draggable False
                droppable True
                xpos 1280/2 ypos 300
            drag:
                drag_name "wrong3"
                child "mini3_pe/kondensator_odp.png"
                droppable False
                dragged detective_dragged
                xpos 1280/10 ypos 520
            drag:
                drag_name "wrong1"
                child "mini3_pe/rezystor_odp.png"
                droppable False
                dragged detective_dragged
                xpos 1280*3/10 ypos 520
            drag:
                drag_name "wrong2"
                child "mini3_pe/zrodlo_odp.png"
                droppable False
                dragged detective_dragged
                xpos 1280*5/10 ypos 520
            drag:
                drag_name "good"
                child "mini3_pe/cewka_odp.png"
                droppable False
                dragged detective_dragged
                xpos 1280*7/10 ypos 520
    screen pe_conclusion():
        vbox xalign 0.2 yalign 0.2:
            text "Pytanie 1: [odp_pe_q1]"
            text "Pytanie 2: [odp_pe_q2]"
            text "Pytanie 3: [odp_pe_q3]"
            text "Pytanie 4: [odp_pe_q4]" 
            text "Pytanie 5: [odp_pe_q5]" 
            text "Pytanie 6: [odp_pe_q6]"
            text "Ocena : [ocena_egz_pe]"
        textbutton "Zakończ" xpos 0.8 ypos 0.9 text_color "#000" text_hover_color "#047" action Jump("pe_run_next")
label minigame_pe:
    scene bg white
    show text "{color=#000000}Egzamin z Podstaw Elektroniki{/color}"
    pause 2
    hide text

    $ answer = "wrong"
    scene bg pe_q1
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(30.1, ui.jumps("next_pe_q2"))
    call screen pe_question1
label next_pe_q2:
    scene bg white
    if answer == "good":
        $ odp_pe_q1 = "Dobra"
    else:
        $ odp_pe_q1 = "Zła"
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(30.1, ui.jumps("next_pe_q3"))
    call screen pe_question2
label next_pe_q3:
    $ odp_pe_q2 = analiza_correct_answer(_return, "Ohma","Ohma ", " Ohma")
    scene bg white
    $ answer = "wrong"
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(30.1, ui.jumps("next_pe_q4"))
    call screen pe_question3
label next_pe_q4:
    scene bg white
    if answer == "good":
        $ odp_pe_q3 = "Dobra"
    else:
        $ odp_pe_q3 = "Zła"
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(30.1, ui.jumps("next_pe_q4_wrong"))
    call screen pe_question4
label next_pe_q4_wrong:
    $ odp_pe_q4 = "Zła"
    jump next_pe_q5
label next_pe_q4_good:
    $ odp_pe_q4 = "Dobra"
label next_pe_q5:
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(30.1, ui.jumps("next_pe_q6"))
    call screen pe_question5
label next_pe_q6:
    $ odp_pe_q5 = analiza_correct_answer(_return, "II Kirchhoffa", "2 Kirchhoffa", "Drugie Kirchhoffa")
    $ answer = "wrong"
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(30.1, ui.jumps("pe_end"))
    call screen pe_question6
label pe_end:
    if answer == "good":
        $ odp_pe_q6 = "Dobra"
    else:
        $ odp_pe_q6 = "Zła"
    python:
        ocena_egz_pe = srednia_egzamin("Dobra", odp_pe_q1, odp_pe_q2, odp_pe_q3, odp_pe_q4, odp_pe_q5, odp_pe_q6)
    call screen pe_conclusion
label pe_run_next:
    jump exams_back5
