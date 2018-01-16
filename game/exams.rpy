label exams:
    scene bg white
    play music "music/bensound-dance.ogg"
    show narrator at left
    ob "Skończyłaś się już uczyć moja droga"
    ob "Czas na sesję"
    ob "Przed Tobą zaliczenia z 5 przedmiotów"
    ob "Baw się dobrze"
    jump minigame_pp1 #done
label exams_back1:
    jump minigame_tpi #done
label exams_back2:
    jump minigame_prawo #done
label exams_back3:
    jump minigame_mat #done
label exams_back4:
    jump minigame_pe #done
label exams_back5:
    stop music
    jump chapter5