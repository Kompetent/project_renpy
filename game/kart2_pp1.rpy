init:
    screen pp1_kart2_question1():
        vbox xalign 0.5 yalign 0.70:
            text "Co znajduje się na drugim miejscu w forzefor(;?;)"
        hbox xalign 0.5 yalign 0.75:
            textbutton "warunek początkowy" text_color "#000000" text_hover_color "#0000FF" action Jump("next_pp1_kart2_q1_wrong")
            textbutton "warunek trwania" text_color "#000000" text_hover_color "#0000FF" action Jump("next_pp1_kart2_q1_good")
            textbutton "zwiekszanie/zmniejszanie licznika" text_color "#000000" text_hover_color "#0000FF" action Jump("next_pp1_kart2_q1_wrong")
    screen pp1_kart2_question2():
        vbox xalign 0.5 yalign 0.70:
            text "Ktora funkcja przekształca tekst na liczbe całkowitą w C?"
        hbox xalign 0.5 yalign 0.75:
            textbutton "atoi" text_color "#000000" text_hover_color "#0000FF" action Jump("next_pp1_kart2_q2_good")
            textbutton "atof" text_color "#000000" text_hover_color "#0000FF" action Jump("next_pp1_kart2_q2_wrong")
            textbutton "atoc" text_color "#000000" text_hover_color "#0000FF" action Jump("next_pp1_kart2_q2_wrong")
    screen pp1_kart2_question3():
        vbox xalign 0.5 yalign 0.70:
            text "Który z podanych operatorów ma najwyższy priorytet w języku C?"
        hbox xalign 0.5 yalign 0.75:
            textbutton " ! " text_color "#000000" text_hover_color "#0000FF" action Jump("next_pp1_kart2_q3_good")
            textbutton " ?: " text_color "#000000" text_hover_color "#0000FF" action Jump("next_pp1_kart2_q3_wrong")
            textbutton " * " text_color "#000000" text_hover_color "#0000FF" action Jump("next_pp1_kart2_q3_wrong")

label pp1_kart2: #DONE
    scene black
    show text "{color=#FFF}{size=+30} Kartkówka druga z PP1 {/size}{/color}"
    pause 5
    hide text
    scene bg white
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(45.1, ui.jumps("next_pp1_kart2_q1_wrong"))
    call screen pp1_kart2_question1
    label next_pp1_kart2_q1_good:
        $ pp1_q1 = "Dobrze"
        jump next_pp1_kart2_q2
    label next_pp1_kart2_q1_wrong:
        $ pp1_q1 = "{color=#f00}Źle{/color}"

label next_pp1_kart2_q2:
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(45.1, ui.jumps("next_pp1_kart2_q2_wrong"))
    call screen pp1_kart2_question2
    label next_pp1_kart2_q2_good:
        $ pp1_q2 = "Dobrze"
        jump next_pp1_kart2_q3
    label next_pp1_kart2_q2_wrong:
        $ pp1_q2 = "{color=#f00}Źle{/color}"

label next_pp1_kart2_q3:
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(45.1, ui.jumps("next_pp1_kart2_q3_wrong"))
    call screen pp1_kart2_question3
    label next_pp1_kart2_q3_good:
        $ pp1_q3 = "Dobrze"
        jump end_kart2_pp1
    label next_pp1_kart2_q3_wrong:
        $ pp1_q3 = "{color=#f00}Źle{/color}"
label end_kart2_pp1:
    #obliczenie oceny
    python:
        ocena_kart2_pp1 = srednia_kartkowka("Dobrze", pp1_q1, pp1_q2, pp1_q3)
    #end
    jump back_wyklad_pp1_3_cd