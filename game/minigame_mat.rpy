init:
    style wpis:
        color "#FF0000"
    screen mat_question1():
        hbox xalign 0.2 yalign 0.2:
            text "Twierdzenie "
            input default "(uzupelnij)":
                style "wpis"
        vbox xalign 0.3 yalign 0.3:
            text "Jeśli f : |a,b| => R jest funkcją ciągłą, to jej obraz jest zbiorem ograniczonym"
            text "Ponadto funkcja f osiąga swoje kresy, tzn. dla pewnych licz c,d należą do <a,b> "
            text "mamy dla każdego x należącego <a,b>    f(d) <= f(x) <= f(c)"
    #Pochodna z funkcji f(x) = x^3
    screen mat_question2():
        hbox xalign 0.2 yalign 0.2:
            text "Pochodna z funkcji f(x) = x^3 + 2x -1 "
            textbutton "100 " text_color "#000000" text_hover_color "#0000AA" action Jump("next_pp1_q7_good")
    #Twierdzenie Lagrange'a 
    #2 warunki: (1) ciagla na <a,b> (2) rozniczkowalna na (a,b)
    screen mat_question3():
        hbox xalign 0.2 yalign 0.2:
            text "Twierdzenie "
    screen mat_question4():
        hbox xalign 0.2 yalign 0.2:
            text "Twierdzenie "
    screen mat_question5():
        hbox xalign 0.2 yalign 0.2:
            text "Twierdzenie "
    screen mat_question6():
        hbox xalign 0.2 yalign 0.2:
            text "Twierdzenie "

    python:
        def analiza_correct_answer(odp, *args):
            zmienna = "Zła"
            for arg in args:
                if(odp.upper() == arg.upper()):
                    zmienna = "Dobra"
                    break
            return zmienna

label minigame_mat:
    scene bg white
    #Twierdzenie Bolzana-Weierstrassa albo Weierstrassa
    call screen mat_question1
    $ analiza_q1 = analiza_correct_answer(_return, "Bolzana-Weierstrassa",  "Weierstrassa")
    "[analiza_q1]"
    return