init:
    screen mat_kart2_question1():
        vbox xalign 0.5 yalign 0.70:
            text "Mówimy, że ciąg (an) jest rozbieżny do + nieskończoności, gdy prawie wszystkie wyrazy ciągu (an) "
        hbox xalign 0.5 yalign 0.75:
            textbutton "są większe od dowolnej liczby dodatniej" text_color "#000000" text_hover_color "#0000FF" action Jump("next_mat_kart2_q1_good")
            textbutton "są mniejsze od dowolnej liczby dodatniej" text_color "#000000" text_hover_color "#0000FF" action Jump("next_mat_kart2_q1_wrong")
            textbutton "są większe od zera " text_color "#000000" text_hover_color "#0000FF" action Jump("next_mat_kart2_q1_wrong")
    screen mat_kart2_question2():
        vbox xalign 0.5 yalign 0.70:
            text "Każdy ciąg posiada co najwyżej ... granice"
        hbox xalign 0.5 yalign 0.75:
            textbutton "cztery" text_color "#000000" text_hover_color "#0000FF" action Jump("next_mat_kart2_q2_wrong")
            textbutton "dwie" text_color "#000000" text_hover_color "#0000FF" action Jump("next_mat_kart2_q2_wrong")
            textbutton "jedną" text_color "#000000" text_hover_color "#0000FF" action Jump("next_mat_kart2_q2_good")
    screen mat_kart2_question3():
        vbox xalign 0.5 yalign 0.70:
            text "Czy istnieje granica dla an = (-1)^n ?"
        hbox xalign 0.5 yalign 0.75:
            textbutton "  Tak  " text_color "#000000" text_hover_color "#0000FF" action Jump("next_mat_kart2_q3_wrong")
            textbutton "  Nie  "  text_color "#000000" text_hover_color "#0000FF" action Jump("next_mat_kart2_q3_good")

label mat_kart2: 
    scene bg white
    show text "{color=#000000}Kartkówka druga z Analizy Matematycznej{/color}"
    pause 2
    hide text

    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(10.1, ui.jumps("next_mat_kart2_q1_wrong"))
    call screen mat_kart2_question1
    label next_mat_kart2_q1_good:
        $ mat_q1 = "Dobrze"
        jump next_mat_kart2_q2
    label next_mat_kart2_q1_wrong:
        $ mat_q1 = "{color=#f00}Źle{/color}"

label next_mat_kart2_q2:
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(10.1, ui.jumps("next_mat_kart2_q2_wrong"))
    call screen mat_kart2_question2
    label next_mat_kart2_q2_good:
        $ mat_q2 = "Dobrze"
        jump next_mat_kart2_q3
    label next_mat_kart2_q2_wrong:
        $ mat_q2 = "{color=#f00}Źle{/color}"

label next_mat_kart2_q3:
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(10.1, ui.jumps("next_mat_kart2_q3_wrong"))
    call screen mat_kart2_question3
    label next_mat_kart2_q3_good:
        $ mat_q3 = "Dobrze"
        jump end_kart2_mat
    label next_mat_kart2_q3_wrong:
        $ mat_q3 = "{color=#f00}Źle{/color}"
label end_kart2_mat:
    #obliczenie oceny
    python:
        ocena_kart2_mat = srednia_kartkowka("Dobrze", mat_q1, mat_q2, mat_q3)
    #end
    jump back_wyklad_mat_3_cd