init:

    image bg pe_q1 = "mini3_pe/question1.png"

    screen pe_question1:
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


label minigame_pe:
    $ answer = "wrong"
    scene bg pe_q1
    show countdown at Position(xalign=.9, yalign=.1)
    $ ui.timer(10.1, ui.jumps("next_pe_q1"))
    call screen pe_question1
label next_pe_q1:
    scene bg white
    if answer == "good":
        $ answer_q1 = "Dobra"
        "{color=#00FF00}[answer_q1]{/color}"
    else:
        $ answer_q1 = "Zła"
        "{color=#FF0000}[answer_q1]{/color}"
