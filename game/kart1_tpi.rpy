init:
    screen tpi_kart1_question1():
        vbox xalign 0.5 yalign 0.70:
            text "Które równanie jest prawdziwe?"
        hbox xalign 0.5 yalign 0.75:
            textbutton " O(n^2) > 2n^2 +3n" text_color "#000000" text_hover_color "#0000FF" action Jump("next_tpi_kart1_q1_good")
            textbutton " 0.5 log n < o(log n)" text_color "#000000" text_hover_color "#0000FF" action Jump("next_tpi_kart1_q1_wrong")
            textbutton " O(n) < 3n" text_color "#000000" text_hover_color "#0000FF" action Jump("next_tpi_kart1_q1_wrong")
    screen tpi_kart1_question2():
        vbox xalign 0.5 yalign 0.70:
            text "Jaką klasę złożoności ma algorytm binarny potęgowania?"
        hbox xalign 0.5 yalign 0.75:
            textbutton "O(log n)" text_color "#000000" text_hover_color "#0000FF" action Jump("next_tpi_kart1_q2_good")
            textbutton "O(pierw(n))" text_color "#000000" text_hover_color "#0000FF" action Jump("next_tpi_kart1_q2_wrong")
            textbutton "O(0.5n)" text_color "#000000" text_hover_color "#0000FF" action Jump("next_tpi_kart1_q2_wrong")
    screen tpi_kart1_question3():
        vbox xalign 0.5 yalign 0.70:
            text "Typowa złożoności algorytmu bąbelkowego?"
        hbox xalign 0.5 yalign 0.75:
            textbutton " O(n^2) " text_color "#000000" text_hover_color "#0000FF" action Jump("next_tpi_kart1_q3_good")
            textbutton " O(n) " text_color "#000000" text_hover_color "#0000FF" action Jump("next_tpi_kart1_q3_wrong")
            textbutton " O(2^n) " text_color "#000000" text_hover_color "#0000FF" action Jump("next_tpi_kart1_q3_wrong")

label tpi_kart1: #DONE
    scene bg white
    show text "{color=#000000}Kartkówka z tpi{/color}"
    pause 2
    hide text

    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(30.1, ui.jumps("next_tpi_kart1_q1_wrong"))
    call screen tpi_kart1_question1
    label next_tpi_kart1_q1_good:
        $ tpi_q1 = "Dobrze"
        jump next_tpi_kart1_q2
    label next_tpi_kart1_q1_wrong:
        $ tpi_q1 = "{color=#f00}Źle{/color}"

label next_tpi_kart1_q2:
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(30.1, ui.jumps("next_tpi_kart1_q2_wrong"))
    call screen tpi_kart1_question2
    label next_tpi_kart1_q2_good:
        $ tpi_q2 = "Dobrze"
        jump next_tpi_kart1_q3
    label next_tpi_kart1_q2_wrong:
        $ tpi_q2 = "{color=#f00}Źle{/color}"

label next_tpi_kart1_q3:
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(30.1, ui.jumps("next_tpi_kart1_q3_wrong"))
    call screen tpi_kart1_question3
    label next_tpi_kart1_q3_good:
        $ tpi_q3 = "Dobrze"
        jump end_kart1_tpi
    label next_tpi_kart1_q3_wrong:
        $ tpi_q3 = "{color=#f00}Źle{/color}"
label end_kart1_tpi:
    #obliczenie oceny
    python:
        ocena_kart1_tpi = srednia_kartkowka("Dobrze", tpi_q1, tpi_q2, tpi_q3)
    #end
    jump back_wyklad_tpi_3_cd