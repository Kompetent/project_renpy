init:
    screen mat_kart1_question1():
        vbox xalign 0.5 yalign 0.70:
            text "Pochodna funcji f(x) = cos x"
        hbox xalign 0.5 yalign 0.75:
            textbutton "sin x" text_color "#000000" text_hover_color "#0000FF" action Jump("next_mat_kart1_q1_wrong")
            textbutton "- sin x" text_color "#000000" text_hover_color "#0000FF" action Jump("next_mat_kart1_q1_good")
            textbutton "- cos x " text_color "#000000" text_hover_color "#0000FF" action Jump("next_mat_kart1_q1_wrong")
    screen mat_kart1_question2():
        vbox xalign 0.5 yalign 0.70:
            text "Czy f(x) = 1/x jest ciągła?"
        hbox xalign 0.5 yalign 0.75:
            textbutton "Tak" text_color "#000000" text_hover_color "#0000FF" action Jump("next_mat_kart1_q2_wrong")
            textbutton "Nie" text_color "#000000" text_hover_color "#0000FF" action Jump("next_mat_kart1_q2_wrong")
            textbutton "Jest ciągła w dziedzinie" text_color "#000000" text_hover_color "#0000FF" action Jump("next_mat_kart1_q2_good")
    screen mat_kart1_question3():
        vbox xalign 0.5 yalign 0.70:
            text "Czy f(x) = tg x jest ciągła?"
        hbox xalign 0.5 yalign 0.75:
            textbutton "Tak" text_color "#000000" text_hover_color "#0000FF" action Jump("next_mat_kart1_q3_wrong")
            textbutton "Nie"  text_color "#000000" text_hover_color "#0000FF" action Jump("next_mat_kart1_q3_wrong")
            textbutton "Jest ciągła w dziedzinie" text_color "#000000" text_hover_color "#0000FF" action Jump("next_mat_kart1_q3_good")

label mat_kart1: 
    scene bg white
    show text "{color=#000000}Kartkówka pierwsza z Analizy Matematycznej{/color}"
    pause 2
    hide text

    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(45.1, ui.jumps("next_mat_kart1_q1_wrong"))
    call screen mat_kart1_question1
    label next_mat_kart1_q1_good:
        $ mat_q1 = "Dobrze"
        jump next_mat_kart1_q2
    label next_mat_kart1_q1_wrong:
        $ mat_q1 = "{color=#f00}Źle{/color}"

label next_mat_kart1_q2:
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(45.1, ui.jumps("next_mat_kart1_q2_wrong"))
    call screen mat_kart1_question2
    label next_mat_kart1_q2_good:
        $ mat_q2 = "Dobrze"
        jump next_mat_kart1_q3
    label next_mat_kart1_q2_wrong:
        $ mat_q2 = "{color=#f00}Źle{/color}"

label next_mat_kart1_q3:
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(45.1, ui.jumps("next_mat_kart1_q3_wrong"))
    call screen mat_kart1_question3
    label next_mat_kart1_q3_good:
        $ mat_q3 = "Dobrze"
        jump end_kart1_mat
    label next_mat_kart1_q3_wrong:
        $ mat_q3 = "{color=#f00}Źle{/color}"
label end_kart1_mat:
    #obliczenie oceny
    python:
        ocena_kart1_mat = srednia_kartkowka("Dobrze", mat_q1, mat_q2, mat_q3)
    #end
    jump back_wyklad_mat_2_cd