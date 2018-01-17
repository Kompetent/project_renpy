init:
    style wpis:
        color "#FF0000"
    screen mat_question1():#DONE
        hbox xalign 0.2 yalign 0.2:
            text "Twierdzenie "
            input default "(uzupelnij)":
                style "wpis"
        vbox xalign 0.3 yalign 0.3:
            text "Jeśli f : |a,b| => R jest funkcją ciągłą, to jej obraz jest zbiorem ograniczonym"
            text "Ponadto funkcja f osiąga swoje kresy, tzn. dla pewnych licz c,d należą do <a,b> "
            text "mamy dla każdego x należącego <a,b>    f(d) <= f(x) <= f(c)"
    screen mat_question2():#DONE
        hbox xalign 0.45 yalign 0.5:
            text "Pochodna z funkcji f(x) = x^3 + 2x -1 w punkcie x = 3"
        hbox xalign 0.45 yalign 0.55:
            textbutton " 56 " text_color "#000000" text_hover_color "#0000AA" action Jump("next_mat_q2_good")
            textbutton " 55 " text_color "#000000" text_hover_color "#0000AA" action Jump("next_mat_q2_wrong")
            textbutton " 58 " text_color "#000000" text_hover_color "#0000AA" action Jump("next_mat_q2_wrong")
    screen mat_question3():#DONE
        vbox xpos 310 ypos 100:
            text "Twierdzenie Lagrange'a :\n\n\n\n" 
            text "ciagla na <a,b> \n\n\n\n"#dobre
            text "rozniczkowalna na (a,b)\n\n\n\n"#dobre
            text "monotoniczna w przedziale (a,b)"#zle
        button:
            style "checkbox_button"
            align (0.15, 0.3)
            action ToggleVariable("mat_q3_button1")
        button:
            style "checkbox_button"
            align (0.15, 0.5)
            action ToggleVariable("mat_q3_button2") 
        button:
            style "checkbox_button"
            align (0.15, 0.7)
            action ToggleVariable("mat_q3_button3")
        textbutton "Następne" xpos 0.8 ypos 0.9 text_color "#000" text_hover_color "#047" action Jump("next_mat_q4")
    screen mat_question4():#DONE
        hbox xalign 0.2 yalign 0.2:
            text "mówimy, ze funkcja ma "
            input default "(uzupelnij)":
                style "wpis"
        vbox xalign 0.3 yalign 0.3:
            text "globalne w punkcie x0 gdy f(x) <= f(x0)"
    screen mat_question5():#DONE
        hbox xalign 0.45 yalign 0.5:
            text "Calka z funkcji f(x) = cos x  + x^3"
        hbox xalign 0.45 yalign 0.55:#druga dobra
            textbutton " - sin x + 2 x^2 " text_color "#000000" text_hover_color "#0000AA" action Jump("next_mat_q5_wrong")
            textbutton " sin x + (1/4)*x^4 " text_color "#000000" text_hover_color "#0000AA" action Jump("next_mat_q5_good")
            textbutton " cos x + (1/3)x^3 " text_color "#000000" text_hover_color "#0000AA" action Jump("next_mat_q5_wrong")
    #an = (-0.5)^n, do czego zbiezny???
    screen mat_question6():
        hbox xalign 0.45 yalign 0.5:
            text "Ciąg an = (-1)^n, do czego zbiezny???"
        hbox xalign 0.45 yalign 0.55:
            textbutton " 0 " text_color "#000000" text_hover_color "#0000AA" action Jump("next_mat_q6_wrong")
            textbutton " 1 " text_color "#000000" text_hover_color "#0000AA" action Jump("next_mat_q6_wrong")
            textbutton "Nie jest zbiezny" text_color "#000000" text_hover_color "#0000AA" action Jump("next_mat_q6_good")
    screen analiza_conclusion():
        vbox xalign 0.2 yalign 0.2:
            text "Pytanie 1: [analiza_q1]"
            text "Pytanie 2: [analiza_q2]"
            text "Pytanie 3: [analiza_q3]"
            text "Pytanie 4: [analiza_q4]" 
            text "Pytanie 5: [analiza_q5]" 
            text "Pytanie 6: [analiza_q6]"
        textbutton "Zakończ" xpos 0.8 ypos 0.9 text_color "#000" text_hover_color "#047" action Jump("analiza_run")
    default mat_q3_button1 = False #True
    default mat_q3_button2 = False #True
    default mat_q3_button3 = False #False
    
    python:
        def analiza_correct_answer(odp, *args):
            zmienna = "Zła"
            if odp is None:
                return zmienna
            for arg in args:
                if(odp.upper() == arg.upper()):
                    zmienna = "Dobra"
                    break
            return zmienna

label minigame_mat:
    scene bg white
    show text "{color=#000000}Egzamin z Analizy Matematycznej{/color}"
    pause 2
    hide text

    scene bg white
    #Twierdzenie Bolzana-Weierstrassa albo Weierstrassa
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(45.1, ui.jumps("next_mat_q2"))
    call screen mat_question1
label next_mat_q2:
    $ analiza_q1 = analiza_correct_answer(_return, "Bolzana-Weierstrassa",  "Weierstrassa")
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(45.1, ui.jumps("next_mat_q2_wrong"))
    call screen mat_question2
label next_mat_q2_wrong:
    $ analiza_q2 = "Zla"
    jump next_mat_q3
label next_mat_q2_good:
    $ analiza_q2 = "Dobra"
label next_mat_q3:
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(45.1, ui.jumps("next_mat_q4"))
    call screen mat_question3
label next_mat_q4:
    python:
        analiza_q3_list = varargs([True, True, False], mat_q3_button1, mat_q3_button2, mat_q3_button3)
        analiza_q3 = pytanie(analiza_q3_list[0], analiza_q3_list[1], analiza_q3_list[2])
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(45.1, ui.jumps("next_mat_q2_wrong"))
    call screen mat_question4
label next_mat_q5:
    $ analiza_q4 = analiza_correct_answer(_return, "maksimum",  "max")
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(45.1, ui.jumps("next_mat_q5_wrong"))
    call screen mat_question5
label next_mat_q5_wrong:
    $ analiza_q5 = "Zla"
    jump next_mat_q6
label next_mat_q5_good:
    $ analiza_q5 = "Dobra"
label next_mat_q6:
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(45.1, ui.jumps("next_mat_q6_wrong"))
    call screen mat_question6
label next_mat_q6_wrong:
    $ analiza_q6 = "Zla"
    jump next_mat_end
label next_mat_q6_good:
    $ analiza_q6 = "Dobra"
label next_mat_end:
    call screen analiza_conclusion
label analiza_run:
    python:
        ocena_egz_mat = srednia_egzamin("Dobra", analiza_q1, analiza_q2, analiza_q3, analiza_q4, analiza_q5, analiza_q6)
    jump exams_back4
    return