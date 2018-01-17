init:
    screen pp1_kart1_question1():
        vbox xalign 0.5 yalign 0.70:
            text "W jakim języku będziesz uczyć się programować?"
        hbox xalign 0.5 yalign 0.75:
            textbutton "Pascal" text_color "#000000" text_hover_color "#0000FF" action Jump("next_pp1_kart1_q1_wrong")
            textbutton "Delphi" text_color "#000000" text_hover_color "#0000FF" action Jump("next_pp1_kart1_q1_wrong")
            textbutton " C " text_color "#000000" text_hover_color "#0000FF" action Jump("next_pp1_kart1_q1_good")
    screen pp1_kart1_question2():
        vbox xalign 0.5 yalign 0.70:
            text "Ktora funkcja wypisuje tekst na consoli w C?"
        hbox xalign 0.5 yalign 0.75:
            textbutton "printf" text_color "#000000" text_hover_color "#0000FF" action Jump("next_pp1_kart1_q2_good")
            textbutton "cout" text_color "#000000" text_hover_color "#0000FF" action Jump("next_pp1_kart1_q2_wrong")
            textbutton "println" text_color "#000000" text_hover_color "#0000FF" action Jump("next_pp1_kart1_q2_wrong")
    screen pp1_kart1_question3():
        vbox xalign 0.5 yalign 0.70:
            text "Znak porównania w języku C"
        hbox xalign 0.5 yalign 0.75:
            textbutton " = " text_color "#000000" text_hover_color "#0000FF" action Jump("next_pp1_kart1_q3_wrong")
            textbutton " ?= " text_color "#000000" text_hover_color "#0000FF" action Jump("next_pp1_kart1_q3_wrong")
            textbutton " == " text_color "#000000" text_hover_color "#0000FF" action Jump("next_pp1_kart1_q3_good")

    python:
        def srednia_kartkowka(t,*args):
            suma = 0
            for a in args:
                if a == t:
                    suma += 1
            print(args.__len__())
            procent = round(float(suma) / args.__len__() *100, 2)
            if procent < 30:
                return 2
            elif procent <60:
                return 3
            elif procent < 90:
                return 4
            else:
                return 5
label pp1_kart1: #DONE
    scene bg white
    show text "{color=#000000}Kartkówka pierwsza z PP1{/color}"
    pause 2
    hide text

    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(30.1, ui.jumps("next_pp1_kart1_q1_wrong"))
    call screen pp1_kart1_question1
    label next_pp1_kart1_q1_good:
        $ pp1_q1 = "Dobrze"
        jump next_pp1_kart1_q2
    label next_pp1_kart1_q1_wrong:
        $ pp1_q1 = "{color=#f00}Źle{/color}"

label next_pp1_kart1_q2:
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(30.1, ui.jumps("next_pp1_kart1_q2_wrong"))
    call screen pp1_kart1_question2
    label next_pp1_kart1_q2_good:
        $ pp1_q2 = "Dobrze"
        jump next_pp1_kart1_q3
    label next_pp1_kart1_q2_wrong:
        $ pp1_q2 = "{color=#f00}Źle{/color}"

label next_pp1_kart1_q3:
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(30.1, ui.jumps("next_pp1_kart1_q3_wrong"))
    call screen pp1_kart1_question3
    label next_pp1_kart1_q3_good:
        $ pp1_q3 = "Dobrze"
        jump end_kart1_pp1
    label next_pp1_kart1_q3_wrong:
        $ pp1_q3 = "{color=#f00}Źle{/color}"
label end_kart1_pp1:
    #obliczenie oceny
    python:
        ocena_kart1_pp1 = srednia_kartkowka("Dobrze", pp1_q1, pp1_q2, pp1_q3)
    #end
    jump back_wyklad_pp1_2_cd