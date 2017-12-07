init:
    init python:
        def detective_dragged(drags, drop):
            if not drop:
                return
            store.answer = drags[0].drag_name
            #store.answer = drop.drag_name
            return True

    image bg desk = Image("desk.jpg")

    screen question1:
        draggroup:
            drag:
                drag_name "question"
                child "mini2_tpi/question1/question.png"
                draggable False
                droppable False
                dragged detective_dragged
                xpos 280 ypos 100
            drag:
                drag_name "place"
                child "mini2_tpi/place.png"
                draggable False
                droppable True
                xpos 430 ypos 400
            drag:
                drag_name "wrong1"
                child "mini2_tpi/question1/1.png"
                droppable False
                dragged detective_dragged
                xpos 1280/10 ypos 600
            drag:
                drag_name "good"
                child "mini2_tpi/question1/2.png"
                droppable False
                dragged detective_dragged
                xpos 1280*3/10 ypos 600
            drag:
                drag_name "wrong2"
                child "mini2_tpi/question1/3.png"
                droppable False
                dragged detective_dragged
                xpos 1280*5/10 ypos 600
            drag:
                drag_name "wrong3"
                child "mini2_tpi/question1/4.png"
                droppable False
                dragged detective_dragged
                xpos 1280*7/10 ypos 600
    screen question2:
        draggroup:
            drag:
                drag_name "question"
                child "mini2_tpi/question1/question.png"
                draggable False
                droppable False
                dragged detective_dragged
                xpos 280 ypos 100
            drag:
                drag_name "place"
                child "mini2_tpi/place.png"
                draggable False
                droppable True
                xpos 430 ypos 400
            drag:
                drag_name "wrong1"
                child "mini2_tpi/question1/1.png"
                droppable False
                dragged detective_dragged
                xpos 1280/10 ypos 600
            drag:
                drag_name "good"
                child "mini2_tpi/question1/2.png"
                droppable False
                dragged detective_dragged
                xpos 1280*3/10 ypos 600
            drag:
                drag_name "wrong2"
                child "mini2_tpi/question1/3.png"
                droppable False
                dragged detective_dragged
                xpos 1280*5/10 ypos 600
            drag:
                drag_name "wrong3"
                child "mini2_tpi/question1/4.png"
                droppable False
                dragged detective_dragged
                xpos 1280*7/10 ypos 600

label minigame_tpi:
    scene bg desk
    call screen question1
    #pause 30
    if answer == "good":
        "{color=#00FF00}Poprawna{/color}"
    else:
        "{color=#FF0000}Nieprawidłowa{/color}"

    call screen question2

    if answer == "good":
        "{color=#00FF00}Poprawna{/color}"
    else:
        "{color=#FF0000}Nieprawidłowa{/color}"