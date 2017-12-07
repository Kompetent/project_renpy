init:
    screen pp1_question1:
        add "mini1_pp1/question1/question.jpg"
        text "Czy przedstawiony fragment kodu skompiluje się?" xpos 400 ypos 560
        textbutton "Tak" xpos 280 ypos 600 text_color "#000000" text_hover_color "#0000AA" action Jump("next_pp1_q2")
        textbutton "Nie" xpos 1000 ypos 600 text_color "#000000" text_hover_color "#0000AA" action Jump("next_pp1_q2")
    screen pp1_question2:
        add "mini1_pp1/question2/question.png"
        text "Jakie liczby wypisze ten kod?" xpos 500 ypos 560
        textbutton "01234" xpos 280 ypos 600 text_color "#000000" text_hover_color "#0000AA" action Jump("next_pp1_q3")
        textbutton "0134" xpos 600 ypos 600 text_color "#000000" text_hover_color "#0000AA" action Jump("next_pp1_q3")
        textbutton "01346" xpos 1000 ypos 600 text_color "#000000" text_hover_color "#0000AA" action Jump("next_pp1_q3")
    screen pp1_question3:
        add "mini1_pp1/question3/question.png"
        text "Jak nazywa się metoda programowania wykorzystana do stworzenia fibo i silnia?" xpos 200 ypos 560
        textbutton "Rekurencja" xpos 280 ypos 600 text_color "#000000" text_hover_color "#0000AA" action Jump("next_pp1_q4")
        textbutton "Iteracja" xpos 1000 ypos 600 text_color "#000000" text_hover_color "#0000AA" action Jump("next_pp1_q4")
    screen pp1_question4:
        add "mini1_pp1/question4/question.png"
        text "Końcowa instrukcja printf wydrukuje" xpos 400 ypos 560
        textbutton "A = 12; B = 34;" xpos 280 ypos 600 text_color "#000000" text_hover_color "#0000AA" action Jump("next_pp1_q5")
        textbutton "Nie skompiluje sie" xpos 600 ypos 600 text_color "#000000" text_hover_color "#0000AA" action Jump("next_pp1_q5")
        textbutton "A = 12; B = -1;" xpos 1000 ypos 600 text_color "#000000" text_hover_color "#0000AA" action Jump("next_pp1_q5")
    screen pp1_question5:
        add "mini1_pp1/question5/question.png"
        text "Jaki będzie wynik działania programu?" xpos 400 ypos 560
        textbutton "cd" xpos 280 ypos 600 text_color "#000000" text_hover_color "#0000AA" action Jump("next_pp1_q6")
        textbutton "c" xpos 600 ypos 600 text_color "#000000" text_hover_color "#0000AA" action Jump("next_pp1_q6")
        textbutton "cde" xpos 1000 ypos 600 text_color "#000000" text_hover_color "#0000AA" action Jump("next_pp1_q6")
    screen pp1_question6:
        add "mini1_pp1/question6/question.png"
        text "Jaka będzie ostatnia wartość wypisane w konsoli?" xpos 400 ypos 560
        textbutton "50" xpos 280 ypos 600 text_color "#000000" text_hover_color "#0000AA" action Jump("next_pp1_q7")
        textbutton "49" xpos 1000 ypos 600 text_color "#000000" text_hover_color "#0000AA" action Jump("next_pp1_q7")
    screen pp1_question7:
        add "mini1_pp1/question7/question.png"
        text "Ile razy wykona się pętla while?" xpos 400 ypos 560
        textbutton "100" xpos 280 ypos 600 text_color "#000000" text_hover_color "#0000AA" action Jump("next_pp1_q8")
        textbutton "10" xpos 500 ypos 600 text_color "#000000" text_hover_color "#0000AA" action Jump("next_pp1_q8")
        textbutton "11" xpos 780 ypos 600 text_color "#000000" text_hover_color "#0000AA" action Jump("next_pp1_q8")
        textbutton "Nieskończenie wiele" xpos 1000 ypos 600 text_color "#000000" text_hover_color "#0000AA" action Jump("next_pp1_q8")
    screen pp1_question8:
        add "mini1_pp1/question8/question.png"
        text "Jaka będzie wartośc zmiennej n?" xpos 400 ypos 560
        textbutton "13" xpos 280 ypos 600 text_color "#000000" text_hover_color "#0000AA" action Jump("next_pp1_end")
        textbutton "14" xpos 1000 ypos 600 text_color "#000000" text_hover_color "#0000AA" action Jump("next_pp1_end")


label minigame_pp1:
    call screen pp1_question1
label next_pp1_q2:
    call screen pp1_question2
label next_pp1_q3:
    call screen pp1_question3
label next_pp1_q4:
    call screen pp1_question4
label next_pp1_q5:
    call screen pp1_question5
label next_pp1_q6:
    call screen pp1_question6
label next_pp1_q7:
    call screen pp1_question7
label next_pp1_q8:
    call screen pp1_question8
label next_pp1_end:
    "Po wszystkim"
    return