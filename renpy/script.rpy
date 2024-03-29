# Определение персонажей игры.
define e = Character('Китамура Эцуко', color="#c8ffc8", image='etsuko')
define n = Character('Мицуги Нацуки', color="#c8ffc8", image='natsuki')
define a = Character('Харута Анна', color="#c8ffc8", image='anna')


init python:         
    xmax = config.screen_width
    ymax = config.screen_height    
    
#init -2 python:
    #declares a new style called "infoscreen"
    style.infoscreen = Style(style.default)
    style.infoscreen_text.size = 24
    style.infoscreen_window.background = "infoscreenBG.png"  #<-- This puts a custom background in the area that displays the text and picture    
    style.infoscreen_frame.background = Frame("box.png", 10, 10) #<--same as above, but in the area that displays the buttons
    style.infoscreen_button.idle_background = Frame("box2.png", 10, 10)
    style.infoscreen_button.hover_background = Frame("box3.png", 10, 10)
    style.infoscreen_button_text.idle_color = "FF731C"
    style.infoscreen_button_text.hover_color = "FF731C"
    style.infoscreen_button_text.selected_color = "#F00"
    style.infoscreen_button.top_padding = 5
    style.infoscreen_button.bottom_padding = 5
    style.infoscreen_bar.left_bar = "bar_full-checks.png"
    style.infoscreen_bar.right_bar = "bar_empty-checks.png"
    style.infoscreen_bar.xmaximum = 209
    style.infoscreen_bar.ymaximum = 34
    style.infoscreen_bar.right_gutter = 0
    style.infoscreen_bar.left_gutter = 0
    style.infoscreen_bar.thumb = None


# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene bg lobby
    show etsuko smile at left
    show anna serious at right
    "О, коробки с едой!"
    e "Откроем пиццу?"
    a "Давай лучше онигири!"
    $ etsuko.likes=("Пицца")                
    $ anna.likes=("Онигири")                        
    $ anna.dislikes=("Пицца")                                    
   
    "А ты как думаешь?"
    menu:
        "Пицца":
#            show etsuko 3 at left
#            show anna 2 at right
            $ anna.pic = "/char/anna serious.png"
            $ etsuko.pic = "/char/etsuko smile.png"
            $ natsuki.pic = "/char/natsuki smile.png"            
            $ etsuko.currentThoughts=("О даа, пицца!")
            $ etsuko.affection += 5
            $ anna.currentThoughts=("Да ладно...")
            $ anna.affection -= 5
            e "Отлично!"
            a "Опять эти чёрствые корочки и высохшие шампиньоны..."
        "Онигири":
#            show etsuko 2 at left
#            show natsuki 6 at right
            # $ etsuko.pic = "etsuko 2.png"
            $ anna.currentThoughts=("Я так люблю онигири!")
            $ anna.affection += 10
            $ etsuko.currentThoughts=("Ну вооот...")
            $ etsuko.affection -= 10
            a "Скорее, за стол!"
            e "Я бы лучше съела пиццу... Ну ладно, онигири тоже вкусные, пусть пицца останется на завтра."
    "М-м, вкусно!"        
    return
