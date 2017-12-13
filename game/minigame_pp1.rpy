init:
    python:
        def countdown(st, at, length=0.0):
            remaining = length - st
            if remaining > 5.0:
                return Text("%.1f" % remaining, color="#f2f", size=72), .1
            elif remaining > 0.0:
                return Text("%.1f" % remaining, color="#f00", size=72), .1
            else:
                return anim.Blink(Text("0.0", color="#f00", size=72)), None
    
    image countdown = DynamicDisplayable(countdown, length=10.0)
    
    image bg pp1_q1 = "mini1_pp1/question1/question.jpg"
    image bg pp1_q2 = "mini1_pp1/question2/question.png"
    image bg pp1_q3 = "mini1_pp1/question3/question.png"
    image bg pp1_q4 = "mini1_pp1/question4/question.png"
    image bg pp1_q5 = "mini1_pp1/question5/question.png"
    image bg pp1_q6 = "mini1_pp1/question6/question.png"
    image bg pp1_q7 = "mini1_pp1/question7/question.png"
    image bg pp1_q8 = "mini1_pp1/question8/question.png"

    screen pp1_question1():
        vbox xalign 0.5 yalign 0.70:
            text "Czy przedstawiony fragment kodu skompiluje się?"
        hbox xalign 0.5 yalign 0.75:
            textbutton "Tak   " text_color "#000000" text_hover_color "#0000FF" action Jump("next_pp1_q1_good")
            textbutton "   Nie" text_color "#000000" text_hover_color "#0000FF" action Jump("next_pp1_q1_wrong")
    screen pp1_question2():
        vbox xalign 0.5 yalign 0.70:
            text "Jakie liczby wypisze ten kod?"
        hbox xalign 0.5 yalign 0.75:
            textbutton "01234 " text_color "#000000" text_hover_color "#0000FF" action Jump("next_pp1_q2_wrong")
            textbutton " 0134 " text_color "#000000" text_hover_color "#0000ff" action Jump("next_pp1_q2_good")
            textbutton " 01346" text_color "#000000" text_hover_color "#0000FF" action Jump("next_pp1_q2_wrong")
    screen pp1_question3():
        vbox xalign 0.5 yalign 0.70:
            text "Jak nazywa się metoda programowania wykorzystana do stworzenia fibo i silnia?"
        hbox xalign 0.5 yalign 0.75:
            textbutton "Rekurencja  " text_color "#000000" text_hover_color "#0000FF" action Jump("next_pp1_q3_good")
            textbutton "  Iteracja" text_color "#000000" text_hover_color "#0000FF" action Jump("next_pp1_q3_wrong")
    screen pp1_question4():
        vbox xalign 0.5 yalign 0.70:
            text "Końcowa instrukcja printf wydrukuje"
        hbox xalign 0.5 yalign 0.75:
            textbutton "A = 12; B = 34;" text_color "#000000" text_hover_color "#0000FF" action Jump("next_pp1_q4_wrong")
            textbutton "Nie skompiluje sie" text_color "#000000" text_hover_color "#0000FF" action Jump("next_pp1_q4_wrong")
            textbutton "A = 12; B = -1;" text_color "#000000" text_hover_color "#0000FF" action Jump("next_pp1_q4_good")
    screen pp1_question5():
        vbox xalign 0.5 yalign 0.70:
            text "Jaki będzie wynik działania programu?"
        hbox xalign 0.5 yalign 0.75:
            textbutton "cd" text_color "#000000" text_hover_color "#0000FF" action Jump("next_pp1_q5_good")
            textbutton "c" text_color "#000000" text_hover_color "#0000FF" action Jump("next_pp1_q5_wrong")
            textbutton "cde" text_color "#000000" text_hover_color "#0000FF" action Jump("next_pp1_q5_good")
    screen pp1_question6():
        vbox xalign 0.5 yalign 0.70:
            text "Jaka będzie ostatnia wartość wypisane w konsoli?"
        hbox xalign 0.5 yalign 0.75:
            textbutton "50  " text_color "#000000" text_hover_color "#0000FF" action Jump("next_pp1_q6_wrong")
            textbutton "  49" text_color "#000000" text_hover_color "#0000FF" action Jump("next_pp1_q6_good")
    screen pp1_question7():
        vbox xalign 0.5 yalign 0.70:
            text "Ile razy wykona się pętla while?"
        hbox xalign 0.5 yalign 0.75:
            textbutton "100 " text_color "#000000" text_hover_color "#0000AA" action Jump("next_pp1_q7_good")
            textbutton " 10 " text_color "#000000" text_hover_color "#0000AA" action Jump("next_pp1_q7_wrong")
            textbutton " 11 " text_color "#000000" text_hover_color "#0000AA" action Jump("next_pp1_q7_wrong")
            textbutton "Nieskończenie wiele" text_color "#000000" text_hover_color "#0000AA" action Jump("next_pp1_q7_wrong")
    screen pp1_question8():
        vbox xalign 0.5 yalign 0.70:
            text "Jaka będzie wartośc zmiennej n?"
        hbox xalign 0.5 yalign 0.75:
            textbutton "15  " text_color "#000000" text_hover_color "#0000FF" action Jump("next_pp1_q8_wrong")
            textbutton "  14" text_color "#000000" text_hover_color "#0000FF" action Jump("next_pp1_q8_good")
    screen pp1_conclusion():
        vbox xalign 0.2 yalign 0.2:
            text "Podsumowanie testu z pp1"
            text "Odpowiedź na 1: [pp1_q1]"
            text "Odpowiedź na 2: [pp1_q2]"
            text "Odpowiedź na 3: [pp1_q3]"
            text "Odpowiedź na 4: [pp1_q4]"
            text "Odpowiedź na 5: [pp1_q5]"
            text "Odpowiedź na 6: [pp1_q6]"
            text "Odpowiedź na 7: [pp1_q7]"
            text "Odpowiedź na 8: [pp1_q8]"
            textbutton "Wyjście" action Return()
