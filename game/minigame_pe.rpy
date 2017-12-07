init:
    init python:
        def detective_dragged(drags, drop):
            if not drop:
                return
            store.detective = drags[0].drag_name
            store.city = drop.drag_name
            return True

    image bg desk = Image("desk.jpg")

    screen see:
        add "desk.jpg"

        draggroup:
            drag:
                drag_name "first"
                child "mini1/1.png"
                droppable False
                dragged detective_dragged
                xpos 100 ypos 100
            drag:
                drag_name "second"
                child "mini1/2.png"
                droppable False
                dragged detective_dragged
                xpos 100 ypos 200
            drag:
                drag_name "third"
                child "mini1/3.png"
                droppable False
                dragged detective_dragged
                xpos 100 ypos 300
            drag:
                drag_name "fourth"
                child "mini1/4.png"
                droppable False
                xpos 100 ypos 400
            drag:
                drag_name "fifth"
                child "mini1/5.png"
                droppable False
                xpos 100 ypos 500
            drag:
                drag_name "choice1"
                child "mini1/1_.png"
                droppable True
                xpos 900 ypos 100
            drag:
                drag_name "choice2"
                child "mini1/2_.png"
                droppable True
                xpos 900 ypos 200
        textbutton "Zatwierdz" xpos 600 ypos 600 text_color "#000000" text_hover_color "#00FF00" action Jump("check")


label minigame_pe:
    #scene bg desk
    call screen see
    pause 30
    "czas minął"
    return
    label check:
        "no nie wiem jeszcze jak to sprawdzic..."
    "patrz jak ładnie"
    return