def starting():
    title_screen = (""" _______                                _______                              
     \      \   ____  __ _________  ____    \      \   ____ ___  _____ __  ______
     /   |   \_/ __ \|  |  \_  __ \/  _ \   /   |   \_/ __ \\  \/  /  |  \/  ___/
    /    |    \  ___/|  |  /|  | \(  <_> ) /    |    \  ___/ >    <|  |  /\___ \ 
    \____|__  /\___  >____/ |__|   \____/  \____|__  /\___  >__/\_ \____//____  >
            \/     \/                              \/     \/      \/          \/                       
    """)
    
    options = ["[1] Start Game",
    "[2] Help",
    "[x] Exit"]
      
    print(title_screen)
    for line in options: 
        print(line)