label minigame_pp1:
    scene bg pp1_q1
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(10.1, ui.jumps("next_pp1_q1_wrong"))
    call screen pp1_question1
    label next_pp1_q1_good:
        $ pp1_q1 = "{color=#0f0}Dobrze{/color}"
        jump next_pp1_q2
    label next_pp1_q1_wrong:
        $ pp1_q1 = "{color=#f00}Źle{/color}"
label next_pp1_q2:
    scene bg pp1_q2
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(10.1, ui.jumps("next_pp1_q2_wrong"))
    call screen pp1_question2
    label next_pp1_q2_good:
        $ pp1_q2 = "{color=#0f0}Dobrze{/color}"
        jump next_pp1_q3
    label next_pp1_q2_wrong:
        $ pp1_q2 = "{color=#f00}Źle{/color}"
label next_pp1_q3:
    scene bg pp1_q3
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(10.1, ui.jumps("next_pp1_q3_wrong"))
    call screen pp1_question3
    label next_pp1_q3_good:
        $ pp1_q3 = "{color=#0f0}Dobrze{/color}"
        jump next_pp1_q4
    label next_pp1_q3_wrong:
        $ pp1_q3 = "{color=#f00}Źle{/color}"
label next_pp1_q4:
    scene bg pp1_q4
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(10.1, ui.jumps("next_pp1_q4_wrong"))
    call screen pp1_question4
    label next_pp1_q4_good:
        $ pp1_q4 = "{color=#0f0}Dobrze{/color}"
        jump next_pp1_q5
    label next_pp1_q4_wrong:
        $ pp1_q4 = "{color=#f00}Źle{/color}"
label next_pp1_q5:
    scene bg pp1_q5
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(10.1, ui.jumps("next_pp1_q5_wrong"))
    call screen pp1_question5
    label next_pp1_q5_good:
        $ pp1_q5 = "{color=#0f0}Dobrze{/color}"
        jump next_pp1_q6
    label next_pp1_q5_wrong:
        $ pp1_q5 = "{color=#f00}Źle{/color}"
label next_pp1_q6:
    scene bg pp1_q6
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(10.1, ui.jumps("next_pp1_q6_wrong"))
    call screen pp1_question6
    label next_pp1_q6_good:
        $ pp1_q6 = "{color=#0f0}Dobrze{/color}"
        jump next_pp1_q7
    label next_pp1_q6_wrong:
        $ pp1_q6 = "{color=#f00}Źle{/color}"
label next_pp1_q7:
    scene bg pp1_q7
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(10.1, ui.jumps("next_pp1_q7_wrong"))
    call screen pp1_question7
    label next_pp1_q7_good:
        $ pp1_q7 = "{color=#0f0}Dobrze{/color}"
        jump next_pp1_q8
    label next_pp1_q7_wrong:
        $ pp1_q7 = "{color=#f00}Źle{/color}"
label next_pp1_q8:
    scene bg pp1_q8
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(10.1, ui.jumps("next_pp1_q8_wrong"))
    call screen pp1_question8
    label next_pp1_q8_good:
        $ pp1_q8 = "{color=#0f0}Dobrze{/color}"
        jump next_pp1_end
    label next_pp1_q8_wrong:
        $ pp1_q8 = "{color=#f00}Źle{/color}"
label next_pp1_end:
    scene bg white
    call screen pp1_conclusion
    #jump minigame_pe
    return