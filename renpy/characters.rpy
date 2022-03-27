init python:
    # declares a class called 'char'
    default_var = '???'
    class char:
        #--------------------------VV--------if you want to change how much affection they start with
        def __init__(self, affection=50, name=default_var, age=default_var, birthday=default_var, profession=default_var, got_here=default_var, likes=default_var, dislikes=default_var, description=default_var, currentThoughts=default_var, super_lvl=default_var, pic='none', super_known=False ): #<-- this line sets all the defaults; the only one you'll probably use
            self.affection = affection
            self.name = name
            self.age = age
            self.profession = profession
            self.birthday = birthday
            self.likes = likes
            self.dislikes = dislikes
            self.description = description
            self.currentThoughts = currentThoughts
            self.got_here = got_here
            self.super_lvl = super_lvl            
            self.super_known = super_known                        
            self.pic = pic
            #You can add more areas if you want, just put self. and whatever it is you need
            
        def add_affection(self, amount):
            self.affection += amount
            if self.affection > affectionMax:
                self.affection = affectionMax

        def add_super_lvl(self, amount):
            self.super_lvl += amount
            if self.super_lvl > affectionMax:
                self.super_lvl = affectionMax

                
        def normalize(self):
            if self.affection > affectionMax:
                self.affection = affectionMax
            if self.affection < 0: 
                self.affection = 0
                
init:
    #declare all the characters here, use the following format. Add as many as you want or need.
    $ etsuko = char(
        name="Китамура Эцуко",  
        profession="Артистка-фокусница",
        age="22",
        got_here="Летела на самолёте на выступление, в какой-то момент отключилась и проснулась уже на базе",
        # pic="etsuko a 1.png"
        )   
    $ natsuki = char(
        name="Мицуги Нацуки",  
        profession="Старшеклассница",        
        age="18",
        got_here="Помнит, как уснула в своей комнате, очнулась на базе",        
        # pic="natsuki a 1.png"
        )   
    $ anna = char(
        name="Харута Анна",  
        profession="Скрипачка",        
        age="19",
        got_here="Ехала в такси с концерта, уснула и проснулась на базе",        
        # pic="anna a 1.png"
        )   
    
    #these are the characters shown on the screen, you can add more as you meet new people
    $ allchars = [etsuko, natsuki, anna]
        
    $ affectionMax = 100 #<-- maximum affection value is changed here
    $ superMax = 100 #<-- maximum superability value is changed here
    $ superKnownGlobal = False #<-- is it Phase 2 where superability existence is revealed
    $ show_profiles = False
    $ viewing = "Китамура Эцуко" #<-- the default character to show when the info screen is first called
    $ main = anna   
        
screen profile_screen:
     tag menu
     zorder 10
     # creates a string for proper display of each fact (+some bars) 
     for i in allchars:
            $ char = i
            if viewing == char.name: 
               $ name = "Имя: " + char.name
               $ profession = "Занятие: " + char.profession
               $ age = "Возраст: " + char.age
               $ birthday = "День рождения: " + char.birthday
               $ likes = "Что любит: " + char.likes
               $ dislikes = "Что не любит: " + char.dislikes
               $ description = char.description
               $ thoughts = "О чём думает: \n \"" + char.currentThoughts + "\""
               $ got_here = "Как здесь оказалась: \n \"" + char.got_here + "\""               
               $ pic = char.pic
               if char.super_known:
                   $ superBar = True
               else:    
                   $ superBar = False                                      
               if char == main: ##For the main character
                   $ friendshipBar = False
               else:
                   $ friendshipBar = True
               $ affection = char.affection    
     
     #actually displays everything          
     frame xminimum 240 xmaximum 240 yminimum ymax: 
       style_group "infoscreen"  
       vbox yalign 0.5 xalign 0.5: 
          for i in allchars:
             #$ textbutton_name, dummy1, dummy2 = i.name.partition(' ') #cuts off the name after the first space
             textbutton i.name action SetVariable("viewing", i.name) xminimum 220 xmaximum 220 yminimum 50   
             #code for future imagebuttons
             #imagebutton idle "i.idlepic" hover "i.hoverpic" action SetVariable("viewing", i.name)
             $ i.normalize()
          textbutton "Return" action Return() ypos 0.8

     window xanchor 0 xpos 240 yalign 0 xminimum 784 xmaximum 784 yminimum ymax ymaximum ymax:
      style_group "infoscreen"   
      vbox spacing 10: 
          vbox:
              text name
              if profession != 'Занятие: ???':
                  text profession
              if age != 'Возраст: ???':
                  text age
              if birthday != 'День рождения: ???':                  
                  text birthday

          vbox xmaximum 500:     
               text likes
               text dislikes
          vbox spacing 10 xmaximum 490:  
              # text description 
              text thoughts            
              text got_here                          
              hbox ypos 0.7:
                if superBar:         
                       text "Суперспособности:"  
                       bar value super_lvl range superMax style "infoscreen_bar" right_bar "bar_empty-pink.png" left_bar "bar_full-pink.png"
                if friendshipBar:
                       text "Симпатия:"  
                       bar value affection range affectionMax style "infoscreen_bar" 
      if pic != 'none':
               add pic xalign 0.6 yalign 0.0 #Tinker with these numbers as needed to change where the image goes
