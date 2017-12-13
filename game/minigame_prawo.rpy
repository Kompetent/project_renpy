init:
    screen input_screen():
        window:
            has vbox
            text "Enter your name."
            input default ""
    screen keymap_screen():
        key "game_menu" action ShowMenu('save')
        key "p" action ShowMenu('preferences')
        key "s" action Screenshot()
    screen button_overlay():
        mousearea:
            area (0, 0, 1.0, 100)
            hovered Show("buttons", transition=dissolve)
            unhovered Hide("buttons", transition=dissolve)
    screen checkboxes():
        button:
            action ToggleDict(char.autocontrol, "Rest")
            xysize (200, 32)
            text "Auto Rest" align (0.0, 0.5)
            if char.autocontrol['Rest']:
                add (im.Scale('content/gfx/interface/icons/checkbox_checked.png', 25, 25)) align (1.0, 0.5)
            elif not char.autocontrol['Rest']:
                add (im.Scale('content/gfx/interface/icons/checkbox_unchecked.png', 25, 25)) align (1.0, 0.5)
    screen buttons():
        hbox:
            textbutton "Save" action ShowMenu("save")
            textbutton "Prefs" action ShowMenu("preferences")
            textbutton "Skip" action Skip()
            textbutton "Auto" action Preference("auto-forward", "toggle")
label minigame_prawo:
    call screen input_screen
    "Przesłanki ochrony dóbr osobistych:\n - istnienie dobra osobistego prawnie chronionego\n - fakt jego naruszenia 
    przez cudze zachowanie\n - bezprawność zachowania naruszającego"
    "Szkodę dzielimy na:\n - majątkową – strata oraz utracenie korzyści (odszkodowanie)\n - niemajątkową – tzw. krzywda, 
    ból fizyczny, psychiczny, negatywne moralne psychiczne doznania"
    "Twórca – może być tylko człowiek, (...), której nazwisko w tym charakterze 
    uwidoczniono na egzemplarzach utworu lub której nazwisko podano do publicznej wiadomości w jakikolwiek inny sposób, 
    (...). Jeśli twórca nie ujawnia autorstwa, w wykonywaniu prawa autorskiego zastępuje 
    go producent lub wydawca"